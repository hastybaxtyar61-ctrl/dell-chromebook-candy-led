# Dell Chromebook 11 (Candy) Activity LED Controller

An optimized, feature-rich Python3 hardware utility to control the physical lid activity indicator light on the Dell Chromebook 11 (Candy) running Linux (tested on MX Linux 25.2 SysVinit).

This project is an updated and expanded Python3 modernization based on the original legacy Python2 implementation by hgeg.

## Features

- **Solid Steady Modes:** Set a solid color that stays illuminated indefinitely.
- **Blink Loops:** Flash any supported hardware color a specific number of times.
- **Dual-Color Strobe:** Alternate rapidly back and forth between two custom colors (e.g., Police Style).
- **Infinite RGB Cycle:** Start a full-spectrum rainbow loop across all hardware phases.
- **Color-Coded Help Menu:** Includes built-in ANSI-colored syntax and typo protection.
- **No Heavy Dependencies:** Communicates directly with the raw `/dev/hidraw0` hardware layer.

## Available Colors

- `red`, `green`, `blue`, `cyan`, `magenta`, `yellow`, `white`, `off`

## Dependencies

To run this utility and allow for future USB communication extensions, you must install the following system packages on MX Linux / Debian:

```bash
sudo apt update && sudo apt install git python3-pip python3-usb
```

---

## Installation

1. Clone this repository into your home directory:
```bash
git clone https://github.com/hastybaxtyar61-ctrl/dell-chromebook-candy-led.git
cd dell-chromebook-candy-led
chmod +x led.py
```

## How to Use

Run the script directly via terminal:

1. **Set a Solid Color:**
```bash
sudo ./led.py magenta
```

2. **Blink a Color X Times:**
```bash
sudo ./led.py green 5
```

3. **Dual Alternating Strobe Flash:**
```bash
sudo ./led.py blue red
```

4. **Infinite RGB Rainbow Cycle:**
```bash
sudo ./led.py RGB
```

### Creating a Global Terminal Shortcut

To run this tool effortlessly from any directory using a short command, add a custom alias to your shell profile configuration: 
```bash
echo "alias chromelight='sudo /home/hasty-baxtyar/candy-led/led.py'" >> ~/.bashrc
source ~/.bashrc
```

Now you can simply use:
```bash
chromelight RGB
chromelight off
```

## License
Distributed under the MIT License. See `LICENSE` for more details.
