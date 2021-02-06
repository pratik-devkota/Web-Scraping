from bs4 import BeautifulSoup
import requests
import re
import time


""" A simple web scraper that displays statistics about COVID-19 regarding the total cases, deaths and the number of people recovered from it. """


p = print # shorter keyword for print function

def fetch_data():
    """ Gets the html from www.worldometers.info/coronavirus
    and processes the code extracting only the data we need.

    NOTE: This function is at the mercy of the actual website from where the stats are being retrieved.
    If the website goes down or if they change their code, this whole program may not work. That is bad
    software design, I know but it works and I'm too lazy to change the code.""" 

    # fetch the page in plain html
    html_file = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(html_file, 'lxml')

   # the stats we need will be appended to this list
    stats = []

    # find all <div> tags with 'maincounter-number' class
    # and append them into above list
    for div in soup.find_all('div', {'class': "maincounter-number"} ):
        stats.append(div.text)

    # self explanatory "making-it-look-pretty" stuff
    p('COVID-19 STATS\n')
    p(f"TOTAL CASES:{stats[0]}")
    p(f"DEATHS:{stats[1]}")
    p(f"RECOVERED:{stats[2]}")

   # The "Last Updated..." part was a bit tough to find
   # since it didn't really have a single tag where I could
   # fetch it...
    div = soup.find('div', class_ = "content-inner").text
    # ... hence, the regex.
    pattern = re.compile(r"Last updated: ([\w]+) ([\d]){0,2}, ([\d]){4}, ([\d]){0,2}:([\d]){0,2} GMT")
    match = pattern.search(str(div))
    p(f"{match.group()}\n")
    # well, I'm sure there are better ways to do it.

# for calculating how long the program took
start_time = time.time()
# execute the function
fetch_data()
# and also print the run-time
p(f"[Fetched in {round(time.time() - start_time, 3)} seconds]")
