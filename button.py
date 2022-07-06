from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "  "
GROUP_ID = "  "

random_people_text = "Random person"
random_image_text = "Random image"

random_people_url = "https://picsum.photos/200"
random_image_url = "https://picsum.photos/200"

likes = 0
dislikes = 0
allower_usernames = ["none"]


async def start_command(update: Update, context: CallbackContext):
	buttons = [[KeyboardButton(random_people_text)], [KeyboardButton(random_image_text)]]
	await context.bot.send_message(chat_id=update.effective_chat.id, text="welcome to my bot", reply_markup=ReplyKeyboardMarkup(buttons))


async def message_handler(update: Update, context: CallbackContext):
	image = ""
	if random_image_text in update.message.text:
		image = get(random_image_url).content
	if random_people_text in update.message.text:
		image = get(random_people_url).content
	if image:
		await context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption="")])

		buttons = [[InlineKeyboardButton("up", callback_data="like")], [InlineKeyboardButton("down", callback_data="dislike")]]
		await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="did you like the image?")


def query_handler(update: Update, context: CallbackContext):
	query = update.callback_query.data
	update.callback_query.answer()

	global likes, dislikes

	if "like" in query:
		likes += 1
	if "dislike" in query:
		dislikes += 1

	print(f"like => {likes} and dislike => {dislikes}")


if __name__ == '__main__':
	application = ApplicationBuilder().token(TOKEN).build()
	application.add_handler(CommandHandler("start", start_command))
	application.add_handler(MessageHandler(filters.TEXT, message_handler))
	application.add_handler(CallbackQueryHandler(query_handler))
	application.run_polling(stop_signals=None)
