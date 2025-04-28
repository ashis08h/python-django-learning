import logging
from django.http import HttpResponseForbidden


logger = logging.getLogger(__name__)


class CustomMiddleware:

    def __init__(self, get_response):
        #Initialize the middleware
        #print("init method.")
        self.get_response = get_response

    def __call__(self, request):
        #print("I am in call method.")
        try:
            logger.info(f"Request Method - {request.method} and request path is {request.path}")
            #print("I am in try")
        except:
            #print("I am in except")
            pass
        #print(f"Request Method - {request.method} and request path is {request.path}")
        response = self.get_response(request)
        return response


class BlockIpAdress:

    def __init__(self, get_response):
        #initialize the middleware
        print("init method")
        self.block_ips = ['127.0.0.2']
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print("ip", ip)
        if ip in self.block_ips:
            return HttpResponseForbidden("Forbidden You are not allowed.")
        response = self.get_response(request)
        return response


class AddContextMiddleware:

    def __init__(self, get_response):
        #initialize the middleware
        print("I am in init method.")
        self.get_response = get_response

    def __call__(self, request):
        print("I am in __call__ method.")
        response = self.get_response(request)
        if hasattr(response, 'context_data'):
            print("come here in temp")
            response.context_data['common_variable'] = "I am custom variable."
        return response

    def process_template_response(self, request, response):
        print("come in process template response")
        if hasattr(response, 'context_data'):
            print("come in temp3")
            response.context_data['common_variable'] = "I am custom variable."
        return response