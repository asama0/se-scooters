from urllib.parse import urlparse, urljoin
from flask import request, flash
from datetime import timedelta
import re

# check if url in get request is safe
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), category='alert-danger')


#TODO: convert lookup key to time delta

from wtforms import ValidationError


class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'this element already exists'
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

def string_to_timedelta(str):
    matchObj = re.match(r'(\d+)\s(\w+)', str, re.M)
    number = int(matchObj.group(1))
    unit = matchObj.group(2)

    if 'hour' in unit:
        return timedelta(hours=number)
    if 'day' in unit:
        return timedelta(days=number)
    if 'week' in unit:
        return timedelta(weeks=number)