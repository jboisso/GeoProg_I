class WGS84Coord():

    def __init__(self, _longitude=0, _latitude=0):      # Variablen definieren, befüllen über a = WGS84Coord(_longitude, _latitude). Wenn nichts gegeben = 0
        self.setLon(_longitude)                         # Variable immer durch setter laufen lassen, auch wenn über Klasse befüllt
        self.setLat(_latitude)                          # Variable immer durch setter laufen lassen, auch wenn über Klasse befüllt

    def setLon(self, longitude):                        #Variable über den Setter verändern
        self.lon = longitude

        if self.lon >180 or self.lon <-180:             # Prüfen des longitudes Wertebereich
            print(f"The given longitude is out ouf bounds, it was corrected.")
        

        while self.lon >180 or self.lon <-180:          # Longitude korrigieren, bis in Wertebereich
            
            if self.lon >180:
                self.lon -= 360
            else:
                self.lon += 360

        return self.lon                                 # Rückgabe der Longitude aus Method
    
    def setLat(self, latitude):                         #Variable über Setter verändern
        self.lat = latitude
        self.counter = 0                                # Initialisieren Counter für Longitude veränderung bei Polüberschreitung
        if self.lat >90 or self.lat <-90:               # Prüfen des Lat Wertebereiches
            print(f"The given latitude is out of bounds, it was corrected.")
        
        while self.lat >90 or self.lat <-90:            # korrigieren der Lat bis in Wertebereich. 91 -> 89 und nicht -91!
            
            if self.lat >90:
                self.lat = 180 - self.lat
                self.counter += 1                       # Counter wird bei jeder Polüberschreitung um 1 erhöht. ist counter danach ungerade, muss Lon um 180° angepasst werden
            else:
                self.lat = -180 - self.lat
                self.counter += 1

        if self.counter%2 == 1 and self.lat%90 != 0 or self.lat%180 == 0:   #Anpassen von Longitude wenn Counter ungerade und Lat nicht ein Vielfaches von Pol und nicht auf Äquator
            print(f"The given longitude was corrected due to the given latitude beeing out of bounds")
            self.lon += 180
            if self.lon > 180:
                self.lon -= 360
            self.counter = 0
        
        return self.lat
     

    def getLat(self):
        self.lat_corr = self.lat
        return self.lat_corr
                
    def getLon(self):
        self.lon_corr = self.lon
        return self.lon_corr
    
    latitude = property(getLat, setLat)                 # Definition des Pseudoattributes. Wird ein solches später verändert, wird der ganze getter-setter ablauch durchlaufen.
    longitude = property(getLon, setLon)

        

P1 = WGS84Coord(0,269)
print(P1.getLon(), P1.getLat())
