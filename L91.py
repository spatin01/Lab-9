#Samantha Patin and Mandy Guo

susan={"age": "26 years old", "height": "5ft 4in", "weight": "138 lbs", "eye color": "green"}

print (susan.get("height"))

dictionary2={"Hello": True, False: "Bye", 6: "seis", "siete": 7, 7: 7.11234, 9.2333: 9}

def my_get_method(target, dictionary):
    if target in dictionary:
        return dictionary[target]
    else:
        return "Key is not in the chosen dictionary."

print(my_get_method("age", susan))
print(my_get_method("Hello", dictionary2))
print(my_get_method(False, dictionary2))
print(my_get_method(6, dictionary2))
print(my_get_method("siete", dictionary2))
print(my_get_method(7, dictionary2))
print(my_get_method(9.2333, dictionary2))

