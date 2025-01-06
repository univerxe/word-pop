from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiofiles
import json, asyncio, os, random
from dotenv import load_dotenv
from aiogram.utils.executor import start_webhook

load_dotenv()
token = os.getenv('WORD_POP_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

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
        "/quiz - Start quiz.\n"
        "/quit - Quit quiz.\n"
        "/learn - Learn new words.\n"
        "/sub - Start receiving notifications.\n"
        "/unsub - Stop receiving notifications.\n"
        "/cmd - Get a list of available commands.\n\n"
        "Let me know how I can assist you! 😊"
    )
    await msg.answer(welcome_text)

quiz_active = {}  # {user_id: True}
quiz_state = {}  # {user_id: {question: "", answer: "", options: []}}

def generate_quiz_question() -> dict:
    random_index = random.randint(0, len(data)-1)
    question = korean[random_index]
    answer = english[random_index]
    options = random.sample([e for e in english if e != answer], 3) + [answer]
    random.shuffle(options)
    return {"question": question, "answer": answer, "options": options}

@dp.message_handler(commands=['quiz']) 
async def cmd_quiz(msg: types.Message):
    user_id = msg.from_user.id
    quiz_active[user_id] = True
    quiz_response = generate_quiz_question()
    # print(quiz_response)
    quiz_state[user_id] = quiz_response
    # print(quiz_state)
    await send_quiz_question(msg, quiz_response["question"], quiz_response["options"])

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
    current_quiz = quiz_state.get(user_id, {})
    if selected_option == current_quiz.get("answer"):
        response = "✅ Correct!"
    else:
        response = f"❌ Incorrect! The correct answer was: {current_quiz.get('answer')}"

    await callback_query.message.edit_text(
        f"{callback_query.message.text}\n\n{selected_option}\n\n{response}"
    )
    
    await asyncio.sleep(2)
    if user_id in quiz_active:
        quiz_response = generate_quiz_question()
        quiz_state[user_id] = quiz_response
        await send_quiz_question(callback_query.message, quiz_response["question"], quiz_response["options"])

@dp.message_handler(commands=['quit'])
async def cmd_quit(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in quiz_active:
        del quiz_active[user_id]
        await msg.answer("Quiz ended. Thanks for playing!")
    else:
        await msg.answer("No active quiz to quit.")
        
sub_users = {}

@dp.message_handler(commands=['sub'])
async def cmd_subscribe(msg: types.Message):
    user_id = msg.from_user.id
    response = await sub_user(bot, user_id)
    await msg.answer(response)
    
@dp.message_handler(commands=['unsub'])
async def cmd_unsubscribe(msg: types.Message):
    user_id = msg.from_user.id
    response = await unsub_user(user_id)
    await msg.answer(response)

async def notify_user(bot, user_id):
    try:
        while True:
            await bot.send_message(user_id, "⏰ Don't forget to practice your vocabulary!")
            await asyncio.sleep(5)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(e)
        
async def sub_user(bot, user_id) -> str:
    if user_id not in sub_users:
        sub_users[user_id] = asyncio.create_task(notify_user(bot, user_id))

        return (f"You have successfully subscribed to hourly notifications! 🎉"
        )
    else:
        return ("You are already subscribed to notifications! 😊")
    
async def unsub_user(user_id) -> str:
    if user_id in sub_users:
        sub_users[user_id].cancel()
        del sub_users[user_id]
        return ("You have successfully unsubscribed from notifications! 😢")
    else:
        return ("You are not subscribed to notifications! 😊")

@dp.message_handler(commands=['learn'])
async def cmd_vocab(msg: types.Message):
    formatted_text = '\n'.join([f"{k} - {e}" for k, e in list(zip(korean, english))[:]])
    await msg.answer(formatted_text)
        
@dp.message_handler(commands=['cmd'])
async def cmd_help(msg: types.Message):
    help_text = (
        "📚 Here's a list of available commands:\n\n"
        "/quiz - Start quiz.\n"
        "/quit - Quit quiz.\n"
        "/learn - Learn new words.\n"
        "/sub - Start receiving notifications.\n"
        "/unsub - Stop receiving notifications.\n"
        "/cmd - Get a list of available commands.\n\n"
        "Let me know how I can assist you! 😊"
    )
    await msg.answer(help_text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)