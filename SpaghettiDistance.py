from math import log

class SpaghettiDistance():
    def __init__(self):
        self.dict = {}
        self.total_sets = 0
        self.total_items = 0

    def get_similarity(self, a, b, normalized=True):
        """ 
        Returns the similarity between A and B. 
        If "normalized" is True, the result is normalized between 0 (less similar) and 1 (more similar). 
        Otherwise, an unbounded float measuring the value of common items is returned.
        """
        if self.total_items == 0:
            return len(a & b) / float(len(a | b))
        dimension = len(a) * len(b)
        score = 1
        for item in (a & b):
            if item not in self.dict or self.dict[item] == 0:
                score = 0
                break
            score *= dimension * ((float(self.dict[item]) / self.total_items) ** 2)
        return -log(score)

    def get_distance(self, a, b):
        """ 
        Returns the distance between A and B. 
        The result is normalized between 0 (less distant) and 1 (more distant). 
        """
        return 1 - self.get_similarity(a, b, True)

    def get_items_value(self, a):
        """ Returns the cumulative value of items in the set. """
        if self.total_items == 0:
            return len(a)
        dimension = len(a)
        score = 1
        for item in a:
            if item not in self.dict:
                score = 0
                break
            score *= dimension * ((float(self.dict[item]) / self.total_items) ** 2)
        return -log(score)

    def add(self, stems):
        """ Add a new set to the context. """
        for item in stems:
            if item in self.dict:
                self.dict[item] += 1
            else:
                self.dict[item] = 1
            self.total_items += 1
        self.total_sets += 1
        
    def forget(self, stems):
        """ Remove a set from the context. """
        for item in stems:
            if item in self.dict:
                self.dict[item] -= 1
                if self.dict[item] == 0:
                    del self.dict[item]
            self.total_items -= 1
        self.total_sets -= 1
