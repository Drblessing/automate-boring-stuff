import webbrowser
import pyperclip

search = pyperclip.paste().strip().replace(" ", "+")


webbrowser.open(f"https://www.google.com/search?q={search}")
