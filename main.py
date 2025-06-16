import os
import time
import datetime
from duolingo import Duolingo

username = os.getenv("DUO_USERNAME")
jwt_token = os.getenv("DUO_JWT")

jam_mulai = datetime.time(6, 0)
jam_berhenti = datetime.time(12, 0)

def belajar():
    print("Robot hidup. Menunggu jam belajar...")

    lingo = Duolingo(username=username, jwt=jwt_token)

    while True:
        sekarang = datetime.datetime.now().time()

        if jam_mulai <= sekarang < jam_berhenti:
            xp = lingo.get_daily_xp_progress()
            print(f"[{datetime.datetime.now()}] XP hari ini: {xp}")
        else:
            print(f"[{datetime.datetime.now()}] Di luar jam belajar.")

        time.sleep(300)

belajar()
