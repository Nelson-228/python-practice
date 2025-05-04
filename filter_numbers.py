for loop in range(1, 21): # Declaring loop as a variable, loop equals the range from 1-20
    if loop % 2 == 0: # (% used to see if there is a left over number, if so, it is odd and does not use the continue command. But if it shoots out a 0, meaning that the number is even, it skips that number, continuing the loop)
        continue
    if loop > 15: # If loop hits the number 15, it breaks the loop.
        break
    print(loop) # The reason why the print(loop) is inside is because we continue this process over and over until the loop breaks. If we place the print outside of this block of code, it only prints out a "17".