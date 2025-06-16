import os
import time
import datetime
from duolingo import Duolingo

# Ambil JWT dari environment variable
jwt_token = os.getenv("DUO_JWT")

# Waktu belajar
jam_mulai = datetime.time(6, 0)     # Jam 6 pagi
jam_berhenti = datetime.time(12, 0) # Jam 12 siang

def belajar():
    print("Robot hidup. Menunggu jam belajar...")

    lingo = Duolingo(jwt=jwt_token)

    while True:
        sekarang = datetime.datetime.now().time()

        if jam_mulai <= sekarang < jam_berhenti:
            xp = lingo.get_daily_xp_progress()
            print(f"[{datetime.datetime.now()}] XP hari ini: {xp}")
        else:
            print(f"[{datetime.datetime.now()}] Di luar jam belajar. Tidur dulu...")
        
        time.sleep(60 * 5)  # tunggu 5 menit

belajar()
