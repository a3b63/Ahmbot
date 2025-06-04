import requests

TOKEN = "7516366789:AAG7IwmcfB7Axi8qsnb1tisVNhIS3LWVCNk"
CHAT_ID = "-1002651258310"
message = "📢 هذا اختبار من بوت التوصيات - تم بنجاح ✅"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)
print("تم إرسال الرسالة:", response.text)
