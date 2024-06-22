#Rock Paper Scissors
import random

def play():
    you = input("enter your choice : 'r' for rock , 'p' for paper, 's' for scissor : ") 
    computer = random.choice(['r','p','s'])
    if you == computer :
        return "it's a tie"
    if is_win(you,computer):
        return 'You Won !'
    return 'You Lost !'
def is_win(me,comp):
    if (me=='r' and comp=='s') or (me=='p' and comp=='r') or (me=='s' and comp=='p'):
        return True
    return False
while True:
    print(play())

