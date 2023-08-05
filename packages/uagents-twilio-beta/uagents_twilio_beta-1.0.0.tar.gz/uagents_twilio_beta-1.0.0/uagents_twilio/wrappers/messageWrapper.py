# Start writing utility wrapper from here
import requests
from uagents import Agent

from uagents_twilio.models import MessageType


class MessageClient:
    """Base class for handling WhatsApp operations"""

    def __init__(
        self,
        agent: Agent,
        to_agent_address: str,
        account_sid: str,
        auth_token: str,
        from_number: str,
        to_number: str,
    ):
        self.agent = agent
        self.to_agent_address = to_agent_address
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.to_number = to_number

    def send_message(self, receiver, message: str, message_type):
        body = message
        twilio = TwilioWrapper(self.account_sid, self.auth_token)
        if message_type == MessageType.whatsapp and not self.from_number.startswith(
            "whatsapp:"
        ):
            self.from_number = f"whatsapp:{self.from_number}"
        twilio.send_message(self.from_number, receiver, body)


class TwilioWrapper:
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.base_url = "https://api.twilio.com/2010-04-01"

    def send_message(self, from_number, to_number, body):
        endpoint = f"{self.base_url}/Accounts/{self.account_sid}/Messages.json"
        data = {"From": from_number, "To": to_number, "Body": body}
        try:
            response = requests.post(
                endpoint, data=data, auth=(self.account_sid, self.auth_token)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to send message: {str(e)}")
