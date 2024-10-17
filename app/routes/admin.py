from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.loan import Loan
from app.models.user import User
from app.models.repayment import Repayment
from app.routes.utils import send_email

bp = Blueprint('admin', __name__)

@bp.route('/admin-dashboard', methods=['GET'])
def admin_dashboard():
    if request.method == 'GET':
        return render_template('admin_dashboard.html')


def is_admin(user_id):
    user = User.get_user_by_id(user_id)
    return user and user.get('is_admin', False)

@bp.route('/loans', methods=['GET'])
@jwt_required()
def get_all_loans():
    current_user = get_jwt_identity()
    if not is_admin(current_user):
        return jsonify({"message": "Unauthorized"}), 403

    loans = list(Loan.get_all_loans())
    for loan in loans:
        loan['_id'] = str(loan['_id'])
    return jsonify(loans), 200

@bp.route('/loan/<loan_id>/approve', methods=['POST'])
@jwt_required()
def approve_loan(loan_id):
    current_user = get_jwt_identity()
    if not is_admin(current_user):
        return jsonify({"message": "Unauthorized"}), 403

    Loan.update_loan_status(loan_id, "Approved")
    subject = "Your Loan Application is Approved"
    body = f"Dear user,\n\nYour loan application has been approved. Congratulations!"
    send_email(subject, body)
    return jsonify({"message": "Loan approved successfully"}), 200

@bp.route('/loan/<loan_id>/reject', methods=['POST'])
@jwt_required()
def reject_loan(loan_id):
    current_user = get_jwt_identity()
    if not is_admin(current_user):
        return jsonify({"message": "Unauthorized"}), 403

    Loan.update_loan_status(loan_id, "Rejected")
    subject = "Your Loan Application is Rejected."
    body = f"Dear user,\n\nYour loan application has been rejected. Sorry!"
    send_email(subject, body)
    return jsonify({"message": "Loan rejected successfully"}), 200

@bp.route('/repayments', methods=['GET'])
@jwt_required()
def get_all_repayments():
    current_user = get_jwt_identity()
    if not is_admin(current_user):
        return jsonify({"message": "Unauthorized"}), 403

    repayments = Repayment.get_all_repayments()
    for item in repayments:
        item['_id'] = str(item['_id'])
    return jsonify(repayments), 200