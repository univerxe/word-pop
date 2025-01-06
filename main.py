from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json, asyncio, os, random
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('WORD_POP_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

subscribed_users = []

with open('./vocab.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    korean = [kr["Korean"] for kr in data ]
    english = [en["English"] for en in data]

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message): 
    welcome_text = (
        f"👋 Welcome {msg.from_user.first_name} to the Word Pop Bot!\n\n"
        "Here's what I can do for you:\n"
        "✅ Send hourly notifications for quiz to keep you on track.\n"
        "✅ Customize notification intervals with a simple command.\n"
        "✅ Start or stop notifications anytime you want.\n\n"
        "📚 Commands:\n"
        "/subscribe - Start receiving notifications.\n"
        "/unsubscribe - Stop receiving notifications.\n"
        "/quiz - Start quiz.\n"
        "/quit - Quit quiz.\n"
        "/learn - Learn new words.\n"
        "/help - Get a list of available commands.\n\n"
        "Let me know how I can assist you! 😊"
    )
    await msg.answer(welcome_text)

@dp.message_handler(commands=['subscribe'])
async def cmd_subscribe(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in subscribed_users:
        subscribed_users.append(user_id)
        await msg.answer(
        f"You have successfully subscribed to hourly notifications! 🎉 \n\n"
        )
    else:
        await msg.answer("You are already subscribed to notifications! 😊")
        
@dp.message_handler(commands=['unsubscribe'])
async def cmd_unsubscribe(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in subscribed_users:
        subscribed_users.remove(user_id)
        await msg.answer("You have successfully unsubscribed from notifications! 😢")
    else:
        await msg.answer("You are not subscribed to notifications! 😊")

current_question = None
correct_answer = None
current_options = None
quiz_active = {}  # {user_id: True}

def generate_quiz_question() -> tuple:
    global current_question, correct_answer, current_options
    random_index = random.randint(0, len(data)-1)
    current_question = korean[random_index]
    correct_answer = english[random_index]
    current_options = random.sample([e for e in english if e != correct_answer], 3) + [correct_answer]
    random.shuffle(current_options)
    return current_question, correct_answer, current_options

@dp.message_handler(commands=['quiz']) 
async def cmd_quiz(msg: types.Message):
    user_id = msg.from_user.id
    quiz_active[user_id] = True
    question, answer, options = generate_quiz_question()
    await send_quiz_question(msg, question, options)

@dp.message_handler(commands=['quit'])
async def cmd_quit(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in quiz_active:
        del quiz_active[user_id]
        await msg.answer("Quiz ended. Thanks for playing!")
    else:
        await msg.answer("No active quiz to quit.")

async def send_quiz_question(msg, question, options):
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=opt, callback_data=f"quiz_{opt}") for opt in options]
    keyboard.add(*buttons)
    await msg.answer(f"Which word correctly translate to Korean word: '{question}'", reply_markup=keyboard)
    
@dp.callback_query_handler(lambda c: c.data.startswith("quiz_"))
async def handle_quiz_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in quiz_active:
        await callback_query.answer("Quiz is not active. Use /quiz to start again.")
        return

    selected_option = callback_query.data.split("_")[1]
    if selected_option == correct_answer:
        response = "✅ Correct!"
    else:
        response = f"❌ Incorrect! The correct answer was: {correct_answer}"

    await callback_query.message.edit_text(
        f"{callback_query.message.text}\n\n{selected_option}\n\n{response}"
    )
    
    # Automatically send next question after a brief delay
    await asyncio.sleep(2)
    if user_id in quiz_active:
        question, answer, options = generate_quiz_question()
        await send_quiz_question(callback_query.message, question, options)

@dp.message_handler(commands=['learn'])
async def cmd_vocab(msg: types.Message):
    formatted_text = '\n'.join([f"{k} - {e}" for k, e in list(zip(korean, english))[:]])
    await msg.answer(formatted_text)
    
async def send_notifications():
    while True:
        for user_id in subscribed_users:
            await bot.send_message(user_id, "Hello")    
        
        await asyncio.sleep(5)
        
@dp.message_handler(commands=['help'])
async def cmd_help(msg: types.Message):
    help_text = (
        "📚 Here's a list of available commands:\n\n"
        "/subscribe - Start receiving notifications.\n"
        "/unsubscribe - Stop receiving notifications.\n"
        "/quiz - Start quiz.\n"
        "/quit - Quit quiz.\n"
        "/learn - Learn new words.\n"
        "/help - Get a list of available commands.\n\n"
        "Let me know how I can assist you! 😊"
    )
    await msg.answer(help_text)

async def on_startup(_):
    asyncio.create_task(send_notifications())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)