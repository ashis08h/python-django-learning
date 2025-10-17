import logging
from django.http import HttpResponseForbidden


logger = logging.getLogger(__name__)


class CustomMiddleware:

    def __init__(self, get_response):
        # initialize the middleware
        print("init method")
        self.get_response = get_response

    def __call__(self, request):
        print("I am in call method")
        try:
            logger.info(f"request method is {request.method} and request path is {request.path}")
            print(f"request method is {request.method} and request path is {request.path}")
            print("I am from try")
        except:
            print("I am from except")
            pass
        response = self.get_response(request)
        return response


class BlockIpAddress:

    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_address = ['127.0.0.2',]

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print("ip", ip)
        if ip in self.ip_address:
            return HttpResponseForbidden("You are not allowed")
        response = self.get_response(request)
        return response
