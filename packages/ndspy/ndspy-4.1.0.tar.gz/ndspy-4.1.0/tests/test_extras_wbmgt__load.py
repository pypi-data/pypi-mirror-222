# Copyright 2020 RoadrunnerWMC
#
# This file is part of ndspy.
#
# ndspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ndspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ndspy.  If not, see <https://www.gnu.org/licenses/>.
"""
Unit tests for ndspy.extras.wbmgt._load.
"""

import ndspy.bmg
import ndspy.extras.wbmgt._load as _load
import pytest

import wbmgt_common


def helper_loadWbmgt(*args, **kwargs):
    """
    Helper function to load a wbmgt file using the patch() function
    """
    bmg = ndspy.bmg.BMG()
    if 'encoding' in kwargs:
        bmg.encoding = kwargs.pop('encoding')
    _load.patch(bmg, *args, **kwargs)
    return bmg


def test_empty():
    """
    Test loading empty files
    """
    bmg = helper_loadWbmgt('#BMG')
    assert not bmg.messages


def test_parseAttributesString():
    """
    Test WBMGTPatcher.parseAttributesString()
    """
    assert _load.WBMGTPatcher.parseAttributesString('[]', 0) == b''
    assert _load.WBMGTPatcher.parseAttributesString('[]', 1) == b'\0'
    assert _load.WBMGTPatcher.parseAttributesString('[]', 2) == b'\0\0'
    assert _load.WBMGTPatcher.parseAttributesString('[]', 3) == b'\0\0\0'
    assert _load.WBMGTPatcher.parseAttributesString('[]', 4) == b'\0\0\0\0'

    # Whitespace
    assert _load.WBMGTPatcher.parseAttributesString('[ 1 , 2 , 3 , 4 , 5 ]', 4) == b'\1\2\3\4'

    # Data truncation and padding
    assert _load.WBMGTPatcher.parseAttributesString('[1,2,3,4,5]', 0) == b''
    assert _load.WBMGTPatcher.parseAttributesString('[1,2,3,4,5]', 8) == b'\1\2\3\4\5\0\0\0'

    # Multi-digit byte values
    assert _load.WBMGTPatcher.parseAttributesString('[,1,23]', 3) == b'\0\1\x23'

    # Implicit zeroes
    assert _load.WBMGTPatcher.parseAttributesString('[,,,,,5]', 8) == b'\0\0\0\0\0\5\0\0'

    # "/" alignment operator
    assert _load.WBMGTPatcher.parseAttributesString('[/5]',      8) == b'\0\0\0\0\5\0\0\0'
    assert _load.WBMGTPatcher.parseAttributesString('[,/5]',     8) == b'\0\0\0\0\5\0\0\0'
    assert _load.WBMGTPatcher.parseAttributesString('[/,5]',     8) == b'\0\0\0\0\0\5\0\0'
    assert _load.WBMGTPatcher.parseAttributesString('[1,3,5/7]', 8) == b'\1\3\5\0\7\0\0\0'


def test_cloneMessageInto():
    """
    Test cloneMessageInto()
    """
    messageA = ndspy.bmg.Message()
    messageB = ndspy.bmg.Message()

    # Null message
    messageA.info = b'\0\1\2\3'
    messageA.isNull = True

    _load.cloneMessageInto(messageA, messageB)

    assert messageB.info == b'\0\1\2\3'
    assert messageB.isNull

    # Non-null message
    messageA.info = b'\4\5\6\7'
    messageA.isNull = False
    messageA.stringParts = ['abcde',
                            ndspy.bmg.Message.Escape(0, b'\0\1\2'),
                            'fghi',
                            ndspy.bmg.Message.Escape(77, b'\3\4\5'),
    ]

    _load.cloneMessageInto(messageA, messageB)

    assert messageB.info == b'\4\5\6\7'
    assert not messageB.isNull
    assert messageB.stringParts[0] == 'abcde'
    assert messageB.stringParts[1].type == 0
    assert messageB.stringParts[1].data == b'\0\1\2'
    assert messageB.stringParts[2] == 'fghi'
    assert messageB.stringParts[3].type == 77
    assert messageB.stringParts[3].data == b'\3\4\5'


def test_messageIDs():
    """
    Test parsing message IDs
    """
    # Basic hex message IDs
    f = """#BMG
0=hello
1=world
A=test 1
b=test 2
9F=test 3"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts == ['hello']
    assert bmg.messages[1].stringParts == ['world']
    assert bmg.messages[0xA].stringParts == ['test 1']
    assert bmg.messages[0xB].stringParts == ['test 2']
    assert bmg.messages[0x9F].stringParts == ['test 3']

    # Custom message IDs
    f = """#BMG
ham=ham
pork=pork
beef=beef
lobster=lobster"""

    # Should be unparseable without custom parse function
    with pytest.raises(Exception):
        helper_loadWbmgt(f)

    # Parse function
    def midParser(s):
        if s == 'ham':
            return 22
        elif s == 'pork':
            return 33
        elif s == 'beef':
            raise RuntimeError('"beef" should be read as a hexadecimal string')
        elif s == 'lobster':
            return 44
        else:
            raise RuntimeError('Unexpected argument: ' + repr(s))

    # Should parse correctly, using that
    bmg = helper_loadWbmgt(f, messageIDParseFunction=midParser)
    assert bmg.messages[22].stringParts == ['ham']
    assert bmg.messages[33].stringParts == ['pork']
    assert bmg.messages[0xbeef].stringParts == ['beef']
    assert bmg.messages[44].stringParts == ['lobster']

    # Invalid message IDs
    f = """#BMG
crab=crab"""  # invalid because it begins with a hex digit but isn't a hex number
    with pytest.raises(Exception):
        helper_loadWbmgt(f, messageIDParseFunction=midParser)


def test_fillerMessages():
    """
    Test filled-in messages
    """
    # Filling in gaps between messages
    f = """#BMG
@INF-SIZE = 11
0=hello
5=world"""
    bmg = helper_loadWbmgt(f)

    assert bmg.messages[0].stringParts == ['hello']
    assert bmg.messages[5].stringParts == ['world']

    for i in range(1, 5):
        assert bmg.messages[i].info == b'\0' * (11 - 4)
        assert not bmg.messages[i].stringParts
        assert bmg.messages[i].isNull

    # Filling in IDs before the first message
    f = """#BMG
@INF-SIZE = 11
5=hello world"""
    bmg = helper_loadWbmgt(f)

    assert bmg.messages[5].stringParts == ['hello world']

    for i in range(5):
        assert bmg.messages[i].info == b'\0' * (11 - 4)
        assert not bmg.messages[i].stringParts
        assert bmg.messages[i].isNull


def test_unicodeEscapeFunction():
    """
    Test the Unicode-escape-function feature
    """
    f = r"""#BMG
0=hello \u{0} world \u{1,2,3} example \u{ 4 , 5 , 666 }\u{AAAAA}"""

    # Should be unparseable without custom escape function
    with pytest.raises(Exception):
        helper_loadWbmgt(f)

    # Escape function
    def uEscaper(v):
        if v <= 5:
            return 'abcdef'[v]
        elif v == 0x666:
            return ndspy.bmg.Message.Escape(666, b'\6\6\6')
        elif v == 0xAAAAA:
            return ndspy.bmg.Message.Escape(123, b'botw')
        else:
            raise RuntimeError('Unexpected argument: ' + repr(v))

    # Should parse correctly, using that
    bmg = helper_loadWbmgt(f, uEscapeFunction=uEscaper)
    assert bmg.messages[0].stringParts[0] == 'hello a world bcd example ef'
    assert bmg.messages[0].stringParts[1].type == 666
    assert bmg.messages[0].stringParts[1].data == b'\6\6\6'
    assert bmg.messages[0].stringParts[2].type == 123
    assert bmg.messages[0].stringParts[2].data == b'botw'


def test_colorParseFunction():
    """
    Test the color-parse-function feature
    """
    def colorEscaper(v):
        return str(v)

    f = r"""#BMG
0=hello \c{ham} world \c{pork}\c{beef}\c{lobster}\c{  crab  }"""

    # Should be unparseable without custom parse function
    with pytest.raises(Exception):
        helper_loadWbmgt(f, colorEscapeFunction=colorEscaper)

    # Parse function
    def colorParser(s):
        if s == 'ham':
            return 22
        elif s == 'pork':
            return 33
        elif s == 'beef':
            raise RuntimeError('"beef" should be read as a hexadecimal string')
        elif s == 'lobster':
            return 44
        elif s == 'crab':
            # This starts with a hex digit but isn't a valid hex string
            # Such a color name should be treated as a name, since BMG
            # defines a "CLEAR" color name for MKW
            return 55
        else:
            raise RuntimeError('Unexpected argument: ' + repr(s))

    # Should parse correctly, using that
    bmg = helper_loadWbmgt(f, colorParseFunction=colorParser, colorEscapeFunction=colorEscaper)
    assert bmg.messages[0].stringParts[0] == 'hello 22 world 33488794455'


def test_escapes():
    """
    Test escape sequences not already covered by other test types
    """
    # Standard C escapes
    f = r"""#BMG
0 = \\\a\b\f\n\r\t\v"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts[0] == '\\\a\b\f\n\r\t\v'

    # Octal escapes
    f = r"""#BMG
0 = \0 \7 \00 \77 \78 \000 \777 \778"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts[0] == '\0 \7 \00 \77 \78 \000 \777 \778'

    f = r"""#BMG
0 = \8"""  # (not a valid octal escape sequence)
    with pytest.raises(Exception):
        helper_loadWbmgt(f)

    # Macro escapes (\m{}, \M{}) are tested elsewhere

    # Hex escapes (\x{})
    f = r"""#BMG
0 = \x{0} \x{ffff} \x{FFFFF} \x{ 1 , 2 , FFFFF , 3 , 4 , 89ABC }"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts[0] == '\x00 \uFFFF \uFFFF \x01\x02\uFFFF\x03\x04\u9ABC'

    # Nintendo escapes (\z{})
    for encoding in ['cp1252', 'utf-16', 'shift-jis', 'utf-8']:
        for msg, data, _ in wbmgt_common.NINTENDO_ESCAPE_TESTS:
            f = '#BMG\n0 = ' + msg
            bmg = helper_loadWbmgt(f, encoding=encoding)

            assert isinstance(bmg.messages[0].stringParts[0], ndspy.bmg.Message.Escape)
            assert bmg.messages[0].stringParts[0].type == 0
            assert bmg.messages[0].stringParts[0].data == data

    f = r"""#BMG
1 = \z{6FF,1}
4 = \z{ 1600 , 1 , 2 , 123456789ABCDEF0123 }  <- (odd number of digits)"""
    bmg = helper_loadWbmgt(f)
    assert isinstance(bmg.messages[1].stringParts[0], ndspy.bmg.Message.Escape)
    assert bmg.messages[1].stringParts[0].type == 0xFF
    assert bmg.messages[1].stringParts[0].data == b'\0\1'
    assert isinstance(bmg.messages[4].stringParts[0], ndspy.bmg.Message.Escape)
    assert bmg.messages[4].stringParts[0].type == 0
    assert bmg.messages[4].stringParts[0].data == b'\0\1\0\0\0\0\0\0\0\2\x45\x67\x89\xAB\xCD\xEF\x01\x23'

    # Unicode escapes (\u{}) are tested elsewhere

    # Color escapes (\c{}) are tested elsewhere


def test_macros():
    """
    Test the macros feature
    """
    # \m{} ================================

    # "If a message with given MID exists (must be defined before and must not
    # have an assigned value), then insert the text of the message."
    # I'm not sure what the "assigned value" part means.
    f = r"""#BMG
0=example
1=hello \m{0} world"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[1].stringParts[0] == 'hello example world'

    # "If the message does not exist, the macro library is searched as fallback."
    f = r"""#BMG
0=hello \m{2} world"""
    bmg = helper_loadWbmgt(f, macros={2: 'two'})
    assert bmg.messages[0].stringParts[0] == 'hello two world'

    # "If this fails too, text »\m{MID}« is inserted."
    f = r"""#BMG
0=hello \m{2} world \m{3,4,5}"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts[0] == r'hello \m{2} world \m{3}\m{4}\m{5}'

    # \M{} ================================
    # "The message is searched in the macro library. If found, then insert the
    # text of the message."
    f = r"""#BMG
0=hello \M{2} world"""
    bmg = helper_loadWbmgt(f, macros={2: 'two'})
    assert bmg.messages[0].stringParts[0] == 'hello two world'

    # "If the message does not exist, text »\M{MID}« is inserted."
    # Note: this fallback occurs even if a message with that ID exists
    f = r"""#BMG
0=distraction
1=hello \M{0} world \M{3,4,5}"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[1].stringParts[0] == r'hello \M{0} world \M{3}\M{4}\M{5}'

    # Different macro formats ================================
    macros = {
        0: 'zero',
        1: ndspy.bmg.Message.Escape(1, b'one'),
        0x222: ['two', ndspy.bmg.Message.Escape(100, b'hundred'), 'twenty', ndspy.bmg.Message.Escape(2, b'two')],
    }
    f = r"""#BMG
0=hello \M{0} world \M{ 1 , 222 }"""
    bmg = helper_loadWbmgt(f, macros=macros)
    assert bmg.messages[0].stringParts[0] == 'hello zero world '
    assert bmg.messages[0].stringParts[1].type == 1
    assert bmg.messages[0].stringParts[1].data == b'one'
    assert bmg.messages[0].stringParts[2] == 'two'
    assert bmg.messages[0].stringParts[3].type == 100
    assert bmg.messages[0].stringParts[3].data == b'hundred'
    assert bmg.messages[0].stringParts[4] == 'twenty'
    assert bmg.messages[0].stringParts[5].type == 2
    assert bmg.messages[0].stringParts[5].data == b'two'


def test_comments():
    """
    Test comments
    """
    f = r"""#BMG
@INF-SIZE = 9#comment
# comment
0=message where this # is not a comment
# but this is
+  and this isn't"""

    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].info == b'\0\0\0\0\0'
    assert bmg.messages[0].stringParts[0] == "message where this # is not a comment and this isn't"


def test_hugeMessageIDs():
    """
    Test that the parser doesn't explode if given an unreasonably large message ID
    """
    f = r"""#BMG
999999=test"""
    with pytest.raises(Exception):
        helper_loadWbmgt(f)


def test_lineFormats():
    """
    Test various line formats
    """
    f = r"""#BMG

# MID ~ ATTRIB32
0 ~ 0x12345678
1 ~ 0x23456789
1 = one

# MID /
10 /
11 /
11 = eleven

# MID '[' ATTRIB ']' /
20 [1,2,3,4] /
21 [2,3,4,5] /
21 = twenty-one

# MID = TEXT
# (this is tested elsewhere)

# MID '[' ATTRIB ']' = TEXT
30 [3,4,5,6] = thirty

# + TEXT
# (this is tested elsewhere)

# MID1 : MID2
# The spec says "This kind of assignment is delayed after all other
# messages are defined", so we will be testing for that.
# 40 is an example of a message not defined until after the MID1:MID2 line
# 41 gets its message text edited after MID1:MID2
# 42 gets its attrib value edited after MID1:MID2
41 = forty-one
42 = forty-two
45 : 40
46 : 41
47 : 42
40 = forty
41 = forty-one but edited
42 [4,5,6,7] /
"""

    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].info == b'\x12\x34\x56\x78'
    assert bmg.messages[0].isNull
    assert not bmg.messages[0].stringParts
    assert bmg.messages[1].info == b'\x23\x45\x67\x89'
    assert not bmg.messages[1].isNull
    assert bmg.messages[1].stringParts[0] == 'one'
    assert bmg.messages[0x10].isNull
    assert not bmg.messages[0x10].stringParts
    assert not bmg.messages[0x11].isNull
    assert bmg.messages[0x11].stringParts[0] == 'eleven'
    assert bmg.messages[0x20].info == b'\1\2\3\4'
    assert bmg.messages[0x20].isNull
    assert not bmg.messages[0x20].stringParts
    assert bmg.messages[0x21].info == b'\2\3\4\5'
    assert not bmg.messages[0x21].isNull
    assert bmg.messages[0x21].stringParts[0] == 'twenty-one'
    assert bmg.messages[0x30].info == b'\3\4\5\6'
    assert not bmg.messages[0x30].isNull
    assert bmg.messages[0x30].stringParts[0] == 'thirty'
    assert not bmg.messages[0x40].isNull
    assert bmg.messages[0x40].stringParts[0] == 'forty'
    assert not bmg.messages[0x41].isNull
    assert bmg.messages[0x41].stringParts[0] == 'forty-one but edited'
    assert bmg.messages[0x42].info == b'\4\5\6\7'
    assert bmg.messages[0x42].isNull
    assert not bmg.messages[0x42].stringParts
    assert not bmg.messages[0x46].isNull
    assert bmg.messages[0x46].stringParts[0] == 'forty-one but edited'
    assert bmg.messages[0x47].info == b'\4\5\6\7'
    assert bmg.messages[0x47].isNull
    assert not bmg.messages[0x47].stringParts


def test_lineContinuations():
    """
    Test line continuations ("+")
    """
    # Test that certain types of lines can't be continued

    f = '#BMG\n+ (erroneous continuation)'
    with pytest.raises(Exception):
        helper_loadWbmgt(f)

    for uncontinuable in ['1 ~ 0x12345678', '1 /', '1 [1] /', '1 : 0']:
        f = '#BMG\n0 = zero\n' + uncontinuable + '\n+ (erroneous continuation)'
        with pytest.raises(Exception):
            helper_loadWbmgt(f)

    f = r"""#BMG
0 = zero
1 = one
  + point five
2 [1,2] = two,
  + including attributes on first line
3 = three,

  + straddling a few

  + blank lines


  + and another one

4 =  four, with
  +  two spaces at the beginning
  +  of each line
"""
    f += '5 = five, with \n'
    f += '  + trailing whitespace \n'
    f += '  + on each line \n'

    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].stringParts[0] == 'zero'
    assert bmg.messages[1].stringParts[0] == 'onepoint five'
    assert bmg.messages[2].info == b'\1\2\0\0'
    assert bmg.messages[2].stringParts[0] == 'two,including attributes on first line'
    assert bmg.messages[3].stringParts[0] == 'three,straddling a fewblank linesand another one'
    assert bmg.messages[4].stringParts[0] == ' four, with two spaces at the beginning of each line'
    assert bmg.messages[5].stringParts[0] == 'five, with trailing whitespace on each line '


def test_fileParameters():
    """
    Test @PARAMETER lines.
    """
    # @INF-SIZE < 4 (should default to 8)
    for size in [-3, 0, 3]:
        f = f"""#BMG
@INF-SIZE = {size}
0=hello world"""
        bmg = helper_loadWbmgt(f)
        assert len(bmg.messages[0].info) == 4

    # 4 < @INF-SIZE < 1000
    f = """#BMG
@INF-SIZE = 4
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert len(bmg.messages[0].info) == 0

    f = """#BMG
@INF-SIZE = 5
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert len(bmg.messages[0].info) == 1

    f = """#BMG
@INF-SIZE = 8
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert len(bmg.messages[0].info) == 4

    f = """#BMG
@INF-SIZE = 73
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert len(bmg.messages[0].info) == 73 - 4

    f = """#BMG
@INF-SIZE = 1000
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert len(bmg.messages[0].info) == 1000 - 4

    # @INF-SIZE > 1000 (should default to 8)
    for size in [1001, 1005, 999999]:
        f = f"""#BMG
@INF-SIZE = {size}
0=hello world"""
        bmg = helper_loadWbmgt(f)
        assert len(bmg.messages[0].info) == 4

    # @DEFAULT-ATTRIBS
    # Check that nothing gets chopped off, even if INF-SIZE is declared
    # second
    f = """#BMG
@DEFAULT-ATTRIBS = [1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]
@INF-SIZE = 10
0=hello world"""
    bmg = helper_loadWbmgt(f)
    assert bmg.messages[0].info == b'\1\2\3\4\5\6'

    # @BMG-MID
    # Is not supported; any nonzero value triggers an exception
    f = """#BMG
@BMG-MID = 0"""
    bmg = helper_loadWbmgt(f)

    f = """#BMG
@BMG-MID = 1"""
    with pytest.raises(Exception):
        bmg = helper_loadWbmgt(f)
