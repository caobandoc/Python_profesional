import time

class FiboIter():
    
    def __init__(self, max_number:int):
        self.max_number = max_number
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        self.counter +=1
        if self.counter == 1:
            return self.n1
        elif self.counter == 2:
            return self.n2
        else:
            self.aux = self.n1+ self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            #swap
            self.n1, self.n2 = self.n2, self.aux
            if self.aux > self.max_number:
                raise StopIteration
            return self.aux
        
if __name__ == "__main__":
    fibonacci = FiboIter(13)
    for element in fibonacci:
        print(element)
        time.sleep(0.2)