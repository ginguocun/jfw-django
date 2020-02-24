from django.utils.deprecation import MiddlewareMixin


class MiddlewareHead(MiddlewareMixin):

    @staticmethod
    def process_response(request, response):
        if request:
            response['Access-Control-Allow-Origin'] = '*'
            response['Content-Type'] = 'application/json;charset=utf-8'
        return response
