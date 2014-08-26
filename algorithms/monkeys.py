import string
import random
import time

character_pool = string.lowercase + ' '
iteration = 1

goal_string = 'methinks it is like a weasel'

def generate_string():
    random_string = ''.join(random.choice(character_pool) for i in range(28))
    return random_string

def score_string(current_string):
    score = 0
    for index, letter in enumerate(current_string):
        if letter == goal_string[index]:
            score += 1
    return score

def modify_string(current_string):
    for index, letter in enumerate(current_string):
        if letter == goal_string[index]:
            pass
        else:
            current_string = (current_string[:index] +
                random.choice(character_pool) + current_string[index + 1:])
            return current_string

best_string = ''
random_string = generate_string()
start = time.time()
while score_string(random_string) != len(goal_string):
    if iteration % 1000 == 0:
        print 'Iteration: %s. Best string: %s (score: %s).' % (iteration,
            best_string, score_string(best_string))

    random_string = modify_string(random_string)

    if score_string(random_string) > score_string(best_string):
        best_string = random_string
    iteration += 1

end = time.time()
print "Time spent: %s seconds." % (round(end - start, 4))