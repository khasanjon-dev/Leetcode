import os
from pprint import pprint

import sib_api_v3_sdk
from dotenv import load_dotenv
from sib_api_v3_sdk.rest import ApiException

load_dotenv()

BREVO_KEY = os.getenv('BREVO_API_KEY')

sib_api_v3_sdk.configuration.api_key['api-key'] = BREVO_KEY
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
    name="Campaign sent via the API",
    subject="My subject",
    sender={"name": "From name", "email": "myfromemail@mycompany.com"}, type="classic",
    html_content="Congratulations! You successfully sent this example campaign via the Brevo API.",
    recipients={"listIds": [2, 7]})
try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
