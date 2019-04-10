import pandas as pd
import json

################################################################################
###### ZIP data from github API and packagist API
#################################################################################
with open('downloads.json') as json_file:  
    downloads_file = json.load(json_file)
    versions = downloads_file['package']['downloads']['versions']

with open('releases.json') as json_file:  
    releases = json.load(json_file)

for release in releases:
    name = release['tag_name']
    if(name in versions):
        release['downloads'] = versions[name]['total']

# todo - change to read directly from API instead

################################################################################
###### Convert to np array
#################################################################################

# todo

################################################################################
###### Plot with matlibplot
#################################################################################

# todo