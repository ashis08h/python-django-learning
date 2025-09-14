import jwt
import datetime


secret_key = "Your secret key"


def create_token(user_id):
   payload = {
       "user_id": user_id,
       "exp": datetime.datetime.now() + datetime.timedelta(minutes=60) # for expiration time
   }
   token = jwt.encode(payload, secret_key, algorithm='HS256')
   return token


def decode_token(token):

    try:
        jwt.decode(token, secret_key, algorithm='HS256')
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"


token = create_token('123')
print(token)

decoded_token = decode_token(token)
print("decoded_token", decoded_token)

