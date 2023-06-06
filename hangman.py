
def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()
    
    def print_hangman_win():
        print()
        print("\t +--------+")
        print("\t         | |")
 
        print("\t         | |")
        print("\t O       | |")
        print("\t/|\\      | |")
        print("\t |       | |")
        print("  ______/_\\______|_|___")
        print("  `````````````````````")
        print()