import requests

with open(r"C:\Users\user\Desktop\dataset_3378_3.txt", encoding="utf-8") as f:
    r = requests.get(f.readline().strip())

while "We" not in r.text:
    r = requests.get(
        "https://stepic.org/media/attachments/course67/3.6.3/" + str(r.text)
    )

with open(
    r"C:\stardiatka_proekt-1\python\Wfiles\temp.txt", "w", encoding="utf-8"
) as file:
    file.write(r.text)

print(r.text)
