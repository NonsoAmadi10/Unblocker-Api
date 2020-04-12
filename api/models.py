from api import db, marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import uuid




class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    email = db.Column(db.String(255), unique=True)
    display_name = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))
    
    
    
    
    def __repr__(self):
        return f"User {self.email}"
    def set_password(self, password):
            self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
    
    
class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'email', 'fullname')