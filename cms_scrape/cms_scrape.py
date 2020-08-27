from bs4 import BeautifulSoup
import requests
import csv

# import the website's source
code = requests.get('https://coreyms.com/').text
# feed it into BeautifulSoup
soup = BeautifulSoup(code, 'lxml')

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Youtube Link'])

# find all occurences of 'article'
for article in soup.find_all('article'):
    # find the heading and print its text
    headline = article.h2.a.text
    print(headline + '\n')

    # find div container with class="entry-content" and print its texts
    summary = article.find('div', class_="entry-content").p.text
    print(summary + '\n')

    # if a link exists in that article, then print it
    try:
        vid_src = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f"Link: https://www.youtube.com/watch?v={vid_id}"
        print(yt_link)
    # if link doesn't exist, then display None
    except Exception as e:
        yt_link = None
        print("Link: None")
    print()
    print()
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close() 
    
    





















