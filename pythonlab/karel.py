    if front_is_blocked():
        drop_beeper()
    else:    
        while front_is_clear():
            turn_left()
            if no_beepers_present():
                put_beeper()
            while front_is_clear():
                move()
                if no_beepers_present():
                    put_beeper()
            return_home()
            for i in range(4):
                move()
        turn_left()
        while front_is_clear():
            if no_beepers_present():
                put_beeper()
            move()
        turn_left()
        turn_left()
        while front_is_clear():
            move()
        turn_left()
