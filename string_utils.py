def split_before_uppercases(formula):
    if not formula:
        return []

    start = 0
    elements = []

    for i in range(1, len(formula)):
        if formula[i].isupper():
            elements.append(formula[start:i])
            start = i

    elements.append(formula[start:])
    return elements

 

def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
            
    return formula, 1

    
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
