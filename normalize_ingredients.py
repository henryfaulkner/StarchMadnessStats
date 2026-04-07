import json
import glob

INGREDIENT_MAP = {
    # Cheese variations
    "Parmesan": "Cheese",
    "Parmigiano-Reggiano": "Cheese",
    "Parmesan cheese": "Cheese",
    "Grated Parmesan": "Cheese",
    "Freshly grated Parmesan cheese": "Cheese",
    "Sharp white Cheddar": "Cheese",
    "Grated sharp white Cheddar": "Cheese",
    "Cheddar": "Cheese",
    "Cheddar cheese": "Cheese",
    "Italian Fontina cheese": "Cheese",
    "Muenster cheese": "Cheese",
    "Queso Fresco": "Cheese",
    "Cotija cheese": "Cheese",
    "Fontina cheese": "Cheese",
    "Farmer's cheese": "Cheese",
    "Ricotta": "Cheese",
    "Gruyere cheese": "Cheese",
    # Butter variations
    "Salted butter": "Butter",
    "Unsalted butter": "Butter",
    "Butter": "Butter",
    # Onion variations
    "Yellow onion": "Onion",
    "White onions": "Onion",
    "Onion": "Onion",
    "Onions": "Onion",
    "Shallot": "Onion",
    "Shallots": "Onion",
    "Leeks": "Onion",
    "Leek": "Onion",
    "Green onions": "Onion",
    "Scallions": "Onion",
    # Salt variations
    "Kosher salt": "Salt",
    "Table salt": "Salt",
    "Salt": "Salt",
    "Coarse salt": "Salt",
    # Pepper variations
    "Black pepper": "Pepper",
    "Pepper": "Pepper",
    "Freshly cracked black pepper": "Pepper",
    "Red pepper flakes": "Pepper",
    # Rice variations
    "White enriched rice": "Rice",
    "Arborio rice": "Rice",
    "Jasmine rice": "Rice",
    "Basmati rice": "Rice",
    "Long-grain white rice": "Rice",
    "Cooked brown or white rice": "Rice",
    # Pasta variations
    "Thin spaghetti": "Pasta",
    # Potato variations
    "Yukon Gold potatoes": "Potato",
    "Yukon gold potatoes": "Potato",
    "Sweet potatoes": "Potato",
    "Idaho potatoes": "Potato",
    "Baking potatoes": "Potato",
    "Starchy potatoes": "Potato",
    # Milk variations
    "Whole milk": "Milk",
    "Full fat milk": "Milk",
    "Evaporated milk": "Milk",
    # Oil variations
    "Vegetable oil": "Oil",
    "Canola oil": "Oil",
    "Olive oil": "Oil",
    "Extra-virgin olive oil": "Oil",
    # Egg variations
    "Large eggs": "Egg",
    "Large egg": "Egg",
    "Egg": "Egg",
    "Eggs": "Egg",
    "Extra-large eggs": "Egg",
    "Egg yolk": "Egg",
    "Egg whites": "Egg",
    "Egg white": "Egg",
    "Large free-range egg": "Egg",
    "Medium egg": "Egg",
    # Flour variations
    "All-purpose flour": "Flour",
    "Bread flour": "Flour",
    "Unbleached all-purpose flour": "Flour",
    # Sugar variations
    "Sugar": "Sugar",
    "Granulated sugar": "Sugar",
    "Brown sugar": "Sugar",
    "Light brown sugar": "Sugar",
    "Dark brown sugar": "Sugar",
    "Packed light brown sugar": "Sugar",
    "Packed brown sugar": "Sugar",
    # Garlic variations
    "Garlic": "Garlic",
    "Garlic cloves": "Garlic",
    # Ginger variations
    "Fresh ginger": "Ginger",
    # Corn variations
    "Corn": "Corn",
    "Fresh corn kernels": "Corn",
    # Chicken variations
    "Rotisserie chicken": "Chicken",
    "Shredded rotisserie chicken": "Chicken",
    "Chicken stock": "Stock",
    "Chicken broth": "Stock",
    "Low-sodium chicken broth": "Stock",
    "Mushroom broth": "Stock",
    # Creme fraiche variations
    "Creme fraiche": "Creme Fraiche",
    "Crème fraiche": "Creme Fraiche",
    "Crème fraîche": "Creme Fraiche",
    "Crème fraîcheur": "Creme Fraiche",
    # Fresh herb variations
    "Fresh cilantro": "Cilantro",
    "Fresh basil leaves": "Fresh Herbs",
    "Fresh parsley": "Parsley",
    "Fresh dill": "Dill",
    "Fresh thyme": "Fresh Herbs",
    "Fresh oregano": "Fresh Herbs",
}


def normalize_ingredient(ing):
    """Apply mapping to normalize ingredients further"""
    return INGREDIENT_MAP.get(ing, ing)


# Process all recipe files
recipe_files = glob.glob("recipes/*.json")

for file in recipe_files:
    with open(file, "r") as f:
        recipe = json.load(f)

    # Normalize each ingredient
    normalized = []
    for ing in recipe.get("normalized_ingredients", []):
        normalized.append(normalize_ingredient(ing))

    recipe["normalized_ingredients"] = normalized

    # Write back
    with open(file, "w") as f:
        json.dump(recipe, f, indent=2, ensure_ascii=False)

    print(f"Updated: {file}")

print(f"\nTotal files processed: {len(recipe_files)}")
