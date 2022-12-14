import os
from dotenv import load_dotenv

load_dotenv()

INPUT_DIR = os.environ.get("INPUT_IMAGE_DIR", "images")
OUTPUT_IMAGE_DIR = os.environ.get("OUTPUT_IMAGE_DIR", "output_images")

INF_SERVER_URL = os.environ.get("INF_SERVER_URL", "")
