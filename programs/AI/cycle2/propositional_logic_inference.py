from sympy import symbols, And, Or, Not, Implies, satisfiable

# Define the symbols
rain = symbols("rain")         # It is raining
hagrid = symbols("hagrid")     # Harry visited Hagrid
dumbledore = symbols("dumbledore")  # Harry visited Dumbledore

# Create the knowledge base (KB) with the given facts
knowledge_base = And(
    Implies(Not(rain), hagrid),                  # If it didn't rain, then Harry visited Hagrid
    Not(And(hagrid, dumbledore)),                 # Harry did not visit both Hagrid and Dumbledore
    Or(hagrid, dumbledore),                       # Harry visited either Hagrid or Dumbledore
    dumbledore                                    # Fact: Harry visited Dumbledore
)

# Display the knowledge base
print("Knowledge Base:")
print(knowledge_base)

# Check satisfiability of the knowledge base
is_satisfiable = satisfiable(knowledge_base)
print("\nIs the knowledge base satisfiable?", is_satisfiable)

# Check if "Harry visited Hagrid"
hagrid_check = satisfiable(knowledge_base.subs({hagrid: True}))
print("\nDid Harry visit Hagrid?", hagrid_check)

# Check if "It rained today"
rain_check = satisfiable(knowledge_base.subs({rain: True}))
print("Did it rain today?", rain_check)
