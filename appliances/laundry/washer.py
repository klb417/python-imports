from ..appliance import Appliance


class Washer(Appliance):
    def __init__(self, color, heat_method):
        super().__init__(color, heat_method)

    def wash_clothes(self, setting="normal"):
        if setting == "delicates":
            print("Time to wash the undies in the {self.heat_method} washer")
        elif setting == "super_scrub":
            print(f"Washing your diapers and bibs in the {self.heat_method} washer")
        else:
            print(
                "Hope you didn't mix your colors and whites in the {self.heat_method} washer"
            )
