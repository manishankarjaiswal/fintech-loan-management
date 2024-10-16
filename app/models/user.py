from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

class User:
    def __init__(self, name, email, phone, password, is_admin=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    @staticmethod
    def create_user(name, email, phone, password):
        user = User(name, email, phone, password)
        mongo.db.users.insert_one(user.__dict__)

    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({"email": email})
    
    @staticmethod
    def get_user_by_id(id):
        return mongo.db.users.find_one({"_id": ObjectId(id)})