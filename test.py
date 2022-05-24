import os
import logging
import webbrowser
import pyperclip

pyperclip.copy("The text to be copied to the clipboard.")

webbrowser.open("https://google.com")


def test_step():
    2
    4
    print("hello")
    3
    4


test_step()

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("Start of program")


c = 0
for folderName, subfolders, filenames in os.walk("venv/lib"):
    c += 1
    c += len(subfolders)
    c += len(filenames)

# print("Enter 1st")
# first = input()
# print("Enter 2")
# second = input()
# print("Enter 3")
# third = input()
# sum_ = first + second + third
# logging.debug(sum_)

# print("The sum is" + sum_)

logging.critical("BIG CRIT")

logging.debug("end of program")
