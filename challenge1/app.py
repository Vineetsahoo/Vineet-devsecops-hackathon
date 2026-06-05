from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

def connect():
    print("Connecting securely...")
    print("Secrets loaded from environment variables")

connect()
