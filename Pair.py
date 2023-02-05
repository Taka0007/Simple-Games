




'''

    Royal Straight Flush (ok
    Straight Flush  (ok
    For of a Kind  (ok
    Full Housen  (ok
    Flush  (ok
    Straight  (ok
    Three of a Kind (ok
    Two Pair  (ok
    One Pair  (ok
    No Pair  (ok


    URL: https://bright777.com/texasholdem2


'''

'''
Number (mod 13)+1

    n%13==12:

         'K'

     n%13==11:

         'Q'

     n%13==10:

         'J'


        その他
    
        K = (n%13) + 1


    マーク

     n//13==0:

     　 '♡' 

     n//13==1:

         '♦' 

     n//13==2:

         '♣' 


        others

         '♠'

'''

import collections
import Cards




Hand_list = ['Royal Straight Flush','Straight Flush','For of a Kind','Full Housen','Flush','Straight',
              'Three of a Kind','Two Pair','One Pair','No Pair']




def Pair(card):


    mark   = [n//13 for n in card]
    number = [n%13  for n in card]
    c = collections.Counter(number)

    mark.sort()
    number.sort()



    num_mark            = len(set(mark))

    values, number_kind = zip(*c.most_common())




    if num_mark==1 and number==[12,11,10,9,1]:

        Hand = 'Royal Straight Flush'


    elif num_mark==1 and len(number_kind)==5 and number[0]-number[4]==5:

        Hand = 'Straight Flush'


    elif len(number_kind)==2 and number_kind[0]==4:

        Hand = 'For of a Kind'


    elif len(number_kind)==2:

        Hand = 'Full House'


    elif num_mark==1:

        Hand = 'Flush'


    elif  len(number_kind) == 5 and number[0]-number[4]==5:


        Hand = 'Straight'


    elif len(number_kind) == 3 and number_kind[0]==3 :

        Hand = 'Three of a Kind'


    elif len(number_kind)==3 and number_kind[0]==2 and number_kind[1]==2:


        Hand = 'Two Pair'


    elif len(number_kind)==4:


        Hand = 'One Pair'


    else:

        Hand = 'No Pair'



    return Hand






    




    


    



    


    


    
