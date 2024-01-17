# MileSync
 Travel Reimburse Management System

# Travel Management System

The Travel Management System is a command-line application that manages employees, trips, and reimbursements for travel expenses. It interacts with a MongoDB database to store and retrieve information.

## Features

1. **Add Employee:**
   - Enter Employee ID and Name.
   - Stores employee info in the MongoDB database.

2. **Add Trip:**
   - Enter Trip ID, Employee ID, Departure Time, Arrival Time, Miles, and Mode of Transportation.
   - Validates and stores trip info in MongoDB.
   - Calculates reimbursement based on transportation.

3. **Request Reimbursement:**
   - Initiates a reimbursement request for a specific trip.
   - Processes and stores reimbursement in MongoDB.

## Project Structure

- **employee.py:** Defines `Employee` and `InsertEmployee` classes.
- **trip.py:** Defines `Trip` and `AddTrip` classes.
- **reimbursement.py:** Defines `Reimbursement` class.
- **travel_management_system.py:** Defines `TravelManagementSystem` class.
- **main.py:** Main script for running the CLI.

## Usage

1. **Clone:**

   ```bash
   git clone https://github.com/msh6/travel-management-system.git
   cd travel-management-system
