# letters_onley=['A','B','C','D','E','F','G','H','I','J']
import random
import time
#---the ----
p1=0
p2=0
detecting_player = 0
#-------
letter_list = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J']
#random.shuffle(letter_list)
print(letter_list)

numbers = '12345678901234567890'
numbers_in_list = list(numbers)
neww=''.join(numbers_in_list)
while True:
    if detecting_player % 2 == 0:
        print('player one turn')
    else:
        print('player two turn')
    while True:
        if detecting_player % 2 == 0:

            x1 = input('please enter your first number : ')
            xx = list(x1)
            detection = []
            while True:
                import string
                all_chaar=list(string.printable)
                all_chaar.append('')
                del all_chaar[0:10]
                for dd in xx :
                    if dd in all_chaar :
                        detection.append('0')
                if '0' not in detection :
                    break
                else:
                    x1=input('enter a valid numbers')
                    xx = list(x1)
                    detection = []
            x1=int(x1)






            
            x2 = input('please enter your second number : ')
            xx = list(x2)
            detection = []
            while True:
                import string
                all_chaar=list(string.printable)
                all_chaar.append('')
                del all_chaar[0:10]
                for dd in xx :
                    if dd in all_chaar :
                        detection.append('0')
                if '0' not in detection :
                    break
                else:
                    x2=input('enter a valid numbers')
                    xx = list(x2)
                    detection = []
            x2=int(x2)

            





            
        else:

            x1 =input('please enter your first number : ')
            xx = list(x1)
            detection = []
            while True:
                import string
                all_chaar=list(string.printable)
                all_chaar.append('')
                del all_chaar[0:10]
                for dd in xx :
                    if dd in all_chaar :
                        detection.append('0')
                if '0' not in detection :
                    break
                else:
                    x1=input('enter a valid numbers')
                    xx = list(x1)
                    detection = []
            x1=int(x1)
            
            x2 =input('please enter your second number : ')
            xx = list(x2)
            detection = []
            while True:
                import string
                all_chaar=list(string.printable)
                all_chaar.append('')
                del all_chaar[0:10]
                for dd in xx :
                    if dd in all_chaar :
                        detection.append('0')
                if '0' not in detection :
                    break
                else:
                    x2=input('enter a valid numbers')
                    xx = list(x2)
                    detection = []
            x2=int(x2)


            




            
        if x1 <21 and x2 <21 and x1!=x2 and x1 != 0 and x2 != 0 :

            if numbers_in_list[x1-1] !='*' and numbers_in_list[x2-1] !='*' :
                #print('we are here ')
                break
            else :

                # checkking_pc_problem
                time.sleep(0.3)
                print('pleaase enter valid numbers')
        else:
            # checkking_pc_problem
            time.sleep(0.3)
            print('pleaase enter valid numbers')
                # taking values from indexing
    #print(x1,x2)
    numbers_in_list[x1 - 1] = letter_list[x1 - 1]
    numbers_in_list[x2 - 1] = letter_list[x2 - 1]
   # checkking for equality
    if numbers_in_list[x1 - 1] == numbers_in_list[x2 - 1]:
       numbers_in_list[x1 - 1] = '*'
       numbers_in_list[x2 - 1] = '*'
       if detecting_player % 2 == 0 :
           p1=p1+1
       else:
           p2=p2+1
       print(''.join(numbers_in_list))
       # important for inatiolize the value
       neww = ''.join(numbers_in_list)
   # not equality case
    else:
        print(''.join(numbers_in_list))
       # intiolize the values to the the original values
    numbers_in_list[x1 - 1] = neww[x1 - 1]
    numbers_in_list[x2 - 1] = neww[x2 - 1]
    print('player 1:',p1,'' , 'player 2:', p2)
    detecting_player=detecting_player+1
    if p1 > 5:
       print('p1ayer 1  is the winnner')
       break
    elif p2 > 5:
        print('player 2  is the winnner')
        break
    elif p1 + p2 == 10:
        print('draw')
        break
    print('==========================')
