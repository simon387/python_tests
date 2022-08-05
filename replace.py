import html
import json

message = (
	f"An exception was raised while handling an update\n"
	f"<pre>update = {html.escape('asd')}"
	"</pre>\n\n"
	f"<pre>context.chat_data = {html.escape(str('asd'))}</pre>\n\n"
	f"<pre>context.user_data = {html.escape(str('context.user_data'))}</pre>\n\n"
	f"<pre>{html.escape('fine')}"
)

message = message[:4400]  # truncate to prevent error
if message.count('pre>') % 2 != 0:
	message += '</pre>'

print(message)

