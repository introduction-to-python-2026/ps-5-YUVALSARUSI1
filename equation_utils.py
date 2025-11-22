import string_utils as yv, equation_utils as vl
def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = yv.parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = yv.count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = yv.count_atoms_in_reaction(products)

    # 2.build equation and solve
    equations, coefficients = vl.build_equations(reactant_atoms, product_atoms)
    coefficients = vl.my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]

