with open('file.txt', 'r') as file:
    text = file.read()

with open('new.file.txt', 'w') as file:
    file.write(text)