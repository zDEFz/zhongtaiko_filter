# zhongtaiko_filter

`zhongtaiko_filter` is a minimal evdev-based input filter for ZhongTaiko [Pro] drum controllers.  
It eliminates ghost keypresses by grabbing the raw input device and forwarding only legitimate hit events (`D`, `F`, `J`, `K`) through a virtual input device.

This ensures cleaner input for games like *Taiko no Tatsujin*, where phantom key events can cause dropped combos or misfires.

## 🛠️ How It Works

- Grabs the ZhongTaiko USB device exclusively using `/dev/input/by-id/...`
- Creates a clean virtual device (`/dev/uinput`) emitting only allowed keys
- Forwards only D/F/J/K key events; all others are silently discarded
- Runs automatically at user login as a `systemd` service with root permissions

## 🔐 Why Root?

This script needs root access to:
- Grab the physical input device
- Create a virtual input device using `uinput`

## 📦 Installation (AUR)

```bash
yay -S taiko-filter
# OR 
paru -S taiko filter
```

## Disclaimer

This script is unofficial and not affiliated with ZhongTaiko or Bandai Namco. Use at your own risk.
