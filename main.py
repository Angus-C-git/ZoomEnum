# ============================================ Imports ============================================ #
import random
import pyautogui
import time

# Globals
join_meeting_btt = "join.png"


def join():
    pyautogui.click(join_meeting_btt)


def try_id(id_candidate):
    print("Checking candidate ID -->", id_candidate)
    print("Make sure you're terminal is green for luck -->")

    pyautogui.press('tab', 2)
    pyautogui.write(str(id_candidate))
    pyautogui.press('tab', 6)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')


def gen_meeting_ids():
    try_id(random.randint(100000000, 999999999))
    while True:
        print("DEBUG _> JOIN")

        join()
        try_id(random.randint(100000000, 999999999))


def init():
    global join_meeting_btt

    # Temporary Method To Start Enumeration
    time.sleep(2)
    join_btt_loc = str(input("Enter path to 'Join a Meeting' button: "))

    print("Looking for zoom Window -->")
    join_meeting_btt = pyautogui.locateOnScreen(join_btt_loc, 0.01)

    while join_meeting_btt is None:
        print("Zoom Window not found, make sure zoom is open and on the primary screen/monitor && the path to the "
              "button screenshot is correct -->")
        try:
            join_meeting_btt = pyautogui.locateOnScreen(join_btt_loc, 0.01)
        except:
            print("Zoom Window not found, make sure zoom is open and on the primary screen/monitor && the path to the "
                  "button screenshot is correct -->")

    print("Zoom Window Found at --> ", join_meeting_btt)
    pyautogui.moveTo(join_meeting_btt)
    pyautogui.click(join_meeting_btt)
    time.sleep(1)
    gen_meeting_ids()


init()
