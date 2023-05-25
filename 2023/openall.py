import re
import webbrowser


def open_links_in_file(file_path):
	with open(file_path, 'r') as file:
		file_content = file.read()
		urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', file_content)
		if urls:
			for url in urls:
				webbrowser.open_new_tab(url)
		else:
			print("No links found in the file.")


# Usage example
file_path = 'file.txt'  # Replace with your file path
open_links_in_file(file_path)
