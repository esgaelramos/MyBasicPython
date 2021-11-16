def run():
    super_list = [
        {"firstname" : "Facundo", "lastname" : "Garcia"},
        {"firstname" : "Miguel", "lastname" : "Torres"},
        {"firstname" : "Pepe", "lastname" : "Rodelo"},
        {"firstname" : "Susana", "lastname" : "Martínez"},
        {"firstname" : "Jose", "lastname" : "Garcia"}
    ]

    for item in super_list:
        print("Mi nombre es", item["firstname"] , "-" , item["lastname"], ", mucho gusto.")
    #Why here add a " ", on item["lastname"] and ", mucho gusto".
    #Nahh, it's only perspective, haha :(
if __name__ == "__main__":
    run()