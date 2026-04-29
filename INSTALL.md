# Setup Guide — tosutosu's YASB Reborn Theme

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/aerokero/tosutosu-yasb.git
cd tosutosu-yasb
```

### Step 2: Find Your YASB Installation
```bash
# Locate YASB installation directory
python -c "import yasb; import os; print(os.path.dirname(yasb.__file__))"
```

This will print something like: `/usr/lib/python3.10/site-packages/yasb` or `C:\Python\Lib\site-packages\yasb`

**Save this path — you'll need it below.**

### Step 3: Install the Custom Localized Weather Widget

Copy the widget file to your YASB installation:

**Linux/macOS:**
```bash
YASB_PATH=$(python -c "import yasb; import os; print(os.path.dirname(yasb.__file__))")
cp widgets/weather_localized.py "$YASB_PATH/src/core/widgets/yasb/"
```

**Windows (PowerShell):**
```powershell
$YASB_PATH = python -c "import yasb; import os; print(os.path.dirname(yasb.__file__))"
Copy-Item "widgets/weather_localized.py" "$YASB_PATH\src\core\widgets\yasb\"
```

### Step 4: Copy Locale Files

Copy the locales folder to your YASB configuration directory:

**Linux/macOS:**
```bash
cp -r locales ~/.config/yasb/
```

**Windows:**
```powershell
Copy-Item -Recurse "locales" "$env:APPDATA\yasb\"
```

### Step 5: Configure YASB

Choose your language variant:

**English:**
```bash
cp config.i18n.en.yaml ~/.config/yasb/config.yaml
# or
cp config.i18n.en.yaml $env:APPDATA\yasb\config.yaml  # Windows
```

**Polish:**
```bash
cp config.i18n.pl.yaml ~/.config/yasb/config.yaml
# or
cp config.i18n.pl.yaml $env:APPDATA\yasb\config.yaml  # Windows
```

Or customize `config.yaml` manually.

### Step 6: Copy Styling

```bash
cp styles.css ~/.config/yasb/
# or
cp styles.css $env:APPDATA\yasb\  # Windows
```

### Step 7: Copy Other Assets

```bash
cp -r launchpad ~/.config/yasb/
cp notes.json ~/.config/yasb/
cp todo.json ~/.config/yasb/
# ... repeat for Windows with Copy-Item
```

### Step 8: Restart YASB

```bash
# Kill the existing YASB process
pkill -f yasb
# or: taskkill /IM yasb.exe  # Windows

# Restart
yasb
```

## Troubleshooting

### Widget Type Error: "unknown type..."
If you see: `weather has unknown type "yasb.weather_localized.WeatherLocalizedWidget"`

**Solution:** Ensure you've copied `weather_localized.py` to the correct YASB directory and restarted YASB.

### Locale Files Not Found
If you see: `Warning: Locale file not found`

**Solution:** Ensure `locales/` folder is copied to your YASB config directory (`~/.config/yasb/` on Linux/macOS).

### Weather Widget Still Shows English
Check `config.yaml` for the `locale` setting:
```yaml
weather:
  type: "yasb.weather_localized.WeatherLocalizedWidget"
  options:
    locale: "pl"  # or "en"
```

### Custom Apps Not Loading
Copy `launchpad/apps.example.json` to `launchpad/apps.json` and update file paths to your system.

## Support

See `README.md` and `CHANGELOG.md` for more information.

For issues, visit: https://github.com/aerokero/tosutosu-yasb/issues
