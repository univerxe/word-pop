messages = {        
    "welcome": {
    "en": '''👋 Welcome, {name}, to the Word Pop Bot! 🌟\n
Here's how I can help you achieve your language learning goals:
✅ Send periodic quiz notifications to keep you motivated and on track.
✅ Flexible controls to start or stop notifications anytime.\n
📚 Available Commands:
❓ /quiz - Start a fun and interactive quiz.
🚶‍♂️ /quit - Exit the current quiz session.
🌐 /setlanguage - Change your learning language (eg., /setlanguage korean).
📖 /learn - Expand your vocabulary with new words.
🔎 /lookup - Find translations or definitions in your personal dictionary.
🔔 /sub - Enable notifications for regular reminders.
🔕 /unsub - Disable notifications whenever you want.\n
🎯 Ready to dive into language learning? Let me know how I can assist you! 😊''',
        
    "ru": '''👋 Добро пожаловать, {name}, в бот Word Pop! 🌟\n
Вот как я могу помочь вам в достижении вашихязыковых целей:
✅ Отправляю периодические уведомления овикторинах, чтобы мотивировать вас и помогать вамоставаться напути к успеху.
✅ Гибкие настройки для начала или остановкиуведомлений в любое время.\n
📚 Доступные команды:
❓ /quiz - Начать интересную и увлекательнуювикторину.
🚶‍♂️ /quit - Завершить текущую сессию викторины.
🌐 /setlanguage - Изменить язык обучения(например, /setlanguage korean).
📖 /learn - Расширяйте словарный запас с новымисловами.
🔎 /lookup - Найдите переводы или определения ввашем личном словаре.
🔔 /sub - Включить уведомления для регулярныхнапоминаний.
🔕 /unsub - Отключить уведомления в любое время\n
🎯 Готовы начать изучение языков? Дайте знать, какя могу вам помочь! 😊''',
    
    "ko": '''👋 {name}님, Word Pop Bot에 오신 것을 환영합니다! 🌟\n
제가 여러분의 언어 학습 목표를 도와드릴 수 있는 방법은다음과 같습니다:
✅ 주기적으로 퀴즈 알림을 보내드려 동기부여를 유지하고학습을 지속할 수 있도록 도와드립니다.
✅ 알림을 언제든지 시작하거나 중지할 수 있는 유연한제어 기능.\n
📚 사용 가능한 명령어:
❓ /quiz - 재미있고 인터랙티브한 퀴즈를 시작합니다.
🚶‍♂️ /quit - 현재 퀴즈 세션을 종료합니다.
🌐 /setlanguage - 학습 언어를 변경합니다 (예: setlanguage korean).
📖 /learn - 새로운 단어로 어휘력을 확장합니다.
🔎 /lookup - 개인 사전에서 번역이나 정의를 찾아봅니다
🔔 /sub - 정기 알림을 활성화합니다.
🔕 /unsub - 언제든지 알림을 비활성화합니다.\n
🎯 언어 학습을 시작할 준비가 되셨나요? 도와드릴방법을 알려주세요! 😊'''
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