class List_PAT:

    def __init__(self, food, amount, food_name = None, amount_pound = None, standard_price = None, calc_price = None):
        self.food = food
        self.amount = amount
        self.__food_name = food_name
        self.__amount_pound = amount_pound
        self.__standard_price = standard_price
        self.__calc_price = calc_price

    def __PriceList_PAT(self):
        if self.food == "Dry Cured Iberian Ham":
            self.__standard_price = 177.80
        elif self.food == "Wagyu Steaks":
            self.__standard_price = 450
        elif self.food == "Matsutake Mushrooms":
            self.__standard_price = 272
        elif self.food == "Kopi Luwak Coffee":
            self.__standard_price = 306.50
        elif self.food == "Moose Cheese":
            self.__standard_price = 487.20
        elif self.food == "White Truffles":
            self.__standard_price = 3600
        elif self.food == "Blue Fin Tuna":
            self.__standard_price = 3603
        elif self.food == "Le Bonnote Potatoes":
            self.__standard_price = 270.81
        else:
            self.__standard_price = 0
#Getter methods. PS: I had a tough time with these, I should remember and maybe reduce the amount of functions as some were quite useless and just complicated things
    def calculation_PAT(self):
        self.__PriceList_PAT()
        return self.amount * self.__standard_price

    def getfood_PAT(self):
        return self.food

    def getpriceperpound_PAT(self):
        return self.__standard_price

    def getamount_PAT(self):
        return self.amount

    def getprice_PAT(self):
        self.__PriceList_PAT()
        return self.__calc_price

    def getprivate(self):
        self.__PriceList_PAT()
