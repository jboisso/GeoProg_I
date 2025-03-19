class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z

    def setX(self, x):
        self._x = x

    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y = y

    def getY(self):
        return self._y

    def setZ(self, z):
        self._x = z

    def getZ(self):
        return self._z
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
    
    def __add__(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    def __sub__(self, subVector):
        return Vector3(self.x - subVector.x, self.y - subVector.y, self.z - subVector.z)
    
    def __mul__(self, multiplikator):
        if type(multiplikator) == Vector3:
            return Vector3(self.x*multiplikator.x, self.y*multiplikator.y, self.z*multiplikator.z)
        else:
            return Vector3(self.x*multiplikator, self.y*multiplikator, self.z*multiplikator)
        
    def __rmul__(self, multiplikator):
        return Vector3(self.x*multiplikator, self.y*multiplikator, self.z*multiplikator)
        
    def dot(self, b):
        return (self.x*b.x + self.y*b.y + self.z*b.z)
    
    def cross(self, b):
        return Vector3(self.y*b.z+b.y*self.z, self.z*b.x+b.z*self.x, self.x*b.y+b.x*self.y)
    
    def normalize(self):
        length = float(self.x**2+self.y**2+self.z**2)**0.5
        return Vector3(float(self.x/length), float(self.y/length), float(self.z/length))
    
    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)

v0 = Vector3(1,0,0)
v1 = Vector3(0,1,0)


