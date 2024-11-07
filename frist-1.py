
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = set(ingredients)  # Use a set for quick lookup

    def matches(self, available_ingredients):
        return self.ingredients.issubset(available_ingredients)

def find_recipes(available_ingredients, recipes):
    matched_recipes = []
    for recipe in recipes:
        if recipe.matches(available_ingredients):
            matched_recipes.append(recipe)
    return matched_recipes

def display_recipes(matched_recipes):
    if matched_recipes:
        print("\nRecipes you can make:")
        for recipe in matched_recipes:
            print(f"- {recipe.name}")
    else:
        print("\nNo recipes match the given ingredients.")

def main():
    # Predefined recipes (name, ingredients)
    recipes = [
        Recipe("Pasta Carbonara", ["spaghetti", "bacon", "eggs", "parmesan", "black pepper"]),
        Recipe("Grilled Cheese Sandwich", ["bread", "cheese", "butter"]),
        Recipe("Tomato Soup", ["tomato", "onion", "garlic", "vegetable broth"]),
        Recipe("Chicken Salad", ["chicken", "lettuce", "tomato", "cucumber", "olive oil"]),
        Recipe("Omelette", ["eggs", "cheese", "milk", "butter"]),
        Recipe("biryani",["vegitables","oil","special masala","water","rice","salad"])
    ]

    # Get user input for available ingredients
    print("Welcome to the Recipe Finder!")
    available_ingredients_input = input("Enter available ingredients (comma-separated): ").lower()
    available_ingredients = set(map(str.strip, available_ingredients_input.split(',')))

    # Find matching recipes
    matched_recipes = find_recipes(available_ingredients, recipes)

    # Display the results
    display_recipes(matched_recipes)

if __name__ == "__main__":
    main(Recipe)



Recipe(input("Enter avalible ingredients"))
print=("recipe")




