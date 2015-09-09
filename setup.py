import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid>=1.0.2',
    'pyramid_jinja2==2.5',
    'pyramid_debugtoolbar==2.4.1',
    'wtforms==2.0.2',
    'waitress==0.8.10',
    'requests==2.7.0',
    'beautifulsoup4==4.4.0',

    # test packages
    'nose==1.3.7',
    'coverage==3.7.1',
    'webtest==2.0.18',

    # nice to have
    'pep8',
    'pyflakes',
]

setup(
    name='Scrape Wikipedia',
    version='0.1a',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    test_suite='scrape_wikipedia',
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = scrape_wikipedia:main
    """,
    paster_plugins=['pyramid'],

    author='Olwethu Ntiyonke',
    author_email='olwethu.a@gmail.com',
    description='Scrape Wikipedia content table',
    keywords='pyramid scrape jinja2 wikipedia wtforms',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 0.1a - Alpha",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Web scrape",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
)
