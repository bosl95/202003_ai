file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
for i, f in enumerate(file):
    file[i] = f.split('.')[0]
print(file)