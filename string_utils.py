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
    x=0
    y=0
    digit_index=None
    for t in range(len(formula)):
        if formula[t].isdigit():
            digit_index = t
            break
    if digit_index == None:
        x=formula
        y=1
    else:
        y = int(formula[digit_index:])
        x = formula[0:digit_index]
    return x, y


def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    parts = split_before_uppercases(molecular_formula)

    for part in parts:
        atom, count = split_at_digit(part)
        atom_counts[atom] = atom_counts.get(atom, 0) + count

    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
