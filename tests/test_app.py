import unittest
from server.server import app  # Import the Flask app from server.py

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        # Setting up the Flask test client
        self.app = app.test_client()  # Create a test client instance
        self.app.testing = True  # Enable testing mode for Flask

    def test_home_price_prediction(self):
        # Test the home price prediction route
        response = self.app.post('/predict_home_price', data=dict(
            total_sqft=1000,
            location='akshaya nagar',
            bhk=3,
            bath=2
        ))
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertIn('estimated_price', response.json)  # Check if 'estimated_price' is in the response

    def test_get_location_names(self):
        # Test the location names endpoint
        response = self.app.get('/get_location_names')
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertIn('locations', response.json)  # Check if 'locations' is in the response

if __name__ == '__main__':
    unittest.main()
