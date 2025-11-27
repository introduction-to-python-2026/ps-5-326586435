def split_before_uppercases(formula):
    split_formula = []
    start = 0
    if not formula:
        return []
    for i in range(1, len(formula)):
        if formula[i].isupper():
           split_formula.append(formula[start:i])
           start = i
    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    digit_index = None
    for i, ch in enumerate(formula):
        if ch.isdigit():
            digit_index = i
            break
    if digit_index is None:
       return formula, 1
    x = formula[:digit_index]
    y = int(formula[digit_index:])
    return x, y
    
def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    parts = split_before_uppercases(molecular_formula)
    for a in parts: 
       atom, count = split_at_digit(a)
       if atom in atom_counts:
        atom_counts[atom] += count
       else:
         atom_counts[atom] = count
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
