#!/bin/bash

echo "🚀 Install dependencies..."
pip install -r requirements.txt

echo "🔧 Install browser Chromium..."
playwright install chromium

echo "✅ Siap menjalankan bot"
python main.py
