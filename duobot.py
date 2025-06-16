from playwright.async_api import async_playwright
import asyncio
import os

# Ambil email dan password dari environment variable
EMAIL = os.getenv("DUOLINGO_EMAIL")
PASSWORD = os.getenv("DUOLINGO_PASSWORD")

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print("🔐 Login ke Duolingo...")
        await page.goto("https://www.duolingo.com/log-in")

        await page.fill('input[name="identifier"]', EMAIL)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')

        await page.wait_for_timeout(7000)

        if "learn" in page.url:
            print("✅ Berhasil login dan siap belajar!")
        else:
            print("❌ Gagal login.")

        await browser.close()
