import pymongo
from datetime import datetime
from trip import Trip

class Reimbursement(Trip):
    
    # Class variable to store the MongoDB collection
    reimbursements_collection = pymongo.MongoClient("mongodb://localhost:27017")["travel_reimbursement"]["reimbursements"]
    def __init__(self, amount,trip_id):
        super().__init__(trip_id, '', '', '', 0, '')  # Initialize Trip attributes
        self.amount = amount
        self.date_processed = datetime.now()
        
    def calculate_reimbursement(self):
        # Simplified reimbursement calculation logic
        return super().calculate_reimbursement()

    def process_reimbursement(self):
        # Process the reimbursement by storing it in the "reimbursements" collection
        Reimbursement_data = {
            "trip_id": self.trip_id,
            "amount": self.amount,
            "date_processed": self.date_processed
        }
        self.reimbursements_collection.insert_one(Reimbursement_data)