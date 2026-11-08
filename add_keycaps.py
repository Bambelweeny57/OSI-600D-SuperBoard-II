#!/usr/bin/env python3
"""Add the switch and keycap 3D models to every keyswitch footprint of the OSI 600D board.

Usage:  python add_keycaps.py "OSI 600D Superboard II Cherry Solder Mask.kicad_pcb"

Close the board in KiCad first. A backup is written next to the board as .bak.
Model paths are relative to the KiCad project folder (src/): ${KIPRJMOD}/../models/...
"""
import re, shutil, sys

MODELS = "${KIPRJMOD}/../models"
SWITCH = MODELS + "/REDragon-MX-ZT02.stp"
SWITCH_OFFSET = (-2.54, -5.08, 0.0)   # switch centre relative to the footprint origin (pad 1)
CAP_OFFSET = (-2.54, -5.08, 7.5)      # keycap sits on the stem, 7.5 mm above the board
KEYCAP = {'SW1': 'Keycap_36_1', 'SW2': 'Keycap_37_2', 'SW3': 'Keycap_38_3', 'SW4': 'Keycap_39_4', 'SW5': 'Keycap_40_5', 'SW6': 'Keycap_41_6', 'SW7': 'Keycap_42_7', 'SW8': 'Keycap_43_8', 'SW9': 'Keycap_44_9', 'SW10': 'Keycap_45_0', 'SW11': 'Keycap_46_COLON', 'SW12': 'Keycap_47_MINUS', 'SW13': 'Keycap_27_RubOut', 'SW14': 'Keycap_30_ESC', 'SW15': 'Keycap_1_Q', 'SW16': 'Keycap_2_W', 'SW17': 'Keycap_3_E', 'SW18': 'Keycap_4_R', 'SW19': 'Keycap_5_T', 'SW20': 'Keycap_6_Y', 'SW21': 'Keycap_7_U', 'SW22': 'Keycap_8_I', 'SW23': 'Keycap_9_O', 'SW24': 'Keycap_10_P', 'SW25': 'Keycap_28_LineFeed', 'SW26': 'Keycap_35_RETURN1.5', 'SW27': 'Keycap_31_CTRL', 'SW28': 'Keycap_11_A', 'SW29': 'Keycap_12_S', 'SW30': 'Keycap_13_D', 'SW31': 'Keycap_14_F', 'SW32': 'Keycap_15_G', 'SW33': 'Keycap_16_H', 'SW34': 'Keycap_17_J', 'SW35': 'Keycap_18_K', 'SW36': 'Keycap_19_L', 'SW37': 'Keycap_48_SEMICOLON', 'SW38': 'Keycap_29_SHIFT_LOCK', 'SW39': 'Keycap_32_REPEAT', 'SW40': 'Keycap_33_BREAK', 'SW41': 'Keycap_34_SHIFT1.5', 'SW42': 'Keycap_20_Z', 'SW43': 'Keycap_21_X', 'SW44': 'Keycap_22_C', 'SW45': 'Keycap_23_V', 'SW46': 'Keycap_24_B', 'SW47': 'Keycap_25_N', 'SW48': 'Keycap_26_M', 'SW49': 'Keycap_49_COMMA', 'SW50': 'Keycap_50_PERIOD', 'SW51': 'Keycap_51_SLASH', 'SW52': 'Keycap_34_SHIFT1.5', 'SW53': 'Keycap_52_Space_bar'}

def model(path, off):
    return ('\t\t(model "' + path + '"\n\t\t\t(offset\n\t\t\t\t(xyz %g %g %g)\n\t\t\t)\n'
            '\t\t\t(scale\n\t\t\t\t(xyz 1 1 1)\n\t\t\t)\n\t\t\t(rotate\n\t\t\t\t(xyz 0 0 0)\n\t\t\t)\n\t\t)' % off)

def main(fn):
    raw = open(fn, 'rb').read()
    crlf = b'\r\n' in raw
    s = raw.decode('utf-8').replace('\r\n', '\n')
    shutil.copyfile(fn, fn + '.bak')
    done = 0
    def fix(m):
        nonlocal done
        blk = m.group(0)
        ref = re.search(r'\(property "Reference" "([^"]+)"', blk).group(1)
        if ref not in KEYCAP:
            return blk
        blk = re.sub(r'\n\t\t\(model "[^"]*"(?:\n\t\t\t.*)*?\n\t\t\)', '', blk)   # drop the old models
        new = model(SWITCH, SWITCH_OFFSET) + '\n' + model(MODELS + '/keycaps/' + KEYCAP[ref] + '.wrl', CAP_OFFSET)
        blk = blk[:blk.rfind('\n\t)')] + '\n' + new + '\n\t)'
        done += 1
        return blk
    s = re.sub(r'\n\t\(footprint "[^"]*".*?\n\t\)', fix, s, flags=re.S)
    if crlf: s = s.replace('\n', '\r\n')
    open(fn, 'w', encoding='utf-8', newline='').write(s)
    print('keyswitch footprints updated:', done)

if __name__ == '__main__':
    main(sys.argv[1])
