import os
from duolingo import Duolingo
import time
import datetime

email = os.getenv("DUO_EMAIL")
password = os.getenv("DUO_PASSWORD")

# Jam mulai dan jam berhenti belajar
jam_mulai = datetime.time(6, 0)   # 06:00 pagi
jam_berhenti = datetime.time(12, 0)  # 12:00 siang

def belajar():
    print("Robot hidup. Menunggu jam belajar...")
    lingo = Duolingo(email, password)

    while True:
        sekarang = datetime.datetime.now().time()

        if jam_mulai <= sekarang < jam_berhenti:
            print("Saatnya belajar Duolingo...")
            try:
                xp = lingo.get_daily_xp_progress()
                print(f"XP hari ini: {xp}")
            except Exception as e:
                print(f"Terjadi error saat belajar: {e}")
            time.sleep(60 * 5)  # belajar setiap 5 menit
        else:
            print("Di luar jam belajar. Istirahat dulu...")
            time.sleep(60 * 15)  # cek lagi tiap 15 menit

belajar()
