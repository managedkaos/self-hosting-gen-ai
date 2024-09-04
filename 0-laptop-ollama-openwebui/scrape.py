from bs4 import BeautifulSoup
import requests
import json

# URL of the webpage you want to scrape
url = 'https://ollama.com/library'  # Replace with the actual URL

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize an empty list to store the dictionaries for each list item
repo_list = []

# Select the unordered list inside the top element
ul = soup.select_one('#repo > ul')

# Function to clean up text
def clean_text(text):
    return ' '.join(text.split()).replace('\xa0', ' ')

# Function to transform downloads_updates list into a dictionary
def transform_downloads_updates(downloads_updates):
    keys = ['Pulls', 'Tags', 'Updated']
    updates_dict = {}
    for i in range(0, len(downloads_updates), 2):
        if i+1 < len(downloads_updates):
            value = downloads_updates[i]
            key = downloads_updates[i+1]
            if key in keys:
                updates_dict[key] = value
    return updates_dict

# Check if the unordered list is found
if ul:
    # Iterate over each list item inside the unordered list
    for li in ul.find_all('li'):
        # Select the name element
        name_elem = li.select_one('a > div.flex.items-center.mb-3 > h2 > span')
        # Select the description element
        desc_elem = li.select_one('a > div.flex.flex-col.space-y-2 > p.max-w-md.break-words')
        # Select the tools and sizes element
        tools_sizes_elem = li.select_one('a > div.flex.flex-col.space-y-2 > div')
        # Select the downloads and updates element using a more general selector
        downloads_updates_elem = li.select_one('a > div.flex.flex-col.space-y-2 > p.my-2.flex.space-x-5.font-medium.text-neutral-500')

        # Extract the text from the name and description elements
        if name_elem and desc_elem and tools_sizes_elem and downloads_updates_elem:
            name = clean_text(name_elem.text.strip())
            description = clean_text(desc_elem.text.strip())

            # Extract and clean tools and sizes
            tools_sizes = [clean_text(span.text.strip()) for span in tools_sizes_elem.find_all('span')]

            # Extract and clean downloads and updates
            downloads_updates = [clean_text(span.text.strip()) for span in downloads_updates_elem.find_all('span')]
            downloads_updates_dict = transform_downloads_updates(downloads_updates)

            # Add the name, description, tools, and sizes to the dictionary
            repo_list.append({
                'name': name,
                'description': description,
                'tools_sizes': tools_sizes,
                'downloads_updates': downloads_updates_dict
            })

# Write the repo_list to a JSON file
with open('library.json', 'w', encoding='utf-8') as f:
    json.dump(repo_list, f, ensure_ascii=False, indent=4)

print('# Scrape complete!')
