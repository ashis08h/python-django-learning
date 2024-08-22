import logging
from django.http import HttpResponseForbidden
logger = logging.getLogger(__name__)


class CustomMiddleware:
    """
    middleware to log the details of each incoming request
    """
    def __init__(self, get_response):
        # Initialize the middleware
        print("init_method")
        self.get_response = get_response

    def __call__(self, request):
        print("in call method.")
        # code to execute for each request before view is called.
        logger.info(f"Request Method: {request.method}, Request Path: {request.path}")
        print(f"Request Method: {request.method}, Request Path: {request.path}")
        response = self.get_response(request)
        return response


class BlockIpMiddleware:
    """
    Middleware to block few ip address.
    """

    def __init__(self, get_response):
        # initialize the middleware
        self.block_ips = ['127.0.0.2']
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print("ip", ip)
        if ip in self.block_ips:
            return HttpResponseForbidden("Forbidden: you are not allowed.")

        response = self.get_response(request)
        return response


class AddContextMiddleware:
    """
    Middleware to add extra variable to all the templates.
    """

    def __init__(self, get_response):
        print("come here in tem4")
        self.get_response = get_response

    def __call__(self, request):
        print("come here in tem3")
        response = self.get_response(request)
        if hasattr(response, 'context_data'):
            print("come here in tem2")
            response.context_data['common_variable'] = 'This is common data.'
        return response

    def process_template_response(self, request, response):
        print("come here in tem1")
        if hasattr(response, 'context_data'):
            print("come here in tem2")
            response.context_data['common_variable'] = 'This is common data.'
        return response