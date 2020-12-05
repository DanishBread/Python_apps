from replit import clear
from game_data import data
import art
from random import randint

game_over= False
score=0
randomindexlist=[]
for _ in range (2):
  randomindexlist.append(randint(0, len(data)-1))

while not game_over:
  print(art.logo, "\n")
  print(f"Compare A: {data[randomindexlist[0]]['name']},\n A {data[randomindexlist[0]]['description']} from {data[randomindexlist[0]]['country']}...")
  print(art.vs)
  print(f"Against B: {data[randomindexlist[1]]['name']},\n A {data[randomindexlist[1]]['description']} from {data[randomindexlist[1]]['country']}!")

  users_answer= input("Who do you think has more followers? A or B\t").lower()
  if data[randomindexlist[0]]['follower_count'] > data[randomindexlist[1]]['follower_count']:
    correct_answer= 'a'
  else:
    correct_answer= 'b'

  if users_answer == correct_answer:
    score+=1
    clear()
    print("You're right! You gained a point!\nNow your current score is", score)
    randomindexlist.pop(0)
    randomindexlist.append(randint(0, len(data)-1))
  else:
    print("Well Played! You scored", score, "points!\nBetter Luck Next Time!")
    game_over= True
  