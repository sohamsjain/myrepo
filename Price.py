elem_dict = {'sodium': 480, 'hydrogen': 600, 'oxygen': 540, 'chlorine': 550, 'carbon': 700, 'calcium': 500}
comp_dict = {'arcaspace': 2000, 'astroscale': 2350, 'astrorocket': 2250, 'blueorigin': 2300, 'celestis': 2400, 'spacex': 2200, 'virgingalactic': 2050}
compound_dict = {'marble': 0, 'propane': 0, 'salt': 0, 'sugar': 0, 'water': 0}

class elements:
    def __init__(self, element_dict=elem_dict, company_dict=comp_dict):
        for k, v in element_dict.items():
            self.__setattr__(k, v)
        for k, v in company_dict.items():
            self.__setattr__(k, v)
        self.calculate_compounds()
        self.elems = [self.sodium, self.hydrogen, self.oxygen, self.chlorine, self.carbon, self.calcium]
        self.compounds = [self.marble, self.propane, self.salt, self.sugar, self.water]
        self.companies = [self.arcaspace, self.astroscale, self.astrorocket, self.blueorigin, self.celestis, self.spacex, self.virgingalactic]

    def calculate_compounds(self):
        self.marble = self.calcium + self.carbon + (2 * self.oxygen)
        self.propane = 2 * (self.calcium + self.hydrogen)
        self.salt = self.sodium + self.chlorine
        self.sugar = self.carbon + self.oxygen + (2 * self.hydrogen)
        self.water = (2 * self.hydrogen) + self.oxygen

    def incur_change(self, ins, ch):
        try:
            x = self.__getattribute__(ins)
            x += self.myround(float(ch/100)*x, 50)
            self.__setattr__(ins, x)
        except:
            pass

    def myround(self, x, base=5):
        return base * round(x / base)

    def get_formatted_price(self):

        self.calculate_compounds()

        text = 'Quote Update\n' \
               'Elements : Price\n'
        for each in elem_dict.keys():
            text += each + ': ' + str(self.__getattribute__(each)) + '\n'

        text += '\n' \
                'Companies : Price\n'
        for each in compound_dict.keys():
            text += each + ': ' + str(self.__getattribute__(each)) + '\n'

        text += '\n' \
                'Companies : Price\n'
        for each in comp_dict.keys():
            text += each + ': ' + str(self.__getattribute__(each)) + '\n'

        return text

