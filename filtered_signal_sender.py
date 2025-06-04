import requests
from datetime import datetime

# معلومات البوت والقناة
bot_token = '7516366789:AAG7IwmcfB7Axi8qsnb1tisVNhIS3LWVCNk'
channel_id = -1001002651258310  # chat_id الرقمي للقناة

# إشارات فنية وهمية - للتجربة
signal_checks = {
    "تقاطع متوسطات": True,
    "RSI في منطقة الشراء": True,
    "MACD يعطي إشارة صعود": True,
    "ADX قوي": False,
    "Candlestick انعكاسي": True
}

# جمع الإشارات المتوافقة
matched_signals = [s for s, ok in signal_checks.items() if ok]

if len(matched_signals) < 3:
    print("🚫 لم يتم إرسال التوصية - أقل من 3 إشارات متوافقة")
else:
    symbol = "BTCUSDT"
    signal_type = "شراء"
    current_price = "67,200"
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M (UTC)")

    # تجهيز رسالة التوصية
    message = "📊 توصية تداول جديدة:\n\n"
    message += f"💰 العملة: {symbol}\n"
    message += f"📈 نوع الصفقة: {signal_type}\n"
    message += f"💵 السعر الحالي: {current_price}\n"
    message += f"📅 وقت الإشارة: {now}\n\n"
    message += "🔍 سبب التوصية:\n"
    message += "\n".join(f"- {s}" for s in matched_signals)
    message += "\n\n#توصيات #عملات #تداول"

    # إرسال التوصية
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': channel_id, 'text': message}
    resp = requests.post(url, data=payload)
    print("✅ تم إرسال التوصية بنجاح", resp.text)
