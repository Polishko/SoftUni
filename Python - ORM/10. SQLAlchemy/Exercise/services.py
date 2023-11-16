from models import Recipe
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
# for recipe_no in recipes_to_add.items():
#     recipe_details = recipe_no[1]
#
#     name, ingredients, instructions = recipe_details[0], recipe_details[1], recipe_details[2]
#     create_recipe(name=name, ingredients=ingredients, instructions=instructions)

# Query all recipes
# with Session() as session:
#     recipes = session.query(Recipe).all()

    # Loop through each recipe and print its details
    # for recipe in recipes:
    #     print(f"Recipe name: {recipe.name}")


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
# update_recipe_by_name(
#     "Spaghetti Carbonara",
#     new_name="Carbonara Pasta",
#     new_ingredients="Pasta, Eggs, Guanciale, Cheese",
#     new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
# )

# Query the updated recipe
# with Session() as session:
#     updated_recipe = session.query(Recipe).filter(Recipe.name == "Carbonara Pasta").first()
#
#     # Print the updated recipe details
#     print("Updated Recipe Details:")
#     print(f"Name: {updated_recipe.name}")
#     print(f"Ingredients: {updated_recipe.ingredients}")
#     print(f"Instructions: {updated_recipe.instructions}")


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
# delete_recipe_by_name("Spaghetti Carbonara")
# delete_recipe_by_name("Carbonara Pasta")

# Query all recipes
# with Session() as session:
#     recipes = session.query(Recipe).all()
#
#     # Loop through each recipe and print its details
#     for recipe in recipes:
#         print(f"Recipe name: {recipe.name}")


# # 5.	Filter Recipes
# Delete all objects (recipes) from the database
# with Session() as session:
#     session.query(Recipe).delete()
#     session.commit()

# Create three Recipe instances with two of them sharing the same ingredient
# recipe1 = create_recipe(
#     'Spaghetti Bolognese',
#     'Ground beef, tomatoes, pasta',
#     'Cook beef, add tomatoes, serve over pasta'
# )
#
# recipe2 = create_recipe(
#     'Chicken Alfredo',
#     'Chicken, fettuccine, Alfredo sauce',
#     'Cook chicken, boil pasta, mix with sauce'
# )
#
# recipe3 = create_recipe(
#     'Chicken Noodle Soup',
#     'Chicken, noodles, carrots',
#     'Boil chicken, add noodles, carrots'
# )

def get_recipes_by_ingredient(ingredient_name: str):
    with Session() as session:
        filtered_recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f"%{ingredient_name.lower()}%")).all()
        return filtered_recipes


# Run the function and print the results
# ingredient_to_filter = 'Chicken'
# filtered_recipes = get_recipes_by_ingredient('Chicken')
#
# print(f"Recipes containing {ingredient_to_filter}:")
# for recipe in filtered_recipes:
#     print(f"Recipe name - {recipe.name}")

