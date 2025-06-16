import os
import time
from duolingo import Duolingo

def belajar():
    username = os.getenv("DUOLINGO_USERNAME")
    jwt = os.getenv("DUOLINGO_JWT")

    if not username or not jwt:
        print("❌ DUOLINGO_USERNAME dan DUOLINGO_JWT belum diset di environment variables!")
        return

    try:
        lingo = Duolingo(username=username, jwt=jwt)
        print("✅ Login berhasil sebagai", username)

        # Contoh: ambil XP hari ini
        streak_info = lingo.get_streak_info()
        print("🔥 Streak:", streak_info.get("site_streak", 0))

        # Cek kursus aktif
        lang = lingo.get_abbreviation_of(language=lingo.get_user_info()["learning_language"])
        print(f"📚 Kursus aktif: {lang.upper()}")

    except Exception as e:
        print("❌ Gagal login atau fetch data:", str(e))

print("🤖 Robot hidup. Menunggu jam belajar...")
belajar()
