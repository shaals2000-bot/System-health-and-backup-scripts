import psutil
import datetime

print("=== System Health Report ===")
print("Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")
print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

# Optional alert if any usage crosses 80%
if psutil.cpu_percent() > 80:
    print("⚠️ Warning: High CPU usage!")
if psutil.virtual_memory().percent > 80:
    print("⚠️ Warning: High Memory usage!")
if psutil.disk_usage('/').percent > 80:
    print("⚠️ Warning: Low Disk Space!")