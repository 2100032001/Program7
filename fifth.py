def intro():
    print("There are many types of birds.")


class Bird:

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

intro()
obj_bird.flight()

intro()
obj_spr.flight()

intro()
obj_ost.flight()
