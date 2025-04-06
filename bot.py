import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# لاگ برای دیباگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توکن واقعی ربات
TOKEN = "7612903580:AAGH7_qCfv3B91U80_aZoaG1yCDm1ilb7no"

# آیدی‌های مجاز (ادمین‌ها) - آیدی خودتو بذار اینجا
ADMIN_IDS = [123456789]

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMIN_IDS:
        await update.message.reply_text("سلام ادمین عزیز! به ربات خوش اومدی.")
    else:
        await update.message.reply_text("سلام! لطفا منتظر تایید ادمین بمونید.")

# هندل پیام‌های عادی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیامت دریافت شد.")

# اجرای اصلی ربات
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
