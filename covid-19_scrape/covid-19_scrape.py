from bs4 import BeautifulSoup
import requests
import re
import time

start_time = time.time()
def p(n):
    """ just giving a shorter keyword for 'print' lol  """
    print(n)

html_file = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(html_file, 'lxml')

stats = []
for div in soup.find_all('div', class_ = "maincounter-number"):
    stats.append(div.text)
p('COVID-19 STATS\n')
p(f"TOTAL CASES:{stats[0]}")
p(f"DEATHS:{stats[1]}")
p(f"RECOVERED:{stats[2]}")

div = soup.find('div', class_ = "content-inner").text
pattern = re.compile(r"Last updated: ([\w]+) ([\d]){0,2}, ([\d]){4}, ([\d]){0,2}:([\d]){0,2} GMT")
match = pattern.search(str(div))
print(f"{match.group()}\n")

p(f"[Fetched in {round(time.time() - start_time, 3)} seconds]")


