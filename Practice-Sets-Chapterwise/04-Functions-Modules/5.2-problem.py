import requests

# URL of GitHub API
url = "https://api.github.com"

# Send GET request
response = requests.get(url)

# Check status
print("Status Code:", response.status_code)

# Print JSON response
print("Response Data:")
print(response.json())