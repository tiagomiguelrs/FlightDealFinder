import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b5d893b47342bc36db9aec6d42fd2bdc/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, token: str=None):
        self.data = None

        if token is not None:
            self._API_TOKEN = token

            self.HEADERS = {
                "Authorization": f"Basic {self._API_TOKEN}"
            }
        else: self._API_TOKEN = None


    def get_r(self):
        if self._API_TOKEN is not None:
            response = requests.get(url=SHEETY_ENDPOINT, headers=self.HEADERS)
        else:
            response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        # {'prices': [{'city': 'Tokyo', 'iataCode': 'HND', 'lowestPrice': 485, 'historical': 485, id': 2},
        #             {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'historical': 551, 'id': 3},
        #             {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'historical': 95, 'id': 4},
        #             {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'historical': 414, 'id': 5},
        #             {'city': 'Dublin', 'iataCode': 'DUB', 'lowestPrice': 378, 'historical': 378, 'id': 6}]}
        self.data = [
            {
                "city": city["city"],
                "iataCode": city["iataCode"],
                "lowestPrice": city["lowestPrice"],
                "historical": city["historical"],
                "id": city["id"]
        } for city in data["prices"]]


    def put_r(self, object_id: str, params: dict):
        body = {
            "price": params
        }
        if self._API_TOKEN is not None:
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{object_id}", json=body, headers=self.HEADERS)
        else:
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{object_id}", json=body)
        response.raise_for_status()