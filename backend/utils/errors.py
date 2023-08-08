def INVALID_FIELD_PARAMETER(field):
    return {'detail': f'{field} is invalid'}


def EMPTY_FIELD(field):
    return {'detail': f'{field} cannot be empty'}


UNEXPECTED_ERROR = {'detail': 'Something went wrong!'}

WRONG_CREDENTIALS = {'detail': 'Wrong credentials!'}


def ALREADY_EXISTS(field):
    return {'detail': f'{field} already exists'}


def NOT_FOUND(field):
    return {'detail': f'{field} not found!'}