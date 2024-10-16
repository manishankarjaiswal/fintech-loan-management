from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.loan import Loan
from app.models.user import User

bp = Blueprint('admin', __name__)

def is_admin(user_id):
    user = User.get_user_by_id(user_id)
    return user and user.get('is_admin', False)

@bp.route('/loans', methods=['GET'])
@jwt_required()
def get_all_loans():
    current_user = get_jwt_identity()
    print(current_user)
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
    return jsonify({"message": "Loan approved successfully"}), 200

@bp.route('/loan/<loan_id>/reject', methods=['POST'])
@jwt_required()
def reject_loan(loan_id):
    current_user = get_jwt_identity()
    if not is_admin(current_user):
        return jsonify({"message": "Unauthorized"}), 403

    Loan.update_loan_status(loan_id, "Rejected")
    return jsonify({"message": "Loan rejected successfully"}), 200