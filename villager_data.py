"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code
    village_file = open(filename)
    
    for line in village_file:
        split_line = line.split('|')
        species.add(split_line[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    # Open csv file
    village_file = open(filename)

    # If search string is all, return all names
    if search_string == "All":
        for line in village_file:
            line_split = line.split('|')
            villagers.append(line_split[0])
    
    # Else only return names of specific species
    else:
        for line in village_file:
            line_split = line.split('|')
            if search_string.lower() == line_split[1].lower():
                villagers.append(line_split[0])


    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    villagers_by_hobby = []

    hobbies = set()
    hobbies_and_names = ()

    with open(filename) as village_file:
    
        # Make a set of the hobbies on the csv file
        for line in village_file:
            line_split = line.split('|')
            hobbies.add(line_split[3])
            # Make a tuple of the hobbies and names of villagers
            hobbies_and_names = hobbies_and_names + (line_split[3], 
                                                     line_split[0])
            
    for hobby in hobbies:
        villagers = []
        for i in range(0, len(hobbies_and_names), 2):

            # If hobby is same as hobbies set, add villagers name to list
            if hobby.lower() == hobbies_and_names[i].lower():
                villagers.append(hobbies_and_names[i + 1])
        # Add villagers list to the villagers_by_hobby list
        villagers_by_hobby.append(villagers)

    return villagers_by_hobby


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
