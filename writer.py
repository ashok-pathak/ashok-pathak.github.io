def writePara(soup, tag, text):
    par = soup.new_tag('p')
    tag.append(par)
    par.string = text
    return 1

def addImage(soup, tag, src, size):
    if size == 0:
        image = soup.new_tag('img', src=src, height="30%", width="30%")
        tag.append(image)
    elif size == 1:
        image = soup.new_tag('img', src=src, height="30%", width="100%")
        tag.append(image)
    return 1

def addLink(soup, tag, text, address):
    linktag = soup.new_tag('a', href=address)
    linktag.string = text
    tag.append(linktag)

def addHeading(soup, tag, text):
    h2 = soup.new_tag("h2")
    tag.append(h2)
    h2.string = text