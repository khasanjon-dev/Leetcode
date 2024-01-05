import os

import sib_api_v3_sdk
from dotenv import load_dotenv
from sib_api_v3_sdk.rest import ApiException

load_dotenv()
BREVO_API_KEY = os.getenv('BREVO_API_KEY')
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = BREVO_API_KEY
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))


def send_email(subject, html, to_address=None, receiver_username=None):
    subject = subject
    sender = {"name": "DevMasters", "email": "khasanjon.eng@gmail.com"}
    html_content = html

    if to_address:
        to = [{"email": to_address, "name": receiver_username}]
    else:
        to = [{"email": "sangeeth123sj@gmail.com", "name": "Sangeeth Joseph"}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
        return {"message": "Email sent successfully!"}
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


content = "hello bu men"
html = f"<h3>{content}</h3>"
subject = "Bu DevMasters"
to_address = 'khasanjon.dev@gmail.com'
receiver_username = "Khasan"
print("Sending mail...")

# Send the email and store the response
email_response = send_email(subject, html, to_address, receiver_username)

# Print the status of the email sending process
print(email_response)
