# Job Application Mailer

A Python application for automating personalized job application emails with PDF attachments.

## Features

- Send personalized emails to multiple companies
- Attach your resume or any PDF file
- Custom email templates with company name variables
- Controlled sending rate to avoid spam filters
- Progress tracking and success reports
- Secure credential management

## Project Structure

```
job_application_mailer/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── templates/
│   ├── __init__.py
│   └── email_templates.py
│
├── utils/
│   ├── __init__.py
│   └── email_sender.py
│
├── data/
│   └── companies.csv
│   └── YourCV.pdf
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

## Installation

### Clone the repository:

```sh
git clone https://github.com/0subodh/job-application-mailer.git
cd job-application-mailer
```

### Create a virtual environment:

```sh
python -m venv venv

# Activate on Windows
venv\Scripts\activate
# OR on Linux/Mac
source venv/bin/activate
```

### Install dependencies:

```sh
pip install -r requirements.txt
```

### Configure the application:

Create a `.env` file with your email credentials:

```sh
EMAIL=your.email@gmail.com
EMAIL_PASSWORD=your_app_password
```

Update the PDF path in `config/settings.py`.
Customize email templates in `templates/email_templates.py` if needed.

## Usage

### Prepare your company list in `data/companies.csv`:

```csv
company_name,email
Google,recruiter@google.com
Microsoft,hr@microsoft.com
Amazon,jobs@amazon.com
```

### Run the application:

```sh
python main.py
```

## Email Security

This application uses environment variables to store sensitive information like email credentials. For Gmail users:

1. Enable 2-Factor Authentication in your Google Account.
2. Generate an App Password:
   - Go to Google Account Settings.
   - Search for "App Passwords".
   - Generate a new app password.
   - Use this password in your `.env` file.

## Customizing Email Templates

Edit `templates/email_templates.py` to customize your email content:

```python
class EmailTemplates:
    @staticmethod
    def job_application(company_name: str) -> dict:
        subject = f"Job Application - Software Developer Position at {company_name}"

        body = f"""
Dear Hiring Manager at {company_name},

I am writing to express my interest in the Software Developer position at {company_name}.
Please find my resume attached.

Best regards,
[Your Name]
        """

        return {
            'subject': subject,
            'body': body
        }
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
