 # tosutosu's YASB Reborn Theme

tosutosu's YASB Reborn is a modern, customizable theme for Yet Another Startpage (YASB). It updates visuals, app icons, and configuration examples to give YASB a refreshed, lightweight look while remaining easy to install and customize.

Version: 2.0.0 — compatible with YASB v2.0.0

## What’s Included
- `config.yaml` — theme configuration and example mappings
- `styles.css` — main stylesheet with theme variables
- `launchpad/` — launcher configuration and icon assets
- `notes.json`, `todo.json` — personal workspace files (optional)

## Installation
1. Clone this repository:

```bash
git clone https://github.com/aerokero/tosutosu-yasb.git
```

2. Choose your language variant:
   - **English**: use `config.i18n.en.yaml`
   - **Polish**: use `config.i18n.pl.yaml`
   - **Custom**: edit `config.yaml` directly

3. Copy your chosen config and `styles.css` into your YASB configuration directory.
4. Refresh or restart YASB to apply the theme.

## Backup folder
The `tosu-yasb/` directory in this workspace contains backups and is intentionally excluded from the packaged theme.

## License
This project is licensed under the MIT License — see `LICENSE` for details.

## Launchpad apps
Do not commit your machine-specific `launchpad/apps.json`. Instead, copy `launchpad/apps.example.json` to `launchpad/apps.json` and update paths/icons for your system.

See `CHANGELOG.md` for upgrade notes.

## Language Variants

Choose from pre-configured language variants:
- `config.i18n.en.yaml` — English widget labels
- `config.i18n.pl.yaml` — Polish widget labels

To add a new language variant, copy `config.yaml`, customize the widget labels for your language, and commit it as `config.i18n.<lang>.yaml`.

## Custom Localized Weather Widget

This theme includes a **custom weather widget** with multi-language support (`widgets/weather_localized.py`).

⚠️ **Note:** The custom widget works only if YASB is **installed from source** (`pip install yasb`), not from the pre-built executable. The frozen YASB installation cannot load custom widgets.

### For source-based YASB installations:

1. **Locate your YASB installation directory**:
   ```bash
   python -c "import yasb; import os; print(os.path.dirname(yasb.__file__))"
   ```

2. **Copy the widget and locales**:
   ```bash
   cp widgets/weather_localized.py <YASB>/src/core/widgets/yasb/
   cp -r locales <YASB_CONFIG_DIR>/
   ```

3. **Enable in config**:
   ```yaml
   weather:
     type: "yasb.weather_localized.WeatherLocalizedWidget"
     options:
       locale: "pl"  # or "en"
   ```

4. **Restart YASB**.

### For executable/frozen YASB:

The built-in weather widget will be used (English only). This is a limitation of the frozen application format.

## Contribute
Suggestions, icon updates, and improvements are welcome via GitHub Issues or Pull Requests.

