from rest_framework.views import exception_handler
from django.http import Http404

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    response.data['result'] = "error"
    #print(exc,"\n",context,"\n",response)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    detail = response.data['detail']
    del response.data['detail']
    response.data['detail'] = detail

    return response
