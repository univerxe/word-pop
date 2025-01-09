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
    },
    "quiz_end": {
        "en": "Quiz ended. Thanks for playing!",
        "ru": "Викторина завершена. Спасибо за игру!",
        "ko": "퀴즈가 종료되었습니다. 플레이 해주셔서 감사합니다!"
    },
    "quiz_not_active": {
        "en": "Quiz is not active. Use /quiz to start again.",
        "ru": "Викторина не активна. Используйте /quizru для начала.",
        "ko": "퀴즈가 활성화되지 않았습니다. 다시 시작하려면 /quiz를 사용하십시오."
    },
    "quiz_quit": {
        "en": "No active quiz to quit.",
        "ru": "Викторина не активна для завершения.",
        "ko": "종료할 활성 퀴즈가 없습니다."
    },
    "lookup": {
        "en": "Please send me the word you want to look up.",
        "ru": "Пожалуйста, отправьте мне слово, которое хотите найти.",
        "ko": "찾고 싶은 단어를 보내주세요."
    },
    "sub": {
        "en": "You are already subscribed to notifications.",
        "ru": "Вы уже подписаны на уведомления.",
        "ko": "이미 알림을 받고 있습니다."
    },
    "unsub": {
        "en": "You are not subscribed to notifications.",
        "ru": "Вы не подписаны на уведомления.",
        "ko": "알림을 받고 있지 않습니다."
    },
    "setlanguage": {
        "en": "Language set to {language}",
        "ru": "Язык установлен на {language}",
        "ko": "언어가 {language}로 설정되었습니다"
    },
    "invalid_language": {
        "en": "Invalid language. Please select a valid language.",
        "ru": "Недопустимый язык. Пожалуйста, выберите допустимый язык.",
        "ko": "잘못된 언어입니다. 유효한 언어를 선택하세요."
    },
    "invalid_lang_idx": {
        "en": "Please specify a language 🇺🇸🇰🇷🇷🇺 : Eg. /setlanguage korean",
        "ru": "Укажите язык 🇺🇸🇰🇷🇷🇺 : Например /setlanguage russian",
        "ko": "언어를 지정하세요 🇺🇸🇰🇷🇷🇺 : 예. /setlanguage korean"
    },
    "subscribed": {
        "en": "You have successfully subscribed to hourly notifications! 🎉",
        "ru": "Вы успешно подписались на ежечасные уведомления! 🎉",
        "ko": "매시간 알림을 성공적으로 구독하셨습니다! 🎉"
    },
    "already_subscribed": {
        "en": "You are already subscribed to notifications! 😊",
        "ru": "Вы уже подписаны на уведомления! 😊",
        "ko": "이미 알림을 받고 있습니다! 😊"
    },
    "unsubscribed": {
        "en": "You have successfully unsubscribed from hourly notifications! 😊",
        "ru": "Вы успешно отписались от ежечасных уведомлений! 😊",
        "ko": "매시간 알림 구독을 성공적으로 취소하셨습니다! 😊"
    },
    "not_subscribed": {
        "en": "You are not subscribed to notifications! 😢",
        "ru": "Вы не подписаны на уведомления! 😢",
        "ko": "알림을 받고 있지 않습니다! 😢"
    },
    "reminder": {
        "en": "⏰ Don't forget to practice your vocabulary!",
        "ru": "⏰ Не забудьте попрактиковать свой словарный запас!",
        "ko": "⏰ 어휘력을 연습하는 것을 잊지 마세요!"
    }
}