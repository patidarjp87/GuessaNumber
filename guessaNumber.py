#script to guess a no. 
print('Game to guess a no. in max 5 round')
n=18
count=1
while count!=6:
 print('Round',count)
 print('guess a number')
 m=eval(input())
 if m>n:
    print('Entered no. is greater than default no.')
    count+=1
 elif m<n:
    print('Entered no. is lesser than default no.')
    count+=1
 else:
    print('Entered no. is correct...!!!,CONGRATULATIONS...you won the game in',count,'Round')
    break
else:
   print('you lose')
input('press enter to exit')
