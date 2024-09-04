from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_services_page_staturs_code(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code,200)
        
    def test_news_page_staturs_code(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code,200)