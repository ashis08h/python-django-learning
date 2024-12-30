import jwt
import datetime


# secret key for encoding/decoding.
secret_key = "your_secret_key"


# create a JWT token.
def create_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60) # expiration time.
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Token has expired."
    except jwt.InvalidTokenError:
        return "Invalid Token"


token = create_jwt(user_id=123)
print("token", token)

decoded_data = decode_jwt(token)
print("decoded_data", decoded_data)