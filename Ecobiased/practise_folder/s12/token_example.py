import jwt
import datetime


# secret key for encoding and decoding
secret_key = "Your_secret_key"


def create_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60) # exptime
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, secret_key, algorithm='HS256')
        return decoded
    except jwt.ExpirdSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"


token = create_jwt('123')
print(token)

decoded_data = decode_jwt(token)
print(decoded_data)