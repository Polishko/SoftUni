from models import Recipe, Chef
from main import Session


# 2. Create recipe
def create_recipe(name: str, ingredients: str, instructions: str):

    with Session() as session:
        new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        session.add(new_recipe)
        session.commit()
        print(f"New recipe added for {new_recipe.name}")


recipes_to_add = {
    "Recipe_1":
        [
            "Spaghetti Carbonara",
            "Pasta, Eggs, Pancetta, Cheese",
            "Cook the pasta, mix it with eggs, pancetta, and cheese"
        ],
    "Recipe_2":
        [
            "Chicken Stir-Fry",
            "Chicken, Bell Peppers, Soy Sauce, Vegetables",
            "Stir-fry chicken and vegetables with soy sauce"
        ],
    "Recipe_3":
        [
            "Caesar Salad",
            "Romaine Lettuce, Croutons, Caesar Dressing",
            "Toss lettuce with dressing and top with croutons"
        ]
}

# Add multiple recipes
for recipe_no in recipes_to_add.items():
    recipe_details = recipe_no[1]

    name, ingredients, instructions = recipe_details[0], recipe_details[1], recipe_details[2]
    create_recipe(name=name, ingredients=ingredients, instructions=instructions)

# Query all recipes
with Session() as session:
    recipes = session.query(Recipe).all()

    Loop through each recipe and print its details
    for recipe in recipes:
        print(f"Recipe name: {recipe.name}")


# 3.	Update Recipe
def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str):
    with Session() as session:
        recipe_to_update = session.query(Recipe).filter_by(name=name).first()
        if recipe_to_update:
            recipe_to_update.name = new_name
            recipe_to_update.ingredients = new_ingredients
            recipe_to_update.instructions = new_instructions
            session.commit()
            print(f"Recipe for {name} successfully updated.")
        else:
            print("Recipe not found.")


# Update a recipe by name
update_recipe_by_name(
    "Spaghetti Carbonara",
    new_name="Carbonara Pasta",
    new_ingredients="Pasta, Eggs, Guanciale, Cheese",
    new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
)

# Query the updated recipe
with Session() as session:
    updated_recipe = session.query(Recipe).filter(Recipe.name == "Carbonara Pasta").first()

    # Print the updated recipe details
    print("Updated Recipe Details:")
    print(f"Name: {updated_recipe.name}")
    print(f"Ingredients: {updated_recipe.ingredients}")
    print(f"Instructions: {updated_recipe.instructions}")


# 4.	Delete Recipe
def delete_recipe_by_name(name: str):
    with Session() as session:
        recipe_to_delete = session.query(Recipe).filter_by(name=name).first()

        if recipe_to_delete:
            session.delete(recipe_to_delete)
            session.commit()
            print(f"Recipe for {name} successfully deleted.")
        else:
            print("Recipe not found")


# Delete a recipe by name

delete_recipe_by_name("Spaghetti Carbonara")
delete_recipe_by_name("Carbonara Pasta")

# Query all recipes

with Session() as session:
    recipes = session.query(Recipe).all()

    # Loop through each recipe and print its details
    for recipe in recipes:
        print(f"Recipe name: {recipe.name}")


# 5.	Filter Recipes
# Delete all objects (recipes) from the database

with Session() as session:
    session.query(Recipe).delete()
    session.commit()

# Create three Recipe instances with two of them sharing the same ingredient

recipe1 = create_recipe(
    'Spaghetti Bolognese',
    'Ground beef, tomatoes, pasta',
    'Cook beef, add tomatoes, serve over pasta'
)

recipe2 = create_recipe(
    'Chicken Alfredo',
    'Chicken, fettuccine, Alfredo sauce',
    'Cook chicken, boil pasta, mix with sauce'
)

recipe3 = create_recipe(
    'Chicken Noodle Soup',
    'Chicken, noodles, carrots',
    'Boil chicken, add noodles, carrots'
)

def get_recipes_by_ingredient(ingredient_name: str):
    with Session() as session:
        filtered_recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f"%{ingredient_name.lower()}%")).all()
        return filtered_recipes


# Run the function and print the results

ingredient_to_filter = 'Chicken'
filtered_recipes = get_recipes_by_ingredient('Chicken')

print(f"Recipes containing {ingredient_to_filter}:")
for recipe in filtered_recipes:
    print(f"Recipe name - {recipe.name}")


# 6.	Recipe Ingredients Swap Transaction
# Delete all objects (recipes) from the database

with Session() as session:
    session.query(Recipe).delete()
    session.commit()

# # Create the first recipe
create_recipe("Pancakes", "Flour, Eggs, Milk", "Mix and cook on a griddle")

# # Create the second recipe
create_recipe("Waffles", "Flour, Eggs, Milk, Baking Powder", "Mix and cook in a waffle iron")


def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    session = Session()
    transaction = session.begin()

    try:
        recipe_1 = session.query(Recipe).filter_by(name=first_recipe_name).first()
        recipe_2 = session.query(Recipe).filter_by(name=second_recipe_name).first()
        recipe_1.ingredients, recipe_2.ingredients = recipe_2.ingredients, recipe_1.ingredients
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        print("An error occurred:", str(e))
    finally:
        session.close()


# Now, swap their ingredients

swap_recipe_ingredients_by_name("Pancakes", "Waffles")
with Session() as session:
    recipe1 = session.query(Recipe).filter_by(name="Pancakes").first()
    recipe2 = session.query(Recipe).filter_by(name="Waffles").first()
    print(f"Pancakes ingredients {recipe1.ingredients}")
    print(f"Waffles ingredients {recipe2.ingredients}")

# 7.	Model Chef
# new model created in models.py

# 8.	Extend the Recipe Model
# modified model in models.py

# 9.	Recipe and Chef Relations

# Create a recipe instance for Bulgarian Musaka

musaka_recipe = Recipe(
    name="Musaka",
    ingredients="Potatoes, Ground Meat, Onions, Eggs, Milk, Cheese, Spices",
    instructions="Layer potatoes and meat mixture, pour egg and milk mixture on top, bake until golden brown."
)

# Create a Bulgarian chef instances

bulgarian_chef1 = Chef(name="Ivan Zvezdev")
bulgarian_chef2 = Chef(name="Uti Buchvarov")

with Session() as session:
    session.add(musaka_recipe)

    session.add(bulgarian_chef1)
    session.add(bulgarian_chef2)

    session.commit()

def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    with Session() as session:
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        chef = session.query(Chef).filter_by(name=chef_name).first()

        if recipe and recipe.chef_id:
            raise Exception(f"Recipe: {recipe_name} already has a related chef")
        if not recipe or not chef:
            raise Exception(f"Recipe or chef not found")
        recipe.chef_id = chef.id
        session.commit()
        return f"Related recipe {recipe_name} with chef {chef_name}"


print(relate_recipe_with_chef_by_name("Musaka", "Ivan Zvezdev"))
print(relate_recipe_with_chef_by_name("Musaka", "Chef Uti"))


# 10. Chef and Recipe Integration
# Delete all objects (recipes and chefs) from the database
with Session() as session:
    session.query(Recipe).delete()
    session.query(Chef).delete()
    session.commit()

# # Create chef instances
chef1 = Chef(name="Gordon Ramsay")
chef2 = Chef(name="Julia Child")
chef3 = Chef(name="Jamie Oliver")
chef4 = Chef(name="Nigella Lawson")

# Create recipe instances associated with chefs
recipe1 = Recipe(name="Beef Wellington", ingredients="Beef fillet, Puff pastry, Mushrooms, Foie gras", instructions="Prepare the fillet and encase it in puff pastry.")
recipe1.chefs = chef1

recipe2 = Recipe(name="Boeuf Bourguignon", ingredients="Beef, Red wine, Onions, Carrots", instructions="Slow-cook the beef with red wine and vegetables.")
recipe2.chefs = chef2

recipe3 = Recipe(name="Spaghetti Carbonara", ingredients="Spaghetti, Eggs, Pancetta, Cheese", instructions="Cook pasta, mix ingredients.")
recipe3.chefs = chef3

recipe4 = Recipe(name="Chocolate Cake", ingredients="Chocolate, Flour, Sugar, Eggs", instructions="Bake a delicious chocolate cake.")
recipe4.chefs = chef4

recipe5 = Recipe(name="Chicken Tikka Masala", ingredients="Chicken, Yogurt, Tomatoes, Spices", instructions="Marinate chicken and cook in a creamy tomato sauce.")
recipe5.chefs = chef3

with Session() as session:
    session.add_all([chef1, chef2, chef3, chef4, recipe1, recipe2, recipe3, recipe4, recipe5])
    session.commit()


def get_recipes_with_chef():
    with Session() as session:
        recipes__with_chef = session.query(Recipe).filter(Recipe.chef_id.isnot(None)).all()

        result = []
        for recipe in recipes__with_chef:
            result.append(f"Recipe: {recipe.name} made by chef: {recipe.chefs.name}")

        return "\n".join(result)


print(get_recipes_with_chef())
