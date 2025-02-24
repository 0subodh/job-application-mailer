import pandas as pd
from config.settings import COMPANIES_CSV, PDF_PATH
from utils.email_sender import EmailSender
from templates.email_templates import EmailTemplates


def main():
    # Initialize email sender
    sender = EmailSender()

    # Read company data
    df = pd.read_csv(COMPANIES_CSV)

    # Send batch emails using template
    sender.send_batch_emails(
        companies_data=df,
        pdf_path=PDF_PATH,
        get_template=EmailTemplates.job_application
    )


if __name__ == "__main__":
    main()
