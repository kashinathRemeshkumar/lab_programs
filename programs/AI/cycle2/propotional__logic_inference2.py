from sympy import symbols, And, Or, Not, Implies, satisfiable

# Define symbols
john_likes_peanuts = symbols("john_likes_peanuts")  # John likes peanuts
peanuts = symbols("peanuts")                        # Peanuts
alive = symbols("alive")                            # Alive status
food = symbols("food")                              # Food status
eats_anil_peanuts = symbols("eats_anil_peanuts")    # Anil eats peanuts
eats_harry_peanuts = symbols("eats_harry_peanuts")  # Harry eats peanuts
apple = symbols("apple")                            # Apple is food
vegetable = symbols("vegetable")                    # Vegetable is food

# Create the knowledge base (KB)
knowledge_base = And(
    Implies(food, john_likes_peanuts),                         # If it's food, then John likes it
    Or(peanuts, apple, vegetable),                             # Peanuts, apple, and vegetable are food
    Implies(And(eats_anil_peanuts, alive), food),              # If Anil eats peanuts and is alive, then it's food
    And(eats_anil_peanuts, alive),                             # Anil eats peanuts and is alive
    Implies(eats_anil_peanuts, eats_harry_peanuts)             # Harry eats peanuts if Anil eats peanuts
)

# Display the knowledge base
print("Knowledge Base:")
print(knowledge_base)

# Check if "John likes peanuts" by setting peanuts to True
john_likes_peanuts_check = satisfiable(knowledge_base.subs({peanuts: True}))
print("\nDoes John like peanuts?", john_likes_peanuts_check[john_likes_peanuts])
