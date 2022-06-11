from writer import *
from bs4 import BeautifulSoup as BS
from docx import Document

import datetime

with open('index.html') as fp:
    tempSoup = BS(fp, features="html.parser")
with open('template.html') as temp:
    soup = BS(temp, features="html.parser")
now = datetime.datetime.now()

head = input('Enter title>')
soup.head.append(soup.new_tag("head", string=head))
original_tag = soup.body
title = soup.new_tag("title")
soup.head.append(title)
title.string = head + ' | Blogpost'
tag = soup.new_tag("div", id="blogpost")
original_tag.insert(4, tag)
h = soup.new_tag('h1')
tag.append(h)
h.string = head
date = soup.new_tag('p')
date.string = now.strftime("%d %b %Y")
tag.append(date)

doc_src = input('Enter Document Source>')
doc = Document(doc_src)
allText=''
for paragraph in doc.paragraphs:
    if len(paragraph.text)>0:
        if paragraph.text[0] == '.':
            if len(paragraph.text) > 1:
                if paragraph.text[1] == '#':
                    bT = soup.new_tag('b')
                    addHeading(soup, bT, paragraph.text[2:])
                    tag.append(bT)
                    allText+=paragraph.text[2:]
                    allText+='\n'
            else:
                addHeading(soup, tag, paragraph.text[1:])
                allText+=paragraph.text[1:]
                allText+='\n'
        else:
            writePara(soup, tag, paragraph.text)
            allText+=paragraph.text
            allText+='\n'


print(allText)
bodyText = allText[:min(500, len(allText))]+'...'
new_temp_tag = tempSoup.new_tag("div", id="blogpost")
tempSoup.body.insert(4, new_temp_tag)
hlink = soup.new_tag('a', href='blogs/'+head.replace(' ', '-')+'.html')
h = soup.new_tag('h1')
hlink.append(h)
h.string = head
new_temp_tag.append(hlink)
date = tempSoup.new_tag('p')
date.string = now.strftime("%d %b %Y")
new_temp_tag.append(date)
link = tempSoup.new_tag('a', href='blogs/'+head.replace(' ', '-')+'.html')
new_temp_tag.append(link)
link.string = bodyText


with open('index.html','w+') as outf:
    outf.write((tempSoup.prettify()))

with open('blogs/'+head.replace(' ', '-')+'.html','w+') as outf:
    outf.write((soup.prettify()))
    input('Your changes have been published! Press return to exit.')
