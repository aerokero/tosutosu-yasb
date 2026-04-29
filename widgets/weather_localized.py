"""
Custom Localized Weather Widget for YASB
Extends the built-in weather widget with multi-language support.

Usage in config.yaml:
  weather:
    type: "widgets.weather_localized.WeatherLocalizedWidget"
    options:
      label: "<span>{icon}</span> {temp}, {feelslike}"
      label_alt: "\udb84\udcc3 {min_temp}, \udb84\udcc2 {max_temp}"
      api_key: "YOUR_API_KEY"
      location: "Poland, Krakow"
      locale: "pl"  # "en" or "pl"
      units: "metric"
      # ... other weather options
"""

import json
from pathlib import Path
from typing import Optional

try:
    # Import YASB weather widget base
    from core.widgets.yasb.weather import WeatherWidget
    from core.validation.widgets.yasb.weather import WeatherWidgetConfig
except ImportError:
    # Fallback for testing
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

    def __init__(self, config: WeatherLocalizedConfig):
        """Initialize with locale support"""
        self.locale = config.locale
        self._translations = {}
        self._load_translations()

        # Call parent constructor
        super().__init__(config)

    def _load_translations(self):
        """Load locale translations from JSON file"""
        locale_file = Path(__file__).parent.parent / "locales" / f"{self.locale}.json"

        if locale_file.exists():
            try:
                with open(locale_file, encoding="utf-8") as f:
                    self._translations = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load locale file {locale_file}: {e}")
                self._translations = {}
        else:
            print(f"Warning: Locale file not found: {locale_file}")

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

        # Apply translations to condition text
        if "condition_text" in self._weather_data:
            original_condition = self._weather_data.get("condition_text", "")
            translated = self._translate(
                f"weather_{original_condition.lower()}",
                original_condition
            )
            self._weather_data["condition_text"] = translated

        # Update labels with translated data
        self._update_label()
