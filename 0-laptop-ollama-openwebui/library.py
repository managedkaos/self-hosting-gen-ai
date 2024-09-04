import json
import dateparser
from datetime import datetime
from tabulate import tabulate

# Function to parse the "Updated" string into a datetime object
def parse_updated_time(updated_str):
    if updated_str:
        cleaned_str = updated_str.replace('Updated', '').strip()
        parsed_date = dateparser.parse(cleaned_str)
        return parsed_date if parsed_date else datetime.min
    return datetime.min

# Load the repo list from the JSON file
with open('library.json', 'r', encoding='utf-8') as f:
    repo_list = json.load(f)

# Convert the "Updated" field to datetime and sort the list
for repo in repo_list:
    updated_str = repo['downloads_updates'].get('Updated', '')
    repo['parsed_updated'] = parse_updated_time(updated_str)

sorted_repo_list = sorted(repo_list, key=lambda x: x['parsed_updated'], reverse=True)

# Remove the 'parsed_updated' key after sorting if it's no longer needed
for repo in sorted_repo_list:
    del repo['parsed_updated']

# Prepare the data for the table
table_data = []
for repo in sorted_repo_list:
    table_data.append([
        repo["name"],
        ', '.join(repo["tools_sizes"]),
        repo["downloads_updates"]["Updated"]
    ])

# Define the table headers
headers = ["Name", "Tools & Sizes", "Updated"]

# Print the table
print(tabulate(table_data, headers=headers, tablefmt="pretty"))
