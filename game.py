
print("""                     Welcome to UVgames
      __________________________________________________
____________§§_____§§§___§§§____§§§___§________§§
______§__§___§_____§___§__§___§__§_______§__§
______§__§___§_____§___§__§___§__§_______§__§
______§__§____§§§___§§§____§§§___§§§§____§__§
_§§____§__§_____________________________§__§____§§
§__§___§__§_____________________________§__§___§__§
§___§__§__§_____________________________§__§__§___§
_§___§__§__§___________________________§__§__§___§
__§___§§§§§§§_________________________§§§§§§§___§
___§____§___§_________________________§___§____§
____§§§§_____§_______________________§_____§§§§
___§___§__§§_§_________§§§§§_________§_§§__§___§
___§___§__§__§_______§§_____§§_______§__§__§___§
____§§§§§§___§______§_________§______§___§§§§§§
____§___§___§_§____§__8____8___§____§_§___§___§
_____§§§___§___§___§___________§___§___§___§§§
________§§§§§___§_§_____________§_§___§§§§§
_____________§§__§§_§§§§§§§§§§§_§§__§§
_______________§__§_§__§___§__§_§__§
________________§_§_§__§___§__§_§_§
_________________§§_§__§___§__§_§§
__________________§§_§_§___§_§_§§
___________________§__§§$0n§§__§
____________________§__§§§§§__§
_____________________§§_____§§
_______________________§§§§§

__________________________________________________
""")
name=input("Please enter your name>>>")
print("You are a carpenter",name)
print("""Uv ｡◕‿‿◕｡ : My table top is broken, can you give me one?
                 
                      ┬──┬ ノ( ゜-゜ノ)
      
"""+name+""" (▀̿Ĺ̯▀̿ ̿) : sure, but can u provide me the dimensions?

Uv ｡◕‿‿◕｡ : No. I dont know about them, but I have broken piece with me, We can try matching with that.
TASK:>>
So, you dont know about the dimensions, the only thing you know is
'its a square with side ranging 1 to 100 units'.
RULES:>>
Remember steps are being counted
You are given 100pts every wrong guess deducts 10pts ¯\_(ツ)_/¯  """)
import random
true_side = random.randint(1,100)
Total = 100
chances = 10
for chance in range(1,11) :
    guess =int(input("Please enter your guess::"))
    if guess < true_side:
        def rectangle(symbol,length,breadth):
            global Total
            global chances
            if length >= 1 and breadth >= 1: 
                for _ in range(length):
                    if _ == 0 or _== (length-1):
                        print((symbol+" ")*breadth)
                    else:
                        print(symbol + " " * (2*(breadth-2)+1) + symbol)
        rectangle('O',guess,guess)
        Total= Total-10
        chances = chances - 1
        print("""           Uv: Yaikks!! you guessed wrong  ಠ╭╮ಠ), 
                it's too small""",name,"""
                                           Current Score:""",Total,
"\n                                           chances left are:",chances)
    elif guess > true_side:
        def rectangle(symbol,length,breadth):
            global Total
            global chances
            if length >= 1 and breadth >= 1: 
                for _ in range(length):
                    if _ == 0 or _== (length-1):
                        print((symbol+" ")*breadth)
                    else:
                        print(symbol + " " * (2*(breadth-2)+1) + symbol)
        rectangle('O',guess,guess)
        Total= Total-10
        chances = chances - 1
        print("""           Uv: Yaikks!! you guessed wrong  ಠ╭╮ಠ), 
           it's too big""",name,""".
                                           Current Score:""",Total,
"\n                                           chances left are:",chances)
    
    else:
        break
if guess == true_side:
    print("""Uv: We are Done""",name,""" （＊＾Ｕ＾）人（≧Ｖ≦＊）/

                       YOU WON!!  ヽ(^◇^*)/
000000000000000_000000000000000
00000000000000___00000000000000
0000000000000_____0000000000000
000000000000_______000000000000
00000000000_________00000000000
0____________ YOU ___________00
000_________ ........_________ 0000
00000 _______ROCK!!_______ 00000
0000000_________________0000000
000000_________0_________000000
00000_______0000000_______00000
0000_____0000000000000_____0000
000___0000000000000000000___000
00_0000000000000000000000000_00
8888888888888888888888888888888



Your score is""",Total)
    if Total==100:
        print("""You are a legend (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧    ╰(◡‿◡✿╰)""")
    elif Total < 100 and Total > 50:
        print("""You are a pro man!! ◃┆◉◡◉┆▷""" )
    else:
        print("""That's a low score (>‘o’)>
Better luck next time""")
else:
    print("""Uv: Damn man!You wasted. I think your guessing skills are nugatory.
          ___________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
__¶_¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶__¶__¶ 
__¶_¶__¶______¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶______¶_¶_¶ 
¶_¶_¶_¶______¶¶¶¶¶¶______¶¶¶¶______¶¶¶¶¶¶¶____¶¶¶¶¶ 
_¶¶¶¶¶______¶¶¶¶¶¶¶___O_¶¶¶¶¶__O__¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶___¶¶¶ 
____¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶ 
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶___¶ 
_____¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶ 
__________¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶ 
___________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶ 
____________¶¶________¶¶¶¶¶¶¶¶¶¶_______¶¶ 
_____________¶¶¶_______________________¶ 
_______________¶¶____¶¶¶¶¶¶¶¶¶¶¶______¶ 
________________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶ 
___________________¶¶¶_____¶¶¶¶¶¶¶¶¶¶ 
______________________¶¶¶¶¶__¶¶¶¶¶¶¶¶¶ 
_____________________________¶¶¶¶¶¶¶¶¶¶ 
______________________________¶¶¶¶¶¶¶¶¶

If you don't have guts, run away!!. otherwise, lets have one more try.You may proove me wrong.
""")
