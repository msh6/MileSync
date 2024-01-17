import pymongo

class Employee:
    "Defining the employee class and its attributes."
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
        
class InsertEmployee(Employee):
    "Class for inserting an employee to the database."
    
    employees_collection = pymongo.MongoClient("mongodb://localhost:27017")["travel_reimbursement"]["employees"]
    
    def insert_employee(self):
        employee_data = {
            "emp_id": self.emp_id,
            "name": self.emp_name
        }
        self.employees_collection.insert_one(employee_data)