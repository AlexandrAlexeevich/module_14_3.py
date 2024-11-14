import telebot
from telebot import types

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Создание главной клавиатуры
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buy_button = types.KeyboardButton("Купить")
main_keyboard.add(buy_button)

# Функция для отправки списка продуктов
def get_buying_list(message):
    products = [
        {"name": "сыр", "description": "Российский", "price": 200},
        {"name": "Колбаса", "description": "молочная", "price": 300},
        {"name": "молоко3", "description": "3.5", "price": 100},
        {"name": "хлеб", "description": "столичный", "price": 40

    for product in products:
        bot.send_message(message.chat.id,
                         f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}')
        # Здесь замените 'image_url' на фактический URL изображения продукта
        # bot.send_photo(message.chat.id, 'image_url')

    # Создание Inline клавиатуры
    inline_keyboard = types.InlineKeyboardMarkup()
    for product in products:
        button = types.InlineKeyboardButton(product["name"], callback_data="product_buying")
        inline_keyboard.add(button)

    bot.send_message(message.chat.id, "Выберите продукт для покупки:", reply_markup=inline_keyboard)

# Хэндлер для кнопки "Купить"
@bot.message_handler(func=lambda message: message.text == "Купить")
def handle_buy(message):
    get_buying_list(message)

# Хэндлер для callback_data
@bot.callback_query_handler(func=lambda call: call.data == "product_buying")
def send_confirm_message(call):
    bot.answer_callback_query(call.id)  # Убирает вращающийся значок на кнопке
    bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")

bot.polling()
