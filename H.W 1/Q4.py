import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
# game loop
POS_X = initial_tx
POS_Y = initial_ty
TARGET_X = light_x
TARGET_Y = light_y
while True:
    turn = ""
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if (POS_Y == TARGET_Y):  # for part 01
        if (POS_X < TARGET_X):
            turn = "E"
            POS_X += 1
        elif (POS_X > TARGET_X):
            turn = "W"
            POS_X -= 1

    if (POS_X == TARGET_X):  # for part 02
        if (POS_Y < TARGET_Y):
            turn = "S"
            POS_Y += 1
        elif (POS_Y > TARGET_Y):
            turn = "N"
            POS_Y -= 1

    if (POS_Y > TARGET_Y and POS_X < TARGET_X):  # for part 03
        turn = "NE"
        POS_Y -= 1
        POS_X += 1
    if (POS_Y > TARGET_Y and POS_X > TARGET_X):
        turn = "NW"
        POS_Y -= 1
        POS_X -= 1
    if (POS_Y < TARGET_Y and POS_X < TARGET_X):
        turn = "SE"
        POS_Y += 1
        POS_X += 1
    if (POS_Y < TARGET_Y and POS_X > TARGET_X):
        turn = "SW"
        POS_Y += 1
        POS_X -= 1

    ## A single line providing the move to be made: N NE E SE S SW W or NW
    print(turn)
