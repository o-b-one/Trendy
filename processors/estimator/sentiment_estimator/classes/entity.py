class Entity:

    def __init__(self, text, label, total_entities):
        self.text = text
        self.label = label
        self.count = 0
        self.total_entities = total_entities
    
    def increment(self):
        self.count += 1
    
    def decrese(self):
        self.count -= 1

    def to_tuple(self):
        return (self.text, self.label, self.count, self.count / self.total_entities)