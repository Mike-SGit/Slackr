from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 400
    message = 'No message specified'

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

"""
Incorrect testing:
    from errors import AccessError, ValueError
    pytest.raises(AccessError)

Correct testing:
    import errors
    pytest.raises(errors.AccessError)
"""
