import requests
import json
import base64
import pandas as pd

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

#Add Column Names to Dataframe
df = pd.DataFrame(columns =['Customer','Key','Summary','Status', 'Created','Updated'])

organisations = []
# Display issues
for item in json_data["issues"]: 
    for organization in item['fields']['customfield_10500']:
        df = df.append({
          'Customer': organization['name'],
          'Key' : item["key"],
          'Summary': item["fields"]["summary"],
          'Status': item["fields"]["status"]["name"],
          'Created': item["fields"]["created"],
          'Updated': item["fields"]["updated"]
       }, ignore_index=True)

df.to_csv (r'Customer_Support_Weekly_Meeting'+str(datetime.now().date())+'.csv')

    


