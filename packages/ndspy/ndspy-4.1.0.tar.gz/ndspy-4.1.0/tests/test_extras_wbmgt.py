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
Unit tests for ndspy.extras.wbmgt.
"""

import ndspy.bmg
import ndspy.extras.wbmgt


################################################################
################################################################
####################### Sample WBMGT data ######################
################################################################
################################################################

# Since the ndspy.extras.wbmgt functions support all of the various
# parser function arguments, the sample WBMGT file should make use of
# all of those.

SAMPLE_WBMGT = """#BMG
@INF-SIZE = 12
0 = hello world
m1 [1,2,3,4,5] = second message
2 [1,3,5/7] /
m3 [2,4,6,8,A,C,E,10,12,14,16] = unicode: \\u{30C4}; color: \\c{reddish}; macro: \\M{3}
"""
def SAMPLE_WBMGT_MESSAGE_ID_PARSE_FUNCTION(s):
    assert s.startswith('m')
    return int(s[1:])
def SAMPLE_WBMGT_U_ESCAPE_FUNCTION(v):
    assert v == 0x30C4
    return chr(v)
def SAMPLE_WBMGT_COLOR_PARSE_FUNCTION(s):
    assert s == 'reddish'
    return ord('!')
def SAMPLE_WBMGT_COLOR_ESCAPE_FUNCTION(v):
    assert v == ord('!')
    return chr(v)
SAMPLE_WBMGT_MACROS = {3: '(macro 3)'}

SAMPLE_WBMGT_KWARGS = {
    'messageIDParseFunction': SAMPLE_WBMGT_MESSAGE_ID_PARSE_FUNCTION,
    'uEscapeFunction': SAMPLE_WBMGT_U_ESCAPE_FUNCTION,
    'colorParseFunction': SAMPLE_WBMGT_COLOR_PARSE_FUNCTION,
    'colorEscapeFunction': SAMPLE_WBMGT_COLOR_ESCAPE_FUNCTION,
    'macros': SAMPLE_WBMGT_MACROS,
}


def helper_checkSampleWBMGT(bmg):
    """
    Check that the provided BMG matches the sample WBMGT data
    """
    assert len(bmg.messages) == 4

    assert bmg.messages[0].info == b'\0\0\0\0\0\0\0\0'
    assert bmg.messages[1].info == b'\1\2\3\4\5\0\0\0'
    assert bmg.messages[2].info == b'\1\3\5\0\7\0\0\0'
    assert bmg.messages[3].info == b'\2\4\6\x08\x0A\x0C\x0E\x10'

    assert bmg.messages[0].stringParts == ['hello world']
    assert bmg.messages[1].stringParts == ['second message']
    assert bmg.messages[2].stringParts == []
    assert bmg.messages[3].stringParts == ['unicode: ツ; color: !; macro: (macro 3)']

    assert not bmg.messages[0].isNull
    assert not bmg.messages[1].isNull
    assert bmg.messages[2].isNull
    assert not bmg.messages[3].isNull


def helper_makeSampleWBMGTForPatching():
    """
    Create a ndspy.bmg.BMG object that can be patched by the sample
    WBMGT data.
    """
    return ndspy.bmg.BMG.fromMessages([
        ndspy.bmg.Message(b'\0' * 8, ['will be overwritten']),
        ndspy.bmg.Message(b'\1' * 8, [], True),
        ndspy.bmg.Message(b'\2' * 8, ['will also be overwritten']),
        ndspy.bmg.Message(b'\3' * 8, [], True),
        ndspy.bmg.Message(b'\4' * 8, ['will be kept']),
    ])


def helper_checkPatchedWBMGT(bmg):
    """
    Check that the BMG produced by helper_makeSampleWBMGTForPatching(),
    and which should've been patched by the sample WBMGT data, actually
    was patched correctly
    """
    # Check that the stuff that shouldn't've been patched, wasn't
    assert len(bmg.messages) == 5

    lastMessage = bmg.messages.pop()
    assert lastMessage.info == b'\4' * 8
    assert lastMessage.stringParts == ['will be kept']
    assert not lastMessage.isNull

    # (After removing that final message,) check the rest of it
    helper_checkSampleWBMGT(bmg)


def helper_makeSampleBMG():
    """
    Create a BMG that matches SAMPLE_WBMGT
    """
    return ndspy.bmg.BMG.fromMessages([
        ndspy.bmg.Message(b'\0\0\0\0\0\0\0\0', ['hello world']),
        ndspy.bmg.Message(b'\1\2\3\4\5\0\0\0', ['second message']),
        ndspy.bmg.Message(b'\1\3\5\0\7\0\0\0', [], True),
        ndspy.bmg.Message(b'\2\4\6\x08\x0A\x0C\x0E\x10', ['unicode: ツ; color: !; macro: (macro 3)']),
    ])


def helper_checkSavedWBMGT(wbmgt):
    """
    wbmgt is a string representing (hopefully) SAMPLE_WBMGT, parsed and
    resaved by ndspy. Check that it seems correct.
    """
    lines = wbmgt.splitlines()

    # Step 1: check that @INF-SIZE is correct
    print(lines)
    assert '@INF-SIZE = 0x0C' in lines

    # Step 2: filter out uninteresting lines
    lines2 = []
    for L in lines:
        if L.startswith('#') or L.startswith('@') or not L:
            continue
        lines2.append(L)
    lines = lines2

    # Step 3: check that the remaining lines are as expected
    assert lines == [
        '     0 = hello world',
        '     1 [1,2,3,4,5] = second message',
        '     2 [1,3,5/7] /',
        '     3 [2,4,6,8,A,C,E,10] = unicode: ツ; color: !; macro: (macro 3)',
    ]


################################################################
################################################################
############################# Tests ############################
################################################################
################################################################



def test_load():
    """
    Test ndspy.extras.wbmgt.load().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__load.py
    """
    # Load WBMGT data
    bmg = ndspy.extras.wbmgt.load(SAMPLE_WBMGT, **SAMPLE_WBMGT_KWARGS)
    # Check that it was loaded correctly
    helper_checkSampleWBMGT(bmg)


def test_loadFromFile(tmp_path):
    """
    Test ndspy.extras.wbmgt.loadFromFile().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__load.py
    """
    fp = tmp_path / 'test.bmg'

    # Write sample WBMGT data to file
    fp.write_text(SAMPLE_WBMGT, encoding='utf-8')

    # Load it back in, and check that it's correct
    # (using both pathlib.Path and str)
    for fp2 in [fp, str(fp)]:
        # Load WBMGT data
        bmg = ndspy.extras.wbmgt.loadFromFile(fp2, **SAMPLE_WBMGT_KWARGS)
        # Check that it was loaded correctly
        helper_checkSampleWBMGT(bmg)


def test_patch():
    """
    Test ndspy.extras.wbmgt.patch().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__load.py
    """
    # Make BMG
    bmg = helper_makeSampleWBMGTForPatching()
    # Patch it with WBMGT data
    ndspy.extras.wbmgt.patch(bmg, SAMPLE_WBMGT, **SAMPLE_WBMGT_KWARGS)
    # Check that it was patched correctly
    helper_checkPatchedWBMGT(bmg)


def test_patchFromFile(tmp_path):
    """
    Test ndspy.extras.wbmgt.patchFromFile().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__load.py
    """
    fp = tmp_path / 'test.txt'

    # Write sample WBMGT data to file
    fp.write_text(SAMPLE_WBMGT, encoding='utf-8')

    # Load it back in, and check that it's correct
    # (using both pathlib.Path and str)
    for fp2 in [fp, str(fp)]:
        # Make BMG
        bmg = helper_makeSampleWBMGTForPatching()
        # Patch it with WBMGT data
        ndspy.extras.wbmgt.patchFromFile(bmg, fp2, **SAMPLE_WBMGT_KWARGS)
        # Check that it was patched correctly
        helper_checkPatchedWBMGT(bmg)


def test_save():
    """
    Test ndspy.extras.wbmgt.save().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__save.py
    """
    # Load BMG to save
    bmg = helper_makeSampleBMG()
    # Save it
    wbmgt = ndspy.extras.wbmgt.save(bmg)
    # Check that it was saved correctly
    helper_checkSavedWBMGT(wbmgt)


def test_saveToFile(tmp_path):
    """
    Test ndspy.extras.wbmgt.saveToFile().

    Note: this is just to test that the function exists and basically
    seems to work. More rigorous testing can be found in
    test_extras_wbmgt__save.py
    """
    fp = tmp_path / 'test.txt'

    # Load BMG to save
    bmg = helper_makeSampleBMG()

    # Using both pathlib.Path and str...
    for fp2 in [fp, str(fp)]:
        # Save it
        ndspy.extras.wbmgt.saveToFile(bmg, fp2)
        # Load it back in as text
        wbmgt = fp.read_text(encoding='utf-8')
        # Check that it was saved correctly
        helper_checkSavedWBMGT(wbmgt)

        # Clear the file contents so as to not taint the next loop
        # iteration
        fp.write_bytes(b'')
