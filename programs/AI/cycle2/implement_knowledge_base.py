# Install the pytholog library if you haven't already


import pytholog as pl

# Create a new knowledge base
new_kb = pl.KnowledgeBase("flavor")

# Populate the knowledge base with facts and rules
new_kb([
    "likes(noor, sausage)",
    "likes(melissa, pasta)",
    "likes(dmitry, cookie)",
    "likes(nikita, sausage)",
    "likes(assel, limonade)",

    "food_type(gouda, cheese)",
    "food_type(ritz, cracker)",
    "food_type(steak, meat)",
    "food_type(sausage, meat)",
    "food_type(limonade, juice)",
    "food_type(mojito, juice)",
    "food_type(cookie, dessert)",

    "flavor(sweet, dessert)",
    "flavor(savory, meat)",
    "flavor(savory, cheese)",
    "flavor(sweet, juice)",
    
    "food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z)",
    "dish_to_like(X, Y) :- likes(X, L), food_type(L, T), flavor(F, T), food_flavor(Y, F), neq(L, Y)"
])

# Query examples
print(new_kb.query(pl.Expr("likes(noor, sausage)")))  # Check if Noor likes sausage
print(new_kb.query(pl.Expr("likes(noor, pasta)")))    # Check if Noor likes pasta

# Find what food items have a sweet flavor
print(new_kb.query(pl.Expr("food_flavor(What, sweet)")))  # Get food items with sweet flavor

# Find a dish Noor might like based on her preferences
print(new_kb.query(pl.Expr("dish_to_like(noor, What)")))  # Dishes Noor might like

# Find what food items have a savory flavor
print(new_kb.query(pl.Expr("food_flavor(What, savory)")))  # Get food items with savory flavor
