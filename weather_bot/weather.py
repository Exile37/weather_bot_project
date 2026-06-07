import os
import swagger_client
from swagger_client.rest import ApiException

WEATHER_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# Иконки для кодов погоды Weatherstack
WEATHER_ICONS = {
    113: "☀️",   # Ясно
    116: "⛅️",  # Переменная облачность
    119: "☁️",  # Облачно
    122: "☁️",  # Пасмурно
    143: "🌫",   # Туман
    176: "🌦",   # Местами дождь
    179: "🌨",   # Местами снег
    182: "🌧",   # Мокрый снег
    185: "🌧",   # Морось с заморозками
    200: "⛈",   # Гроза
    227: "🌨",   # Метель
    230: "❄️",  # Вьюга
    248: "🌫",   # Туман с заморозками
    260: "🌫",   # Морозный туман
    263: "🌦",   # Лёгкий моросящий дождь
    266: "🌧",   # Морось
    281: "🌧",   # Замерзающая морось
    284: "🌧",   # Сильная замерзающая морось
    293: "🌦",   # Лёгкий дождь
    296: "🌧",   # Дождь
    299: "🌧",   # Умеренный дождь
    302: "🌧",   # Сильный дождь
    305: "🌧",   # Проливной дождь
    308: "🌧",   # Очень сильный дождь
    311: "🌧",   # Лёгкий замерзающий дождь
    314: "🌧",   # Замерзающий дождь
    317: "🌨",   # Снег с дождём
    320: "🌨",   # Лёгкий снег
    323: "❄️",  # Снег
    326: "❄️",  # Умеренный снег
    329: "❄️",  # Сильный снег
    332: "❄️",  # Очень сильный снег
    335: "❄️",  # Метель
    338: "❄️",  # Буран
    350: "🌨",   # Ледяной дождь
    353: "🌦",   # Лёгкий ливень
    356: "🌧",   # Ливень
    359: "🌧",   # Проливной ливень
    362: "🌨",   # Снег с дождём
    365: "🌨",   # Сильный снег с дождём
    368: "🌨",   # Лёгкий снегопад
    371: "❄️",  # Сильный снегопад
    374: "🌨",   # Лёгкий ледяной дождь
    377: "🌨",   # Ледяной дождь
    386: "⛈",   # Гроза с дождём
    389: "⛈",   # Сильная гроза с дождём
    392: "⛈",   # Гроза со снегом
    395: "⛈",   # Сильная гроза со снегом
}

WIND_DIRS = {
    "N": "↑ С", "NNE": "↑ ССВ", "NE": "↗ СВ", "ENE": "→ ВСВ",
    "E": "→ В", "ESE": "→ ВЮВ", "SE": "↘ ЮВ", "SSE": "↓ ЮЮВ",
    "S": "↓ Ю", "SSW": "↓ ЮЮЗ", "SW": "↙ ЮЗ", "WSW": "← ЗЮЗ",
    "W": "← З", "WNW": "← ЗСЗ", "NW": "↖ СЗ", "NNW": "↑ ССЗ",
}


def _get_api():
    configuration = swagger_client.Configuration()
    configuration.api_key["access_key"] = WEATHER_API_KEY
    return swagger_client.DefaultApi(swagger_client.ApiClient(configuration))


def _weather_icon(code):
    return WEATHER_ICONS.get(code, "🌡")


def _wind_dir(direction):
    return WIND_DIRS.get(str(direction), str(direction))


def get_current_weather(city: str) -> str:
    try:
        api = _get_api()
        resp = api.get_current_weather(
            access_key=WEATHER_API_KEY,
            query=city,
            units="m",
            language="ru",
        )

        if not resp or not resp.current:
            return "❌ Не удалось получить погоду. Проверь название города."

        loc = resp.location
        cur = resp.current
        icon = _weather_icon(cur.weather_code)
        desc = ", ".join(cur.weather_descriptions) if cur.weather_descriptions else "—"

        return (
            f"{icon} <b>Погода в {loc.name}, {loc.country}</b>\n"
            f"🕐 Обновлено: {cur.observation_time}\n\n"
            f"🌡 Температура: <b>{cur.temperature}°C</b> (ощущается как {cur.feelslike}°C)\n"
            f"📋 {desc}\n\n"
            f"💨 Ветер: {_wind_dir(cur.wind_dir)} {cur.wind_speed} км/ч\n"
            f"💧 Влажность: {cur.humidity}%\n"
            f"🌂 Осадки: {cur.precip} мм\n"
            f"☁️ Облачность: {cur.cloudcover}%\n"
            f"👁 Видимость: {cur.visibility} км\n"
            f"🕶 UV-индекс: {cur.uv_index}\n"
        )

    except ApiException as e:
        return f"❌ Ошибка API: {e.status} — {e.reason}"
    except Exception as e:
        return f"❌ Ошибка: {e}"


def get_forecast(city: str, days: int = 3) -> str:
    try:
        api = _get_api()
        resp = api.get_weather_forecast(
            access_key=WEATHER_API_KEY,
            query=city,
            forecast_days=days,
            hourly=0,
            units="m",
            language="ru",
        )

        if not resp or not resp.forecast:
            return "❌ Не удалось получить прогноз. Проверь название города."

        loc = resp.location
        cur = resp.current
        icon = _weather_icon(cur.weather_code)
        desc = ", ".join(cur.weather_descriptions) if cur.weather_descriptions else "—"

        lines = [
            f"{icon} <b>Прогноз для {loc.name}, {loc.country}</b>\n",
            f"<b>Сейчас:</b> {cur.temperature}°C, {desc}\n",
        ]

        forecast_data = resp.forecast
        # forecast — это объект ForecastResponseForecast, дни лежат в .forecast_day
        day_list = forecast_data.forecast_day if hasattr(forecast_data, "forecast_day") else []

        if not day_list and hasattr(forecast_data, "to_dict"):
            # Fallback: попробуем достать через словарь
            d = forecast_data.to_dict()
            # ключ может быть датой
            day_list = list(d.values()) if d else []

        if not day_list:
            lines.append("\n⚠️ Данные прогноза недоступны на вашем тарифе Weatherstack.")
        else:
            lines.append("\n<b>Прогноз по дням:</b>")
            for day in day_list[:days]:
                day_dict = day.to_dict() if hasattr(day, "to_dict") else day
                date = day_dict.get("date", "—")
                max_t = day_dict.get("maxtemp_c") or day_dict.get("max_temp") or "?"
                min_t = day_dict.get("mintemp_c") or day_dict.get("min_temp") or "?"
                avg_t = day_dict.get("avgtemp_c") or day_dict.get("avg_temp") or "?"
                precip = day_dict.get("total_precip_mm") or day_dict.get("precip") or 0
                code = day_dict.get("weather_code")
                d_icon = _weather_icon(code) if code else "🌡"
                descriptions = day_dict.get("weather_descriptions") or []
                d_desc = ", ".join(descriptions) if descriptions else "—"

                lines.append(
                    f"\n{d_icon} <b>{date}</b>\n"
                    f"   🌡 {min_t}°C … {max_t}°C (ср. {avg_t}°C)\n"
                    f"   📋 {d_desc}\n"
                    f"   🌂 Осадки: {precip} мм"
                )

        return "\n".join(lines)

    except ApiException as e:
        return f"❌ Ошибка API: {e.status} — {e.reason}"
    except Exception as e:
        return f"❌ Ошибка: {e}"
