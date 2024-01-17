from employee import Employee
from trip import Trip
from reimbursement import Reimbursement

class TravelManagementSystem:
    "Class for Travel Management System that initiates all the work."
    def __init__(self):
        self.employees = []
        self.trips = []
        self.reimbursements = []
        
    def add_employee(self, emp_id, name):
        employee = Employee(emp_id, name)
        self.employees.append(employee)
        return employee
    
    def add_trip(self, trip_id, emp_id, departure_time, 
        arrival_time, miles, mode_of_transportation):
        trip = Trip(trip_id, emp_id, departure_time, arrival_time, miles, mode_of_transportation)
        self.trips.append(trip)
        return trip
        
    def request_reimbursement(self, trip):
        amount = trip.calculate_reimbursement()
        reimbursement = Reimbursement(amount, trip.trip_id)
        self.reimbursements.append(reimbursement)
        return reimbursement