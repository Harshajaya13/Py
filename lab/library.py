class Library:
    def __init__(self,acc_num,publisher,title,author):
        self.acc_num=acc_num
        self.publisher=publisher
        self.title=title
        self.author=author
    
    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")
    def compute(self,delay):
        self.delay = delay
        self.fine = self.delay * 0.5
    def display(self):
        print(f"fine is {self.fine} for {self.delay} days of delay.")
        
l = Library(12345,"Penguin","The Great Gatsby","F. Scott Fitzgerald")
l.read()
l.compute(4)
l.display()
