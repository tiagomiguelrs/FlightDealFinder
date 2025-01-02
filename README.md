# Flight Deal Finder

## Description
This project is a flight deal finder application that searches for the best flight prices and sends notifications to the user. It integrates with various APIs to fetch flight data, manage data, and send notifications.

## Features
Flight Search: Uses the Amadeus API to search for flight prices based on the destination IATA codes and departure date.

Data Management: Manages flight data using a custom data manager that interacts with a Google Sheets API (Sheety).

Notifications: Sends notifications about flight deals using the Twilio API.

Environment Variables: Utilizes environment variables to securely store API keys and tokens.

## How It Works
Initialize Environment Variables: The application retrieves API keys and tokens from environment variables.

Set Departure Date and Origin: The departure date and origin IATA code are set.

Fetch Data: The data manager fetches the required data from a Google Sheet.

Search for Flights: The flight search module uses the Amadeus API to find flight prices for the given destinations and departure date.

Update Data: The flight data module updates the data with the latest flight prices.

Send Notifications: The notification manager sends a message with the flight deals to the user's phone number using Twilio.

Save Data: The updated flight data is saved back to the Google Sheet.
