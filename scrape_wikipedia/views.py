import logging

import requests
from bs4 import BeautifulSoup
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from .forms import UrlForm

logger = logging.getLogger('scrape_wikipedia')


@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    """
    Homepage displays a welcome message and present the user with an input box that asks for a Wikipedia URL
    and a submit button.
    """
    form = UrlForm(request.POST)
    if request.method == 'POST' and form.validate():
        url = form.url.data
        request.session['scrape_url'] = url
        return HTTPFound(location=request.relative_url('view_scraped_content'))
    return {'form': form, 'project': 'Scrape Wikipedia'}


@view_config(name='view_scraped_content', renderer='view_scraped_content.jinja2')
def view_scraped_content(request):
    """
    Check if a valid Wikipedia URL exists in session if it does download the HTML source code for the given page and
    scrape the table of contents for the given page. Storing the url in session allows us to repeat this process for
    every page reload provided the user was initially redirected here after submitting a form with a valid Wikipedia
    URL else just display a link back to the page with the form.
    """
    scrape_url = request.session.get('scrape_url')
    contents_table = None
    if scrape_url:
        response = requests.get(scrape_url)
        soup = BeautifulSoup(response.text)
        contents_table = soup.find("div", {"id": "toc"})
    return {'contents_table': contents_table, 'project': 'Scrape Wikipedia'}
