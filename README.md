# Dell Chromebook 11 (Candy) Activity LED Controller

An optimized, feature-rich Python 3 hardware utility to control the physical lid activity indicator light on the Dell Chromebook 11 (Candy) running Linux (tested on MX Linux 25.2 SysVinit).

This project is an updated and expanded Python 3 modernization based on the original legacy Python 2 implementation by hgeg.

## Features

- **📦 Native Debian Installer (.deb):** Easily deploy the utility as a system application.
- **🔑 Passwordless Hardware Access:** Bundled with custom kernel `udev` rules so you can switch colors without typing `sudo`.
- **🎨 ANSI-Colored TUI:** Features a beautiful, color-coded terminal user interface menu with integrated syntax safeguards.
- **⚡ Global Shortcut:** Accessible natively system-wide via the simple `chromelight` command.
- **✨ Multiple Lighting Modes:** Supports solid colors, blink loops, dual-color strobe flashes, and an infinite RGB rainbow cycle.

## Available Colors

- `red`, `green`, `blue`, `cyan`, `magenta`, `yellow`, `white`, `off`

---

## 💾 Installation

The easiest way to install this tool on MX Linux or Debian is by using our custom compiled pre-release package:

1. Head over to the **Releases** tab on this repository and download the latest `.deb` installer.
2. Open your terminal in the directory where the file was downloaded and run:
```bash
sudo apt install ./chromelight_0.2.4_all.deb
```

*(Note: The installer automatically pulls down required hardware dependencies like `python3-usb` and configures your system permissions).*

---

## 🚀 How to Use

Once installed, simply open any terminal window on your machine and invoke the tool natively:

1. **Open the Help TUI Menu:**
```bash
chromelight
```

2. **Set a Solid Color:**
```bash
chromelight magenta
```

3. **Blink a Color X Times:**
```bash
chromelight green 5
```

4. **Dual Alternating Strobe Flash:**
```bash
chromelight blue red
```

5. **Infinite RGB Rainbow Cycle:**
```bash
chromelight RGB
```

## 🛠️ Active Development
⚠️ **Note:** A dedicated Graphical User Interface (GUI) wrapper application is currently in the testing phase and will be added in an upcoming development release. 

## License
Distributed under the MIT License. See `LICENSE` for more details.
