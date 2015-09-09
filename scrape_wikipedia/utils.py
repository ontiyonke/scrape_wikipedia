import re
from urlparse import urlparse

import settings


def get_host_regex():
    """
    gets the allowed domains to scrape from.
    """
    allowed_domains = getattr(settings, 'ALLOWED_DOMAINS', ['wikipedia.org'])
    if not allowed_domains:
        return re.compile('') # allow all by default
    regex = r'^(.*\.)?(%s)$' % '|'.join(re.escape(d) for d in allowed_domains if d is not None)
    return re.compile(regex)


def is_allowed(url):
    """
    checks if the inserted url is in the allowed domains, for this case
    """
    regex = get_host_regex()
    host = urlparse(url).hostname or ''
    return bool(regex.search(host))
