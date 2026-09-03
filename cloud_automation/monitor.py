import shutil
from datetime import datetime

total, used, free = shutil.disk_usage("/")
free_gb = free // (1024**3)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log_line = f"[{current_time}] Cron Check: {free_gb} GB free\n"

with open("/workspaces/my-first-cloud-code/cloud_automation/server_health.log", "a") as file:
    file.write(log_line)
    