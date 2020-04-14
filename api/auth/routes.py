import re
from flask import jsonify, request
from api import db
from api.models import User
from api.auth import bp
from flask_jwt_extended import create_access_token




@bp.route('/register' , methods =['POST'])
def register():
    data = request.get_json(force=True)
    display_name = data['display_name']
    email = data['email']
    password = data['password']
    
    # Validate json body request
    try :
        if not data:
            return {"message": "Kindly input user info"}, 200
        elif not display_name or not email:
            return {"message":
                        "You are missing some fields"}, 400
        elif not password:
            return { "message": "Password cannot be empty"}, 400     
    except:
        return {"KeyError": "Kindly check for missing fields"}, 404
        
        
    if not re.match(
            r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email):
        return {'error': 'Provide a valid email address'}, 400

    elif not str.isalpha(display_name):
        return {'error':
                    'Display Name can only contain alphabets'}, 400

    if len(password) < 7:
        return {'error':
                    'Password must be at least 8 characters long!'}, 400
    elif re.search('[0-9]', (password)) is None:
        return {'error':
                    'Password must be alphanumeric'}, 400
    else:
        #Check if user exist
        user = User.query.filter_by(email=email).first()
        present_display_name = User.query.filter_by(display_name=display_name).first()
        if user or present_display_name:
            return jsonify({ "error": "This is an existing User"}), 400
           # else go ahead and register the user
        new_user = User(display_name=display_name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        payload = { "id": new_user.id, "email": new_user.email, display_name:new_user.display_name}
        token = create_access_token(identity=payload)
        response = {'success': True, 'message': 'Account Creation Successful', 'token': token}
        return jsonify(response), 201