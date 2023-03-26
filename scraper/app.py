import requests
from bs4 import BeautifulSoup
import csv
import io

base_url = "https://www.gunviolencearchive.org"
url = "https://www.gunviolencearchive.org/export-finished?filename=public%3A//export-e757dde5-08ba-4c99-b007-83326d138ea1.csv&uuid=0484b316-f676-44bc-97ed-ecefeabae077&return_href=reports/mass-shooting"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')


button = soup.find('a', text='Download')

csv_link = button['href']


csv_response = requests.get(base_url + csv_link, headers=headers)
csv_content = csv_response.content

csv_reader = csv.reader(io.StringIO(csv_content.decode('utf-8')), delimiter=',')

with open('mass_shooting.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in csv_reader:
        csv_writer.writerow(row)


