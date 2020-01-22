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
df = pd.DataFrame(columns =['Key','Issue Type', 'Created', 'Reporter','Assignee', 'Status','Task Name', 'Time Spent', 'Original Estimate', 'Time Remaining', 'Time Spent Hours'])

i=2
# Display issues
for item in json_data["issues"]: 
   
   assignedTo =""
   if item["fields"]["assignee"] is None:
      assignedTo ="Unassigned"
   else: 
       assignedTo = item["fields"]["assignee"]["displayName"]
              
   df = df.append({'Key' : item["key"],
          'Issue Type': item["fields"]["issuetype"]["name"],
          'Created': item["fields"]["created"],
          'Reporter': item["fields"]["creator"]["displayName"],
          'Assignee': assignedTo,
          'Status': item["fields"]["status"]["name"],
          'Task Name': item["fields"]["summary"],
          'Time Spent': item["fields"]["timespent"],
          'Original Estimate' : item["fields"]["aggregatetimeoriginalestimate"],
          'Time Remaining': "=J"+str(i) +"-I" +str(i),
          'Time Spent Hours': "=((I"+str(i)+"/60)/60)",
          'Original Estimate Hours':"=((J"+str(i)+"/60)/60)", 
          'Time Remaining Hours': "=((K"+str(i)+"/60)/60)",},ignore_index = True)
   i = i + 1  
            
df.to_csv (r'PATH'+str(datetime.now().date())+'.csv')
print("done")

