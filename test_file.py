import unittest
import json
import pytest
from passenger import Passenger
from plane import Plane
# from flight import Flight


class Testing(unittest.TestCase):
    plane = Plane(5, "200", "6")
    plane.add_to_record()
    passenger = Passenger("fName", "lName", "passportID", 23)
    # flight = Flight("origin", "destination", plane, "departure time")
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
                if flight["flightID"] == "FlightID":
                    destination = flight["destination"]
                    break
            self.assertEquals(destination, "destination")

    def test_vehicle(self):
        with open("vehicle_records.json", "r") as file:
            json_file = json.load(file)
            vehicle_json = json_file["vehicle"]["plane"]
            for vehicle in vehicle_json:
                if vehicle["id"] == "testID":
                    self.assertEquals(int(vehicle["capacity"]), 5)
                    break

    def test_change_trip(self):
        self.flight.changeVehicle("Heliplane")
        self.flight.changeDestination("Test")
        self.flight.changeOrigin("TestOrigin")
        self.flight.changeDepartureTime("newTime")
        flight_json = json_open("flight_records.json")
        for flight in flight_json:
            if flight["flightID"] == "flightid":
                self.assertEquals(flight["vehicle"], "heliplane")
                self.assertEquals(flight["destination"], "Test")
                self.assertEquals(flight["origin"], "TestOrigin")
                self.assertEquals(flight["departure"], "newTime")
                break

    def test_add_passenger_to_flight(self):
        self.flight.add_passenger(self.passenger)
        flight_json = json_open("flight_records.json")
        for flight in flight_json:
            if flight["flightID"] == "flightid":
                for passenger in flight:
                    if passenger["passport"] == "passportID":
                        self.assertEquals(passenger["fName"], "fName")
                        self.assertEquals(passenger["lName"], "lName")
                        self.assertEquals(passenger["age"], "age")
                        break

    def test_report(self):
        self.assertIsNotNone(self.flight.report())


def json_open(file_name, perms="r"):
    with open(file_name, perms) as file:
        json_file = json.load(file)
        return json_file[0]
