def make_division_by(n):
    """This closure return a function that returns the division of an x number by n
    """
    pass

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # Output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # Output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) #Output is 3
    
if __name__ == '__main__':
    run()