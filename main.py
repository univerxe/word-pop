from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiofiles
import json, asyncio, os, random
from dotenv import load_dotenv
from aiogram.utils.executor import start_webhook

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
    
messages = {
    "welcome": {
        "en": '''👋 Welcome {name} to the Word Pop Bot!\n\n
        Here's what I can do for you:\n
        ✅ Send hourly notifications for quiz to keep you on track.\n
        ✅ Start or stop notifications anytime you want.\n\n
        📚 Commands:\n
        /quiz - Start quiz in English.\n
        /quizru - Start quiz in Russian.\n
        /quit - Quit quiz.\n
        /learn - Learn new words.\n
        /sub - Start receiving notifications.\n
        /unsub - Stop receiving notifications.\n
        /cmd - Get a list of available commands.\n\n
        Let me know how I can assist you! 😊''',
        
        "ru": '''👋 Добро пожаловать {name} в бота Word Pop!\n\n
        Вот что я могу сделать для вас:\n
        ✅ Отправлять уведомления для викторины каждый час.\n
        ✅ Включать и выключать уведомления в любое время.\n\n
        📚 Команды:\n
        /quiz - Начать викторину на английском.\n
        /quizru - Начать викторину на русском.\n
        /quit - Закончить викторину.\n
        /learn - Изучать новые слова.\n
        /sub - Включить уведомления.\n
        /unsub - Выключить уведомления.\n
        /cmd - Получить список команд.\n\n
        Дайте мне знать, чем я могу помочь! 😊''',
        
        "ko": '''👋 Word Pop Bot에 오신 것을 환영합니다 {name}님!\n\n
        제가 할 수 있는 일입니다:\n
        ✅ 매시간 퀴즈 알림을 보내드립니다.\n
        ✅ 언제든지 알림을 시작하거나 중지할 수 있습니다.\n\n
        📚 명령어:\n
        /quiz - 영어 퀴즈 시작.\n
        /quizru - 러시아어 퀴즈 시작.\n
        /quit - 퀴즈 종료.\n
        /learn - 새로운 단어 학습.\n
        /sub - 알림 시작.\n
        /unsub - 알림 중지.\n
        /cmd - 사용 가능한 명령어 목록.\n\n
        도움이 필요하시면 알려주세요! 😊'''
    },
    "quiz": { 
        "en": "Which word correctly translate to Korean word: '{question}'",
        "ru": "Какое слово правильно переводится на корейский язык: '{question}'",
        "ko": "한국어 단어 '{question}'의 올바른 번역은 무엇입니까?"
    },
    "correct": {
        "en": "✅ Correct!",
        "ru": "✅ Правильно!",
        "ko": "✅ 정답!"
    },
    "incorrect": {
        "en": "❌ Incorrect! The correct answer was: {answer}",
        "ru": "❌ Неверно! Правильный ответ: {answer}",
        "ko": "❌ 틀렸습니다! 정답은: {answer}"
    }
}

user_language = {}  # {user_id: "en"}
    
@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message): 
    user_id = msg.from_user.id
    language = msg.from_user.language_code
    language = user_language.get(user_id, language)
    if language in ['ko', 'ko-KR', 'kor']: language = 'ko'
    elif language in ['ru', 'ru-RU', 'rus']: language = 'ru'
    user_language[user_id] = language
    welcome_text = messages["welcome"].get(language, messages["welcome"]["en"]).format(name=msg.from_user.first_name)
    
    await msg.answer(welcome_text)

@dp.message_handler(commands=['setlanguage'])
async def cmd_set_language(msg: types.Message):
    user_id = msg.from_user.id
    try:
        language = msg.text.split()[1].lower()[:2]
        # print(language)
        if language in ["en", "ru", "ko"]:
            user_language[user_id] = language
            await msg.answer(f"Language set to: {'English 🇺🇸' if language == 'en' else 'Korean 🇰🇷' if language == 'ko' else 'Russian 🇷🇺'}")
        else:
            user_language[user_id] = "en"
            await msg.answer(f"Invalid language. Supported languages are: English 🇺🇸, Korean 🇰🇷, Russian 🇷🇺")
    except IndexError:
        user_language[user_id] = "en"
        await msg.answer("Please specify a language 🇺🇸🇰🇷🇷🇺 : Eg. /setlanguage korean")

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
    
@dp.message_handler(commands=['quizru'])
async def cmd_quiz_ru(msg: types.Message):
    user_id = msg.from_user.id
    quiz_active[user_id] = True
    quiz_response = generate_quiz_question(user_language.get(user_id, "ru"))
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
        quiz_response = generate_quiz_question(current_quiz["lang"])
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
        
@dp.message_handler(commands=['lookup'])
async def cmd_lookup(msg: types.Message):
    await msg.answer("Please send me the work want to look up.")
    await msg.answer("🔍 You can lookup words in English or Russian.")
        
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
            await asyncio.sleep(43200)
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