import pymongo
from datetime import datetime

class Trip:
    "Defining a trip class and its attributes."
    def __init__(self, trip_id, emp_id, departure_time, arrival_time, miles, mode_of_transportation):
        self.trip_id = trip_id
        self.emp_id = emp_id
        self.departure_time = self.parse_datetime(departure_time)
        self.arrival_time = self.parse_datetime(arrival_time)
        self.miles = miles
        self.mode_of_transportation = mode_of_transportation
        
    def parse_datetime(self, datetime_input):
        # Custom method to parse datetime from string or datetime object
        if isinstance(datetime_input, str):
            try:
                return datetime.strptime(datetime_input, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                print("Error parsing datetime. Please use the format 'YYYY-MM-DDTHH:MM:SS'")
                return None
        elif isinstance(datetime_input, datetime):
            return datetime_input
        else:
            print("Invalid datetime format.")
            return None
            
    def calculate_reimbursement(self):
        # Simplified reimbursement calculation
        if self.mode_of_transportation == "Car" or "car":
            # Assuming a fixed rate per mile for car trips
            rate_per_mile = 0.5
            distance_travelled = self.miles
            reimbursement_amount = rate_per_mile * distance_travelled
        elif self.mode_of_transportation == "Plane" or "plane":
            # Assuming a fixed amount for plane trips
            reimbursement_amount = 120.00
        else:
            reimbursement_amount = 0
        return reimbursement_amount
            
class AddTrip(Trip):
    "Class for inserting an trip to the atabase."
    trips_collection = pymongo.MongoClient("mongodb://localhost:27017")["travel_reimbursement"]["trips"]
    
    def insert_trip(self):
        trip_data = {
            "trip_id": self.trip_id,
            "emp_id": self.emp_id,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "mode_of_transportation": self.mode_of_transportation
        }
        self.trips_collection.insert_one(trip_data)