from random import randint

print("Welcome to the Dice Game!")
print("***********************************")
 
file=open("Authorised_Names.txt","r")
AllNames=file.read()
file.close()
eachname=AllNames.split(",")
length=len(eachname)

authorised="no"
while authorised=="no":
    player1=input("\nInput first players name: ")
    player1=player1.title()
    for i in range(length):
        if player1==eachname[i]:
            print("You are authorised!")
            authorised="yes"
            break
    else:
        print("That name is not authorised")
        
authorised="no"
while authorised=="no":
    player2=input("\nInput second players name: ")
    player2=player2.title()
    while player1==player2:
        print("You can't have the same player against themseleves!")
        player2=input("\nPlease input another name: ")
        player2=player2.title()
    for i in range(length):
        if player2==eachname[i]:
            print("You are authorised!")
            authorised="yes"
            break
    else:
        print("That name is not authorised")

Round=0
score1=0
score2=0

while Round<6:
    print("\nPress ENTER to do",player1+"'s GO")
    input()
    player1roll1=randint(1,6)
    player1roll2=randint(1,6)
    total1=player1roll1+player1roll2
    print(player1,"rolled a",player1roll1,"and a",player1roll2)
    score1+=total1
    total1a=total1/2
    total1b=int(total1a)
    if total1a==total1b:
        print("They add up to become even! An additional 10 points to you")
        score1+=10
        if player1roll1==player1roll2:
            additionalroll=randint(1,6)
            print("They are both the same! You recieved an additional",additionalroll,"points.")
            score1+=additionalroll
    else:
        print("They add up to become odd. Minus 5 point!")
        score1-=5
        if score1<0:
            score1=0
    print (player1+"'s current score is",score1)
        
    print("\nPress ENTER to do",player2+"'s GO")
    input()
    player2roll1=randint(1,6)
    player2roll2=randint(1,6)
    total2=player2roll1+player2roll2
    print(player2,"rolled a",player2roll1,"and a",player2roll2)
    score2+=total2
    total2a=total2/2
    total2b=int(total2a)
    if total2a==total2b:
        print("They add up to become even! An additional 10 points to you")
        score2+=10
        if player1roll1==player1roll2:
            additionalroll=randint(1,6)
            print("They are both the same! You recieved an additional",additionalroll,"points.")
            score2+=additionalroll           
    else:
        print("They add up to become odd. Minus 5 point!")
        score2-=5
        if score2<0:
            score2=0
    print (player2+"'s current score is",score2)
    
    Round+=1
    
if score1>score2:
    print("\n"+player1,"won! Their score was",score1,"points")
    print(player2,"had a score of",score2,"points")
    print(player1,"won by",score1-score2,"points!")
    winscore=score1
    winner=player1
elif score2>score1:
    print("\n"+player2,"won! Their score was",score2,"points")
    print(player1,"had a score of",score1,"points")
    print(player2,"won by",score2-score1,"points!")
    winscore=score2
    winner=player2
else:
    player1score=0
    player2score=0
    winscore=score1
    score1=str(score1)
    print("\nIt is a draw with both people with score of",score1)
    input("Press ENTER to commence the draw breaker \n")
    while player1score == player2score:
        player1score=randint(1,6)
        player2score=randint(1,6)
        if player1score>player2score:
            print(player1,"won, after rolling a",player1score,"in the extra round")
            print(player2,"rolled a",player2score,":(")
            winner=player1
        elif player2score>player1score:
            print(player2,"won, after rolling a",player2score,"in the extra round")
            print(player1,"rolled a",player1score,":(")
            winner=player2
 
file=open("Highscore.txt","a")
file.write(str(winscore)+","+winner+"\n")
file.close()


file = open("Highscore.txt" , "r")
lines = file.read()
file.close()
allover=lines.split("\n")
allover.sort(reverse=True)

matching_100 = [s for s in allover if "100" in s]
matching_101 = [s for s in allover if "101" in s]
matching_102 = [s for s in allover if "102" in s]
matching_103 = [s for s in allover if "103" in s]
matching_104 = [s for s in allover if "104" in s]
matching_105 = [s for s in allover if "105" in s]
matching_106 = [s for s in allover if "106" in s]
matching_107 = [s for s in allover if "107" in s]
matching_108 = [s for s in allover if "108" in s]
matching_109 = [s for s in allover if "109" in s]
matching_11 = [s for s in allover if "11" in s]
matching_12 = [s for s in allover if "12" in s]
matching_13 = [s for s in allover if "13" in s]
matching_14 = [s for s in allover if "14" in s]

sortedlist=[]
sortedlist.extend(matching_100)
sortedlist.extend(matching_101)
sortedlist.extend(matching_102)
sortedlist.extend(matching_103)
sortedlist.extend(matching_104)
sortedlist.extend(matching_105)
sortedlist.extend(matching_106)
sortedlist.extend(matching_107)
sortedlist.extend(matching_108)
sortedlist.extend(matching_109)
sortedlist.extend(matching_11)
sortedlist.extend(matching_12)
sortedlist.extend(matching_13)
sortedlist.extend(matching_14)

sortedlist.sort()
sortedlist.reverse()
sortedlist.extend(allover)

print("\nThe top 5 scores are:")
for i in range (5):
    print(sortedlist[i])




















