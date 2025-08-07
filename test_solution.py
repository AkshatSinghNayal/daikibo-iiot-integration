import json
import unittest
from main import convert_format_1, convert_format_2

class TestFormatConversion(unittest.TestCase):
    def setUp(self):
        # Load test data
        with open('data-1.json', 'r') as f:
            self.data_1 = json.load(f)
        with open('data-2.json', 'r') as f:
            self.data_2 = json.load(f)
        with open('data-result.json', 'r') as f:
            self.expected_result = json.load(f)
            
    def test_format_1_conversion(self):
        result = convert_format_1(self.data_1)
        self.assertEqual(result['timestamp'], self.expected_result['timestamp'])
        self.assertEqual(result['deviceId'], self.expected_result['deviceId'])
        self.assertEqual(result['sensorData'], self.expected_result['sensorData'])
        self.assertEqual(result['status'], self.expected_result['status'])
        
    def test_format_2_conversion(self):
        result = convert_format_2(self.data_2)
        # Check if all fields match the expected format
        self.assertIn('deviceId', result)
        self.assertIn('timestamp', result)
        self.assertIn('sensorData', result)
        self.assertIn('status', result)
        
        # Check field contents
        for sensor in result['sensorData']:
            self.assertIn('sensorType', sensor)
            self.assertIn('value', sensor)

if __name__ == '__main__':
    unittest.main()