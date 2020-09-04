#In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks.
# The last person to take a stick wins. For example:

def make_move(sticks):
    if sticks > 3:
        if sticks % 4 == 1: return 1
        elif sticks % 4 == 0: return 2
        else : return 3
    else :
        return sticks


sticks = 21
Is_computer_step = True
next_stickers = 0

while sticks > 0 :

    next_stickers = make_move(sticks)

    if Is_computer_step:
        sticks = sticks - next_stickers
        print(f"Computer takes --> {next_stickers} {sticks}sticks left")
        Is_computer_step = False
    else:
        sticks = sticks - next_stickers
        print(f"Player  takes  --> {next_stickers} {sticks}sticks left")
        Is_computer_step = True
else :
    print(f"Computer win!") if  not Is_computer_step else print(f"Player win! REALLY")

