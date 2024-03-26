from bs4 import BeautifulSoup
import csv

# Your HTML data
html_file_path = 'scrapperdata.html'
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_data = file.read()

soup = BeautifulSoup(html_data, 'html.parser')

# Prepare CSV file
csv_file = 'items.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['Name', 'Image URL', 'Damage', 'Damage Type', 'Knockback', 'Critical Strike Chance', 'Use Time', 'Available'])

    for tr in soup.find_all('tr'):
        # Extract the image alt attribute as the item name
        img_alt = tr.find('td').find('img')['alt'].replace(' item sprite', '')

        # Extract the image URL
        img_url = tr.find('td').find('img')['src']

        # Extracting other specified values
        td_elements = tr.find_all('td')
        damage = td_elements[2].get_text(strip=True)
        damage_type = td_elements[3].get_text(strip=True)
        knockback = td_elements[4].get_text(strip=True)
        critical_strike_chance = td_elements[5].get_text(strip=True)
        use_time = td_elements[6].get_text(strip=True)

        # Handling the available value, converting visual indicators to text
        available = 'NO'  # Default to 'NO' if not the ✔️ symbol
        if td_elements[9].find('span', class_='t-yes'):
            available = 'YES'
        elif td_elements[9].find('span', class_='t-no'):
            available = 'NO'

        writer.writerow([img_alt, img_url, damage, damage_type, knockback, critical_strike_chance, use_time, available])

print(f'CSV file "{csv_file}" has been created.')
