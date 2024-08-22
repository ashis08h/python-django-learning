class CustomMiddleware:

    def __init__(self, get_response):
        # Initialize the middleware
        self.get_response = get_response

    def __class__(self):

        # code to execute for each request before view is called.
        print("request received.")
        respose = 