# TODO: THIS CLASS WILL BE RESPONSIBLE FOR KEEPING SCORE DISPLAYING TEXT ETC.

class GameComponents:
    def __init__(self):
        self.score = 0

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score