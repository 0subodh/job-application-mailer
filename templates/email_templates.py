class EmailTemplates:
    @staticmethod
    def job_application(company_name: str) -> dict:
        subject = f"Inquiry about Software Developer Position at {company_name}"

        body = f"""
            Dear Hiring Manager at {company_name},

            I am writing to express my strong interest in potential software development opportunities at {company_name}. I am particularly drawn to {company_name}'s innovative approach to technology and its impact in the industry.

            Please find my resume attached to this email.

            Thank you for considering my application.

            Best regards,
            Subodh Adhikari
        """

        return {
            'subject': subject,
            'body': body
        }
