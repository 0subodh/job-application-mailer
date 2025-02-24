import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email Settings
EMAIL_SETTINGS = {
    'sender_email': os.getenv('EMAIL'),
    'sender_password': os.getenv('EMAIL_PASSWORD'),
    'smtp_server': "smtp.gmail.com",
    'smtp_port': 587,
    'delay': 5  # seconds between emails
}

# File paths
PDF_PATH = "data/Subodh_Adhikari.pdf"
COMPANIES_CSV = "data/companies.csv"
