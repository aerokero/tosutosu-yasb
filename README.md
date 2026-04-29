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

2. Copy `config.yaml` and `styles.css` into your YASB configuration directory.
3. Refresh or restart YASB to apply the theme.

## Backup folder
The `tosu-yasb/` directory in this workspace contains backups and is intentionally excluded from the packaged theme.

## License
This project is licensed under the MIT License — see `LICENSE` for details.

## Launchpad apps
Do not commit your machine-specific `launchpad/apps.json`. Instead, copy `launchpad/apps.example.json` to `launchpad/apps.json` and update paths/icons for your system.

See `CHANGELOG.md` for upgrade notes.

## Localization

This repository includes a small starter i18n helper to keep widget strings consistent across languages.

- Translations live in `i18n/translations.json`.
- To generate a localized copy of `config.yaml`, run:

```bash
python scripts/apply_i18n.py en
```

This produces `config.i18n.en.yaml`. The script performs simple replacements for known widget strings (starter set). Edit `i18n/translations.json` to add or tweak translations.

## Contribute
Suggestions, icon updates, and improvements are welcome via GitHub Issues or Pull Requests.

