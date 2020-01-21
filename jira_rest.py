import requests
import json
import base64

# Base encode email and api token
cred =  "Basic " + base64.b64encode(b'<JIRA EMAIL>:<JIRA API KEY>').decode("utf-8") 
# Set header parameters
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization" : cred
}


# Update your site url 
url = 'https://jira.atlassian.net/rest/api/3/search?jql=' + "JQL Query"

# Send request and get response
response = requests.request(
   "GET", 
   url,
   headers=headers
)

# Decode Json string to Python
json_data = json.loads(response.text)

# Display issues
for item in json_data["issues"]:
    print(item["key"] + "\t" +
        item["fields"]["issuetype"]["name"] + "\t" +
        item["fields"]["created"]+ "\t" +
        item["fields"]["creator"]["displayName"] + "\t" +
        item["fields"]["status"]["name"] + "\t" +
        item["fields"]["summary"] + "\t" +
        str(((item["fields"]["timespent"]/60)/60)) + "\t" +
        str(item["fields"]["aggregatetimeoriginalestimate"]) + "\t"
        )
    
