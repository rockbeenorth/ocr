import cv2
import pytesseract
import os
import time
import datetime as dt

test_files = os.listdir(path='img_test/')
print(test_files)

data = {}

for file in test_files:

    fpath = f"img_test/{file}"

    extract = cv2.imread(fpath)
    text = pytesseract.image_to_string(extract, lang='eng+rus')

    print(text)
    print(dt.datetime.fromtimestamp(os.path.getctime(fpath)))

    data[file] = {
        "text": text,
        "created" : str(dt.datetime.fromtimestamp(os.path.getctime(fpath))),
        "modified" : str(dt.datetime.fromtimestamp(os.path.getmtime(fpath))),
    }

with open("save.txt", "w") as f:
    f.write(str(data))

print("data saved to save.txt")

print(data)