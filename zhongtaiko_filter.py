#!/usr/bin/env python3
import sys
import evdev
import time
from evdev import UInput, ecodes, InputDevice

# 0) Unbuffered prints
print("🟢 Script started")
sys.stdout.flush()

# 1) Open your physical drum device (persistent by-id path)
dev = InputDevice('/dev/input/by-id/usb-03eb_Keyboard-event-kbd')

# 2) Grab it so no one else sees its events
try:
    dev.grab()
except Exception as e:
    print(f"⚠️ Failed to grab device: {e}")
    sys.exit(1)

print("Taiko filter running. Press D/F/J/K on the drum to see it forwarded.")
sys.stdout.flush()

# 3) Create a uinput device advertising only D, F, J, K
ui = UInput(
    { ecodes.EV_KEY: [ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K] },
    name="taiko-filter",
    version=0x3
)

# 4) Loop and forward only the allowed keys
try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY and event.code in (
            ecodes.KEY_D, ecodes.KEY_F, ecodes.KEY_J, ecodes.KEY_K
        ):
            # Print the event that was handled
            print(f"Handled event: {event}")
            
            # Forward the event to the uinput device
            ui.write_event(event)
            ui.syn()          
        # all other events are dropped (blocked)
finally:
    # 5) Cleanup on exit
    ui.close()
    dev.ungrab()
    print("🛑 Taiko filter stopped")
    sys.stdout.flush()
