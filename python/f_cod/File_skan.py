# просканировать папку
import os

with os.scandir(r'\\STARDIADKA\Users\user\Desktop\130 руб') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')