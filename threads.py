import threading, time


def takeANap():
    time.sleep(2)
    print("Wake up Mr. Bless!")


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print("End of the program!")
