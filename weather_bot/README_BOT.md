# 🌤 Weather Telegram Bot

Бот погоды на основе Weatherstack API + aiogram 3.

## Команды бота

| Команда | Описание |
|---------|----------|
| `/weather Москва` | Текущая погода |
| `/forecast Лондон` | Прогноз на 3 дня |
| `Берлин` | Просто напиши город — получишь погоду |

---

## 🚀 Деплой на Railway

### 1. Получи токены

- **Telegram Bot Token** → [@BotFather](https://t.me/BotFather) → `/newbot`
- **Weatherstack API Key** → [weatherstack.com](https://weatherstack.com) → бесплатный план

### 2. Залей на GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ВАШ_НИК/weather-bot.git
git push -u origin main
```

### 3. Создай проект на Railway

1. Зайди на [railway.app](https://railway.app) → New Project → Deploy from GitHub
2. Выбери свой репозиторий
3. Перейди в **Variables** и добавь:

```
BOT_TOKEN=7123456789:AAF...твой_токен...
WEATHERSTACK_API_KEY=abc123...твой_ключ...
```

4. Railway автоматически запустит бота через `python bot.py`

---

## 🚀 Деплой на Render

1. Зайди на [render.com](https://render.com) → New → **Background Worker**
2. Подключи GitHub репозиторий
3. Настройки:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
4. Добавь переменные окружения:
   - `BOT_TOKEN`
   - `WEATHERSTACK_API_KEY`

---

## 💻 Локальный запуск

```bash
# Установи зависимости
pip install -r requirements.txt

# Установи переменные
export BOT_TOKEN="твой_токен"
export WEATHERSTACK_API_KEY="твой_ключ"

# Запусти
python bot.py
```

---

## 📁 Структура проекта

```
weather-bot/
├── bot.py              # Основной файл бота (aiogram)
├── weather.py          # Сервис погоды (Weatherstack API)
├── swagger_client/     # Авто-сгенерированный клиент API
├── requirements.txt
├── Procfile
└── railway.json
```
