import pickle
import re

class Wordset:
    def __init__(self,seed):
        self.seed = seed
        self.decendants = {seed}
    
    def extend(self):
        next_generation = set()
        for word in self.decendants:
            for i in range(len(word)):
                patt = re.compile(word[:i]+'[a-z]'+word[i+1:])
                matches = {x for x in vocab if patt.match(x)}
                next_generation |= matches
        self.decendants = next_generation
        return next_generation

def loadvocab(filename):
    with open(filename,'rb') as f:
        return pickle.load(f)
        
solution = ['tooth','paste']

index = 0
vocab = {x for x in loadvocab('vocab.pickle') if len(x) == len(solution[0])}

while index < len(solution)-1:
    start = Wordset(solution[index])
    end = Wordset(solution[index+1])
    while len(start.decendants & end.decendants) == 0:
        start.extend()
        if len(start.decendants & end.decendants) == 0:
            end.extend()
    common_words = start.decendants & end.decendants
    if solution[index+1] in common_words:
        index += 1
    else:
        solution.insert(index+1, common_words.pop())
print(solution)
