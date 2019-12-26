text = input()
print(text)
K = input("Введите системное время ПК: ")

for i in range(len(text)):
    if text[i] == ".":
        text = (text.replace(text[i], K))

print(text)




