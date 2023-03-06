"""
The various HTTP responses for use in returning proper HTTP codes.
"""
from django.http import HttpResponse


#
class GenericHttpResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super(GenericHttpResponse, self).__init__(*args, **kwargs)
        self["Content-Type"] = "application/json"


#
class HttpCreated(GenericHttpResponse):
    status_code = 201


#
class HttpAccepted(GenericHttpResponse):
    status_code = 202


#
class HttpNoContent(GenericHttpResponse):
    status_code = 204

    def __init__(self, *args, **kwargs):
        super(HttpNoContent, self).__init__(*args, **kwargs)
        del self["Content-Type"]


#
class HttpMultipleChoices(GenericHttpResponse):
    status_code = 300


#
class HttpSeeOther(GenericHttpResponse):
    status_code = 303


#
class HttpNotModified(GenericHttpResponse):
    status_code = 304


#
class HttpBadRequest(GenericHttpResponse):
    status_code = 400


#
class HttpUnAuthorized(GenericHttpResponse):
    status_code = 401


#
class HttpMissedRequiredField(GenericHttpResponse):
    status_code = 402


#
class HttpForbidden(GenericHttpResponse):
    status_code = 403


#
class HttpNotFound(GenericHttpResponse):
    status_code = 404


#
class HttpMethodNotAllowed(GenericHttpResponse):
    status_code = 405


#
class HttpNotAcceptable(GenericHttpResponse):
    status_code = 406


#
class HttpMultipleObjectsFound(GenericHttpResponse):
    status_code = 407


#
class HttpObjectNotFound(GenericHttpResponse):
    status_code = 408


#
class HttpConflict(GenericHttpResponse):
    status_code = 409


#
class HttpGone(GenericHttpResponse):
    status_code = 410


#
class HttpRequestNotPermitted(GenericHttpResponse):
    status_code = 411


#
class HttpUnsupportedMediaType(GenericHttpResponse):
    status_code = 415


#
class HttpUnprocessableEntity(GenericHttpResponse):
    status_code = 422


#
class HttpTooManyRequests(GenericHttpResponse):
    status_code = 429


#
class HttpApplicationError(GenericHttpResponse):
    status_code = 500


#
class HttpNotImplemented(GenericHttpResponse):
    status_code = 501
