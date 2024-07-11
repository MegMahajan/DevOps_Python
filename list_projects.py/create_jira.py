# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://megharm30.atlassian.net/rest/api/3/issue"
API_TOKEN= "ATATT3xFfGF0iI3uzNCovfjDRc2TUC9q-64NA7nCdT_2VxpH3VxN8hKWGdZkM5hDz5P9Dj0FWz0Duhpkh09kQEpGh99de_2ULxFXp4QxphK1SBL3cWuyV_lv2u_5vkCH2PrarZgN4Yh5jV21x_okP4KquhPThhVntee8oz8Y0OFN4mYertq2yf0=CC5D5832"

auth = HTTPBasicAuth("megharm30@gmail.com", API_TOKEN)


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
   
   
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First Jira Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    
    "issuetype": {
      "id": "10003"
    },
    
    "project": {
      "key": "MEG"
    },
    
  
    "summary": "My first jira ticket",
  
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))