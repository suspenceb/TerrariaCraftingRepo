from bs4 import BeautifulSoup
import csv

# Open and read the HTML file
with open('armorData.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find_all('tr')

data = []

for row in rows:
    name = row.find_all('td')[1].get_text(strip=True)

    image_url = row.find('img')['src']

    defenses = [td.get_text(strip=True) for td in row.find_all('td', style="text-align:center")]

    # Ensure we only take the first four defense values
    if len(defenses) >= 4:
        head_defense, chest_defense, boots_defense, total = defenses[:4]
    else:
        # Handle cases where there are not enough defense values
        # This line can be adjusted based on how you wish to handle missing data
        head_defense, chest_defense, boots_defense, total = defenses + [None] * (
                    4 - len(defenses))  # Fill missing values with None

    details_td = row.find('td', class_='small')
    if details_td is not None:
        details_html = str(details_td.encode_contents())
    else:
        details_html = 'N/A'

    data.append([name, image_url, head_defense, chest_defense, boots_defense, total, details_html])

# Specify the CSV file path
csv_file_path = 'output.csv'

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Image URL', 'HeadDefense', 'ChestDefense', 'BootsDefense', 'Total', 'Details'])
    writer.writerows(data)

print("CSV file has been created with the extracted data.")
