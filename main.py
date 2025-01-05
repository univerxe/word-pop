from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.filter import Command
import json
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('WORD_POP_TOKEN')
print(token)

# token = "7921174919:AAGE7xRICsMAY6jsBrjJt4MkPb1Da2U54E0"

bot = Bot(token)
dp = Dispatcher(bot)

subscribed_users = []

with open('./vocab.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    korean = [kr["Korean"] for kr in data ]
    english = [en["English"] for en in data]
    # print('\n'.join(korean)) 
    
with open('./quiz.json', 'r', encoding = "utf-8") as file:
    quiz_data = json.load(file)
    questions = [ques["question"] for ques in quiz_data]
    answers = [ans["answer"] for ans in quiz_data]
    options = [opt["options"] for opt in quiz_data]

@dp.message_handler(commands=['quiz'])
async def cmd_quiz(msg: types.Message):
    # Get the first quiz question (you can randomize this later)
    current_quiz = quiz_data[0]
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=option, callback_data=option) for option in current_quiz["options"]]
    keyboard.add(*buttons)
    
    await msg.answer(current_quiz["question"], reply_markup=keyboard)

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message): 
    welcome_text = (
        f"👋 Welcome {msg.from_user.first_name} to the Word Pop Bot!\n\n"
        "Here's what I can do for you:\n"
        "✅ Send hourly notifications to keep you on track.\n"
        "✅ Customize notification intervals with a simple command.\n"
        "✅ Start or stop notifications anytime you want.\n\n"
        "📚 Commands:\n"
        "/subscribe - Start receiving notifications.\n"
        "/unsubscribe - Stop receiving notifications.\n"
        "/notify - Set a custom notification interval (coming soon).\n"
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
        "Set the time interval for notifications . \n"
        "Example"
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

@dp.message_handler(commands=['vocab'])
async def cmd_vocab(msg: types.Message):
    formatted_text = '\n'.join([f"{k} - {e}" for k, e in list(zip(korean, english))[:5]])
    await msg.answer(formatted_text)
    
async def send_notifications():
    while True:
        for user_id in subscribed_users:
            await bot.send_message(user_id, "Hello")    
        
        await asyncio.sleep(5)

async def on_startup(_):
    asyncio.create_task(send_notifications())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




# @dp.message_handler(commands=['start']) 
# async def cmd_start(msg: types.Message):
#     formatted_text = '\n'.join([f"{k} - {e}" for k, e in zip(korean, english)])
#     await msg.answer(formatted_text)








    