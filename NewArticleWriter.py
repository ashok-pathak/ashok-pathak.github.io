from bs4 import BeautifulSoup as BS
import datetime
now = datetime.datetime.now()
rules = '''
The Technology Club | notblind development team
HOW TO USE NotBlindWriter(R)
When prompted with 'Write here>', write down the text of your article.
After pressing 'return', you will be asked for the 'command>' prompt.
Enter 'exit' to exit the article.
Enter 'image' to insert an image.
Enter 'newline' to go to the next line.

NOTE: THIS SOFTWARE IS STILL IN BETA!!!
'''
print(rules)
title = input('Enter title>')
head = input('Enter heading>')
with open('C:\\Users\\adity\\Documents\\Desktop\\Misc\\not blind\\template.html') as fp:
    soup = BS(fp, features="html.parser")
head_tag = soup.head
title_tag = soup.new_tag("title")
title_tag.string = title
head_tag.append(title_tag)
original_tag = soup.body
new_tag = soup.new_tag("div", id="blogpost")
original_tag.append(new_tag)
h = soup.new_tag('h1')
h.string = head
new_tag.append(h)
date = soup.new_tag('p')
date.string = now.strftime("%Y-%m-%d %H:%M")
new_tag.append(date)
while True:
    inp = input('Write here>')
    if inp != '':
        par = soup.new_tag('p')
        new_tag.append(par)
        par.string = inp
    else:
        pass
    command = input('command>')
    if command == 'exit':
        break
    elif command == 'newline':
        pass
    elif command == 'image':
        src = input('imgsrc>')
        ty = input('type>')
        if ty == 'info':
            image = soup.new_tag('img', src=src, height="30%", width="30%")
        elif ty == 'major':
            image = soup.new_tag('img', src=src, height="30%", width="100%")
        new_tag.append(image)
        img_var = True
    else:
        print('Invalid command! Moving to newline!!')
hr=soup.new_tag('hr')
new_tag.append(hr)
with open('C:\\Users\\adity\\Documents\\Desktop\\Misc\\not blind\\'+head+'.html','w+') as outf:
    outf.write((soup.prettify()))
    input('Your changes have been published! Press return to exit.')