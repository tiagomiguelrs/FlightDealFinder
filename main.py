import os
from datetime import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

AMADEUS_KEY = os.environ.get("AMADEUS_KEY", "Message")
AMADEUS_SECRET = os.environ.get("AMADEUS_SECRET", "Message")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "Message")
TWILIO_SID = os.environ.get("TWILIO_SID", "Message")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN", "Message")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER", "Message")
MY_NUMBER = os.environ.get("MY_NUMBER", "Message")

DEPARTURE = datetime(year=2024, month=12, day=23).strftime("%Y-%m-%d")

ORIGIN_IATA = "OPO"

data_manager = DataManager()
data_manager.get_r()

dest_iata_list = [data_manager.data[city_i]["iataCode"] for city_i in range(len(data_manager.data))]

flight_search = FlightSearch(key=AMADEUS_KEY, secret=AMADEUS_SECRET)
flight_search.find_prices(dest_iata_list=dest_iata_list, origin_iata=ORIGIN_IATA, flight_date=DEPARTURE)

flight_data = FlightData(data_manager, flight_search)
flight_data.update_data()

messenger = NotificationManager(TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER, MY_NUMBER)
messenger.send_message(data_manager)

flight_data.send_to_sheety()