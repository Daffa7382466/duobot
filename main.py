import os
from duolingo import Duolingo
import time
import datetime

# Ambil email & password dari Environment Variable
email = os.getenv("DUO_EMAIL")
password = os.getenv("DUO_PASSWORD")

# Jam bot akan berhenti
jam_berhenti = datetime.time(2, 0)

def belajar():
    print("Robot belajar mulai...")
    lingo = Duolingo(email, password)

    while True:
        sekarang = datetime.datetime.now().time()
        if sekarang >= jam_berhenti:
            print("Sudah malam. Robot tidur...")
            break

        xp = lingo.get_daily_xp_progress()
        print(f"XP hari ini: {xp}")

        time.sleep(60 * 5)

belajar()
