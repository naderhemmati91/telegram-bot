import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات با موفقیت راه‌اندازی شد.")

async def main():
    app = (
        ApplicationBuilder()
        .token("توکن‌_ربات‌_تو‌")
        .proxy_url("socks5://127.0.0.1:8086")  # فقط همین کافیه!
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
