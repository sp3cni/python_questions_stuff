class fox(): 

    def __init__(self, ):

        self.cache = { 2: 2, 1: 1, 0: 1 }  

    def climb_up(self,n):

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.climb_up(n-1) + self.climb_up(n-2) + self.climb_up(n-3)

        return self.cache[n]
