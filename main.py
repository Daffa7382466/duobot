import os
from duolingo_api import Duolingo
import time
from datetime import datetime

# Ambil username dan password dari Environment Variables Railway
username = os.environ.get("DUOLINGO_USERNAME")
password = os.environ.get("DUOLINGO_PASSWORD")

def belajar():
    print("Robot hidup. Menunggu jam belajar...")

    # Waktu belajar (jam dan menit)
    jam_belajar = 11
    menit_belajar = 5

    while True:
        sekarang = datetime.now()

        if sekarang.hour == jam_belajar and sekarang.minute == menit_belajar:
            print("Waktunya belajar! Login ke Duolingo...")

            try:
                lingo = Duolingo(username=username, password=password)
                info = lingo.get_user_info()
                print(f"Berhasil login sebagai {info['username']}! Total XP: {info['totalXp']}")

            except Exception as e:
                print("Gagal login ke Duolingo:", str(e))

            break

        time.sleep(10)

belajar()
