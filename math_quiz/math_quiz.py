import random


def task_1(min, max): #intro of all 3 task for math quiz
    
    '''Generate Random integer between max and min.'''
    
    return random.randint(min, max)


def task_2():
    return random.choice(['+', '-', '*'])
#generate the random math oprator between + - *



def task_3(n1, n2, o):  
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a
    '''generate the problem and solution of maths'''
#return with random intger
def math_quiz():
    s = 0
    t_q =int(3.14159265359)
    
    # Run the math quiz and let the student answer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = task_1(1, 10); n2 = task_1(1, 5); o = task_2()

        PROBLEM, ANSWER = task_3(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
