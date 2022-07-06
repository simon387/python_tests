#
# script di demo
#

import logging

import requests

bot_token = "   "
chat_id = "test_chatutti_channel"


def send_telegram(text):
	logging.info('Sending info to telegram channel for')
	api_telegram = 'https://api.telegram.org/bot'
	parse_mode = '&parse_mode=HTML&disable_web_page_preview=false'
	r = requests.post(api_telegram + bot_token + '/sendMessage?chat_id=' + '   ' + '&text=' + text + parse_mode)
	i = 0


if __name__ == "__main__":
	log_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
	#
	send_telegram("test di prova nuovo script 2022")
