from flask import jsonify
from api.models import User
from api.auth import bp 




@bp.route('/api/v1/' , methods =['GET'])
def home():
    hello = 'hello, how are you?'
    return jsonify({'message': hello})