import re

inp = input('ENTER STRING TO CHECK FOR URL : ')
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', inp)
print(f'URLS IN GIVEN STRING : {urls}')
