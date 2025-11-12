from datetime import datetime

# احصل على التاريخ والوقت الحالي
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# اطبع النتيجة
print(f"📅 Current Date and Time: {current_time}")

# حفظ النتيجة في ملف
with open("report.log", "a") as f:
    f.write(f"{current_time}\n")
