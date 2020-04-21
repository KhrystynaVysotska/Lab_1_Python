class Ship:
    number_of_ships = 0

    def __init__(self, tonnazh_of_ship_in_tonnes=45324, name_of_ship="Olympic", number_of_passengers=2435,
                 type_of_ship="passenger liner",
                 length_of_ship_in_metres=263.83, speed_of_ship_in_miles_per_hour=42.5):
        self.tonnazh_of_ship_in_tonnes = tonnazh_of_ship_in_tonnes
        self.name_of_ship = name_of_ship
        self.number_of_passengers = number_of_passengers
        self.type_of_ship = type_of_ship
        self.length_of_ship_in_metres = length_of_ship_in_metres
        self.speed_of_ship_in_miles_per_hour = speed_of_ship_in_miles_per_hour
        Ship.number_of_ships += 1

    def __del__(self):
        print("Ship " + self.name_of_ship + " was successfully deleted!")

    def __str__(self):
        return "Name of ship:           " + self.name_of_ship + "\n" + \
               "Tonnazh of ship:        " + str(self.tonnazh_of_ship_in_tonnes) + " t\n" + \
               "Amount of passengers:   " + str(self.number_of_passengers) + "\n" + \
               "Type of ship:           " + self.type_of_ship + "\n" + \
               "Length of ship:         " + str(self.length_of_ship_in_metres) + " m\n" + \
               "Speed of ship:          " + str(self.speed_of_ship_in_miles_per_hour) + " miles/hour\n"

    @staticmethod
    def get_number_of_ships():
        return Ship.number_of_ships


if __name__ == "__main__":
    first_ship = Ship(3500, "Victoria", 850, "sailing ship")
    second_ship = Ship(3245, "Titanic", 235, "passenger liner", 223.34, 40.3)
    third_ship = Ship()
    ships = [first_ship, second_ship, third_ship]
    for ship in ships:
        print(ship)