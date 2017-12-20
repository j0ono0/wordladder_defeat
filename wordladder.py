import pickle
import re

class Wordlib:
    def __init__(self,filename):
        self.full = self.load('vocab.pickle')
        
    def load(self,filename):
        with open(filename,'rb') as f:
            return pickle.load(f)        
    
    def len(self,length):
        return {x for x in self.full if len(x) == length}
            

class Wordfamily:
    def __init__(self,seed,vocab):
        self.seed = seed
        self.decendants = {seed}
        self.vocab = vocab
    
    def extend(self):
        next_generation = set()
        for word in self.decendants:
            for i in range(len(word)):
                patt = re.compile(word[:i]+'[a-z]'+word[i+1:])
                matches = {x for x in self.vocab if patt.match(x)}
                next_generation |= matches
        self.decendants = next_generation
        return next_generation


vocab = Wordlib('vocab.pickle')
solution = ['tooth','paste']
index = 0

while index < len(solution)-1:
    start = Wordfamily(solution[index],vocab.len(len(solution[0])))
    end = Wordfamily(solution[index+1],vocab.len(len(solution[0])))
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
