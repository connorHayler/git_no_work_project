import json


class Flight:
    def __init__(self, flight_id, destination, origin, vehicle, duration):
        self.flight_id = flight_id
        self.destination = destination
        self.origin = origin
        self.vehicle = vehicle
        self.duration = duration
        self.add_records()

    def add_records(self):
        new_flight = {'id': self.flight_id,
                      'destination': self.destination,
                      'origin': self.origin,
                      'vehicle': self.vehicle.dic,
                      'duration': self.duration,
                      'passenger': []
                      }

        # Reads, Updates and Closes json file
        try:
            with open("flight_records.json", "r+") as read_file:
                data = json.load(read_file)
                data["flight"].append(new_flight)
                read_file.seek(0)
                json.dump(data, read_file, indent=4)
        except FileNotFoundError as err:
            return "File not found"

    def add_passenger(self, passenger):
        with open("flight_records.json", "r+") as file:
            data = json.load(file)
            for index, flight in enumerate(data["flight"]):
                if flight["id"] == self.flight_id:
                    break
            data["flight"][index]["passenger"].append(passenger.dic)
            file.seek(0)
            json.dump(data, file, indent=4)

    def generate_flight_attendees(self):
        try:
            identity = open("passengers.json", "r")
            id = json.load(identity)
            for value, key in id.items():
                if not isinstance(key, list):
                    for x, y in key.items():
                        print(x, ':', y)
                else:
                    for i in key:
                        for s, m in i.items():
                            print(s, ':', m)
        except FileNotFoundError as err:
            return "File not found"

    # Function to change flight trip details
    def manage_flight_trips(flight_id, destination, origin, vehicle, duration):
        flight_trp = flight_id
        # Open json file as read only to get a dict
        try:
            with open("flights.json", "r") as file:
                json_file = json.load(file)
                flights_json = json_file["flight"]

            # Iterate through dict to see if flight id is the same as what was inputted
            for flight in flights_json:
                # If there's a flight with the same id, change the details
                if flight["id"] == flight_trp:
                    flight["destination"] = destination
                    flight["origin"] = origin
                    flight["vehicle"] = vehicle
                    flight["duration"] = duration

                    # # Iterate through the passengers of the flight
                    # for passenger in flight["passenger"]:
                    #     # If there's a passenger with the same id, change details
                    #     if passenger["passport"] == passenger_id:
                    #         passenger["seat"] = seat
        except FileNotFoundError as err:
            return "File not found"
        try:
            # Write changes to the json file
            with open("flights.json", "w") as f:
                json.dump(json_file, f, indent=4)  # serializing back to the original file
        except FileNotFoundError as err:
            return "File not found"

    # User input
    # create_flight("JH255", "Portugal", "England", "Plane", "200")
    # manage_flight_trips("W1", "Greece", "USA", "Helicopter", "120")
    # print(generate_flight_attendees())
