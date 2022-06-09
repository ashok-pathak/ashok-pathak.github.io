from writer import *
from bs4 import BeautifulSoup as BS
import datetime

with open('index.html') as fp:
    tempSoup = BS(fp, features="html.parser")
with open('template.html') as temp:
    soup = BS(temp, features="html.parser")
now = datetime.datetime.now()
rules = '''
The Technology Club | notblind development team
HOW TO USE NotBlindWriter(R)
When prompted with 'Write here>', write down the text of your article.
After pressing 'return', you will be asked for the 'command>' prompt.
Enter 'exit' to exit the article.
Enter 'image' to insert an image.
Enter 'newline' to go to the next line.
Enter 'link' to insert a link.

NOTE: THIS SOFTWARE IS STILL IN BETA!!!
'''
print(rules)
head = input('Enter title>')
original_tag = soup.body
new_tag = soup.new_tag("div", id="blogpost")
original_tag.insert(4, new_tag)
hlink = soup.new_tag('a', href='blogs/'+head.replace(' ', '-')+'.html')
h = soup.new_tag('h1')
h.string = head
hlink.append(h)
date = soup.new_tag('p')
date.string = now.strftime("%d %b %Y")
new_tag.append(date)
while True:
    inp = input('Write here>')
    if inp != '':
        writePara(soup, new_tag, inp)
    else:
        pass
    command = input('command>')
    if command == 'exit':
        break
    elif command == 'newline':
        pass
    elif command == 'image':
        src = input('imgsrc>')
        while True:
            ty = input('type (small "info" or big "major")>')
            if ty == 'info':
                addImage(soup, new_tag, src, 0)
                break
            elif ty == 'major':
                addImage(soup, new_tag, src, 1)
                break
            else:
                print("Invalid Input")
    elif command == 'link':
        link = input('Enter link URL')
        text = input('Enter link text')
        addLink(soup, new_tag, text, link)


    else:
        print('Invalid command! Moving to newline!!')

bodyText = new_tag.contents[2].text[:min(100, len(new_tag.contents[2].text))]+'...'
new_temp_tag = tempSoup.new_tag("div", id="blogpost")
tempSoup.body.insert(4, new_temp_tag)
h = tempSoup.new_tag('h1')
h.string = head
new_temp_tag.append(h)
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
