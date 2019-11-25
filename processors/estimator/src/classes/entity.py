class Entity:

    def __init__(self, text, label,id, total_entities):
        self.text = text
        self.label = label
        self.id = id
        self.count = 0
        self.total_entities = total_entities
    
    def increment(self):
        self.count += 1
    
    def decrese(self):
        self.count -= 1

    def add_to_total(self, total_to_add):
        self.total_entities += total_to_add

    def get_ratio(self):
        total = self.total_entities if self.total_entities is not None and self.total_entities > 0 else 1
        return self.count / total

    def to_tuple(self):
        
        return (self.text, self.label, self.id, self.count, self.total_entities, self.get_ratio())