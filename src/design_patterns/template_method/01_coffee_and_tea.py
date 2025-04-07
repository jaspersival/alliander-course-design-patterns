class Coffee:
    def prepare_recipe(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self):
        print("Boiling water")

    def brew_coffee_grinds(self):
        print("Dripping Coffee through filter")

    def pour_in_cup(self):
        print("Pouring into cup")

    def add_sugar_and_milk(self):
        print("Adding sugar and milk")


class Tea:
    def prepare_recipe(self):
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self):
        print("Boiling water")

    def steep_tea_bag(self):
        print("Steeping the tea")

    def pour_in_cup(self):
        print("Pouring into cup")

    def add_lemon(self):
        print("Adding Lemon")
