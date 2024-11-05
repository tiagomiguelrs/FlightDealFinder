from twilio.rest import Client
from data_manager import DataManager

class NotificationManager(Client):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, sid: str, token: str, from_number: str, to_number: str):
        super().__init__(sid, token)
        self.from_number = from_number
        self.to_number = to_number


    def send_message(self, sheety: DataManager):
        message_body = ""
        for city_i in range(len(sheety.data)):
            message_body += (f"Your flight to {sheety.data[city_i]['city']} "
                             f"is priced {sheety.data[city_i]['lowestPrice']}€ "
                             f"with a historical low of {sheety.data[city_i]['historical']}€.\n")

        self.messages.create(
            body=message_body,
            from_=self.from_number,
            to=self.to_number,
        )
