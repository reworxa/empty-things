text : str = input("Enter text : ")
word : str = input("Enter word : ")

stext = text.split(" ")

i = 0
global count
count = 0

for i in range(len(stext)):
    if word == stext[i]:
        i += 1
        count += 1
    else: 
        i += 1
        

print(count)
