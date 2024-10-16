# Simple Loan Management System

## Objective
This project is a simple FinTech loan management system where users can:
- Register and log in
- Apply for loans
- Track loan status (Pending, Approved, Rejected, Repaid)
- Make loan repayments
- Admin can approve/reject loan applications and track all loan statuses.

## Features
1. **User Registration & Login**:
   - Register users with details (name, email, phone, password) and is_admin for admin user.
   - Login using JWT for authentication or session management.

2. **Loan Application**:
   - Logged-in users can apply for loans by providing loan amount, tenure, interest rate, and reason.
   - Applications are stored in MongoDB.

3. **Loan Status Tracking**:
   - Users can view their loan status (Pending, Approved, Rejected, Repaid) on a dashboard.
   - Admin can approve or reject loans.

4. **Loan Repayment**:
   - Users can make repayments towards their loan, and the system will update the balance and track repayment history.

5. **Admin Functionality**:
   - Admin users can approve/reject loan applications.
   - Admin can view all loan applications and repayment statuses.

## Tools & Technologies
- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Version Control**: Git

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Flask-PyMongo
- Git
- Flask-JWT-Extended
- bcrypt

### Steps to Run Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/loan-management-system.git
   cd loan-management-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB**:
   - Ensure MongoDB is running locally.
   - Modify the `config.py` file to include your MongoDB connection string.

4. **Run the Flask App**:
   ```bash
   flask run
   ```

5. **Access the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.
   - Use the provided registration and login pages to create users and test loan functionalities.

### MongoDB Schema
- **Users Collection**: Stores user details (name, email, password (hashed), phone).
- **Loans Collection**: Stores loan details (user ID, loan amount, tenure, interest rate, status).
- **Repayments Collection**: Tracks repayment transactions (amount paid, date, balance).

## Assumptions
- The project assumes users are authenticated using JWT tokens for secure API access.
- MongoDB is used to store all user, loan, and repayment data.

## API Documentation
- **User Registration**: `POST /register`
- **User Login**: `POST /login`
- **Loan Application**: `POST /apply`
- **Loan Status**: `GET /status`
- **Loan Repayment**: `POST /repay/<loan_id>`
- **GET Loan Repayments**: `GET /repayments/<loan_id>`
- **Admin Approve/Reject**: `POST /loan/<loan_id>/approve(reject)`
- **Admin Get All loans**: `GET /loans`
