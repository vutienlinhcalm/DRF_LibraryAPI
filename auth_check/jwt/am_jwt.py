from datetime import datetime, timedelta
import jwt
import uuid

class am_jwt:
    jwtSecretKey = "djalisdSDNNkialero364nsa8ndn0skemx16ydbh9osdh7fu"
    jwtAlgorithm = "HS512"

    def create_jwt_token(user_id, jwtSecretKey, expiration):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration)
        payload = {
        'user_id': user_id,
        'exp': expiration_time,
        'jti': str(uuid.uuid4())  # Generate a unique JTI (JWT ID)
        }
        token = jwt.encode(payload, jwtSecretKey, algorithm='HS256')

        return token