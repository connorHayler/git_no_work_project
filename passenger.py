import json


# Creates a passenger and adds passenger info to database
class Passenger:
    def __init__(self, first_name, last_name, passport_number, age):
        self.f_name = first_name
        self.l_name = last_name
        self.passport = passport_number
        self.age = age

    def add_record(self):
        dic = {'passport': self.passport,
               'fName': self.f_name.lower(),
               'lName': self.l_name.lower(),
               'age': self.age}
        # Some function to not reduce seat number

        # Reads, Updates and Closes json file
        with open("passenger_records.json", "r+") as file:
            data = json.load(file)
            data["passenger"].append(dic)
            file.seek(0)
            json.dump(data, file, indent=4)
