from rest_framework.exceptions import APIException


class BadRequestException(APIException):
    status_code = 400
    default_detail = 'Bad request'
    default_code = 'bad_request'


class NotFoundException(APIException):
    status_code = 404
    default_code = 'Not found register'
    default_code = 'not_found'
