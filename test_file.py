import unittest
import json
import pytest
from passenger import Passenger
from plane import Plane
from flight import Flight


class Testing(unittest.TestCase):
    plane = Plane(5, 200, 6)
    plane.add_to_record()
    passenger = Passenger("fName", "lName", "passportID", 23)
    flight = Flight("flightID", "destination", "origin", plane, "duration")
    passenger.add_record()

    def test_passenger_create(self):
        self.assertIsInstance(self.passenger, Passenger)
        self.assertIsNotNone(self.passenger.f_name)
        with open("passenger_records.json", "r") as file:
            json_file = json.load(file)
            passenger_json = json_file["passenger"]
            for person in passenger_json:
                if person["passport"] == "passportID":
                    self.assertEquals(person["fName"], "fname")
                    break

    def test_flight_trip(self):
        self.assertIsInstance(self.flight, Flight)
        with open("flight_records.json", "r") as file:
            json_file = json.load(file)
            flight_json = json_file["flight"]
            for flight in flight_json:
                if flight["id"] == "FlightID":
                    self.assertEquals(flight["destination"], "destination")
                    break

    def test_vehicle(self):
        with open("vehicle_records.json", "r") as file:
            json_file = json.load(file)
            vehicle_json = json_file["vehicle"]["plane"]
            for vehicle in vehicle_json:
                if vehicle["id"] == "testID":
                    self.assertEquals(int(vehicle["capacity"]), 5)
                    break

    def test_change_trip(self):
        self.flight.manage_flight_trips("bad", "people", self.plane, 20000)
        flight_json = json_open("flight_records.json")
        flight_json = flight_json["flight"]
        for flight in flight_json:
            if flight["id"] == "flightID":
                self.assertEquals(flight["destination"], "bad")
                self.assertEquals(flight["origin"], "people")
                self.assertEquals(flight["duration"], 20000)
                break

    def test_add_passenger_to_flight(self):
        self.flight.add_passenger(self.passenger)
        flight_json = json_open("flight_records.json")
        flight_json = flight_json["flight"]
        for flight in flight_json:
            if flight["id"] == "flightID":
                for passenger in flight["passenger"]:
                    if passenger["passport"] == "passportID":
                        self.assertEquals(passenger["fName"], "fname")
                        self.assertEquals(passenger["lName"], "lname")
                        self.assertEquals(passenger["age"], 23)
                        break

    def test_report(self):
        self.assertIsInstance(self.flight.report(), list)


def json_open(file_name, perms="r"):
    with open(file_name, perms) as file:
        json_file = json.load(file)
        return json_file
