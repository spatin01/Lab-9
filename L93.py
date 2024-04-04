#Samantha Patin and Mandy Guo

class_list=["Abigail","Lopez","Anastacia", "Aguirre",
            "Emma", "Lombrado", "Sydney", "Eidelbes",
            "Therese", "Burns", "Mandy", "Guo",
            "Samantha", "Patin", "Viviana", "Antimo",
            "Abigail", "Newton", "Elise", "Ward", "Leena", "Bradley"
]

print (class_list[::2])
print (class_list[1::2])

firstnames=class_list[::2]
lastnames=class_list[1::2]


def firstletter(list):
    letters=[]
    for x in lastnames:
        name=x
        letters.append(name[0])
    return letters

    
firstletter(lastnames)

def histogram(list1):
    d=dict()
    for word in list1:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
    return d

print(histogram(firstletter(lastnames)))
