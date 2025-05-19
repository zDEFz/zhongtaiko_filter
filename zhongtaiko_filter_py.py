#!/usr/bin/env python3
import sys
import evdev
import time
import os
from evdev import UInput, ecodes, InputDevice

DEVICE_PATH = '/dev/input/by-id/usb-03eb_Keyboard-event-kbd'

# 0) Unbuffered prints
def log(msg):
    print(msg)
    sys.stdout.flush()

log("🟢 Script started")

# 1) Wait for the device to appear
for attempt in range(30):  # wait up to ~30 seconds
    if os.path.exists(DEVICE_PATH):
        break
    log(f"⏳ Waiting for device: {DEVICE_PATH}")
    time.sleep(1)
else:
    log(f"❌ Device not found after waiting: {DEVICE_PATH}")
    sys.exit(1)

# 2) Try to open and grab the device
try:
    dev = InputDevice(DEVICE_PATH)
    dev.grab()
except Exception as e:
    log(f"⚠️ Failed to open or grab device: {e}")
    sys.exit(1)

log("✅ Taiko filter running. Press D/F/J/K on the drum to see it forwarded.")

# 3) Create the uinput device
ui = UInput(
    { ecodes.EV_KEY: [ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K] },
    name="taiko-filter",
    version=0x3
)

# 4) Event loop
try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY and event.code in (
            ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K
        ):
            log(f"➡️ Handled event: {event}")
            ui.write_event(event)
            ui.syn()
finally:
    ui.close()
    dev.ungrab()
    log("🛑 Taiko filter stopped")
