# OSI 600D Superboard II (Cherry) - verification report, rev 1.0

Checked against all five sheets of the OSI 600 rev D schematic (28 Aug 1980).

## Sheet 3 check

Oscillator (X1, U58, R35/R36, C57, C65), clock doubler (U79), U29 divider, U78 32/64 mux, U76, the U30/U59/U60/U61 video counters, U65/U69 one-shots, U57 baud divider, U63/U64 cassette/serial flip-flops, U66 cassette input, Q1/Q2 RS-232, and J2/J3 all match.

One error found and fixed: U56 pin 12 and U78 pin 9 were on the oscillator net. On the schematic they are a separate signal (U78 3Y drives U56 pin 12), and the copper already kept them apart. They now have their own net, MODE32_GATE. Without this fix, Update PCB would have tied U78's output to the crystal oscillator.

Clock nets renamed: OSC (U58 pin 3), OSC_X2 (doubled clock from U79), OSC_DIV4 (U29 QB).

## Routing completed

All 84 breaks are now connected; no net is split and no new copper is closer than 0.2 mm to another net.

- 79 were hairline breaks under 0.3 mm, where a track stopped at or overlapped a pad, via or track without an endpoint inside it, so KiCad did not see a connection. Each got a short bridging segment on the same layer.
- New tracks longer than 0.3 mm:
  - AUTO_0161 (track fragment): 0.7 mm, 0.4 mm wide
  - AUTO_0521 (track fragment): 4.2 mm, 0.4 mm wide
  - BK0 (U72.2): 2.0 mm, 0.4 mm wide
  - GND (track fragment): 3.2 mm, 0.6 mm wide
  - GND (R74*.2): 1.0 mm, 0.6 mm wide
- Power bridges use 0.6 mm track, signals 0.4 mm. No new vias were needed.

## Rev 1.0 - final once-over (from your edited board)

Your edits were kept: the 338 copper-art lines with exposed solder mask, the two removed copper-art pieces, and the moved R68 text.
- Off-centre track ends at vias: 290 -> 106. Ends meeting at the same via are now moved together; anything that would break a junction or reduce clearance below 0.15 mm was left.
- Nets renamed to the OSI schematic names:
  - ACIA_CLK -> Tx_CLOCK (sheet 1 "Tx CLOCK")
  - ELx_CLOCK -> ETx_CLOCK, ELx_DATA -> ETx_DATA (J2 external transmit, sheet 1)
  - 1200_BAUD -> 499.2KHz, 300_BAUD -> 124.8KHz (J3 pins 12 and 10, sheet 3)
  - AUTO_0650 -> Rx_DATA_3 (U67 pin 10, sheet 1/3 "Rx DATA 3")
  - AUTO_0699 -> ~{CTS_3} (U67 pin 8, "CTS 3")
- Checked: no copper of two different nets overlaps anywhere (tracks, pads, vias, copper graphics), the exposed copper lettering touches no net, every pad keeps its net apart from the renames above, no net is split.
- Schematic regenerated to match; netlist identical to the PCB (269 nets, 0 differences). Footprints linked to the delivered schematic files.

## Rev 0.9

- SW40 (Break key): the right-hand 1.7 mm plastic-peg hole is removed, because it cut through the GND strip along the right edge. A silkscreen circle and "SNIP PEG" note mark where it was, so that peg can be snipped off the switch before fitting.

## Rev 0.8 - second DRC pass

KiCad stops listing each error type at about 200, so the rev 0.7 report only showed the first batch of thin tracks and off-centre track ends. This pass fixed the rest across the whole board:
- Thin tracks: 697 -> 9. 646 widened to 0.2 mm (only where 0.2 mm clearance is kept), 46 removed that sat inside other same-net copper.
- Track ends inside a via but not at its centre: 1,944 -> 290. The rest are left because moving them would detach another track that joins mid-way (T-junction) or reduce clearance.
- Pads U5-13 and U57-13 narrowed to 1.4 mm (same fix as the other six DIP pads).
- Checked afterwards: every pad keeps its net, no net is split, no shorts.

Expected to remain and safe to exclude: about 290 off-centre track ends, the 79 solder-mask bridges inside the exposed "HE-3-V0" copper lettering, 122 vias connected on one side only (original holes), 10 short dangling tracks (original stubs and four 0.25 mm bridges), 0.15-0.2 mm clearances (set Default clearance to 0.15 mm), library-footprint warnings, silkscreen and courtyard warnings.

## Rev 0.7 - DRC clean-up

- Copper art: the "Ohio Scientific Model 600 CPU" lettering and other orphan copper (51 AUTO nets with no pads or vias) are now plain unconnected copper graphics: 385 tracks converted to copper lines, 6 shapes had their net cleared. Same copper, no more dangling-track or clearance-between-letters errors.
- Thin tracks: 192 GND/Vcc tracks under the 0.2 mm minimum widened to 0.2 mm, only where that keeps 0.2 mm clearance; 35 removed that sat entirely inside other same-net copper. 1 left (no room).
- Track ends not centred on vias: 143 snapped onto the via centre (clearance checked); 36 leftover zero-length pieces removed. 15 left as they were, because moving them would break a T-junction or reduce clearance.
- Dangling tracks: 47 removed that were fully inside other same-net copper. 4 original stubs kept (GND, Vcc, VRAM_A4, VRAM_A5).
- Clearance: pads J1-36, J1-38, U5-2, U30-3, U57-4 and U57-16 narrowed from 1.6 to 1.4 mm (0.3 mm ring on the 0.8 mm drill) to clear the original tracks running past them, which were 0.11-0.14 mm away.
- SW54 (shift lock): footprint type set to through-hole, outline moved from the Margin layer to F.Fab, courtyard added.
- Checked afterwards: every pad has the same net as before, no net is split, no shorts.

## Rev 0.6 changes

- C65 moved 0.23 mm left so pad 1 sits on the original hole; it now clears the MODE32_GATE track by 0.23 mm (this was the DRC short).
- References KiCad could not annotate renamed: R73* -> R87 (LED resistor, sheet 5), R74* -> R88 (DD pull-down, sheet 1), R86* -> R89 (DAC 510R pull-up, sheet 5), R62A -> R90 (sheet 3), SHIFT_LOCK -> SW54. Nets named after them renamed to match. R86 (1K pull-up) stays on sheet 3.
- Schematic rebuilt on 5 sheets matching the OSI pages. Decoupling capacitors now sit on the sheet of the IC they are next to on the PCB.
- Logic ICs are now multi-unit symbols drawn as gates (NAND, NOR, AND, XOR, inverters, Schmitt inverters, open-collector buffers, tri-state buffers, comparators), with flip-flops, one-shots and the 74LS139 as one block per half. Each gate is on the sheet where OSI drew it; each IC's VCC/GND unit is in the power section of its main sheet.
- Footprints re-linked to the new sheet paths.

## Rev 0.5 - copper clean-up

- 1,378 copper circles removed. Each sat exactly on a via or pad of the same net, whose copper already covers it.
- 20 copper graphic lines converted to real tracks (same layer, width and net).
- 1 copper polygon removed (completely inside other same-net copper). The other 77 are kept as netted graphic polygons: they are the teardrop-style fillets where tracks meet pads, and removing them would change the copper.
- 21 large drill-only vias (3.0, 3.05, 4.5 and 5.0 mm, no copper, no tracks) converted to board-only NPTH footprints H1-H21. The two 3.05 mm holes by the space bar are the stabiliser holes.
- 16 vias that had no copper ring now have a 1.4 mm ring on a 0.8 mm drill, each checked for at least 0.2 mm clearance. Several are the original jumper holes near J3 (Rx DATA, Rx DATA 1/2/3, CTS, CTS 3, 300 BAUD), so wire links can now be soldered there.
- Kept on purpose: 5 copper circles slightly larger than the via they surround (two vias on the C62/D27 net and one on Vcc), and 4 zero-length tracks that are the only copper at their point.
- Not touched: the original artwork on Eco1.User / Eco2.User (reference layers, not plotted). Delete those layers' contents if you no longer need them.
- Checked after clean-up: every pad keeps its net, no net is split, no shorts.

## Rev 0.4 changes

- F1 bypass removed: the 3.2 mm B.Cu track from clip 1 (270.47, 75.19) to clip 2 (270.47, 92.73) is deleted.
- The input side of F1 (clip 1, and the six 1.2 mm power-input holes around x 276-294, y 42-64) is now net +5V_IN. Clip 2, C5, D15 and the rest of the board stay on Vcc, matching sheet 5 (fuse ahead of D15 and C5).
- Schematic split into a top-level sheet with six sub-sheets following the OSI pages. Nets that cross sheets use global labels; nets inside one sheet use local labels. Footprints are re-linked to the new sheet paths.

## Earlier corrections (still included)

- U72 pad 2 (Q1 = BK0): added to BK0 net
- C36: value 0.1Uf -> 0.1uF
- R85: value 100K -> 10M
- C66: value ? -> 0.1uF
- C67: value ? -> 0.1uF
- U17: value 74LS159 -> 74LS139
- SW40: removed stray net from non-plated hole
- U7: pad number "DD" -> "15"
- C69: value ? -> 0.1uF
- C68: value ? -> 0.1uF
- C62: value ? -> 0.1uF
- U54: value 74LS175 -> 74LS157
- 688 vias: copper diameter set to the matching copper ring (drill unchanged)
- net J3_12_U29_12 -> 1200_BAUD (88 items)
- net C63_2_J4_2 -> NOISE (2 items)
- net VID1 -> VID (1 items)
- net NC -> GND (6 items)
- net 02 -> PHI2 (73 items)
- net 00 -> PHI0 (41 items)
- net U13_20_U21_4 -> ~{PHI2} (117 items)
- net U13_18_U18_3 -> ~{MCS} (23 items)
- net U14_9_U17_12 -> ~{ACS} (16 items)
- net U15_1_U16_1 -> F000_FFFF (33 items)
- net U16_2_U17_15 -> ~{F000_FFFF} (12 items)
- net U15_3_U23_7 -> ~{E000_FFFF} (33 items)
- net U23_10_U73_5 -> ~{A000_BFFF} (30 items)
- net U22_4_U23_15 -> ~{0000_1FFF} (11 items)
- net U22_7_U31_8 -> ~{RAM_0000} (26 items)
- net U22_9_U32_8 -> ~{RAM_0400} (13 items)
- net U22_10_U33_8 -> ~{RAM_0800} (14 items)
- net U22_11_U34_8 -> ~{RAM_0C00} (13 items)
- net U22_12_U35_8 -> ~{RAM_1000} (17 items)
- net U22_13_U36_8 -> ~{RAM_1400} (29 items)
- net U22_14_U37_8 -> ~{RAM_1800} (38 items)
- net U22_15_U38_8 -> ~{RAM_1C00} (38 items)
- net U73_12_U9_20 -> ~{ROM_A000} (40 items)
- net U10_20_U73_13 -> ~{ROM_A800} (35 items)
- net U11_20_U73_14 -> ~{ROM_B000} (26 items)
- net U12_20_U73_15 -> ~{ROM_B800} (29 items)
- net U20_12_U24_1 -> ~{RD_D000} (50 items)
- net U20_13_U74_1 -> ~{RD_D400} (31 items)
- net U20_10_U72_9 -> ~{WR_D800} (21 items)
- net U20_11_U21_11 -> ~{WR_DC00} (7 items)
- net U2_13_U2_4 -> WKB (18 items)
- net U15_10_U24_15 -> VRAM_BE (14 items)
- net U74_15_U79_3 -> CRAM_BE (28 items)
- net U18_6_U56_4 -> V (25 items)
- net U53_1_U54_1 -> ~{VA} (46 items)
- net U15_5_U15_6 -> BK0 (20 items)
- net U15_11_U15_12 -> BK1 (11 items)
- net U72_7_U76_4 -> MODE32 (53 items)
- net ~{RTS} -> ~{ACIA_CTS} (112 items)
- net U14_5_U68_13 -> ~{ACIA_RTS} (43 items)
- net U14_3_U14_4 -> ACIA_CLK (70 items)
- net U39_5_U40_5 -> VRAM_A0 (21 items)
- net U39_6_U40_6 -> VRAM_A1 (21 items)
- net U39_7_U40_7 -> VRAM_A2 (21 items)
- net U39_4_U40_4 -> VRAM_A3 (24 items)
- net U39_3_U40_3 -> VRAM_A4 (25 items)
- net U39_2_U40_2 -> VRAM_A5 (27 items)
- net U39_1_U40_1 -> VRAM_A6 (28 items)
- net U39_17_U40_17 -> VRAM_A7 (21 items)
- net U39_16_U40_16 -> VRAM_A8 (28 items)
- net U39_15_U40_15 -> VRAM_A9 (27 items)
- net U24_10_U39_14 -> VRAM_D0 (21 items)
- net U24_3_U39_13 -> VRAM_D1 (23 items)
- net U24_6_U39_12 -> VRAM_D2 (19 items)
- net U25_13_U39_11 -> VRAM_D3 (41 items)
- net U25_10_U40_14 -> VRAM_D4 (15 items)
- net U25_3_U40_13 -> VRAM_D5 (17 items)
- net U25_6_U40_12 -> VRAM_D6 (19 items)
- net U24_13_U40_11 -> VRAM_D7 (32 items)
- net U41_9_U42_6 -> CG_D0 (10 items)
- net U41_10_U42_5 -> CG_D1 (9 items)
- net U41_10_U41_11 -> CG_D2 (11 items)
- net U41_13_U42_3 -> CG_D3 (5 items)
- net U41_14_U42_14 -> CG_D4 (7 items)
- net U41_15_U42_13 -> CG_D5 (9 items)
- net U41_16_U42_12 -> CG_D6 (10 items)
- net U41_17_U42_11 -> CG_D7 (11 items)
- net U19_9_U30_14 -> C0 (10 items)
- net U19_10_U30_13 -> C1 (11 items)
- net U19_12_U30_12 -> C2 (13 items)
- net U30_11_U53_3 -> C3 (54 items)
- net U53_6_U59_14 -> C4 (39 items)
- net U53_10_U59_13 -> C5 (30 items)
- net U53_13_U59_12 -> C6 (9 items)
- net U54_3_U59_11 -> C7 (63 items)
- net U41_8_U60_14 -> C8 (43 items)
- net U41_7_U60_13 -> C9 (21 items)
- net U41_6_U60_12 -> C10 (21 items)
- net U54_6_U78_12 -> C11 (34 items)
- net U54_10_U61_14 -> C12 (18 items)
- net U54_13_U61_13 -> C13 (17 items)
- net U55_3_U61_12 -> C14 (14 items)
- net U55_6_U61_11 -> C15 (54 items)
- net U30_2_U42_2 -> CLK (80 items)
- net U43_3_U43_4 -> T1 (8 items)
- net U19_13_U43_12 -> T2 (34 items)
- net U43_11_U56_13 -> T3 (34 items)
- net U62_10_U70_1 -> DB (18 items)
- net U65_12_U70_13 -> ~{HS} (13 items)
- net U65_4_U70_12 -> ~{VS} (14 items)
- net R4_2_SHIFT_LOCK_1 -> KB_COL0 (54 items)
- net R5_2_SW22_1 -> KB_COL1 (55 items)
- net R3_2_SW13_1 -> KB_COL2 (91 items)
- net R6_2_SW12_1 -> KB_COL3 (69 items)
- net R2_2_SW11_1 -> KB_COL4 (60 items)
- net R7_2_SW10_1 -> KB_COL5 (67 items)
- net R1_2_SW17_1 -> KB_COL6 (62 items)
- net R8_2_SW1_1 -> KB_COL7 (68 items)
- net D3_2_SHIFT_LOCK_3 -> KB_ROW0 (81 items)
- net D4_2_SW15_2 -> KB_ROW1 (72 items)
- net D5_2_SW43_2 -> KB_ROW2 (102 items)
- net D6_2_SW29_2 -> KB_ROW3 (89 items)
- net D7_2_SW16_2 -> KB_ROW4 (74 items)
- net D8_2_SW23_2 -> KB_ROW5 (60 items)
- net D1_2_SW10_2 -> KB_ROW6 (58 items)
- net D2_2_SW1_2 -> KB_ROW7 (67 items)
- net D3_1_R73_1 -> KB_DRV0 (14 items)
- net D4_1_R71_1 -> KB_DRV1 (17 items)
- net D5_1_R70_1 -> KB_DRV2 (20 items)
- net D6_1_R67_1 -> KB_DRV3 (14 items)
- net D7_1_R68_1 -> KB_DRV4 (13 items)
- net D8_1_R69_1 -> KB_DRV5 (11 items)
- net D1_1_R75_1 -> KB_DRV6 (26 items)
- net D2_1_R74_1 -> KB_DRV7 (22 items)
- net C63_1_D17_2 -> DAC_SUM (38 items)
- net R84_2_R85_1 -> ~{BREAK} (26 items)
- net D30_1_D31_2 -> POR_CAP (8 items)
- net C65_1_U56_12 split: U56.12 + U78.9 -> MODE32_GATE; remainder -> OSC

## Still for you to decide

- Jumper options from sheet 3 not on this board: U62 pin 8 (inverted RS-232 receive), U67 pin 10 (Rx DATA 3) and U67 pin 8 (CTS 3) have no destination. J3 pin 7 (-V IN) is hard-wired to GND, so the RS-232 output only swings 0 to +5 V.
- J3 pin 10 is named 300_BAUD; sheet 3 labels it 124.8 kHz. Same signal, name only.
- R40 / R48 designators are swapped relative to sheet 1 (both 220R).
- SW38 (Cherry) and SHIFT_LOCK are in parallel at the same matrix position - fit only one.
- 16 vias still have no copper ring; the 5 mm mounting holes are modelled as vias.
- R85 set to 10M per sheet 5; revert if 100K was intentional.

## Schematic

Top-level sheet plus five sub-sheets (292 parts, 374 symbol units). Its netlist matches the PCB exactly (269 nets, 0 differences), and the footprints are linked to the symbols, so Update PCB from Schematic should report no changes.