import os
import requests

WEATHER_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
BASE_URL = "http://api.weatherstack.com"

WEATHER_ICONS = {
    113: "☀️", 116: "⛅️", 119: "☁️", 122: "☁️", 143: "🌫",
    176: "🌦", 179: "🌨", 182: "🌧", 200: "⛈", 227: "🌨",
    230: "❄️", 263: "🌦", 266: "🌧", 293: "🌦", 296: "🌧",
    299: "🌧", 302: "🌧", 305: "🌧", 320: "🌨", 323: "❄️",
    326: "❄️", 329: "❄️", 353: "🌦", 356: "🌧", 386: "⛈",
}

WIND_DIRS = {
    "N": "↑С", "NNE": "↑ССВ", "NE": "↗СВ", "ENE": "→ВСВ",
    "E": "→В", "ESE": "→ВЮВ", "SE": "↘ЮВ", "SSE": "↓ЮЮВ",
    "S": "↓Ю", "SSW": "↓ЮЮЗ", "SW": "↙ЮЗ", "WSW": "←ЗЮЗ",
    "W": "←З", "WNW": "←ЗСЗ", "NW": "↖СЗ", "NNW": "↑ССЗ",
}


def _icon(code):
    return WEATHER_ICONS.get(code, "🌡")


def _wind(d):
    return WIND_DIRS.get(d, d)


def get_current_weather(city: str) -> str:
    try:
        r = requests.get(f"{BASE_URL}/current", params={
            "access_key": WEATHER_API_KEY,
            "query": city,
            "units": "m",
        }, timeout=10)
        data = r.json()

        if "error" in data:
            code = data["error"].get("code", "")
            info = data["error"].get("info", "Неизвестная ошибка")
            return f"❌ Ошибка API ({code}): {info}"

        loc = data["location"]
        cur = data["current"]
        icon = _icon(cur.get("weather_code", 0))
        desc = ", ".join(cur.get("weather_descriptions", [])) or "—"

        return (
            f"{icon} <b>Погода в {loc['name']}, {loc['country']}</b>\n"
            f"🕐 Обновлено: {cur['observation_time']}\n\n"
            f"🌡 Температура: <b>{cur['temperature']}°C</b> (ощущается как {cur['feelslike']}°C)\n"
            f"📋 {desc}\n\n"
            f"💨 Ветер: {_wind(cur['wind_dir'])} {cur['wind_speed']} км/ч\n"
            f"💧 Влажность: {cur['humidity']}%\n"
            f"🌂 Осадки: {cur['precip']} мм\n"
            f"☁️ Облачность: {cur['cloudcover']}%\n"
            f"👁 Видимость: {cur['visibility']} км\n"
            f"🕶 UV-индекс: {cur['uv_index']}\n"
        )
    except Exception as e:
        return f"❌ Ошибка: {e}"


def get_forecast(city: str, days: int = 3) -> str:
    try:
        r = requests.get(f"{BASE_URL}/forecast", params={
            "access_key": WEATHER_API_KEY,
            "query": city,
            "forecast_days": days,
            "units": "m",
        }, timeout=10)
        data = r.json()

        if "error" in data:
            code = data["error"].get("code", "")
            info = data["error"].get("info", "Неизвестная ошибка")
            # Код 105 = функция недоступна на бесплатном плане
            if code == 105:
                return (
                    "⚠️ Прогноз недоступен на бесплатном плане Weatherstack.\n\n"
                    "Используй /weather для текущей погоды — это работает бесплатно."
                )
            return f"❌ Ошибка API ({code}): {info}"

        loc = data["location"]
        cur = data["current"]
        icon = _icon(cur.get("weather_code", 0))
        desc = ", ".join(cur.get("weather_descriptions", [])) or "—"

        lines = [
            f"{icon} <b>Прогноз для {loc['name']}, {loc['country']}</b>\n",
            f"<b>Сейчас:</b> {cur['temperature']}°C, {desc}\n",
            "<b>Прогноз по дням:</b>",
        ]

        forecast = data.get("forecast", {})
        for date, day in list(forecast.items())[:days]:
            d_icon = _icon(day.get("weather_code", 0))
            d_desc = ", ".join(day.get("weather_descriptions", [])) or "—"
            lines.append(
                f"\n{d_icon} <b>{date}</b>\n"
                f"   🌡 {day['mintemp_c']}°C … {day['maxtemp_c']}°C (ср. {day['avgtemp_c']}°C)\n"
                f"   📋 {d_desc}\n"
                f"   🌂 Осадки: {day.get('total_precip_mm', 0)} мм"
            )

        return "\n".join(lines)
    except Exception as e:
        return f"❌ Ошибка: {e}"
