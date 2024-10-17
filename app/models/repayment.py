from app import mongo
from datetime import datetime

class Repayment:
    def __init__(self, loan_id, amount, payment_date=None):
        self.loan_id = loan_id
        self.amount = amount
        self.payment_date = payment_date or datetime.utcnow()

    @staticmethod
    def create_repayment(loan_id, amount):
        repayment = Repayment(loan_id, amount)
        mongo.db.repayments.insert_one(repayment.__dict__)

    @staticmethod
    def get_repayments_by_loan(loan_id):
        return list(mongo.db.repayments.find({"loan_id": loan_id}).sort({"payment_date":-1}))
    
    @staticmethod
    def get_all_repayments():
        return list(mongo.db.repayments.find({}).sort({"payment_date":-1}))