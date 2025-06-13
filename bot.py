import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglashni yoqish (xatoliklarni ko'rish uchun foydali)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Foydalanuvchi /start buyrug'ini yuborganda ishga tushadi."""
    
    user_name = update.message.from_user.first_name
    
    # Yangi, mazmunli xabar matni
    welcome_text = (
        f"Salom, {user_name}! 🌿\n\n"
        f"**Florix - O'simlik Tashxis Tizimi**ga xush kelibsiz!\n\n"
        f"Bu yerda siz o'simliklaringizdagi kasalliklar yoki zararkunandalarni "
        f"rasm orqali osongina aniqlashingiz mumkin.\n\n"
        f"Tashxisni boshlash uchun quyidagi tugmani bosing."
    )
    
    # Web App ma'lumotlari
    web_app = WebAppInfo(url="https://florix.vercel.app/")

    # Yangi, aniqroq tugma matni
    button = InlineKeyboardButton(
        text="🔍 Tashxisni Boshlash",  # Tugma matni
        web_app=web_app
    )

    # Klaviatura yaratish
    keyboard = InlineKeyboardMarkup([[button]])

    # Xabar yuborish. Matnni "MarkdownV2" formatida yuboramiz.
    # Bu **qalin** yozuv kabi formatlashni qo'llab-quvvatlaydi.
    # Telegramda buni to'g'ri ko'rsatish uchun ba'zi belgilar oldidan "\" qo'yish kerak.
    # Lekin f-string bilan oddiyroq bo'lishi uchun formatsiz variant ham yaxshi.
    # Quyida formatsiz, ammo ishonchli variant:
    
    welcome_text_simple = (
        f"Salom, {user_name}! 🌿\n\n"
        f"Florix - O'simlik Tashxis Tizimiga xush kelibsiz!\n\n"
        f"O'simlikingizdagi kasallik yoki zararkunandani rasm orqali aniqlash uchun "
        f"quyidagi tugmani bosing."
    )
    
    await update.message.reply_text(
        welcome_text_simple,
        reply_markup=keyboard
    )

def main() -> None:
    """Botni ishga tushurish uchun asosiy funksiya."""
    
    # Sizning bot tokeningiz
    TOKEN = "7827986103:AAHYmjWD-ZI9BfqWCWXHrTfGvQzdYV0f1qw" 

    # Botni yaratish
    application = Application.builder().token(TOKEN).build()

    # Buyruqqa ishlov beruvchini qo'shish
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushurish
    print("O'simlik tashxis boti ishga tushdi...")
    application.run_polling()


if __name__ == '__main__':
    main()