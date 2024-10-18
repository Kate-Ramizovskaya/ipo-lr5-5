str=input("Введите строку:") #ввод строки для поиска "и"
bukv="и"


index=[]
kolv=0

for i in range(len(str)):
    char = str[i].lower()
    if char in bukv:
        index.append(i)
        kolv+=1

print("Кол-во букв <<и>>", kolv)