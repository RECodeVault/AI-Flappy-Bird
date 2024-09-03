class GameComponents:
    def __init__(self):
        self.score = 0
        self.generation_count = 0

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score
