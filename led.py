#!/usr/bin/env python3
import sys, time
from random import randrange as rand

devpath = '/dev/hidraw0'
colors = {'red':0x01,'green':0x02,'blue':0x03,'cyan':0x06,'magenta':0x05,'yellow':0x04,'white':0x07,'off':0x08}
chsum = lambda b0, b1, b3: (21*b0**2 + 19*b1 - 3*b3) % 255

def send_hex(color_name):
    cmd = bytearray.fromhex('ff'*64)
    cmd[0] = 0x11
    cmd[1] = colors.get(color_name, 0x07)
    cmd[3] = rand(255)
    cmd[2] = chsum(cmd[0], cmd[1], cmd[3])
    try:
        with open(devpath, 'wb') as f: f.write(cmd)
    except Exception as e:
        print(f"\033[1;31mError speaking to hardware layer: {e}\033[0m"); sys.exit(1)

def print_help():
    C = '\033[1;36m'  # Cyan
    G = '\033[1;32m'  # Green
    W = '\033[1;37m'  # White
    R = '\033[1;31m'  # Red
    M = '\033[1;35m'  # Magenta
    Y = '\033[1;33m'  # Yellow
    B = '\033[1;34m'  # Blue
    K = '\033[1;30m'  # Bold Black / Dark Gray
    O = '\033[0m'     # Reset
    
    print(f"{C}=== CHROMELIGHT LED COMMAND MENU ==={O}")
    print(f"{W}Usage Layouts:{O}")
    print(f"  {G}chromelight [color]{O}             -> Set a solid steady light")
    print(f"  {G}chromelight [color] [number]{O}    -> Blink a color a set number of times")
    print(f"  {G}chromelight [color1] [color2]{O}    -> Strobe flash back and forth between two colors")
    print(f"  {G}chromelight RGB{O}                 -> Start infinite full RGB rainbow cycle")
    print(f"  {G}chromelight off{O}                 -> Shut off the activity light instantly")
    print(f"\n{W}Available Hardware Colors:{O}")
    print(f"  {R}red{O}, {G}green{O}, {B}blue{O}, {C}cyan{O}, {M}magenta{O}, {Y}yellow{O}, {W}white{O}, {K}off{O}")
    print(f"{C}===================================={O}\n")

if __name__ == '__main__':
    # Keep lower() for standard colors, but we check for 'RGB' natively
    args = [a.lower() for a in sys.argv[1:]]
    raw_args = sys.argv[1:] # Keep a raw version to explicitly capture capitalized "RGB"
    
    if not args: print_help(); sys.exit(0)
    
    # Catching uppercase 'RGB' or lowercase 'rgb' safely in the typo detector
    if len(raw_args) == 1 and (raw_args[0] == 'RGB' or raw_args[0].lower() == 'rgb'):
        print("Starting RGB loop... Press Ctrl+C to stop."); seq = ['red','yellow','green','cyan','blue','magenta']
        try:
            while True:
                for c in seq: send_hex(c); time.sleep(0.5)
        except KeyboardInterrupt: send_hex('off')
    elif len(args) == 2 and args[0] in colors and args[1] in colors:
        print(f"Starting {args[0]} <-> {args[1]} strobe... Press Ctrl+C to stop.")
        try:
            while True: send_hex(args[0]); time.sleep(0.25); send_hex(args[1]); time.sleep(0.25)
        except KeyboardInterrupt: send_hex('off')
    elif len(args) > 1 and args[1].isdigit():
        if args[0] in colors:
            print(f"Blinking {args[0]} {args[1]} times..."); [ (send_hex(args[0]), time.sleep(0.3), send_hex('off'), time.sleep(0.3)) for _ in range(int(args[1])) ]
        else: print_help()
    elif args[0] in colors:
        send_hex(args[0]); print(f"LED is now solid {args[0]}")
    else:
        print("\n\033[1;31m[!] Error: Invalid command or typo detected.\033[0m"); print_help()
