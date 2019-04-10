import pandas as pd
import json
import matplotlib.pyplot as plt

plt.ion()

################################################################################
###### ZIP data from github API and packagist API
#################################################################################
with open('downloads.json') as json_file:  
    downloads_file = json.load(json_file)
    versions = downloads_file['package']['downloads']['versions']

with open('releases.json') as json_file:  
    releases = json.load(json_file)

cleaned = []
accumulated_downloads = 0
releases.reverse()
for release in releases:
    name = release['tag_name']
    if(name in versions):
        item = json.loads(r'{}')
        item['name'] = name
        item['created_at'] = release['created_at']
        accumulated_downloads = accumulated_downloads + versions[name]['total']
        item['accumulated_downloads'] = accumulated_downloads
        cleaned.append(item)

################################################################################
###### Convert to pandas df
#################################################################################

df = pd.DataFrame(cleaned)
df['created_at'] = pd.to_datetime(df['created_at'])

################################################################################
###### Plot with matlibplot
#################################################################################

df.plot(x='created_at', y='accumulated_downloads')
plt.show()
input("Press any key to continiue")