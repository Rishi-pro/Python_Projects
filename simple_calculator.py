#ask user for numbers
opt_1= int(input('please enter a number accordingly\n1. addition\n2. subtraction\n3. multiplication\n'))

#this is for 1 as addition
if opt_1==1:
    ask_user= int(input('please enter a number :'))
    ask_user_2= int(input('please enter another number :'))
    print('the addtion of these numbers is ',ask_user + ask_user_2)

#now this would for subtraction
if opt_1==2:
    subt_user= int(input('enter a number :'))
    subt_user_2= int(input(' enter another number :'))
    print('your answer is ',subt_user - subt_user_2)
    
#now this would be for multiplication
if opt_1==3:
    mult_user= int(input('enter a number: '))
    mult_user_2= int(input('enter another number'))
    print('your answer is ',mult_user * mult_user_2)

# just normal greetings for the user to use it
print('thanks for using my code')
