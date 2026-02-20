import requests

r = requests.get('https://api.github.com/events')
with open('requests.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)
    print("The file has been written sucessfully.")