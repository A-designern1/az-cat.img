import requests

while True:
    command = input()
    if command == 'add':
        req = requests.get("https://aws.random.cat/meow")
        cat = req.text
        cat_url = cat[9:-2]
        cat_url = cat_url.replace("\\", '')
        req1 = requests.get(cat_url)
        file = open('cat.jpg', 'wb')
        file.write(req1.content)
        file.close()