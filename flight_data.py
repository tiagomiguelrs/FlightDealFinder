from data_manager import DataManager
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, sheety: DataManager, flights: FlightSearch):
        self.sheety = sheety
        # [{"city": city_name, "iataCode": iata_code, "lowestPrice": lowest_price, "historical": historical_price, "id": row_id},
        #  {"city": city_name, "iataCode": iata_code, "lowestPrice": lowest_price, "historical": historical_price, "id": row_id},
        #  ...]
        self.flights = flights
        # {iata_code: price,
        #  iata_code: price,
        #  ...}


    def update_data(self):
        for city_i in range(len(self.sheety.data)):
            iata = self.sheety.data[city_i]["iataCode"]
            self.sheety.data[city_i]["lowestPrice"] = self.flights.data[iata]
            if float(self.flights.data[iata]) < self.sheety.data[city_i]["historical"]:
                self.sheety.data[city_i]["historical"] = float(self.flights.data[iata])


    def send_to_sheety(self):
        for city_i in range(len(self.sheety.data)):
            update_dict ={
                "city": self.sheety.data[city_i]["city"],
                "iataCode": self.sheety.data[city_i]["iataCode"],
                "lowestPrice": self.sheety.data[city_i]["lowestPrice"],
                "historical": self.sheety.data[city_i]["historical"]
            }
            self.sheety.put_r(object_id=str(self.sheety.data[city_i]["id"]), params=update_dict)

