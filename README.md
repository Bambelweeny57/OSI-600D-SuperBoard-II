<p align="center">
  <img src="https://github.com/Bambelweeny57/OSI-600D-SuperBoard-II/blob/main/images/osi-600d-banner.png" width="100%" alt="OSI 600D Superboard II Banner">
</p>

### Ohio Scientific (OSI) 600D Superboard II Recreation

This repository contains an open-source hardware recreation of the **600D variant** of the classic 1978 Ohio Scientific Superboard II single-board computer. 

The goal of this project is to modernise and preserve the original design using modern design tools and components, specifically targetting standard **Cherry MX keyswitches** while maintaining functional fidelity with the vintage 6502 hardware. 

### 🛠 Project Status & Progress

This project is a work-in-progress. Here is the current development roadmap: 

* [x] **Gerber Import:** Initial conversion into KiCad 10 based on the original reproduction Gerber files by Grant (Klyball).
* [x] **Visual Enhancements:** Added proper modern Soldermask and Silkscreen layers to the board layout.
* [/] **Schematic Reverse Engineering:** Started recreating the original logic gates and traces natively into KiCad schematics (In Progress).
* [ ] **Footprint Refinement:** Evaluating the transition from raw imported copper geometry to native KiCad component footprints.
* [ ] **PCB Routing Finalisation:** Reviewing and completing unverified circuit paths.

### 📐 Hardware Specifications (OSI 600D)

The original Superboard II (Model 600) was an entry-level microcomputer featuring: 

* **CPU:** MOS Technology 6502 running at 1 MHz
* **Memory:** 4KB RAM (expandable to 8KB onboard) and 8KB Microsoft BASIC in ROM
* **Video output:** Monochrome composite video (24 lines x 24 characters text/graphics matrix)
* **Keyboard:** 53-key integrated keyboard matrix (adapted to Cherry MX switches in this variant)
* **Storage:** Audio cassette interface / RS-232 serial option

### 🤝 How to Contribute & Next Steps

If you are a vintage computing enthusiast or a hardware designer, your help is welcome! The primary focus areas right now are: 

1. **Schematic Mapping:** Helping map out the traces to finish the KiCad schematic generation.
2. **Footprint Standardization:** Deciding on whether to replace the imported legacy copper pads with actual native KiCad footprints for easier component sourcing.
3. **Validation:** Reviewing the layout against original OSI 600D engineering sheets to verify trace accuracy.

### 📜 Credits & Acknowledgments

* **Grant (Klyball):** For the foundational Gerber files that made this layout reconstruction possible.
* **Ohio Scientific Instruments (OSI):** For creating the original single-board masterpiece back in 1978.

### ⚖️ License

This project is shared for educational and preservation purposes. Please review original schematic copyrights where applicable.
