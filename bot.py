import pyautogui as pt
from time import sleep

# Mouse click workaround for MAC OS
# from pynput.mouse import Controller, Button
# mouse = Controller()

# replace click() by  mouse.click()
# example
# mouse.click(Button.left, 1)


def openWhatsapp():  # opens whatsapp if the app is pinned on the taskbar
    global x, y, a, b
    position = pt.locateOnScreen(
        "app.png", confidence=0.6
    )  # capture image of the whatsapp icon using snip or screenshot and crop , and add to the root directory as "app.png"
    print(position)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 20, y + 20, duration=0.5)  # adjust depending on your computer
    pt.click()


def getChat():
    global x, y
    # position1 = pt.locateOnScreen("chat.png", confidence=0.6)             # comment this area if the chat is already open in the whatsapp window
    # print(position1)
    # x = position1[0]
    # y = position1[1]
    # pt.moveTo(x + 20, y + 20, duration=0.5)
    # pt.click()
    chat = pt.locateOnScreen(
        "smile.png", confidence=0.6
    )  # capture image of the smiley icon using snip or screenshot and crop , and add to the root directory as "smile.png"  # this will be the anchor point for further pointer locations
    # print(chat)
    pt.moveTo(
        chat[0] + 500, chat[1] - 50, duration=0.5
    )  # adjust depending on your computer
    pt.doubleClick()  # tags the recent msg to your reply
    pt.moveTo(
        chat[0] + 150, chat[1] + 15, duration=0.5
    )  # adjust depending on your computer
    pt.click()  # select the textbox


def res(message):
    pt.typewrite(message, interval=0.1)  # enters the msg in the text box


def check():
    chat = pt.locateOnScreen("smile.png", confidence=0.6)
    if pt.pixelMatchesColor(
        int(chat[0] + 50), int(chat[1] - 35), (38, 45, 49), tolerance=10
    ):  # adjust depending on your computer  #also replace the rgb values of the pointer location if needed #these vales are for the dark theme that i have been using
        print("newmsg")
        getChat()
        res(
            "Your Custom Message\n"
        )  # "\n"->"new line" is read as "Enter" which send the msg #remove if needed while debugging to avoid sapm
        sleep(1)
    else:
        print("no new msgs")


openWhatsapp()
while True:
    check()
    sleep(1)
