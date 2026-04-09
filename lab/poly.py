class Polynomial:
    def __init__(self, terms):
        self.terms = terms   

    def add(self, other):
        result = {}

       
        for power in self.terms:
            result[power] = self.terms[power]

        
        for power in other.terms:
            if power in result:
                result[power] += other.terms[power]
            else:
                result[power] = other.terms[power]

        return Polynomial(result)

    def display(self):
        print(self.terms)
        
p1 = Polynomial({2: 3, 1: 2, 0: 1})
p2 = Polynomial({2: 1, 1: 4, 0: 2})
p3 = p1.add(p2)
p3.display()