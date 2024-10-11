from collections import deque

# List of recipes
recipes = [
    {"RecipeID": 1, "RecipeName": "Spaghetti Carbonara", "Ingredients": ["spaghetti", "eggs", "cheese", "bacon", "pepper"]},
    {"RecipeID": 2, "RecipeName": "Chicken Curry", "Ingredients": ["chicken", "curry powder", "coconut milk", "onion", "garlic"]},
    {"RecipeID": 3, "RecipeName": "Caesar Salad", "Ingredients": ["romaine lettuce", "croutons", "Caesar dressing", "parmesan cheese"]},
    {"RecipeID": 4, "RecipeName": "Beef Stew", "Ingredients": ["beef", "carrots", "potatoes", "onion", "broth"]},
    {"RecipeID": 5, "RecipeName": "Vegetable Stir Fry", "Ingredients": ["mixed vegetables", "soy sauce", "garlic", "ginger"]},
    {"RecipeID": 6, "RecipeName": "Chocolate Cake", "Ingredients": ["flour", "cocoa powder", "sugar", "eggs", "butter"]},
    {"RecipeID": 7, "RecipeName": "Pancakes", "Ingredients": ["flour", "milk", "eggs", "baking powder", "sugar"]},
    {"RecipeID": 8, "RecipeName": "Tomato Soup", "Ingredients": ["tomatoes", "onion", "garlic", "vegetable broth"]},
    {"RecipeID": 9, "RecipeName": "Margarita Pizza", "Ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil"]},
    {"RecipeID": 10, "RecipeName": "Tacos", "Ingredients": ["taco shells", "ground beef", "lettuce", "cheese", "salsa"]},
    {"RecipeID": 11, "RecipeName": "Lentil Soup", "Ingredients": ["lentils", "carrots", "celery", "onion", "vegetable broth"]},
    {"RecipeID": 12, "RecipeName": "Grilled Cheese Sandwich", "Ingredients": ["bread", "cheese", "butter"]},
    {"RecipeID": 13, "RecipeName": "Quiche Lorraine", "Ingredients": ["pie crust", "eggs", "cream", "cheese", "bacon"]},
    {"RecipeID": 14, "RecipeName": "BBQ Ribs", "Ingredients": ["pork ribs", "BBQ sauce", "spices"]},
    {"RecipeID": 15, "RecipeName": "Fruit Salad", "Ingredients": ["mixed fruits", "honey", "lime juice"]},
    {"RecipeID": 16, "RecipeName": "Stuffed Peppers", "Ingredients": ["bell peppers", "rice", "ground meat", "tomato sauce"]},
    {"RecipeID": 17, "RecipeName": "Fish Tacos", "Ingredients": ["fish", "taco shells", "cabbage", "lime"]},
    {"RecipeID": 18, "RecipeName": "Baked Ziti", "Ingredients": ["ziti pasta", "marinara sauce", "mozzarella", "parmesan"]},
    {"RecipeID": 19, "RecipeName": "Chicken Alfredo", "Ingredients": ["fettuccine", "chicken", "alfredo sauce", "parmesan"]},
    {"RecipeID": 20, "RecipeName": "Shrimp Scampi", "Ingredients": ["shrimp", "garlic", "butter", "parsley", "lemon"]},
]

# Stack for undoing recipe changes
undo_stack = []

# Queue for pending recipes
pending_recipes = deque()

# Function to display all recipes
def display_recipes():
    print("\nAll Recipes:")
    for recipe in recipes:
        print(f"ID: {recipe['RecipeID']}, Recipe: {recipe['RecipeName']}, Ingredients: {', '.join(recipe['Ingredients'])}")

# Function to add a recipe to the pending queue
def add_pending_recipe(recipe_id):
    for recipe in recipes:
        if recipe["RecipeID"] == recipe_id:
            pending_recipes.append(recipe)
            print(f"Recipe '{recipe['RecipeName']}' is added to the pending recipes.")
            return
    print("Invalid Recipe ID. Please choose a valid recipe from the list.")

# Function to process the next recipe in the pending queue
def process_pending_recipe():
    if pending_recipes:
        next_recipe = pending_recipes.popleft()
        undo_stack.append(next_recipe)
        print(f"Processing recipe '{next_recipe['RecipeName']}'.")
    else:
        print("No pending recipes to process.")

# Function to undo the last recipe change
def undo_last_change():
    if undo_stack:
        last_recipe = undo_stack.pop()
        pending_recipes.appendleft(last_recipe)
        print(f"Undo successful: '{last_recipe['RecipeName']}' has been returned to pending recipes.")
    else:
        print("No recipe changes to undo.")

# Function to view pending recipes
def view_pending_recipes():
    if pending_recipes:
        print("\nPending Recipes:")
        for recipe in pending_recipes:
            print(f"- {recipe['RecipeName']}")
    else:
        print("No pending recipes at the moment.")

# Main menu for interaction
def recipe_management_app():
    while True:
        print("\nOptions:")
        print("1. Display All Recipes")
        print("2. Add Recipe to Pending Queue")
        print("3. Process Next Pending Recipe")
        print("4. Undo Last Recipe Change")
        print("5. View Pending Recipes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_recipes()
        elif choice == '2':
            display_recipes()
            try:
                recipe_id = int(input("Enter Recipe ID to add to pending queue: "))
                add_pending_recipe(recipe_id)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            process_pending_recipe()
        elif choice == '4':
            undo_last_change()
        elif choice == '5':
            view_pending_recipes()
        elif choice == '6':
            print("Exiting recipe management app.")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Run the recipe management app
recipe_management_app()
