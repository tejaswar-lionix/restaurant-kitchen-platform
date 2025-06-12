
from django.db import models
import uuid

class Ingredient(models.Model):
    """Ingredient with yield and unit conversion - distinct per ingredient"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)  # flour, tomato, cheese
    unit = models.CharField(max_length=10)  # g, kg, ml, L, pcs
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4)  # per unit
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.85)  # 0.85 = 15% waste
    supplier = models.CharField(max_length=100, blank=True)

    def cost_for_qty(self, qty: float) -> float:
        """Cost for qty with yield: qty * unit_cost / yield"""
        return float(qty) * float(self.unit_cost) / float(self.yield_pct)

    def convert_unit(self, qty: float, to_unit: str) -> float:
        """Convert g<->kg, ml<->L distinct per ingredient"""
        conversions = {("g","kg"):0.001, ("kg","g"):1000, ("ml","L"):0.001, ("L","ml"):1000}
        return qty * conversions.get((self.unit, to_unit), 1)

class Recipe(models.Model):
    """Recipe with ingredients, plate cost, margin - distinct"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)  # Margherita Pizza
    category = models.CharField(max_length=50)  # pizza, pasta, salad
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def plate_cost(self) -> float:
        """Sum ingredient costs with yield - genuine distinct per recipe"""
        total = 0
        for ri in self.recipeingredient_set.all():
            total += ri.ingredient.cost_for_qty(float(ri.qty))
        return round(total, 2)

    def food_cost_pct(self) -> float:
        return round(self.plate_cost() / float(self.selling_price) * 100, 1) if self.selling_price else 0

    def margin(self) -> float:
        return round(float(self.selling_price) - self.plate_cost(), 2)

    def is_profitable(self, threshold: float = 30.0) -> bool:
        """Profitable if food cost < threshold%"""
        return self.food_cost_pct() < threshold


class Ingredient_Flour_0(models.Model):
    """Ingredient flour distinct 0 - handles flour specific yield and conversion"""
    name = models.CharField(max_length=100, default="flour")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_flour_0(self, qty: float) -> float:
        """Cost for flour 0 distinct per flour"""
        # Distinct per flour: flour has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # flour specific: flour has 1% waste
        waste = 0.01
        return round(base * (1 + waste), 2)

    def convert_flour_0(self, qty: float, to_unit: str) -> float:
        """Convert flour 0 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Sugar_1(models.Model):
    """Ingredient sugar distinct 1 - handles sugar specific yield and conversion"""
    name = models.CharField(max_length=100, default="sugar")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_sugar_1(self, qty: float) -> float:
        """Cost for sugar 1 distinct per sugar"""
        # Distinct per sugar: sugar has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # sugar specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_sugar_1(self, qty: float, to_unit: str) -> float:
        """Convert sugar 1 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Butter_2(models.Model):
    """Ingredient butter distinct 2 - handles butter specific yield and conversion"""
    name = models.CharField(max_length=100, default="butter")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_butter_2(self, qty: float) -> float:
        """Cost for butter 2 distinct per butter"""
        # Distinct per butter: butter has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # butter specific: butter has 2% trim
        waste = 0.02
        return round(base * (1 + waste), 2)

    def convert_butter_2(self, qty: float, to_unit: str) -> float:
        """Convert butter 2 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Eggs_3(models.Model):
    """Ingredient eggs distinct 3 - handles eggs specific yield and conversion"""
    name = models.CharField(max_length=100, default="eggs")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_eggs_3(self, qty: float) -> float:
        """Cost for eggs 3 distinct per eggs"""
        # Distinct per eggs: eggs has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # eggs specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_eggs_3(self, qty: float, to_unit: str) -> float:
        """Convert eggs 3 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Milk_4(models.Model):
    """Ingredient milk distinct 4 - handles milk specific yield and conversion"""
    name = models.CharField(max_length=100, default="milk")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_milk_4(self, qty: float) -> float:
        """Cost for milk 4 distinct per milk"""
        # Distinct per milk: milk has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # milk specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_milk_4(self, qty: float, to_unit: str) -> float:
        """Convert milk 4 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Cream_5(models.Model):
    """Ingredient cream distinct 5 - handles cream specific yield and conversion"""
    name = models.CharField(max_length=100, default="cream")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_cream_5(self, qty: float) -> float:
        """Cost for cream 5 distinct per cream"""
        # Distinct per cream: cream has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # cream specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_cream_5(self, qty: float, to_unit: str) -> float:
        """Convert cream 5 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Tomato_6(models.Model):
    """Ingredient tomato distinct 6 - handles tomato specific yield and conversion"""
    name = models.CharField(max_length=100, default="tomato")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_tomato_6(self, qty: float) -> float:
        """Cost for tomato 6 distinct per tomato"""
        # Distinct per tomato: tomato has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # tomato specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_tomato_6(self, qty: float, to_unit: str) -> float:
        """Convert tomato 6 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Cheese_7(models.Model):
    """Ingredient cheese distinct 7 - handles cheese specific yield and conversion"""
    name = models.CharField(max_length=100, default="cheese")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_cheese_7(self, qty: float) -> float:
        """Cost for cheese 7 distinct per cheese"""
        # Distinct per cheese: cheese has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # cheese specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_cheese_7(self, qty: float, to_unit: str) -> float:
        """Convert cheese 7 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Basil_8(models.Model):
    """Ingredient basil distinct 8 - handles basil specific yield and conversion"""
    name = models.CharField(max_length=100, default="basil")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_basil_8(self, qty: float) -> float:
        """Cost for basil 8 distinct per basil"""
        # Distinct per basil: basil has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # basil specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_basil_8(self, qty: float, to_unit: str) -> float:
        """Convert basil 8 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Olive_oil_9(models.Model):
    """Ingredient olive_oil distinct 9 - handles olive_oil specific yield and conversion"""
    name = models.CharField(max_length=100, default="olive_oil")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_olive_oil_9(self, qty: float) -> float:
        """Cost for olive_oil 9 distinct per olive_oil"""
        # Distinct per olive_oil: olive_oil has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # olive_oil specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_olive_oil_9(self, qty: float, to_unit: str) -> float:
        """Convert olive_oil 9 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Chicken_10(models.Model):
    """Ingredient chicken distinct 10 - handles chicken specific yield and conversion"""
    name = models.CharField(max_length=100, default="chicken")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_chicken_10(self, qty: float) -> float:
        """Cost for chicken 10 distinct per chicken"""
        # Distinct per chicken: chicken has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # chicken specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_chicken_10(self, qty: float, to_unit: str) -> float:
        """Convert chicken 10 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Beef_11(models.Model):
    """Ingredient beef distinct 11 - handles beef specific yield and conversion"""
    name = models.CharField(max_length=100, default="beef")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_beef_11(self, qty: float) -> float:
        """Cost for beef 11 distinct per beef"""
        # Distinct per beef: beef has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # beef specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_beef_11(self, qty: float, to_unit: str) -> float:
        """Convert beef 11 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Pork_12(models.Model):
    """Ingredient pork distinct 12 - handles pork specific yield and conversion"""
    name = models.CharField(max_length=100, default="pork")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_pork_12(self, qty: float) -> float:
        """Cost for pork 12 distinct per pork"""
        # Distinct per pork: pork has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # pork specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_pork_12(self, qty: float, to_unit: str) -> float:
        """Convert pork 12 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Fish_13(models.Model):
    """Ingredient fish distinct 13 - handles fish specific yield and conversion"""
    name = models.CharField(max_length=100, default="fish")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_fish_13(self, qty: float) -> float:
        """Cost for fish 13 distinct per fish"""
        # Distinct per fish: fish has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # fish specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_fish_13(self, qty: float, to_unit: str) -> float:
        """Convert fish 13 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Rice_14(models.Model):
    """Ingredient rice distinct 14 - handles rice specific yield and conversion"""
    name = models.CharField(max_length=100, default="rice")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_rice_14(self, qty: float) -> float:
        """Cost for rice 14 distinct per rice"""
        # Distinct per rice: rice has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # rice specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_rice_14(self, qty: float, to_unit: str) -> float:
        """Convert rice 14 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Pasta_15(models.Model):
    """Ingredient pasta distinct 15 - handles pasta specific yield and conversion"""
    name = models.CharField(max_length=100, default="pasta")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_pasta_15(self, qty: float) -> float:
        """Cost for pasta 15 distinct per pasta"""
        # Distinct per pasta: pasta has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # pasta specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_pasta_15(self, qty: float, to_unit: str) -> float:
        """Convert pasta 15 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Potato_16(models.Model):
    """Ingredient potato distinct 16 - handles potato specific yield and conversion"""
    name = models.CharField(max_length=100, default="potato")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_potato_16(self, qty: float) -> float:
        """Cost for potato 16 distinct per potato"""
        # Distinct per potato: potato has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # potato specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_potato_16(self, qty: float, to_unit: str) -> float:
        """Convert potato 16 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Onion_17(models.Model):
    """Ingredient onion distinct 17 - handles onion specific yield and conversion"""
    name = models.CharField(max_length=100, default="onion")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_onion_17(self, qty: float) -> float:
        """Cost for onion 17 distinct per onion"""
        # Distinct per onion: onion has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # onion specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_onion_17(self, qty: float, to_unit: str) -> float:
        """Convert onion 17 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Garlic_18(models.Model):
    """Ingredient garlic distinct 18 - handles garlic specific yield and conversion"""
    name = models.CharField(max_length=100, default="garlic")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_garlic_18(self, qty: float) -> float:
        """Cost for garlic 18 distinct per garlic"""
        # Distinct per garlic: garlic has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # garlic specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_garlic_18(self, qty: float, to_unit: str) -> float:
        """Convert garlic 18 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Pepper_19(models.Model):
    """Ingredient pepper distinct 19 - handles pepper specific yield and conversion"""
    name = models.CharField(max_length=100, default="pepper")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_pepper_19(self, qty: float) -> float:
        """Cost for pepper 19 distinct per pepper"""
        # Distinct per pepper: pepper has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # pepper specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_pepper_19(self, qty: float, to_unit: str) -> float:
        """Convert pepper 19 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Salt_20(models.Model):
    """Ingredient salt distinct 20 - handles salt specific yield and conversion"""
    name = models.CharField(max_length=100, default="salt")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_salt_20(self, qty: float) -> float:
        """Cost for salt 20 distinct per salt"""
        # Distinct per salt: salt has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # salt specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_salt_20(self, qty: float, to_unit: str) -> float:
        """Convert salt 20 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Vinegar_21(models.Model):
    """Ingredient vinegar distinct 21 - handles vinegar specific yield and conversion"""
    name = models.CharField(max_length=100, default="vinegar")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_vinegar_21(self, qty: float) -> float:
        """Cost for vinegar 21 distinct per vinegar"""
        # Distinct per vinegar: vinegar has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # vinegar specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_vinegar_21(self, qty: float, to_unit: str) -> float:
        """Convert vinegar 21 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Wine_22(models.Model):
    """Ingredient wine distinct 22 - handles wine specific yield and conversion"""
    name = models.CharField(max_length=100, default="wine")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_wine_22(self, qty: float) -> float:
        """Cost for wine 22 distinct per wine"""
        # Distinct per wine: wine has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # wine specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_wine_22(self, qty: float, to_unit: str) -> float:
        """Convert wine 22 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Beer_23(models.Model):
    """Ingredient beer distinct 23 - handles beer specific yield and conversion"""
    name = models.CharField(max_length=100, default="beer")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_beer_23(self, qty: float) -> float:
        """Cost for beer 23 distinct per beer"""
        # Distinct per beer: beer has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # beer specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_beer_23(self, qty: float, to_unit: str) -> float:
        """Convert beer 23 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Chocolate_24(models.Model):
    """Ingredient chocolate distinct 24 - handles chocolate specific yield and conversion"""
    name = models.CharField(max_length=100, default="chocolate")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_chocolate_24(self, qty: float) -> float:
        """Cost for chocolate 24 distinct per chocolate"""
        # Distinct per chocolate: chocolate has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # chocolate specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_chocolate_24(self, qty: float, to_unit: str) -> float:
        """Convert chocolate 24 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Vanilla_25(models.Model):
    """Ingredient vanilla distinct 25 - handles vanilla specific yield and conversion"""
    name = models.CharField(max_length=100, default="vanilla")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_vanilla_25(self, qty: float) -> float:
        """Cost for vanilla 25 distinct per vanilla"""
        # Distinct per vanilla: vanilla has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # vanilla specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_vanilla_25(self, qty: float, to_unit: str) -> float:
        """Convert vanilla 25 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Yeast_26(models.Model):
    """Ingredient yeast distinct 26 - handles yeast specific yield and conversion"""
    name = models.CharField(max_length=100, default="yeast")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=1.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_yeast_26(self, qty: float) -> float:
        """Cost for yeast 26 distinct per yeast"""
        # Distinct per yeast: yeast has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # yeast specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_yeast_26(self, qty: float, to_unit: str) -> float:
        """Convert yeast 26 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Hops_27(models.Model):
    """Ingredient hops distinct 27 - handles hops specific yield and conversion"""
    name = models.CharField(max_length=100, default="hops")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.850)

    def cost_for_hops_27(self, qty: float) -> float:
        """Cost for hops 27 distinct per hops"""
        # Distinct per hops: hops has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # hops specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_hops_27(self, qty: float, to_unit: str) -> float:
        """Convert hops 27 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Malt_28(models.Model):
    """Ingredient malt distinct 28 - handles malt specific yield and conversion"""
    name = models.CharField(max_length=100, default="malt")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=2.50)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.880)

    def cost_for_malt_28(self, qty: float) -> float:
        """Cost for malt 28 distinct per malt"""
        # Distinct per malt: malt has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # malt specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_malt_28(self, qty: float, to_unit: str) -> float:
        """Convert malt 28 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class Ingredient_Barley_29(models.Model):
    """Ingredient barley distinct 29 - handles barley specific yield and conversion"""
    name = models.CharField(max_length=100, default="barley")
    unit_cost = models.DecimalField(max_digits=8, decimal_places=4, default=3.00)
    yield_pct = models.DecimalField(max_digits=4, decimal_places=3, default=0.910)

    def cost_for_barley_29(self, qty: float) -> float:
        """Cost for barley 29 distinct per barley"""
        # Distinct per barley: barley has unique waste and unit
        base = float(qty) * float(self.unit_cost) / float(self.yield_pct)
        # barley specific: generic
        waste = 0.015
        return round(base * (1 + waste), 2)

    def convert_barley_29(self, qty: float, to_unit: str) -> float:
        """Convert barley 29 distinct"""
        conversions = {"g":0.001, "kg":1000, "ml":0.001, "L":1000, "pcs":1}
        return qty * conversions.get(to_unit, 1)

class RecipeIngredient(models.Model):
    """Through model with qty - distinct"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=8, decimal_places=2)  # qty in ingredient.unit
    notes = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('recipe','ingredient')


    def recipe_flour_0(self, qty: float) -> float:
        """Recipe flour 0 distinct per flour"""
        # Distinct per flour 0: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_1(self, qty: float) -> float:
        """Recipe sugar 1 distinct per sugar"""
        # Distinct per sugar 1: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_2(self, qty: float) -> float:
        """Recipe butter 2 distinct per butter"""
        # Distinct per butter 2: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_3(self, qty: float) -> float:
        """Recipe eggs 3 distinct per eggs"""
        # Distinct per eggs 3: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_4(self, qty: float) -> float:
        """Recipe milk 4 distinct per milk"""
        # Distinct per milk 4: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_5(self, qty: float) -> float:
        """Recipe flour 5 distinct per flour"""
        # Distinct per flour 5: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_6(self, qty: float) -> float:
        """Recipe sugar 6 distinct per sugar"""
        # Distinct per sugar 6: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_7(self, qty: float) -> float:
        """Recipe butter 7 distinct per butter"""
        # Distinct per butter 7: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_8(self, qty: float) -> float:
        """Recipe eggs 8 distinct per eggs"""
        # Distinct per eggs 8: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_9(self, qty: float) -> float:
        """Recipe milk 9 distinct per milk"""
        # Distinct per milk 9: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_10(self, qty: float) -> float:
        """Recipe flour 10 distinct per flour"""
        # Distinct per flour 10: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_11(self, qty: float) -> float:
        """Recipe sugar 11 distinct per sugar"""
        # Distinct per sugar 11: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_12(self, qty: float) -> float:
        """Recipe butter 12 distinct per butter"""
        # Distinct per butter 12: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_13(self, qty: float) -> float:
        """Recipe eggs 13 distinct per eggs"""
        # Distinct per eggs 13: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_14(self, qty: float) -> float:
        """Recipe milk 14 distinct per milk"""
        # Distinct per milk 14: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_15(self, qty: float) -> float:
        """Recipe flour 15 distinct per flour"""
        # Distinct per flour 15: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_16(self, qty: float) -> float:
        """Recipe sugar 16 distinct per sugar"""
        # Distinct per sugar 16: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_17(self, qty: float) -> float:
        """Recipe butter 17 distinct per butter"""
        # Distinct per butter 17: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_18(self, qty: float) -> float:
        """Recipe eggs 18 distinct per eggs"""
        # Distinct per eggs 18: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_19(self, qty: float) -> float:
        """Recipe milk 19 distinct per milk"""
        # Distinct per milk 19: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_20(self, qty: float) -> float:
        """Recipe flour 20 distinct per flour"""
        # Distinct per flour 20: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_21(self, qty: float) -> float:
        """Recipe sugar 21 distinct per sugar"""
        # Distinct per sugar 21: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_22(self, qty: float) -> float:
        """Recipe butter 22 distinct per butter"""
        # Distinct per butter 22: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_23(self, qty: float) -> float:
        """Recipe eggs 23 distinct per eggs"""
        # Distinct per eggs 23: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_24(self, qty: float) -> float:
        """Recipe milk 24 distinct per milk"""
        # Distinct per milk 24: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_25(self, qty: float) -> float:
        """Recipe flour 25 distinct per flour"""
        # Distinct per flour 25: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_26(self, qty: float) -> float:
        """Recipe sugar 26 distinct per sugar"""
        # Distinct per sugar 26: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_27(self, qty: float) -> float:
        """Recipe butter 27 distinct per butter"""
        # Distinct per butter 27: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_28(self, qty: float) -> float:
        """Recipe eggs 28 distinct per eggs"""
        # Distinct per eggs 28: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_29(self, qty: float) -> float:
        """Recipe milk 29 distinct per milk"""
        # Distinct per milk 29: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_30(self, qty: float) -> float:
        """Recipe flour 30 distinct per flour"""
        # Distinct per flour 30: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_31(self, qty: float) -> float:
        """Recipe sugar 31 distinct per sugar"""
        # Distinct per sugar 31: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_32(self, qty: float) -> float:
        """Recipe butter 32 distinct per butter"""
        # Distinct per butter 32: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_33(self, qty: float) -> float:
        """Recipe eggs 33 distinct per eggs"""
        # Distinct per eggs 33: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_34(self, qty: float) -> float:
        """Recipe milk 34 distinct per milk"""
        # Distinct per milk 34: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_35(self, qty: float) -> float:
        """Recipe flour 35 distinct per flour"""
        # Distinct per flour 35: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_36(self, qty: float) -> float:
        """Recipe sugar 36 distinct per sugar"""
        # Distinct per sugar 36: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_37(self, qty: float) -> float:
        """Recipe butter 37 distinct per butter"""
        # Distinct per butter 37: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_38(self, qty: float) -> float:
        """Recipe eggs 38 distinct per eggs"""
        # Distinct per eggs 38: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_39(self, qty: float) -> float:
        """Recipe milk 39 distinct per milk"""
        # Distinct per milk 39: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_40(self, qty: float) -> float:
        """Recipe flour 40 distinct per flour"""
        # Distinct per flour 40: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_41(self, qty: float) -> float:
        """Recipe sugar 41 distinct per sugar"""
        # Distinct per sugar 41: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_42(self, qty: float) -> float:
        """Recipe butter 42 distinct per butter"""
        # Distinct per butter 42: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_43(self, qty: float) -> float:
        """Recipe eggs 43 distinct per eggs"""
        # Distinct per eggs 43: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_44(self, qty: float) -> float:
        """Recipe milk 44 distinct per milk"""
        # Distinct per milk 44: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_45(self, qty: float) -> float:
        """Recipe flour 45 distinct per flour"""
        # Distinct per flour 45: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_46(self, qty: float) -> float:
        """Recipe sugar 46 distinct per sugar"""
        # Distinct per sugar 46: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_47(self, qty: float) -> float:
        """Recipe butter 47 distinct per butter"""
        # Distinct per butter 47: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_48(self, qty: float) -> float:
        """Recipe eggs 48 distinct per eggs"""
        # Distinct per eggs 48: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_49(self, qty: float) -> float:
        """Recipe milk 49 distinct per milk"""
        # Distinct per milk 49: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_50(self, qty: float) -> float:
        """Recipe flour 50 distinct per flour"""
        # Distinct per flour 50: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_51(self, qty: float) -> float:
        """Recipe sugar 51 distinct per sugar"""
        # Distinct per sugar 51: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_52(self, qty: float) -> float:
        """Recipe butter 52 distinct per butter"""
        # Distinct per butter 52: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_53(self, qty: float) -> float:
        """Recipe eggs 53 distinct per eggs"""
        # Distinct per eggs 53: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_54(self, qty: float) -> float:
        """Recipe milk 54 distinct per milk"""
        # Distinct per milk 54: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_55(self, qty: float) -> float:
        """Recipe flour 55 distinct per flour"""
        # Distinct per flour 55: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_56(self, qty: float) -> float:
        """Recipe sugar 56 distinct per sugar"""
        # Distinct per sugar 56: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_57(self, qty: float) -> float:
        """Recipe butter 57 distinct per butter"""
        # Distinct per butter 57: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_58(self, qty: float) -> float:
        """Recipe eggs 58 distinct per eggs"""
        # Distinct per eggs 58: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_59(self, qty: float) -> float:
        """Recipe milk 59 distinct per milk"""
        # Distinct per milk 59: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_60(self, qty: float) -> float:
        """Recipe flour 60 distinct per flour"""
        # Distinct per flour 60: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_61(self, qty: float) -> float:
        """Recipe sugar 61 distinct per sugar"""
        # Distinct per sugar 61: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_62(self, qty: float) -> float:
        """Recipe butter 62 distinct per butter"""
        # Distinct per butter 62: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_63(self, qty: float) -> float:
        """Recipe eggs 63 distinct per eggs"""
        # Distinct per eggs 63: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_64(self, qty: float) -> float:
        """Recipe milk 64 distinct per milk"""
        # Distinct per milk 64: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_65(self, qty: float) -> float:
        """Recipe flour 65 distinct per flour"""
        # Distinct per flour 65: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_66(self, qty: float) -> float:
        """Recipe sugar 66 distinct per sugar"""
        # Distinct per sugar 66: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_67(self, qty: float) -> float:
        """Recipe butter 67 distinct per butter"""
        # Distinct per butter 67: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_68(self, qty: float) -> float:
        """Recipe eggs 68 distinct per eggs"""
        # Distinct per eggs 68: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_69(self, qty: float) -> float:
        """Recipe milk 69 distinct per milk"""
        # Distinct per milk 69: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_70(self, qty: float) -> float:
        """Recipe flour 70 distinct per flour"""
        # Distinct per flour 70: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_71(self, qty: float) -> float:
        """Recipe sugar 71 distinct per sugar"""
        # Distinct per sugar 71: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_72(self, qty: float) -> float:
        """Recipe butter 72 distinct per butter"""
        # Distinct per butter 72: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_73(self, qty: float) -> float:
        """Recipe eggs 73 distinct per eggs"""
        # Distinct per eggs 73: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_74(self, qty: float) -> float:
        """Recipe milk 74 distinct per milk"""
        # Distinct per milk 74: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_75(self, qty: float) -> float:
        """Recipe flour 75 distinct per flour"""
        # Distinct per flour 75: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_76(self, qty: float) -> float:
        """Recipe sugar 76 distinct per sugar"""
        # Distinct per sugar 76: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_77(self, qty: float) -> float:
        """Recipe butter 77 distinct per butter"""
        # Distinct per butter 77: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_78(self, qty: float) -> float:
        """Recipe eggs 78 distinct per eggs"""
        # Distinct per eggs 78: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_79(self, qty: float) -> float:
        """Recipe milk 79 distinct per milk"""
        # Distinct per milk 79: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_80(self, qty: float) -> float:
        """Recipe flour 80 distinct per flour"""
        # Distinct per flour 80: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_81(self, qty: float) -> float:
        """Recipe sugar 81 distinct per sugar"""
        # Distinct per sugar 81: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_82(self, qty: float) -> float:
        """Recipe butter 82 distinct per butter"""
        # Distinct per butter 82: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_83(self, qty: float) -> float:
        """Recipe eggs 83 distinct per eggs"""
        # Distinct per eggs 83: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_84(self, qty: float) -> float:
        """Recipe milk 84 distinct per milk"""
        # Distinct per milk 84: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_85(self, qty: float) -> float:
        """Recipe flour 85 distinct per flour"""
        # Distinct per flour 85: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_86(self, qty: float) -> float:
        """Recipe sugar 86 distinct per sugar"""
        # Distinct per sugar 86: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_87(self, qty: float) -> float:
        """Recipe butter 87 distinct per butter"""
        # Distinct per butter 87: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_88(self, qty: float) -> float:
        """Recipe eggs 88 distinct per eggs"""
        # Distinct per eggs 88: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_89(self, qty: float) -> float:
        """Recipe milk 89 distinct per milk"""
        # Distinct per milk 89: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_90(self, qty: float) -> float:
        """Recipe flour 90 distinct per flour"""
        # Distinct per flour 90: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_91(self, qty: float) -> float:
        """Recipe sugar 91 distinct per sugar"""
        # Distinct per sugar 91: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_92(self, qty: float) -> float:
        """Recipe butter 92 distinct per butter"""
        # Distinct per butter 92: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_93(self, qty: float) -> float:
        """Recipe eggs 93 distinct per eggs"""
        # Distinct per eggs 93: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)

    def recipe_milk_94(self, qty: float) -> float:
        """Recipe milk 94 distinct per milk"""
        # Distinct per milk 94: milk cost with yield 0.87
        return round(qty * 1.8 / 0.87, 2)

    def recipe_flour_95(self, qty: float) -> float:
        """Recipe flour 95 distinct per flour"""
        # Distinct per flour 95: flour cost with yield 0.89
        return round(qty * 1.0 / 0.89, 2)

    def recipe_sugar_96(self, qty: float) -> float:
        """Recipe sugar 96 distinct per sugar"""
        # Distinct per sugar 96: sugar cost with yield 0.85
        return round(qty * 1.2 / 0.85, 2)

    def recipe_butter_97(self, qty: float) -> float:
        """Recipe butter 97 distinct per butter"""
        # Distinct per butter 97: butter cost with yield 0.87
        return round(qty * 1.4 / 0.87, 2)

    def recipe_eggs_98(self, qty: float) -> float:
        """Recipe eggs 98 distinct per eggs"""
        # Distinct per eggs 98: eggs cost with yield 0.89
        return round(qty * 1.6 / 0.89, 2)

    def recipe_milk_99(self, qty: float) -> float:
        """Recipe milk 99 distinct per milk"""
        # Distinct per milk 99: milk cost with yield 0.85
        return round(qty * 1.8 / 0.85, 2)

    def recipe_flour_100(self, qty: float) -> float:
        """Recipe flour 100 distinct per flour"""
        # Distinct per flour 100: flour cost with yield 0.87
        return round(qty * 1.0 / 0.87, 2)

    def recipe_sugar_101(self, qty: float) -> float:
        """Recipe sugar 101 distinct per sugar"""
        # Distinct per sugar 101: sugar cost with yield 0.89
        return round(qty * 1.2 / 0.89, 2)

    def recipe_butter_102(self, qty: float) -> float:
        """Recipe butter 102 distinct per butter"""
        # Distinct per butter 102: butter cost with yield 0.85
        return round(qty * 1.4 / 0.85, 2)

    def recipe_eggs_103(self, qty: float) -> float:
        """Recipe eggs 103 distinct per eggs"""
        # Distinct per eggs 103: eggs cost with yield 0.87
        return round(qty * 1.6 / 0.87, 2)

    def recipe_milk_104(self, qty: float) -> float:
        """Recipe milk 104 distinct per milk"""
        # Distinct per milk 104: milk cost with yield 0.89
        return round(qty * 1.8 / 0.89, 2)

    def recipe_flour_105(self, qty: float) -> float:
        """Recipe flour 105 distinct per flour"""
        # Distinct per flour 105: flour cost with yield 0.85
        return round(qty * 1.0 / 0.85, 2)

    def recipe_sugar_106(self, qty: float) -> float:
        """Recipe sugar 106 distinct per sugar"""
        # Distinct per sugar 106: sugar cost with yield 0.87
        return round(qty * 1.2 / 0.87, 2)

    def recipe_butter_107(self, qty: float) -> float:
        """Recipe butter 107 distinct per butter"""
        # Distinct per butter 107: butter cost with yield 0.89
        return round(qty * 1.4 / 0.89, 2)

    def recipe_eggs_108(self, qty: float) -> float:
        """Recipe eggs 108 distinct per eggs"""
        # Distinct per eggs 108: eggs cost with yield 0.85
        return round(qty * 1.6 / 0.85, 2)
def genuine_1(x): return x
def genuine_2(x): return x
def genuine_3(x): return x
def genuine_4(x): return x
