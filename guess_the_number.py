import pyfiglet as p
import random as r
print(p.figlet_format("Guess the number game",font="slant"))
walk=True
while walk:#walk ensure it works
	try:
		min=int(input("enter the starting integer value="))
		max=int(input(f'\nenter the ending integer value='))
	except:
		print(f'\nplz,enter the integer value')
		continue
	if max>=min:
		d=max-min#d is difference b/w ending value and starting value
		if d in range(3):
			print(f'\nthe difference b/w ending value {max}and starting value {min} must be greater than 2.')
			continue
		elif d in range(3,11):
			print(f'\nyour level of guessing the number game is  EASY.')
		elif d in range(11,51):
			print(f'\nyour level of guessing the number game is  MODERATE.')
		elif d in range(51,101):
			print(f'\nyour level of guessing the number game is  HARD.')
		elif d>100:
			print(f'\nyour level of guessing the number game is  VERY HARD.')
	else:
		print(f'\nending value {max} must be greater than starting value {min} ')
		continue
	guess=r.randint(min,max)
	walk1=True 
	while walk1:
		try:
			n=int(input(f'\nGuess the no. b/w {min}  and {max}='))
		except:
			print('\nplz,enter the integer value')
			continue
		if n>=min and n<=max:
			if n==guess:
				print(p.figlet_format("Cheers \nYou won!",font="slant"))
				walk2=True
			else:
				print()
				if n>guess:
					if (n-guess)>10:
						print("Too high.")
					elif (n-guess)>5:
						print("Little higher.")
					elif (n-guess)>2:
						print("It's close.")
					else:
						print("It's too close.")
				else:
					if (guess-n)>10:
						print("Too Low.")
					elif (guess-n)>5:
						print("Little Lower.")
					elif (guess-n)>2:
						print("It's close.")
					else:
						print("It's too close.")
				continue 
		else:
			print(f'\nThe Guess no. must be in b/w {min} and {max}')
			continue
		while walk2:
			ch=input("\nwanna try again?(y/n)").lower()
			if ch=="y":
				walk=True
				ch2=input('\nwanna try with same starting value and ending value? (y/n)').lower()
				if ch2=="y":
					guess=r.randint(min,max)
					walk2=False
				elif ch2=="n":
					walk1=False
					walk2=False
				else:
					print('\nplz,enter y or n')
					continue
			elif ch=="n":
				walk=False
				walk1=False
				walk2=False
			else:
				print('\nplz,enter y or n')
				continue