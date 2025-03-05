class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
        
    def ausgabe(self):
        print(f"Vektor: {(self.x, self.y, self.z)}")
        print(f"Der Vektor hat die Länge {self.len()}")


v1 = Vector3(3,4,5)
v2 = Vector3()
v1.ausgabe()
v2.ausgabe()


