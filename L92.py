#Samantha Patin and Mandy Guo

class_list={"Lopez": "Abigail", "Aguirre": "Anastacia",
            "Lombrado": "Emma", "Eidelbes": "Sydney",
            "Burns": "Therese", "Guo": "Mandy",
            "Patin": "Samantha", "Antimo": "Viviana",
            "Newton": "Abigail", "Ward": "Elise", "Bradley": "Leena"
}

def histogram(dictionary):
    firstnames=class_list.values()
    d=dict()
    for word in firstnames:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
    return d

print(histogram(class_list))


