from bs4 import BeautifulSoup
import requests
import re
import time


""" A simple web scraper that displays statistics about COVID-19 regarding the total cases, deaths and the number of people recovered from it. """

class Stats:
    def __init__(self, total, deaths, recovered, last_updated):
        self.total = total
        self.deaths = deaths
        self.recovered = recovered
        self.last_updated = last_updated

# for calculating how long the program took
start_time = time.time()

def getPage(url):
    """ Fetch the page in plain html and
    return a BeautifulSoup object with that html """
    html = requests.get(url)
    return BeautifulSoup(html.text, 'html.parser')

def getStats(url):
    """ Processes the html from the url extracting only the data we need. """

    soup = getPage(url)

    # the stats we need will be appended to this list
    stats_list = []

    # find all <div> tags with 'maincounter-number' class
    # and append them into above list
    for div in soup.find_all('div', {'class': "maincounter-number"} ):
        stats_list.append(div.text)

    # The "Last Updated..." part was a bit tough to find
    # since it didn't really have a single tag where I could
    # fetch it...
    div = soup.find('div', {"class": "content-inner"}).text
    # ... hence, the regex.
    pattern = re.compile(r"Last updated: ([\w]+) ([\d]){0,2}, ([\d]){4}, ([\d]){0,2}:([\d]){0,2} GMT")
    match = pattern.search(str(div))
    # well, I'm sure there are better ways to do it.

    total = stats_list[0]
    deaths = stats_list[1]
    recovered = stats_list[2]
    last_updated = match.group()
    return Stats(total, deaths, recovered, last_updated)


url = "https://www.worldometers.info/coronavirus/"

stats = getStats(url)

print('COVID-19 STATS\n')
print(f"TOTAL CASES: {stats.total}")
print(f"DEATHS: {stats.deaths}")
print(f"RECOVERED: {stats.recovered}")
print(stats.last_updated)
print(f"[Fetched in {round(time.time() - start_time, 3)} seconds]")

# Note: This function is at the mercy of the actual website from where the stats are being retrieved.
# If the website goes down or if they change their code, this whole program may not work. 
# That is bad software design, I know but it works and I'm too lazy to change the code.
