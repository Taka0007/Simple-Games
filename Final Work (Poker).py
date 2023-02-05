# Author: Takahiro Namatame
# Date: 2021.12.16



# import

import random
import numpy as np
import Cards as Ca
import Pair  as P
import tkinter as tk


'''

  Memo about cards definition
  
  Prepare  0-52  Number

  Use  zip()  to make pare of  mark and number??

   0-12  ♡
  13-25  ♦
  26-38  ♣
  39-51  ♠         (mod 13) + 1    is the Card's Number


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


        その他

        S= '♠' 

  
'''




# Prepare Cards (52 Cards)

random_list = list(range(0,52))


# 20 Cards Choice ( Including exchange cards )

Selected_cards = random.sample(random_list , 20)


# Divid list into 4 parts

Split_list = list( np.array_split( Selected_cards , 4) )


Pre_Player_cards  =  Split_list[0] 
Pre_COM_cards     =  Split_list[1] 
Player_change     =  Split_list[2]
COM_change        =  Split_list[3]


Pre_Player_cards.sort()
Pre_COM_cards.sort()


#  Preparation of cards is finished




#print(Selected_cards)
#print(Pre_Player_cards)
#print(COM_cards)





# Player Cards

p1 = Ca.Card(Pre_Player_cards[0])
p2 = Ca.Card(Pre_Player_cards[1])
p3 = Ca.Card(Pre_Player_cards[2])
p4 = Ca.Card(Pre_Player_cards[3])
p5 = Ca.Card(Pre_Player_cards[4])


Player_cards = [p1,p2,p3,p4,p5]


#print( 'Player Cards', Player_cards)


# COM Cards

c1 = Ca.Card(Pre_COM_cards[0])
c2 = Ca.Card(Pre_COM_cards[1])
c3 = Ca.Card(Pre_COM_cards[2])
c4 = Ca.Card(Pre_COM_cards[3])
c5 = Ca.Card(Pre_COM_cards[4])

COM_cards = [c1,c2,c3,c4,c5]


COM_cards.sort()


#print( 'COM Cards' , COM_cards)


COM_Hand    = P.Pair(Pre_COM_cards)
Player_Hand = P.Pair(Pre_Player_cards)


#print(COM_Hand)
#print(Player_Hand)


#print( 'COM Cards' , COM_cards, COM_Hand)


#print( 'Player Cards', Player_cards,Player_Hand)




Hand_list = ['Royal Straight Flush','Straight Flush','For of a Kind','Full Housen','Flush','Straight',
              'Three of a Kind','Two Pair','One Pair','No Pair']




result_ = 'Now Loading….'




def result(A, B):


    COM_Hand_number    = Hand_list.index(A)

    Player_Hand_number = Hand_list.index(B)

    P_number = [n%13  for n in Pre_Player_cards]

    C_number = [n%13  for n in Pre_COM_cards]



    P_number.sort()
    C_number.sort()



    PCN = [n for n in set(P_number) if P_number.count(n)>1]

    CCN = [n for n in set(C_number) if C_number.count(n)>1]

    PCN.sort()
    CCN.sort()



    PCN.append(9999)
    CCN.append(9999)






    if COM_Hand_number > Player_Hand_number:


        result_ = 'YOU WIN!'


    elif COM_Hand_number < Player_Hand_number:

        result_ = 'YOU LOSE…'



    elif COM_Hand_number==Player_Hand_number and Player_Hand =='No Pair':

        result_ = 'DRAW'


    elif COM_Hand_number == Player_Hand_number  and  PCN[0]>CCN[0]:

        result_ = 'YOU WIN!'



    elif COM_Hand_number ==Player_Hand_number  and  PCN[0]<CCN[0]:


        result_ = 'YOU LOSE…'



    else:


        result_ = 'DRAW'



    return result_






#print(result())




result_ = result(COM_Hand, Player_Hand)



window = tk.Tk()

window.title = ('The Poker Game')





L_window = tk.Frame(window, padx=20, pady=10, bd=2, relief='raised', bg='greenyellow')

L_window.pack(side=tk.LEFT, fill=tk.BOTH)


R_window = tk.Frame(window, padx=20, pady=10, bd=2, relief='raised')

R_window.pack(side=tk.RIGHT, fill=tk.BOTH)



label1 = tk.Label(L_window, font='Times 18', bd = 1, relief = 'solid', text='COM')

hand1 = [tk.Label(L_window, bg = 'medium sea green', bd =1, relief ='solid', width=10, height=8, font='Times 12') for i in range(5)]

label2 = tk.Label(L_window, text='Poker', font='Times 24')

hand2 = [tk.Label(L_window, bg='medium sea green', bd=1, relief='solid', width=10, height=8, font='Times 12', text=Player_cards[i])for i in range(5)]

label3 = tk.Label(L_window, font='Times 18', bd=1, relief='solid', text='Player')




def Checked():


    for i in range(5):


        if isChecked[i].get():


            Ex['state'] = tk.NORMAL

            break


    else:


        Ex['state'] = tk.DISABLED
        

        
        
Alfa = ['A','B','C','D','E']

isChecked = [tk.BooleanVar() for i in range(5)]

check = [tk.Checkbutton(L_window, bg='white',text=Alfa[i], font='Times 12', variable=isChecked[i], command=Checked) for i in range(5)]


label1.grid(row=0, column=0, columnspan=5, pady=5)
label2.grid(row=2, column=0, columnspan=5)

label3.grid(row=5, column=0, columnspan=5, pady=5)



def Game(result_, COM_Hand_, Player_Hand_):


    for i in range(5):


        hand1[i].configure(text=COM_cards[i])


    label2.configure(text=result_)
    label1.configure(text=COM_Hand_)
    label3.configure(text=Player_Hand_)

    for i in range(5):
        check[i]['state'] = tk.DISABLED

    Game_button['state'] = tk.DISABLED
    Ex['state'] = tk.DISABLED



def newresult(A, B, C):

    New_COM_Hand     = A

    New_Player_Hand  = B

    Pre_Player_cards = C
    
    New_COM_Hand_number    = Hand_list.index(A)

    New_Player_Hand_number = Hand_list.index(B)

    New_P_number = [n%13  for n in Pre_Player_cards]

    New_C_number = [n%13  for n in Pre_COM_cards]



    New_P_number.sort()
    New_C_number.sort()



    PCN = [n for n in set(New_P_number) if New_P_number.count(n)>1]

    CCN = [n for n in set(New_C_number) if New_C_number.count(n)>1]

    PCN.sort()
    CCN.sort()



    PCN.append(9999)
    CCN.append(9999)






    if New_COM_Hand_number > New_Player_Hand_number:


        result_ = 'YOU WIN!'


    elif New_COM_Hand_number < New_Player_Hand_number:

        result_ = 'YOU LOSE…'



    elif New_COM_Hand_number == New_Player_Hand_number and New_Player_Hand =='No Pair':

        result_ = 'DRAW'


    elif New_COM_Hand_number == New_Player_Hand_number  and  PCN[0]>CCN[0]:

        result_ = 'YOU WIN!'



    elif New_COM_Hand_number == New_Player_Hand_number  and  PCN[0]<CCN[0]:


        result_ = 'YOU LOSE…'



    else:


        result_ = 'DRAW'



    return result_




def Exchange():

          

    for i in range(5):


        if isChecked[i].get():


            Pre_Player_cards[i] = Player_change[i]
            

            Player_cards[i] = Ca.Card(Pre_Player_cards[i])
            

            hand2[i].configure(text=Player_cards[i])


    New_Player_Hand = P.Pair(Pre_Player_cards)
        

    new_result = newresult(COM_Hand, New_Player_Hand, Pre_Player_cards)
        

    Game(new_result, COM_Hand, New_Player_Hand)


        

'''

p1 = Ca.Card(Pre_Player_cards[0])
p2 = Ca.Card(Pre_Player_cards[1])
p3 = Ca.Card(Pre_Player_cards[2])
p4 = Ca.Card(Pre_Player_cards[3])
p5 = Ca.Card(Pre_Player_cards[4])


Player_cards = [p1,p2,p3,p4,p5]


Player_cards.sort()




'''


Game_button = tk.Button(R_window, text='GAME!', font='Times 18', command=lambda: Game(result_, COM_Hand, Player_Hand))

Ex   = tk.Button(R_window, text='Exchange', font='Times 18', command=Exchange, state=tk.DISABLED)



for i in range(5):


    hand1[i].grid(row=1, column=i)

    hand2[i].grid(row=3, column=i)

    check[i].grid(row=4, column=i)



Game_button.pack(fill=tk.X, padx=2, pady=2)

Ex.pack(fill=tk.X, padx=2, pady=2)




window.mainloop()


'''

label    = tk.Label(window, text = COM_cards[0], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label2   = tk.Label(window, text = COM_cards[1], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label3   = tk.Label(window, text = COM_cards[2], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label4   = tk.Label(window, text = COM_cards[3], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label5   = tk.Label(window, text = COM_cards[4], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')

label6   = tk.Label(window, text = Player_cards[0], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label7   = tk.Label(window, text = Player_cards[1], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label8   = tk.Label(window, text = Player_cards[2], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label9   = tk.Label(window, text = Player_cards[3], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')
label10  = tk.Label(window, text = Player_cards[4], width = 6, height = 4, bg = 'green', fg='white', font='Times 17')

label11  = tk.Label(window, text = result,width = 11, height = 3, bg ='red', fg ='white',font='Times 19')


COM_Hand = tk.Label(window, text = COM_Hand, width =12, height =7, bg='red', fg='blue', font='Times 8')

Player_Hand =tk.Label(window, text=Player_Hand, width=12,height=7, bg='red',fg='blue',font='Times 8')


label .grid( row=1, column=0)
label2.grid( row=1, column=1)
label3.grid( row=1, column=2)
label4.grid( row=1, column=3)
label5.grid( row=1, column=4)

label6 .grid( row=3, column=0)
label7 .grid( row=3, column=1)
label8 .grid( row=3, column=2)
label9 .grid( row=3, column=3)
label10.grid( row=3, column=4)
label11.grid( row=2, column=0, columnspan=5)


COM_Hand.grid(row=0,column=2)
Player_Hand.grid(row=5,column=2)


window.mainloop()



'''












