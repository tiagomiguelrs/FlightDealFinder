import requests

FLIGHT_ORDERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
AMADEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
TOKEN_HEADER = {'Content-Type': 'application/x-www-form-urlencoded'}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, key: str=None, secret: str=None):
        self.data = None

        self._API_KEY = key
        self._API_SECRET = secret
        self._API_TOKEN = ""
        self.get_new_token()

        self.flights_order_header = {
            "Authorization": f"Bearer {self._API_TOKEN}"
        }


    def find_prices(self, dest_iata_list: list[str], origin_iata: str, flight_date: str):
        """Returns the price for the cheapest flight"""

        flight_search_results = {}
        for dest_iata in dest_iata_list:
            flight_orders_data = {
                "originLocationCode": origin_iata,
                "destinationLocationCode": dest_iata,
                "departureDate": flight_date,
                "adults": "1",
                "max": "2"  # Must be at least 2, otherwise gives an error "400 Client Error: Bad Request for url"
            }
            response = requests.get(url=FLIGHT_ORDERS_ENDPOINT, params=flight_orders_data, headers=self.flights_order_header)
            response.raise_for_status()
            data = response.json()
            flight_search_results[dest_iata] = data["data"][0]["price"]["total"]
        self.data = flight_search_results


    def get_new_token(self):
        """Gets a new token if the user does not have one"""

        token_data = {
            'grant_type': 'client_credentials',
            'client_id': self._API_KEY,
            'client_secret': self._API_SECRET
        }

        auth_response = requests.post(url=AMADEUS_TOKEN_ENDPOINT, data=token_data, headers=TOKEN_HEADER)
        auth_response.raise_for_status()
        self._API_TOKEN = auth_response.json().get("access_token")     # Gets the value for the key "access_token"
