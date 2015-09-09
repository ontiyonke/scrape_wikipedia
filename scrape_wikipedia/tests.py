import unittest
from pyramid import testing


class TestViewScrapedContent(unittest.TestCase):

    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_empty_view_scraped_content(self):
        """
        Test for when a user lands on the scrape results page without submitting a Wikipedia URL.
        """
        from .views import view_scraped_content
        info = view_scraped_content(self.request)
        self.assertEqual(info['project'], 'Scrape Wikipedia')
        self.assertIsNone(info['contents_table'])

    def test_valid_view_scraped_content(self):
        """
        Test for when a valid Wikipedia URL was saved on session
        """
        from .views import view_scraped_content
        self.request.session['scrape_url'] = 'https://en.wikipedia.org/wiki/Pylons_project'
        info = view_scraped_content(self.request)
        self.assertEqual(info['project'], 'Scrape Wikipedia')
        self.assertIsNotNone(info['contents_table'])

    def test_invalid_view_scraped_content(self):
        """
        Test for when a invalid Wikipedia URL was saved on session
        """
        from .views import view_scraped_content
        self.request.session['scrape_url'] = 'https://en.wikipedia.org/wiki/Pylons_project1111'
        info = view_scraped_content(self.request)
        self.assertEqual(info['project'], 'Scrape Wikipedia')
        self.assertIsNone(info['contents_table'])


class TestUrlForm(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_valid_wikipedia_url_submit(self):
        from .forms import UrlForm
        url = 'https://en.wikipedia.org/wiki/Pylons_project'
        form = UrlForm(url=url)
        self.assertTrue(form.validate())
        self.assertEqual(form.data['url'], url)
        self.assertEqual(len(form.errors), 0)

    def test_invalid_missing_protocol_wikipedia_url_submit(self):
        from .forms import UrlForm
        invalid_url = 'www.wikipedia.org/wiki/Pylons_project'
        form = UrlForm(url=invalid_url)
        self.assertFalse(form.validate())
        self.assertEqual(form.data['url'], invalid_url)
        self.assertGreater(len(form.errors), 0)

    def test_invalid_empty_wikipedia_url_submit(self):
        from .forms import UrlForm
        empty_url = ''
        form = UrlForm(url=empty_url)
        self.assertFalse(form.validate())
        self.assertEqual(form.data['url'], empty_url)
        self.assertGreater(len(form.errors), 0)

    def test_invalid_wikipedia_url_submit(self):
        from .forms import UrlForm
        invalid_url = 'invalid url'
        form = UrlForm(url=invalid_url)
        self.assertFalse(form.validate())
        self.assertEqual(form.data['url'], invalid_url)
        self.assertGreater(len(form.errors), 0)


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_invalid_wikipedia_url_submit(self):
        from .utils import is_allowed
        invalid_url = 'invalid url'
        self.assertFalse(is_allowed(invalid_url))

    def test_invalid_domain_wikipedia_url_submit(self):
        from .utils import is_allowed
        invalid_url = 'https://google.co.za'
        self.assertFalse(is_allowed(invalid_url))

    def test_valid_domain_wikipedia_url_submit(self):
        from .utils import is_allowed
        invalid_url = 'https://en.wikipedia.org/wiki/Pylons_project'
        self.assertTrue(is_allowed(invalid_url))


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from scrape_wikipedia import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_get_home_page(self):
        res = self.testapp.get('/', status=200)
        self.assertEqual(res.status_code, 200)
        # check if we have a form to submit a Wikipedia URL on.
        self.assertGreater(len(res.forms), 0)
