import logging
from django.http import HttpResponseForbidden


logger = logging.getLogger(__name__)


class CustomMiddleware:

    def __init__(self, get_response):
        # Initialize the middleare
        print("init method")
        self.get_response = get_response

    def __call__(self, request):
        print("I am in call method")
        try:
            logger.info(f"Request Method - {request.method} and request path is {request.path}")
            print(f"Request Method - {request.method} and request path is {request.path}")
            print("I am from try.")
        except:
            print("I am from except")
            pass
        response = self.get_response(request)
        return response


class BlockIpAdress:

    def __init__(self, get_response):
        self.get_response = get_response
        self.block_ips = ['127.0.0.2']

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print("ip", ip)
        if ip in self.block_ips:
            return HttpResponseForbidden("You are not allowed.")
        response = self.get_response(request)
        return response