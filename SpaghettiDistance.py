class SpaghettiDistance():
    def __init__(self):
        self.dict = {}
        self.total_sentences = 0

    def get_similarity(self, a, b, normalized=True):
        """ 
        Returns the similarity between A and B. 
        If "normalized" is True, the result is normalized between 0 (less similar) and 1 (more similar). 
        Otherwise, an unbounded float measuring the value of common items is returned.
        """
        total_sentences = self.total_sentences if self.total_sentences > 0 else 1
        score = 0
        for word in (a & b):
            word_count = self.dict[word] if word in self.dict else 0
            score += 1 - (float(word_count) / total_sentences)

        if not normalized:
            total_score = 1
        else:
            total_score = 0
            for word in (a | b):
                word_count = self.dict[word] if word in self.dict else 0
                total_score += 1 - (float(word_count) / total_sentences)
        return score / total_score if total_score > 0 else 0

    def get_distance(self, a, b):
        """ 
        Returns the distance between A and B. 
        The result is normalized between 0 (less distant) and 1 (more distant). 
        """
        return 1 - self.get_similarity(a, b, True)

    def get_items_value(self, a):
        """ Returns the cumulative value of items in the set. """
        if self.total_sentences <= 0:
            return len(a)
        score = 0
        for word in a:
            word_count = self.dict[word] if word in self.dict else 0
            score += 1 - (float(word_count) / self.total_sentences)
        return score

    def add(self, stems):
        """ Add a new set to the context. """
        for word in stems:
            if word in self.dict:
                self.dict[word] += 1
            else:
                self.dict[word] = 1
        self.total_sentences += 1
        
    def forget(self, stems):
        """ Remove a set from the context. """
        for word in stems:
            if word in self.dict:
                self.dict[word] -= 1
                if self.dict[word] == 0:
                    del self.dict[word]
        self.total_sentences -= 1
