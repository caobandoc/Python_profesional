import time

def fibo_gen(max:int):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        counter += 1
        if counter == 1:
            yield n1
        elif counter == 2:
            yield n2
        else:
            aux = n1 + n2
            if aux > max:
                raise StopIteration
            n1, n2 = n2, aux
            yield aux

if __name__ == "__main__":
    fibonnaci = fibo_gen(int(input("Ingresa el numero maximo: ")))
    try:
        for element in fibonnaci:
            print(element)
            time.sleep(0.5)
    except:
        print("Termino de iterar")