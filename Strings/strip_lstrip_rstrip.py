url = '  https://google.com  '

url = url.strip()
print(url)

# print(url.strip('https://'))
# print(url.lstrip('https://'))


url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)