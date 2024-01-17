from datetime import datetime
from employee import InsertEmployee
from trip import AddTrip
from reimbursement import Reimbursement
from travel_management_system import TravelManagementSystem

def main():
    tms = TravelManagementSystem()

    while True:
        print("\nWelcome to the Travel Management System CLI")
        print("1. Add Employee")
        print("2. Add Trip")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            employee = tms.add_employee(emp_id=emp_id, name=emp_name)
            insert_employee = InsertEmployee(emp_id=employee.emp_id, emp_name=employee.emp_name)
            insert_employee.insert_employee()
            print(f"Employee '{employee.emp_name}' added successfully.")

        elif choice == "2":
            trip_id = input("Enter Trip ID: ")
            emp_id = input("Enter Employee ID: ")
            departure_time = input("Enter Departure Time (format: 'YYYY-MM-DDTHH:MM:SS'): ")
            arrival_time = input("Enter Arrival Time (format: 'YYYY-MM-DDTHH:MM:SS'): ")
            miles = float(input("Enter Miles traveled: "))
            mode_of_transportation = input("Enter Mode of Transportation: ")

            # Ensure the datetime strings are in the correct format
            try:
                datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S")
                datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                print("Error parsing datetime. Please use the format 'YYYY-MM-DDTHH:MM:SS'")
                continue

            trip = tms.add_trip(
                trip_id=trip_id,
                emp_id=emp_id,
                departure_time=departure_time,
                arrival_time=arrival_time,
                miles=miles,
                mode_of_transportation=mode_of_transportation
            )

            add_trip = AddTrip(
                trip_id=trip.trip_id,
                emp_id=trip.emp_id,
                departure_time=trip.departure_time,
                arrival_time=trip.arrival_time,
                miles=trip.miles,
                mode_of_transportation=trip.mode_of_transportation
            )
            add_trip.insert_trip()
            print(f"Trip '{trip.trip_id}' added successfully.")

            reimbursement = tms.request_reimbursement(trip)
            reimbursement.process_reimbursement()
            print(f"Reimbursement requested and processed: ${reimbursement.amount}")

        elif choice == "3":
            print("Exiting the Travel Management System CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()