import pyautogui
import time
import pyperclip
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

WHATSAPP_ICON = (1294, 1152)
EMPTY_SPACE = (1742, 395)
CHAT_BOX = (930, 1092)

SELECT_START = (695, 275)
SELECT_END = (1742
              , 1055)

def get_latest_message():
    # Select chat history
    pyautogui.moveTo(SELECT_START[0], SELECT_START[1])
    pyautogui.dragTo(SELECT_END[0], SELECT_END[1], duration=2)

    time.sleep(0.5)

    # Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)

    # Backup copy
    pyautogui.hotkey("ctrl", "insert")
    time.sleep(0.3)

    # Remove selection
    pyautogui.click(EMPTY_SPACE[0], EMPTY_SPACE[1])
    time.sleep(0.2)

    text = pyperclip.paste()
    return text.strip()

def extract_last_line(chat_text):
    lines = chat_text.split("\n")
    last = ""
    for line in reversed(lines):
        if line.strip() != "":
            last = line.strip()
            break
    return last


def ai_generate_reply(message):
    res = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content":
                ( " Reply only to the last message"
                    "Keep reply short, natural Hinglish. "
                    "No name, no date, no sender. "
                    "No long explanations."
                    "You are Rajbir, an Indian coder who talks in friendly Hinglish. "
                    "Always reply naturally, emotionally, and move the conversation forward. "
                    "Ask follow-up questions and never give robotic answers." )
            },
            {"role": "user", "content": message}
        ]
    )
    return res.output_text.strip()


def send_reply(text):
    pyautogui.click(CHAT_BOX[0], CHAT_BOX[1])
    time.sleep(0.2)
    pyautogui.write(text, interval=0.02)
    time.sleep(0.2)
    pyautogui.press("enter")

print(" AI WhatsApp Bot Started…\nDo NOT touch your mouse or keyboard.")

pyautogui.click(WHATSAPP_ICON[0], WHATSAPP_ICON[1])
time.sleep(2)
pyautogui.click(100, 100)
time.sleep(1)

last_message = ""

while True:
    try:
        chat = get_latest_message()
        latest = extract_last_line(chat)

        if latest != "" and latest != last_message:
            print("\nNEW MESSAGE DETECTED:", latest)

            reply = ai_generate_reply(latest)
            print("BOT:", reply)

            send_reply(reply)

            last_message = latest

        time.sleep(1)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(2)
