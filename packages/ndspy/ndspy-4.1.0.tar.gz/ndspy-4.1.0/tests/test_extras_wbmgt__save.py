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
Unit tests for ndspy.extras.wbmgt._save.
"""

import ndspy
import ndspy.bmg
import pytest

import wbmgt_common


def wbmgtHas(bmg, line):
    """
    Helper function to verify that the BMG's wbmgt output contains the
    given line.
    (Each line in the wbmgt output is lstripped before comparing.)
    """
    lines = ndspy.extras.wbmgt.save(bmg).splitlines()
    for line2 in lines:
        if line == line2.lstrip():
            return True

    # Instead of returning False, we print the wbmgt and raise an
    # exception, since that makes debugging a lot easier
    print('wbmgt contents:')
    print('\n'.join(lines))
    raise Exception(f'{line} is not in the wbmgt!')


def test_empty():
    """
    Test saving empty files
    """
    bmg = ndspy.bmg.BMG()
    textLines = ndspy.extras.wbmgt.save(bmg).splitlines()

    for line in textLines:
        assert not line or line.startswith('#') or line.startswith('@')


def test_parameters():
    """
    Test the @PARAMETER lines at the top
    """

    # Easy ones first: @PRODUCED-BY and @BMG-MID
    bmg = ndspy.bmg.BMG()

    assert wbmgtHas(bmg, f'@PRODUCED-BY = ndspy-{ndspy.VERSION[0]}.{ndspy.VERSION[1]}.{ndspy.VERSION[2]}')
    assert wbmgtHas(bmg, '@BMG-MID = 0')

    # Now for @INF-SIZE...
    assert wbmgtHas(bmg, '@INF-SIZE = 0x08')

    bmg.messages.append(ndspy.bmg.Message())
    assert wbmgtHas(bmg, '@INF-SIZE = 0x04')

    bmg.messages[0].info += b'\0' * 3
    assert wbmgtHas(bmg, '@INF-SIZE = 0x07')

    bmg.messages[0].info += b'\0' * 5
    assert wbmgtHas(bmg, '@INF-SIZE = 0x0C')

    # (Check that having messages with different info lengths triggers
    # an exception)
    bmg.messages.append(ndspy.bmg.Message())
    with pytest.raises(ValueError):
        assert ndspy.extras.wbmgt.save(bmg)
    bmg.messages.pop()

    # And finally, @DEFAULT-ATTRIBS
    bmg.messages[0].info = b'\1\2\3\4'
    assert wbmgtHas(bmg, '@DEFAULT-ATTRIBS = [1,2,3,4]')


def test_nullAndEmptyMessages():
    """
    Test null and empty messages
    """

    # Null message
    bmg = ndspy.bmg.BMG()
    bmg.messages.append(ndspy.bmg.Message(isNull=True))
    assert wbmgtHas(bmg, '0 /')

    # Empty message
    bmg.messages[0] = ndspy.bmg.Message()
    assert wbmgtHas(bmg, '0 =')


def test_attributes():
    """
    Test attributes strings.
    """
    bmg = ndspy.bmg.BMG()

    # Empty attributes
    # We have to check this via @DEFAULT-ATTRIBS because there's no way
    # to prevent it from becoming the default, since there are no other
    # zero-length strings we can put in other messages
    bmg.messages.append(ndspy.bmg.Message(b'', 'hello world'))
    assert wbmgtHas(bmg, '@DEFAULT-ATTRIBS = []')

    # Now we add some dummy messages with weird but matching attributes,
    # to ensure that the @DEFAULT-ATTRIBS doesn't continue to swallow
    # the first message's attributes.
    # We'll have 8 bytes of info data, to start with.
    bmg.messages.append(ndspy.bmg.Message(b'\xDE\xAD\xBE\xEF' * 2))
    bmg.messages.append(ndspy.bmg.Message(b'\xDE\xAD\xBE\xEF' * 2))
    bmg.messages.append(ndspy.bmg.Message(b'\xDE\xAD\xBE\xEF' * 2))

    # All zeros
    bmg.messages[0].info = b'\0' * 8
    assert wbmgtHas(bmg, '0 [] = hello world')

    # All zeros but with one nonzero byte
    for i, expected in enumerate(['[1]', '[,2]', '[,,3]', '[,,,4]', '[/5]', '[/,6]', '[/,,7]', '[/,,,8]']):
        bmg.messages[0].info = bytearray(8)
        bmg.messages[0].info[i] = i + 1
        assert wbmgtHas(bmg, f'0 {expected} = hello world')

    # All nonzero bytes, two digits long
    bmg.messages[0].info = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0'
    assert wbmgtHas(bmg, f'0 [12,34,56,78,9A,BC,DE,F0] = hello world')


def test_stringMessageParts():
    """
    Test saving string-typed portions of Message.stringParts.
    """
    bmg = ndspy.bmg.BMG()
    bmg.messages.append(ndspy.bmg.Message())

    # Basic string
    bmg.messages[0].stringParts = ['hello world']
    assert wbmgtHas(bmg, '0 = hello world')

    # C escapes (other than \n)
    bmg.messages[0].stringParts = ['hello \\\a\b\f\r\t\v world']
    assert wbmgtHas(bmg, r'0 = hello \\\a\b\f\r\t\v world')

    # \n
    bmg.messages[0].stringParts = ['hello \n world']
    assert wbmgtHas(bmg, r'0 = hello \n')
    assert wbmgtHas(bmg, '+  world')  # two spaces, because there's a space after the \n

    # Unicode character escapes
    bmg.messages[0].stringParts = ['hello \x00\x80\x9F\uFFFF world']
    assert wbmgtHas(bmg, r'0 = hello \x{0}\x{80}\x{9f}\x{ffff} world')

    # Messages ending in whitespace
    bmg.messages[0].stringParts = ['hello world   ']
    assert wbmgtHas(bmg, r'0 = hello world   ')


def test_escapeMessageParts():
    """
    Test saving Message.Escape-typed portions of Message.stringParts.
    """
    bmg = ndspy.bmg.BMG()
    bmg.messages.append(ndspy.bmg.Message())

    # Simplest possible case
    bmg.messages[0].stringParts = [ndspy.bmg.Message.Escape(0, b'')]
    assert wbmgtHas(bmg, r'0 = \z{400}')

    # More advanced cases
    for _, data, msg in wbmgt_common.NINTENDO_ESCAPE_TESTS:
        bmg.messages[0].stringParts = [ndspy.bmg.Message.Escape(0, data)]
        assert wbmgtHas(bmg, '0 = ' + msg)
