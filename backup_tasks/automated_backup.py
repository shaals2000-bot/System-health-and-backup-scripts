import os
import shutil
from datetime import datetime

# Set your source and backup folders
source_folder = r"D:\backup_tasks\source_data"
backup_root = r"D:\backup_tasks\remote_server"

# Make sure source folder exists
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"Created source folder at {source_folder}")

# Create remote backup folder if not exists
os.makedirs(backup_root, exist_ok=True)

# Timestamp for each backup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_root, f"backup_{timestamp}")

try:
    # Copy all files/folders from source to backup
    shutil.copytree(source_folder, backup_folder)

    # Show success message
    print(f"[{timestamp}] ✅ Backup successful!")
    print(f"Files copied to: {backup_folder}")

    # Log result (simple text log)
    with open("backup_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Backup successful. Copied to: {backup_folder}\n")

except Exception as e:
    print(f"[{timestamp}] ❌ Backup failed: {e}")
    with open("backup_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Backup failed: {e}\n")