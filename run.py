from random import shuffle
import time

questionsAnswers = [
    ("Big O of stack insert", "1"),
    ("Big O of heap insert", "log(n)")
]

shuffle(questionsAnswers)
correct = 0
times = []

for (q, a) in questionsAnswers:
    start = time.time()
    print q
    theirA = raw_input()
    end = time.time()
    times.append(end-start)
    if theirA == a:
        correct+=1

print "You got", correct, "correct and your times were", times

