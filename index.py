from appliances import DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "hamster wheel")
samsung_dryer = Dryer("red", "gas")

samsung_washer.wash_clothes("super_scrub")
samsung_dryer.dry_clothes("low")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

can_opener = CanOpener("purple")
can_opener.open_can()
