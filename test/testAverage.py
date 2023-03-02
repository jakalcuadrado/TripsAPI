import requests

# Define the base URL for the API
BASE_URL = 'http://localhost:5000'

# Define the test cases
test_cases = [
    {'params': {'region': 'Prague'}, 'expected_output': {'weekly_average_trips in Prague': 1.0}},
    {'params': {'bbox': '14.0,49.8,14.6,50.2'}, 'expected_output': {'weekly_average_trips in 14.0,49.8,14.6,50.2': 1.0}},
]

# Test the endpoint for each test case
for i, test_case in enumerate(test_cases):
    params = test_case['params']
    expected_output = test_case['expected_output']

    # Send the request to the API
    response = requests.get(f'{BASE_URL}/weekly_average_trips', params=params)
    print(response)
    print()
    # Check the response status code
    assert response.status_code == 200, f'Test case {i+1} failed: Unexpected status code {response.status_code}'

    # Check the response content
    response_json = response.json()
    assert response_json == expected_output, f'Test case {i+1} failed: Unexpected response {response_json}'

    print(f'Test case {i+1} passed')
