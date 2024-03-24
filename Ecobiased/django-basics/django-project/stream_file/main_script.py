# import os
# import requests
# import time
#
# # Define the path to the file to be uploaded
# file_path = 'C:/Users/user/Desktop/ss.png'
#
# while True:
#     # Open the file
#     with open(file_path, 'rb') as file:
#         # Make a POST request to the Django server to upload the file
#         response = requests.post('http://localhost:8000/stream-file/', files={'file': file})
#
#         # Print the response from the server
#         print(response.json())
#
#     # Sleep for 60 seconds (1 minute) before uploading the file again
#     time.sleep(60)
