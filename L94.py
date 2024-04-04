#Samantha Patin and Mandy Guo

red_velvet={"flour": "3 cups", "baking soda": "1 tsp",
            "cocoa powder": " 2 Tbs", "salt": "1/2 tsp",
            "butter": "1/2 cup", "sugar": "2 cups", "oil": "1 cup",
            "eggs": "4", "vanilla": "1 Tbs", "vinegar": "1 tsp",
            "dye": "red", "buttermilk": "1 cup"
}

lemon={"flour": "1.5 cups", "baking powder": "2 tsp", "salt": "0.5 tsp",
       "butter": "0.5 cup", "sugar": "1 cup", "eggs": "2", "vanilla": "1.5 tsp",
       "milk": "0.5 cup", "lemon": "2"
}

ingrv=red_velvet.keys()
ingl=lemon.keys()

def firstletter(lists):
    food=[]
    for x in ingrv:
        if x in red_velvet and x in lemon:
            ingredients=x
            food.append(ingredients)
            
    return food
print (firstletter(ingrv))

