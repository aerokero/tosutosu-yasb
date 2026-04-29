"""
Custom Localized Weather Widget for YASB
Extends the built-in weather widget with multi-language support.

Installation:
  1. Copy this file to your YASB installation:
     cp widgets/weather_localized.py <YASB_PATH>/src/core/widgets/yasb/
  2. Copy locales folder:
     cp -r locales <YASB_CONFIG_DIR>/

Usage in config.yaml:
  weather:
    type: "yasb.weather_localized.WeatherLocalizedWidget"
    options:
      label: "<span>{icon}</span> {temp}, {feelslike}"
      locale: "pl"  # "en" or "pl"
      # ... other weather options
"""

import json
from pathlib import Path
from typing import Optional

try:
    # Import YASB weather widget base
    from yasb.weather import WeatherWidget
    from core.validation.widgets.yasb.weather import WeatherWidgetConfig
except ImportError:
    try:
        # Fallback: try different import paths
        from core.widgets.yasb.weather import WeatherWidget
        from core.validation.widgets.yasb.weather import WeatherWidgetConfig
    except ImportError:
        # Last resort: define stubs for testing
        WeatherWidget = object
        WeatherWidgetConfig = type("WeatherWidgetConfig", (), {})


class WeatherLocalizedConfig(WeatherWidgetConfig):
    """Extended config with locale support"""
    locale: str = "en"  # "en" or "pl"


class WeatherLocalizedWidget(WeatherWidget):
    """
    Localized weather widget that translates weather descriptions
    to the configured language.
    """

    validation_schema = WeatherLocalizedConfig

    def __init__(self, config):
        """Initialize with locale support"""
        # Ensure config has locale attribute
        if not hasattr(config, 'locale'):
            config.locale = "en"
        
        self.locale = config.locale
        self._translations = {}
        self._load_translations()

        # Call parent constructor
        super().__init__(config)

    def _load_translations(self):
        """Load locale translations from JSON file"""
        # Try multiple possible paths for locales directory
        possible_paths = [
            Path(__file__).parent.parent / "locales",  # Same repo structure
            Path.home() / ".config" / "yasb" / "locales",  # User config dir
            Path.home() / ".yasb" / "locales",  # Alt YASB config dir
        ]

        locale_file = None
        for base_path in possible_paths:
            candidate = base_path / f"{self.locale}.json"
            if candidate.exists():
                locale_file = candidate
                break

        if locale_file and locale_file.exists():
            try:
                with open(locale_file, encoding="utf-8") as f:
                    self._translations = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load locale file {locale_file}: {e}")
                self._translations = {}
        else:
            print(f"Warning: Locale file not found for {self.locale}")

    def _translate(self, key: str, fallback: str) -> str:
        """Translate a key or return fallback"""
        return self._translations.get(key, fallback)

    def process_weather_data(self, weather_data: dict):
        """
        Process weather data and apply translations
        Override parent method to localize weather text
        """
        # Call parent processing
        super().process_weather_data(weather_data)

        # Apply translations to condition text if available
        if hasattr(self, '_weather_data') and "condition_text" in self._weather_data:
            original_condition = self._weather_data.get("condition_text", "")
            translated = self._translate(
                f"weather_{original_condition.lower()}",
                original_condition
            )
            self._weather_data["condition_text"] = translated

            # Update labels with translated data
            if hasattr(self, '_update_label'):
                self._update_label()

