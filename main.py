def main():
    print_intro()
    print_driver_dict(create_driver_dict(gather_driver_info()))

def print_intro():
    print("2021 F1 Drivers")
    print("===============")
    print("")

#Takes driver info to form into lists
def gather_driver_info():
    driver_info_list = []
    drivers_list = {
        "Max, Verstappen, 33, Red Bull",
        "Lewis, Hamilton, 44, Mercedes",
        "Valtteri, Bottas, 77, Mercedes",
        "Lando, Norris, 4, McLaren",
        "Sergio, Perez, 11, Red Bull",
        "Charles, Leclerc, 16, Ferrari",
        "Carlos, Sainz, 55, Ferrari",
        "Daniel, Ricciardo, 3, McLaren",
        "Pierre, Gasly, 10, AlphaTauri",
        "Fernando, Alonso, 14, Alpine",
        "Esteban, Ocon, 31, Alpine",
        "Sebastian, Vettel, 5, Aston Martin",
        "Lance, Stroll, 18, Aston Martin",
        "Yuki, Sonoda, 22, AlphaTauri",
        "George, Russell, 63, Williams",
        "Nicholas, Latifi, 6, Williams",
        "Kimi, Raikkonen, 7, Alfa Romeo",
        "Antonio, Giovinazzi, 99, Alfa Romeo",
        "Mick, Schumacher, 47, Haas",
        "Nikita, Mazepin, 9, Haas"
    }
    for driver in drivers_list:
        driver_info = driver.split(", ")
        driver_info[2] = int(driver_info[2])
        driver_info_list.append(driver_info)
    return driver_info_list

#Turns lists into dicts
def create_driver_dict(driver_info_list):
    driver_dict_list = []
    for driver_info in driver_info_list:
        driver_dict = {"firstname": driver_info[0], "lastname": driver_info[1], "number": driver_info[2], "brand": driver_info[3]}
        driver_dict_list.append(driver_dict)
    return driver_dict_list

#Sorts dicts and prints the output
def print_driver_dict(driver_dict_list):
    driver_dict_list = sorted(driver_dict_list, key = lambda item: item["lastname"])
    for driver in driver_dict_list:
        if driver["number"] == 44:
            print(driver["firstname"], driver["lastname"], driver["number"], driver["brand"], "YEET!")
        else:
            print(driver["firstname"], driver["lastname"], driver["number"], driver["brand"])

    print("")

    driver_dict_list = sorted(driver_dict_list, key = lambda item: item["number"])
    for driver in driver_dict_list:
        if driver["number"] == 44:
            print(driver["firstname"], driver["lastname"], driver["number"], driver["brand"], "YEET!")
        else:
            print(driver["firstname"], driver["lastname"], driver["number"], driver["brand"])
            
main()