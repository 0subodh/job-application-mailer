import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pathlib import Path
import pandas as pd
import time
from datetime import datetime
from config.settings import EMAIL_SETTINGS


class EmailSender:
    def __init__(self):
        self.settings = EMAIL_SETTINGS

    def create_message(self, recipient, subject, body, pdf_path):
        message = MIMEMultipart()
        message["From"] = self.settings['sender_email']
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with open(pdf_path, "rb") as file:
            pdf_attachment = MIMEApplication(file.read(), _subtype="pdf")
            pdf_attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=Path(pdf_path).name
            )
            message.attach(pdf_attachment)

        return message

    def send_email(self, recipient, subject, body, pdf_path):
        try:
            message = self.create_message(recipient, subject, body, pdf_path)

            with smtplib.SMTP(self.settings['smtp_server'],
                              self.settings['smtp_port']) as server:
                server.starttls()
                server.login(self.settings['sender_email'],
                             self.settings['sender_password'])
                server.send_message(message)
            return True

        except Exception as e:
            print(f"\nError sending email: {str(e)}")
            return False

    def send_batch_emails(self, companies_data, pdf_path, get_template):
        total_companies = len(companies_data)
        successful_sends = 0
        failed_sends = 0

        print("\nStarting email campaign...")
        print(f"Total emails to send: {total_companies}")
        print(f"Delay between emails: {self.settings['delay']} seconds\n")

        for index, row in companies_data.iterrows():
            company_name = row['company_name']
            recipient_email = row['email']

            # Get email content from template
            email_content = get_template(company_name)

            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] Sending email {index + 1}/{total_companies} "
                  f"to {company_name}...", end="")

            success = self.send_email(
                recipient_email,
                email_content['subject'],
                email_content['body'],
                pdf_path
            )

            if success:
                print(" ✓ Sent!")
                successful_sends += 1
            else:
                print(" ✗ Failed!")
                failed_sends += 1

            if index < total_companies - 1:
                print(f"Waiting {self.settings['delay']} seconds...")
                time.sleep(self.settings['delay'])

        print(f"\nEmail campaign completed!")
        print(f"Successfully sent: {successful_sends}")
        print(f"Failed: {failed_sends}")
        print(
            f"Total time: {total_companies * self.settings['delay']} seconds")
