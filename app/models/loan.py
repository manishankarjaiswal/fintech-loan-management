from app import mongo
from bson import ObjectId
from datetime import datetime

class Loan:
    def __init__(self, user_id, amount, tenure, interest_rate, reason, status="Pending"):
        self.user_id = user_id
        self.amount = amount
        self.tenure = tenure
        self.interest_rate = interest_rate
        self.reason = reason
        self.status = status
        self.application_date = datetime.utcnow()
        self.outstanding_balance = amount

    @staticmethod
    def create_loan(user_id, amount, tenure, interest_rate, reason):
        loan = Loan(user_id, amount, tenure, interest_rate, reason)
        result = mongo.db.loans.insert_one(loan.__dict__)
        return str(result.inserted_id)

    @staticmethod
    def get_loan_by_id(loan_id):
        return mongo.db.loans.find_one({"_id": ObjectId(loan_id)})
    
    @staticmethod
    def get_all_loans():
        return mongo.db.loans.find({})

    @staticmethod
    def get_loans_by_user(user_id):
        return list(mongo.db.loans.find({"user_id": user_id}))

    @staticmethod
    def update_loan_status(loan_id, status):
        mongo.db.loans.update_one({"_id": ObjectId(loan_id)}, {"$set": {"status": status}})

    @staticmethod
    def update_outstanding_balance(loan_id, amount):
        mongo.db.loans.update_one(
            {"_id": ObjectId(loan_id)},
            {"$inc": {"outstanding_balance": -amount}}
        )