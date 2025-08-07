import json
from datetime import datetime
import time

# This function converts data from format 1 to the unified format
def convert_format_1(data):
    # Create a copy of the input data to modify
    result = data.copy()
    
    # If the timestamp is in ISO format, convert it to milliseconds
    if isinstance(result.get('timestamp'), str):
        # Parse ISO format timestamp to datetime object
        dt = datetime.fromisoformat(result['timestamp'].replace('Z', '+00:00'))
        # Convert to milliseconds (Unix timestamp * 1000)
        result['timestamp'] = int(dt.timestamp() * 1000)
    
    # Make any other necessary adjustments to match target format
    # Rename fields if needed based on the target format
    if 'deviceID' in result and 'deviceId' not in result:
        result['deviceId'] = result.pop('deviceID')
    
    # Process nested structures if needed
    if 'sensorData' in result and isinstance(result['sensorData'], list):
        for sensor in result['sensorData']:
            if 'sensor_type' in sensor and 'sensorType' not in sensor:
                sensor['sensorType'] = sensor.pop('sensor_type')
            if 'reading_value' in sensor and 'value' not in sensor:
                sensor['value'] = sensor.pop('reading_value')
    
    return result

# This function converts data from format 2 to the unified format
def convert_format_2(data):
    # Create a copy of the input data to modify
    result = data.copy()
    
    # Rename fields if necessary to match target format
    if 'device_id' in result and 'deviceId' not in result:
        result['deviceId'] = result.pop('device_id')
    
    if 'sensor_data' in result and 'sensorData' not in result:
        result['sensorData'] = result.pop('sensor_data')
    
    # Process nested structures if needed
    if 'sensorData' in result and isinstance(result['sensorData'], list):
        for sensor in result['sensorData']:
            if 'sensor_type' in sensor and 'sensorType' not in sensor:
                sensor['sensorType'] = sensor.pop('sensor_type')
            if 'reading_value' in sensor and 'value' not in sensor:
                sensor['value'] = sensor.pop('reading_value')
    
    return result

# The code below would be used to run tests in the repl environment
if __name__ == "__main__":
    # This would load and process test data
    print("Running tests for Daikibo IIoT data integration...")