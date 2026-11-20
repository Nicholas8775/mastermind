import os
import random


class MMGame:

    def __init__(self, history=None, answer=None, evaluation=None, won=False, game_size=4):

        if history is None:
            self.attempts = []
        else:
            self.attempts = history
        
        if answer is None:
            self.secret = ()
            for _ in range(game_size):
                self.secret = (*self.secret, random.randint(1,9))
        else:
            self.secret = answer
        
        if evaluation is None:
            self.evaluation = []
        else:
            self.evaluation = evaluation
    
    def make_guess(self, guess):
        self.attempts.append(guess)
        self.row_feedback(-1)

    def get_attempt_entry(self, index):
        return self.attempts[index]
    
    def get_answer(self):
        return list(self.secret)
    
    def row_feedback(self, row_num):
        checked = [False] * len(self.secret)
        list_of_mismatched = []
        matched = 0
        mismatched = 0
        
        # checking for matched
        for i in range(len(self.secret)):
            if self.secret[i] == int(self.attempts[row_num][i]):
                checked[i] = True
                matched += 1
            else:
                list_of_mismatched.append(i)

        # checking for mismatched
        for i in list_of_mismatched:
            for j in list_of_mismatched:
                if i != j and not checked[j] and int(self.attempts[row_num][i]) == self.secret[j]:
                    checked[j] = True
                    mismatched += 1
                    break

        wrong = (len(self.secret) - matched) - mismatched
        self.evaluation.append((matched, mismatched, wrong))
