## Wikipedia Table of Contents Scraper

Project forked from [Alvaro Aguirre] (https://github.com/aaguirre/FrameWars.Contacs)

Simple application to scrape the table of contents from a Wikipedia page:

* 1. The homepage shows a welcome message and present the user with an input box that asks for a Wikipedia URL
    and a submit button.
* 2. When the submit button is clicked, the application downloads the HTML source code for the given page and scrapes
    the table of contents for the given page.
* 3. The table of contents is posted back to the user in a new page in html format.
* 4. The showing the table of contents provides a reset button that will allow the user to restart the process.

### Settings
------------
**ALLOWED_DOMAINS**: List of domains to scrape from.


### Getting up and running
---------------------------

##### Basics


The steps below will get you up and running with a local development environment.
We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the
requirements for local development:

* $ pip install -e <path-to-setup.py>

Run **develop** on your new database:

* $ python setup.py develop

You can now run the **pserve** command:

* $ pserve development.ini

Open up your browser to http://127.0.0.1:6543/ to see the site running locally.


##### Test coverage

To run the tests, check your test coverage:

* $ nosetests

