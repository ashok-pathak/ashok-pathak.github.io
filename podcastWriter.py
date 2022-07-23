from bs4 import BeautifulSoup as BS

with open('podcasts.html') as fp:
    soup = BS(fp, features="html.parser")

embed = '''<iframe src="{PODCAST_URL}" height="10%px" width="100%" frameborder="0" scrolling="no"></iframe>'''

url = input('Enter URL of episode\n->')
title = input('Enter title info\n->')
#mtdt = input('Enter metadata info\n->')

url = url.replace("episodes", "embed/episodes")

podDiv = soup.new_tag('div', id="blogpost")

h = soup.new_tag('h1')
h.string = title

ifrm = soup.new_tag('iframe', src = url, height="200px", width="100%", frameborder="0", scrolling="yes")

podDiv.append(ifrm)
podDiv.append(h)

soup.body.insert(4, podDiv)
with open('podcasts.html','w+') as outf:
    outf.write((soup.prettify()))

input("PODCAST UPDATE SUCCESSFUL!")

