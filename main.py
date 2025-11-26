import string_utils as su
import equation_utils as eu

def balance_reaction(reaction):

    reactants, products = su.parse_chemical_reaction(reaction)

    reactant_atoms = su.count_atoms_in_reaction(reactants)
    product_atoms  = su.count_atoms_in_reaction(products)

    equations, coefficients = eu.build_equations(reactant_atoms, product_atoms)

    coefficients = eu.my_solve(equations, coefficients) + [1]

    return coefficients



