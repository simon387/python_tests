import logging
from logging.handlers import RotatingFileHandler

from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, filters, MessageHandler

import constants as const

logging.basicConfig(
	handlers=[
		RotatingFileHandler(
			'amazon-scraper.log',
			maxBytes=10240000,
			backupCount=5
		),
		logging.StreamHandler()
	],
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.DEBUG
)


async def unknown_command(update: Update, context: CallbackContext):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="text🦁")


if __name__ == '__main__':
	application = ApplicationBuilder().token(const.TELEGRAM_TOKEN_BOT).build()
	application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
	application.run_polling(stop_signals=None)
