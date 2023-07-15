import smtplib

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

MY_EMAIL="mailt6419@gmail.com"
MY_PASSWORD="abcdefu123"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
     def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )