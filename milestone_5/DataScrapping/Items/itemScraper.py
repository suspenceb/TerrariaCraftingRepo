import csv
from bs4 import BeautifulSoup

with open('itemsData.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Prepare CSV file
with open('items.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Image URL', 'Effect', 'Accessible'])

    for row in soup.find_all('tr'):
        # Extracting the full item name from the title attribute
        item_name_link = row.find('td').find('a')
        item_name = item_name_link['title'] if item_name_link and 'title' in item_name_link.attrs else "Name not found"

        # Extracting the image URL
        img_tag = row.find('td').find('img')
        img_url = img_url = img_tag['src'] if img_tag else 'Image URL not found'

        # Extracting the effect
        effect_container = row.find('td').find_next_sibling('td').find_next_sibling('td')
        effect = ''.join(effect_container.stripped_strings) if effect_container else 'Effect not found'

        # Determining accessibility
        accessibility_icon = row.find_all('td')[-2].find('span')  # Assumes the second last td contains accessibility info
        accessible = 0 if accessibility_icon and 't-yes' in accessibility_icon.get('class', []) else 1

        writer.writerow([item_name, img_url, effect, accessible])

print("CSV file has been created successfully.")