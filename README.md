# D-Hondt-Method
This is one of the 3 tasks that we were given in one of my first-year subject.

We had to create a program that obtains the elections result using the D'Hondt Method. The user has to give the info like this:
(Endor,etc are examples of territories and A,B,C,etc are examples of parties) 
{’Endor’: {’mandates’: 7, ’votes’: {’A’:12000, ’B’:7500, ’C’:5250, ’D’:3000}},
 ’Hoth’: {’mandates’: 6, ’votes’: {’B’:11500, ’A’:9000, ’E’:5000, ’D’:1500}},
 ’Tatooine’: {’mandates’: 3,’votes’: {’A’:3000, ’B’:1900}}}

It returns a list of tuples sorted by the number of mandates and in case of a tie by number of votes, each tuples contains the party name, their mandates and their votes.
