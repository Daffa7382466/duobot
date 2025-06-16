import os
import time
from duolingo_api import Duolingo

def belajar():
    username = os.getenv("DUOLINGO_USERNAME")
    jwt_token = os.getenv("DUOLINGO_JWT")

    if not username or not jwt_token:
        print("❌ Username atau JWT Duolingo belum diset di Railway Environment Variables.")
        return

    try:
        lingo = Duolingo(username=username, jwt=jwt_token)
        print(f"✅ Login berhasil sebagai {username}")
        print("🎯 Misi harian:")
        for goal in lingo.get_daily_goals():
            print(f"- {goal['title']}: {goal['completed']}")
    except Exception as e:
        print("❌ Gagal login atau mengambil data:", e)

print("🤖 Robot hidup. Menunggu jam belajar...")

# Looping setiap 10 menit
while True:
    belajar()
    time.sleep(600)  # 600 detik = 10 menit
