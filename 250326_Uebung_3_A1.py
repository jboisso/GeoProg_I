import math

class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self):
        return 0
    
    def distance(self, P1, P2):
        return(((P1.X-P2.X)**2+(P1.Y-P2.Y)**2)**0.5)

    def __str__(self):
        return self.name
        
class Punkt:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y 

    def __iter__(self):                     #erlaubt es Punkte direkt als Tupel aufzurufen mit tuple(self.punktinstanz)
        return iter((self.X, self.Y))

class Kreis(Figur):
    def __init__(self, radius, center):
        super().__init__("Kreis")
        self.radius = radius
        self.center = center

    def umfang(self):
        return(2*self.radius*math.pi)
    
    def __str__(self):
        return f"Objekt: {self.name}, M={tuple(self.center)}, r={self.radius}, Umfang = {self.umfang()}"

class Dreieck(Figur):
    def __init__(self, P1, P2, P3):
        super().__init__("Dreieck")
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3

    def umfang(self):
        return self.distance(self.P1, self.P2)+self.distance(self.P2, self.P3)+self.distance(self.P1, self.P3)

    def __str__(self):    
        return f"Objekt: {self.name}, Umfang = {self.umfang()}, Eckpunkte: {tuple(self.P1)}, {tuple(self.P2)}, {tuple(self.P3)}."
    
class Rechteck(Figur):
    def __init__(self, P1, P2):
        super().__init__("Rechteck")
        self.P1 = P1
        self.P2 = P2
    
    def umfang(self):
        return 2*abs(self.P1.X-self.P2.X)+2*abs(self.P1.Y-self.P2.Y)
    
    def __str__(self):
        return f"Objekt: {self.name}, Umfang = {self.umfang()}, Eckpunkte: {tuple(self.P1)}, {self.P1.X, self.P2.Y}, {tuple(self.P2)}, {self.P2.X, self.P1.Y} "
    
class Polygon(Figur):
    def __init__(self, *args):
        super().__init__("Polygon")
        self.points = args

    def umfang(self):
        umfang = 0
        for i in range(len(self.points)):
           umfang += self.distance(self.points[i], self.points[(i+1) % len(self.points)])
        return umfang

    def __str__(self):
        points = ', '.join(f"({p.X}, {p.Y})" for p in self.points)
        return f"Objekt: {self.name}, Umfang = {self.umfang()}, Eckpunkte: {points}"


k1 = Kreis(10, Punkt(5,5))
print(k1)
d1 = Dreieck(Punkt(0,0), Punkt(5,0), Punkt(0,5))
print(d1)
r1 = Rechteck(Punkt(0,0), Punkt(5,5))
print(r1)
p1 = Polygon(Punkt(0,0), Punkt(1,1), Punkt(3,0), Punkt(5,9), Punkt (0,10))
print(p1)