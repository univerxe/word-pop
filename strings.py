messages = {        
    "welcome": {
    "en": '''👋 Welcome, {name}, to the Word Pop Bot! 🌟
    
Here's how I can help you achieve your language learning goals:
✅ Send periodic quiz notifications to keep you motivated and on track.
✅ Flexible controls to start or stop notifications anytime.

📚 Available Commands:
❓ /quiz - Start a fun and interactive quiz.
🚶‍♂️ /quit - Exit the current quiz session.
🌐 /setlanguage - Change your learning language (eg., /setlanguage korean).
📖 /learn - Expand your vocabulary with new words.
🔎 /lookup - Find translations or definitions in your personal dictionary.
🔔 /sub - Enable notifications for regular reminders.
🔕 /unsub - Disable notifications whenever you want.

🎯 Ready to dive into language learning? Let me know how I can assist you! 😊''',
        
    "ru": '''👋 Добро пожаловать, {name}, в бот Word Pop! 🌟
    
Вот как я могу помочь вам в достижении вашихязыковых целей:
✅ Отправляю периодические уведомления овикторинах, чтобы мотивировать вас и помогать вамоставаться напути к успеху.
✅ Гибкие настройки для начала или остановкиуведомлений в любое время.

📚 Доступные команды:
❓ /quiz - Начать интересную и увлекательнуювикторину.
🚶‍♂️ /quit - Завершить текущую сессию викторины.
🌐 /setlanguage - Изменить язык обучения(например, /setlanguage korean).
📖 /learn - Расширяйте словарный запас с новымисловами.
🔎 /lookup - Найдите переводы или определения ввашем личном словаре. 
🔔 /sub - Включить уведомления для регулярныхнапоминаний.
🔕 /unsub - Отключить уведомления в любое время

🎯 Готовы начать изучение языков? Дайте знать, какя могу вам помочь! 😊''',
    
    "ko": '''👋 {name}님, Word Pop Bot에 오신 것을 환영합니다! 🌟 

여러분의 언어 학습을 도와드릴 방법은 다음과 같습니다:
✅ 주기적인 퀴즈 알림으로 동기 부여
✅ 알림 시작/중지의 유연한 제어 

📚 사용 가능한 명령어:
❓ /quiz - 재미있는 퀴즈 시작
🚶‍♂️ /quit - 퀴즈 종료
🌐 /setlanguage - 언어 변경 (예: setlanguage korean)
📖 /learn - 새로운 단어 배우기
🔎 /lookup - 번역/정의 찾기
🔔 /sub - 정기 알림 활성화
🔕 /unsub - 알림 비활성화 

🎯 언어 학습을 시작할 준비가 되셨나요? 어떤 도움이 필요하신지 말씀해 주세요! 😊'''
},
    

    "quiz": { 
        "en": "Which word correctly translate to Korean word: '{question}'",
        "ru": "Какое слово правильно переводится на корейский язык: '{question}'",
        "ko": "한국어 단어 '{question}'의 올바른 번역은 무엇일까요? 함께 생각해봐요!"
    },
    "correct": {
        "en": "✅ Correct!",
        "ru": "✅ Правильно!",
        "ko": "✅ 정답이에요! 잘했어요!"
    },
    "incorrect": {
        "en": "❌ Incorrect! The correct answer was: {answer}",
        "ru": "❌ Неверно! Правильный ответ: {answer}",
        "ko": "❌ 틀렸어요! 정답은: {answer}입니다. 다음에 더 잘해봐요!"
    },
    "quiz_end": {
        "en": "Quiz ended. Thanks for playing!",
        "ru": "Викторина завершена. Спасибо за игру!",
        "ko": "퀴즈가 끝났어요! 참여해 주셔서 정말 감사합니다! 다음에 또 도전해 보세요!"
    },
    "quiz_not_active": {
        "en": "Quiz is not active. Use /quiz to start again.",
        "ru": "Викторина не активна. Используйте /quizru для начала.",
        "ko": "현재 퀴즈가 진행 중이 아니에요. 다시 시작하려면 /quiz를 입력해 주세요!"
    },
    "quiz_quit": {
        "en": "No active quiz to quit.",
        "ru": "Викторина не активна для завершения.",
        "ko": "종료할 활성 퀴즈가 없어요. 새로운 퀴즈를 시작해 보세요!"
    },
    "lookup": {
        "en": "Please send me the word you want to look up.",
        "ru": "Пожалуйста, отправьте мне слово, которое хотите найти.",
        "ko": "찾고 싶은 단어를 알려주세요! 함께 알아봐요."
    },
    "sub": {
        "en": "You are already subscribed to notifications.",
        "ru": "Вы уже подписаны на уведомления.",
        "ko": "이미 알림을 구독하고 계세요! 계속 함께해요."
    },
    "unsub": {
        "en": "You are not subscribed to notifications.",
        "ru": "Вы не подписаны на уведомления.",
        "ko": "아직 알림을 구독하고 있지 않아요. 구독해 보실래요?"
    },
    "setlanguage": {
        "en": "Language set to {language}",
        "ru": "Язык установлен на {language}",
        "ko": "언어가 {language}로 설정되었어요! 이제 더 편하게 사용하세요."
    },
    "invalid_language": {
        "en": "Invalid language. Please select a valid language.",
        "ru": "Недопустимый язык. Пожалуйста, выберите допустимый язык.",
        "ko": "잘못된 언어입니다. 유효한 언어를 선택해 주세요!"
    },
    "invalid_lang_idx": {
        "en": "Please specify a language 🇺🇸🇰🇷🇷🇺 : Eg. /setlanguage korean",
        "ru": "Укажите язык 🇺🇸🇰🇷🇷🇺 : Например /setlanguage russian",
        "ko": "언어를 지정해 주세요 🇺🇸🇰🇷🇷🇺 : 예. /setlanguage korean."
    },
    "subscribed": {
        "en": "You have successfully subscribed to hourly notifications! 🎉",
        "ru": "Вы успешно подписались на ежечасные уведомления! 🎉",
        "ko": "매시간 알림을 성공적으로 구독했어요! 🎉 이제 놓치는 거 없이 함께해요!"
    },
    "already_subscribed": {
        "en": "You are already subscribed to notifications! 😊",
        "ru": "Вы уже подписаны на уведомления! 😊",
        "ko": "이미 알림을 구독하고 계세요! 😊 계속 함께해요!"
    },
    "unsubscribed": {
        "en": "You have successfully unsubscribed from hourly notifications! 😊",
        "ru": "Вы успешно отписались от ежечасных уведомлений! 😊",
        "ko": "매시간 알림 구독을 성공적으로 취소했어요! 😊 다음에 또 만나요!"
    },
    "not_subscribed": {
        "en": "You are not subscribed to notifications! 😢",
        "ru": "Вы не подписаны на уведомления! 😢",
        "ko": "아직 알림을 구독하고 있지 않아요! 😢 구독해 보실래요?"
    },
    "reminder": {
        "en": "⏰ Don't forget to practice your vocabulary!",
        "ru": "⏰ Не забудьте попрактиковать свой словарный запас!",
        "ko": "⏰ 어휘 연습하는 거 잊지 마세요! 함께 성장해요!"
    }
}

