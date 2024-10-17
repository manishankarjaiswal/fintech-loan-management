from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.loan import Loan
from app.models.repayment import Repayment
from app.routes.utils import send_email

bp = Blueprint('loan', __name__)

@bp.route('/dashboard', methods=['GET'])
def apply_dashboard():
    if request.method == 'GET':
        return render_template("dashboard.html")
    
@bp.route('/apply-loan', methods=['GET'])
def apply_loan_dashboard():
    if request.method == 'GET':
        return render_template("loan_application.html")

@bp.route('/apply', methods=['POST'])
@jwt_required()
def apply_loan():
    if request.method == 'GET':
        return render_template("loan_application.html")
    
    current_user = get_jwt_identity()
    data = request.get_json()
    amount = data.get('amount')
    tenure = data.get('tenure')
    interest_rate = data.get('interest_rate')
    reason = data.get('reason')

    loan_id = Loan.create_loan(current_user, int(amount), tenure, interest_rate, reason)
    return jsonify({"message": "Loan application submitted successfully", "loan_id": loan_id}), 201

@bp.route('/loan-status', methods=['GET'])
def loan_status_page():
    if request.method == 'GET':
        return render_template("loan_status.html")

@bp.route('/status', methods=['GET'])
@jwt_required()
def loan_status():
    current_user = get_jwt_identity()
    loans = Loan.get_loans_by_user(current_user)
    for loan in loans:
        loan['_id'] = str(loan['_id'])
    return jsonify(loans), 200

@bp.route('/loan-emi', methods=['GET'])
def loan_emi():
    if request.method == 'GET':
        return render_template("repay.html")

@bp.route('/repay/<loan_id>', methods=['POST'])
@jwt_required()
def repay_loan(loan_id):
    data = request.get_json()
    amount = int(data.get('amount'))

    loan = Loan.get_loan_by_id(loan_id)
    if not loan:
        return jsonify({"message": "Loan not found"}), 404

    if int(loan['outstanding_balance']) < int(amount):
        return jsonify({"message": "Repayment amount exceeds outstanding balance"}), 400

    Repayment.create_repayment(loan_id, amount)
    Loan.update_outstanding_balance(loan_id, amount)
    subject = "Your EMI payment is Successfull"
    body = f"Dear user,\n\nYour loan EMI payment is Successfull. Congratulations!"
    send_email(subject, body)

    return jsonify({"message": "Repayment successful"}), 200

@bp.route('/repayments/<loan_id>', methods=['GET'])
@jwt_required()
def get_repayments(loan_id):
    repayments = Repayment.get_repayments_by_loan(loan_id)
    for item in repayments:
        item['_id'] = str(item['_id'])
    return jsonify(repayments), 200