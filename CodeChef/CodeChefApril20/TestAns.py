'''
The final exam is tomorrow and Chef is one of the students who are going to take the exam.
In the exam, there are K question forms. 
Each form has N multiple-choice questions (numbered 1 through N). In each question,
there are M possible answers (numbered 1 through M) and exactly one of those answers is correct.
Chef will receive one of the K forms.
Unfortunately, Chef was busy cooking, so he did not study. Instead, he broke into the university's database and
stole the sheets containing the correct answers to the questions for all K forms. 
Let's number the answer sheets 1 through K. For each valid i and j, 
let's denote the correct answer to the i-th question in the j-th answer sheet by Ci,j. 
The problem is that Chef cannot know which answer sheet contains 
the correct answers for the form he receives during the exam. In addition,
he can remember the answers to all questions in all answer sheets,
but he cannot answer any questions based on his knowledge of the subjects in them.
Help Chef choose the answers to his N questions in such a way that the worst-case (smallest possible)
number of correctly answered questions is maximised.
'''

'''
T denoting the number of test cases
N , M , K where #N is total questions #M is the total options to each question #K is the number of sets
C11 C12   #for K=2 N=4 M=2
C21 C22
C31 C32
C41 C42
'''

import random
import sys


def reset_ppo(le):
    something = []
    for j_iter in range(le):
        something.append(0)
    return something


def leaked_answers(N, M, K):
    marks_per_set_col = reset_ppo(K)
    for j_iter in range(N):
        point_per_option_row = reset_ppo(M)
        answers = list(sys.stdin.readline().split())
        for k_iter in range(K):
            point_per_option_row[int(answers[k_iter]) - 1] += 1
        best_option = [i for i, x in enumerate(point_per_option_row) if x == max(point_per_option_row)]
        best_option = list(map(lambda x: x + 1, best_option))
        print(best_option[random.randint(0, len(best_option) - 1)], end=" ")


test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
    sec_line = list(sys.stdin.readline().split())
    NN = int(sec_line[0])
    MM = int(sec_line[1])
    KK = int(sec_line[2])
    leaked_answers(NN, MM, KK)
