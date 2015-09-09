import wtforms

from scrape_wikipedia import settings
from .validators import ValidDomain


class UrlForm(wtforms.Form):
    """
    Simple form that only allows valid Wikipedia page(s) URLs to be submitted.
    """
    allowed_domains = getattr(settings, 'ALLOWED_DOMAINS', ['wikipedia.org'])
    url = wtforms.StringField(u'Wikipedia url',  [
        wtforms.validators.required(), wtforms.validators.length(max=512), wtforms.validators.URL(),
        ValidDomain(message=u'Only URLs on the {0} domain(s) are allowed.'.format(allowed_domains)),
    ])
