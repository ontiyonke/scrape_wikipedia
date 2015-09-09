from wtforms import ValidationError

from .utils import is_allowed


class ValidDomain(object):
    """
    Simple validator to check if the entered URL is with the allowed domains.

    :param message:
        Error message to raise in case of a validation error.
    """
    def __init__(self, message=None):
        if not message:
            message = u'Invalid domain URL.'
        self.message = message

    def __call__(self, form, field):
        if not is_allowed(field.data):
            raise ValidationError(self.message)
