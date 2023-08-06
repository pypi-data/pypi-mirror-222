#!/usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/env python3
from time import sleep
from ANSIController import Terminal,_print

## more info `https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`

__author__ = 'JoOx01'
__desc__ = """Basic Python Module to control & color & style text in terminal"""

def main():
    t = Terminal()
    while True:
        _print(f"""-----------------------
{t.get_color('green',5)}{__desc__}{t.get_reset()}
-----------------------{t.get_color('yellow',5)}
╔═══╦═╗░╔╦═══╦══╦══╗
║╔═╗║║╚╗║║╔═╗╠╣╠╩╣╠╝
║║░║║╔╗╚╝║╚══╗║║░║║░
║╚═╝║║╚╗║╠══╗║║║░║║░
║╔═╗║║░║║║╚═╝╠╣╠╦╣╠╗
╚╝░╚╩╝░╚═╩═══╩══╩══╝{t.get_reset()}
-----------------------
by {t.get_color('red',1)}{__author__}{t.get_reset()}
-----------------------
[1] Print ALL Colors
[2] Print ALL Styles
[3] Print Colors With Styles
[4] Print IDs
[5] Print All
[6] X O   # soon 
[7] Snake # soon
[8] Move Game
[9] Colorize Text
[10] Clear Screen
[11] Progress
[-1] End
-----------------------
>>> 
-----------------------""")
        t.force_move_to_up()
        t.move_to_left(50)
        # t.move_to_up(start_line=True)
        choice = str(input(">>> "))
        if choice == "1":
            t.print_colors()
            input()
        if choice == "2":
            t.print_styles()
            input()
        if choice == "3":
            t.print_colors_styles()
            input()
        if choice == "4":
            t.print_id_colors()
            input()
        if choice == "5":
            t.print_test()
            input()
        if choice == "8":
            t.game(60,60,2)
        if choice == "9":
            text = str(input(f"Text `[your_color_code]`: {t.get_color('green')}"))
            t.get_reset()
            t.print_colorize(text)
            input()
        if choice == "10":
            t.clear_screen()
        if choice == "11":
            t.move_to_down(1)
            max_value = int(input("Max Value: "))
            increase = int(input("Increase Value: "))
            texts = []
            c = 1
            _print("[Rules] %c% current , %m% max , %p% percent , %b% bar\n")
            while True:
                txt = str(input(f"Text Progress Line ({c}) [-1 To End] : "))
                if txt == "-1":
                    break
                texts.append(txt)
                c+=1
            t.add_progress(texts,max_value,increase)
            while not t.is_progress_finish():
                t.increase_progress(all=True)
                c = 0
                for text in texts:
                    t.set_progress_inc_value(10+c,c,False)
                    c+=1
                t.print_progress()
                sleep(.2)
        if choice == '-1':
            t.clear_line()
            _print("\nThx For Using Bye\n")
            break
if __name__ == '__main__':
    try:
        main()
    except:
        pass