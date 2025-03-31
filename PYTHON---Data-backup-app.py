import os
import shutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def backup_files(source_dir, backup_dir):
    """Backs up files from source_dir to backup_dir."""
    if not os.path.exists(source_dir):
        logging.error(f"Source directory {source_dir} does not exist.")
        return
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_subdir = os.path.join(backup_dir, f'backup_{timestamp}')
    os.makedirs(backup_subdir)
    
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(backup_subdir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    
    logging.info(f"Backup completed successfully at {timestamp}.")
    print(f"Backup completed successfully at {timestamp}.")


def schedule_backup(source_dir, backup_dir, interval):
    """Schedules backups at a given interval (in seconds)."""
    try:
        while True:
            backup_files(source_dir, backup_dir)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Backup scheduling stopped.")
        logging.info("Backup scheduling stopped.")


if __name__ == "__main__":
    source = input("Enter the source directory: ")
    backup = input("Enter the backup directory: ")
    interval = int(input("Enter backup interval in seconds: "))
    
    schedule_backup(source, backup, interval)
