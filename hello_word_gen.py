#this programs reconstruct a hello word phrase using G.A

import random
import string


def fitness(_str):
    #print (_str)

    word = _str.gen
    i = 0
    score = 0
    #dumb way to compare is max equal letter into the real string
    for x in 'hello world':
        if x == word[i]:
            score += 1
        i += 1
    _str.score = score
    return score



class Cromossome:
    def __init__(self, gen=0, score=0):
        self.gen = gen
        self.score = score
    def __repr__(self):
        return '%s - %d' % (self.gen, self.score)

class Population(object):
    def __init__(self, size):
        self.individuos = []
        self.size = size

    def init_pop(self, n=None):
        if n is None:
            n = self.size
        self.individuos = []
        letters = string.ascii_lowercase
        for i in range(n):
            self.individuos.append(Cromossome(''.join(random.choice(letters) for x in range(5)) + ' '+ ''.join(random.choice(letters)
                for x in range(5)),0))


def make_roullet(pop):

    for p in pop:
        fitness(p)

    sum_fit = sum(fitness(p) for p in pop)
    return sum_fit

def turn_roullete(pop, sum_fit):

    import random
    current = 0
    pick = random.randint(0, sum_fit)
    #print ('selected: %d' % pick)
    for p in pop:
        current += p.score
        if current >= pick:
            return p


"""
for x in range(30):
    print(turn_roullete(pop.individuos, sum_fit))
    print ('\n')
print (sum_fit)
"""
def crossover(pop, sum_fit):
    new_gen = []
    #actualy we do it as much as we want...
    for x in range(int(len(pop)/2)):
        son_1 = Cromossome()
        son_2 = Cromossome()
        parent_2 = turn_roullete(pop, sum_fit).gen
        parent_1 = turn_roullete(pop, sum_fit).gen

        cross = random.randint(0, len(parent_2))
        son_1.gen = parent_1[0:cross] + parent_2[cross:]
        son_2.gen = parent_2[0:cross] + parent_1[cross:]

        new_gen.append(son_1)
        new_gen.append(son_2)
    return new_gen

pop = Population(204)
pop.init_pop()

#sorting the pop by its score
import operator
#we need to run the roullete


generations = 0
while True:
    generations += 1
    sum_fit = make_roullet(pop.individuos)
    pop.individuos.sort(key=operator.attrgetter('score'))
    #print ('overeal pop fit: %s' % sum_fit)
    #print ('the best gen is: %s' % pop.individuos[-1])
    if int(pop.individuos[-1].score) == 11:
        break
    pop.individuos = crossover(pop.individuos, sum_fit)
    #print()
print ('Qtd gen: %d' % generations)
