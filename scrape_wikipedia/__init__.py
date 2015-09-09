from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.scan()

    config.add_static_view('static', 'scrape_wikipedia:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("scrape_wikipedia:templates")
    return config.make_wsgi_app()
