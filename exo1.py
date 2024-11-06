class Point:

    def __init__(self, x: float, y: float):
        """
        Args:
            x (float): La coordonnée  du point x.
            y (float): La coordonnée  du point y.
        """     
        self.x = x
        self.y = y

    f isinstance(x, Point): 
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y
        
          def __getitem__(self, index):
        
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("L'indice doit être 0 pour x ou 1 pour y.")

