import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")

while "We" not in r.text:
    r = requests.get(
        "https://stepic.org/media/attachments/course67/3.6.3/" + str(r.text)
    )

print(r.text)
