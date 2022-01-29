remove_duplicate = lambda some_list:list(set(some_list))

def run():
    random_list = [1,1,2,2,4,5,6,6]
    print(remove_duplicate(random_list))
    
if __name__ == '__main__':
    run()