#!/usr/bin/env python3
import sys
import os
import time
from evdev import InputDevice, UInput, ecodes

DEVICE_PATH = '/dev/input/by-id/usb-03eb_Keyboard-event-kbd'

def log(msg):
    print(msg, flush=True)

log("🟢 Script started")

# 1) Wait for device with exponential backoff
delay = 0.01
for attempt in range(50):
    if os.path.exists(DEVICE_PATH):
        break
    if attempt < 10:
        time.sleep(delay)
        delay = min(delay * 1.2, 0.1)
    else:
        time.sleep(0.1)
else:
    log(f"❌ Device not found: {DEVICE_PATH}")
    sys.exit(1)

# 2) Open device with minimal setup
try:
    dev = InputDevice(DEVICE_PATH)
    dev.grab()
    fd = dev.fd
except Exception as e:
    log(f"⚠️ Device error: {e}")
    sys.exit(1)

log("✅ Taiko filter running")

# 3) Pre-configure uinput with minimal capabilities
ui = UInput(
    {ecodes.EV_KEY: [ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K]},
    name="taiko-filter",
    version=0x3
)

# 4) Pre-cache key codes for fastest lookup
TARGET_KEYS = frozenset([ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K])
EV_KEY = ecodes.EV_KEY

# 5) Ultra-optimized main loop - no select(), direct blocking read
try:
    read_event = dev.read_one
    write_event = ui.write_event
    syn = ui.syn
    
    while True:
        event = read_event()
        if event and event.type == EV_KEY and event.code in TARGET_KEYS:
            write_event(event)
            syn()

except KeyboardInterrupt:
    pass
except Exception as e:
    log(f"⚠️ Runtime error: {e}")
finally:
    ui.close()
    dev.ungrab()
    log("🛑 Taiko filter stopped")
