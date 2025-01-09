from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiofiles
import json, asyncio, os, random
from dotenv import load_dotenv
from aiogram.utils.executor import start_webhook
from strings import messages

load_dotenv()
# token = os.getenv('WORD_POP_TOKEN')
token = os.getenv('TEST_BOT_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

with open('./vocab_en_ru.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    korean = [kr["Korean"] for kr in data ]
    english = [en["English"] for en in data]
    russian = [ru["Russian"] for ru in data]

def get_message(user_id, key, **kwargs):
    lang = user_language.get(user_id, "en")
    return messages[key].get(lang, messages[key]["en"]).format(**kwargs)

user_language = {}  # {user_id: "en"}
    
@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message): 
    user_id = msg.from_user.id
    language = msg.from_user.language_code
    language = user_language.get(user_id, language)
    if language in ['ko', 'ko-KR', 'kor']: language = 'ko'
    elif language in ['ru', 'ru-RU', 'rus']: language = 'ru'
    user_language[user_id] = language
    welcome_text = get_message(user_id, "welcome", name=msg.from_user.first_name)
    await msg.answer(welcome_text)

@dp.message_handler(commands=['setlanguage'])
async def cmd_set_language(msg: types.Message):
    user_id = msg.from_user.id
    try:
        language = msg.text.split()[1].lower()[:2]
        # print(language)
        if language in ["en", "ru", "ko"]:
            user_language[user_id] = language
            await msg.answer(get_message(user_id, "setlanguage", language=language))
        else:
            user_language[user_id] = user_language.get(user_id, "en")
            await msg.answer(get_message(user_id, "invalid_language"))
    except IndexError:
        user_language[user_id] = user_language.get(user_id, "en")
        await msg.answer(get_message(user_id, "invalid_lang_idx"))

quiz_active = {}  # {user_id: True}
quiz_state = {}  # {user_id: {question: "", answer: "", options: [], lang: ""}}

def generate_quiz_question(lang) -> dict:
    random_index = random.randint(0, len(data)-1)
    question = korean[random_index]
    
    if lang == "ru":
        answer = russian[random_index]
        options = random.sample([r for r in russian if r != answer], 3) + [answer]
    else:
        answer = english[random_index]
        options = random.sample([e for e in english if e != answer], 3) + [answer]
        
    random.shuffle(options)
    return {"question": question, "answer": answer, "options": options, "lang": lang}

@dp.message_handler(commands=['quiz'])
async def cmd_quiz(msg: types.Message):
    user_id = msg.from_user.id
    quiz_active[user_id] = True
    quiz_response = generate_quiz_question(user_language.get(user_id, "en"))
    quiz_state[user_id] = quiz_response
    await send_quiz_question(msg, quiz_response["question"], quiz_response["options"])

async def send_quiz_question(msg, question, options):
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=opt, callback_data=f"quiz_{i}") for i, opt in enumerate(options)]
    keyboard.add(*buttons)
    lang = user_language.get(msg.from_user.id, "en")
    quiz_text = messages["quiz"][lang].format(question=question)
    await msg.answer(quiz_text, reply_markup=keyboard)
    
@dp.callback_query_handler(lambda c: c.data.startswith("quiz_"))
async def handle_quiz_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    lang = user_language.get(user_id, "en")
    if user_id not in quiz_active:
        await callback_query.answer(get_message(user_id, "quiz_not_active", language=lang), show_alert=True, cache_time=3)
        return

    selected_index = int(callback_query.data.split("_")[1])
    current_quiz = quiz_state.get(user_id, {})
    selected_option = current_quiz.get("options")[selected_index]
    
    if selected_option == current_quiz.get("answer"):
        response = get_message(user_id, "correct")
    else:
        response = get_message(user_id, "incorrect", answer=current_quiz.get("answer"))

    await callback_query.message.edit_text(
        f"{callback_query.message.text}\n\n{selected_option}\n\n{response}"
    )
    
    await asyncio.sleep(2)
    if user_id in quiz_active:
        quiz_response = generate_quiz_question(current_quiz["lang"])
        quiz_state[user_id] = quiz_response
        await send_quiz_question(callback_query.message, quiz_response["question"], quiz_response["options"])

@dp.message_handler(commands=['quit'])
async def cmd_quit(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in quiz_active:
        del quiz_active[user_id]
        await msg.answer(get_message(user_id, "quiz_end"))
    else:
        await msg.answer(get_message(user_id, "quiz_quit"))
        
@dp.message_handler(commands=['lookup'])
async def cmd_lookup(msg: types.Message):
    await msg.answer(get_message(msg.from_user.id, "lookup"))
        
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
            await bot.send_message(user_id, get_message(user_id, "reminder"))
            await asyncio.sleep(43200)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(e)
        
async def sub_user(bot, user_id) -> str:
    if user_id not in sub_users:
        sub_users[user_id] = asyncio.create_task(notify_user(bot, user_id))
        return get_message(user_id, "subscribed")
    else:
        return get_message(user_id, "already_subscribed")
    
async def unsub_user(user_id) -> str:
    if user_id in sub_users:
        sub_users[user_id].cancel()
        del sub_users[user_id]
        return get_message(user_id, "unsubscribed")
    else:
        return get_message(user_id, "not_subscribed")

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