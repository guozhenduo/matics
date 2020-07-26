class Area:
    def __init__(self,a,b = 1):
        try:
            try:
                self.a = int(a)
                self.b = int(b)
            except:
                self.a = float(a)
                self.b = float(b)

        except:
            raise TypeError("Error Type! ")
            exit()

        

    def rectangle(self):
        return self.a * self.b 

    def square(self):
        return self.a * self.b 

    def triangle(self):
        return self.a * self.b / 2

    def parallelogram(self):
        return self.a * self.b
    
    def trapezoid(self,h):
        return (self.a + self.b) * h / 2

    def circle(self):
        return (self.a ** 2) * 3.141

class Volume:
    def __init__(self,a,b,h):
        try:
            try:
                self.a = int(a)
                self.b = int(b)
                self.h = int(h)
            except:
                self.a = float(a)
                self.b = float(b)
                self.h = float(h)

        except:
            raise TypeError("Type Error! ")

    def rectangle(self):
        return self.a * self.b * self.h

    def square(self):
        return self.a * self.b * self.h
