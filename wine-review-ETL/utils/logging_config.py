import logging
import os
import datetime


log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(log_folder, f"log_{timestamp}.log")

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_file_path,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
