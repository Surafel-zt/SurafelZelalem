# The code must respond as correct or incorrect to questions
# The code must also give a second chance if the answer is incorrect
start = input("""
Read the following Scenario. If you understand the Scenario and want to continue enter Y.
If you do not understand the scenario and do not want to continue enter N.
There is 1 house between D and F. C is between E and G. F is neighbor of G.
There are two houses between A and G.
Who lives in the second corner? 
Who lives in the middle? 
Who lives between B and G? 
Who is the neighbor of A? 
How many houses are there between B and E?""")

if start == 'Y' or start == 'y':
    second_corner = input("Who lives in the second corner: ")
    if second_corner == 'D' or second_corner == 'd':
        print('correct!')
    elif second_corner != 'D' or second_corner != 'd':
        second_chance = input('Incorrect, Do you want a second chance, enter Y to continue or any key to exit: ')
        if second_chance == 'Y' or second_chance == 'y':
            second_corner = input("Who lives in the second corner: ")
            if second_corner != 'D' and second_corner != 'd':
                print('Good bye!')
                exit()
            else:
                print("Correct!")
        else:
            print('Good bye!')
            exit()
    else:
        print('Good bye!')
        exit()

    lives_in_middle = input("who lives in the middle?: ")
    if lives_in_middle == 'G' or lives_in_middle == 'g':
        print('correct!')
    elif lives_in_middle != 'G' or lives_in_middle != 'g':
        second_chance = input('Incorrect, Do you want a second chance, enter Y to continue or any key to exit: ')
        if second_chance == 'Y' or second_chance == 'y':
            lives_in_middle = input("who lives in the middle?: ")
            if lives_in_middle != 'G' and lives_in_middle != 'g':
                print('Good bye!')
                exit()
            else:
                print('correct!')
        else:
            print('Good bye!')
            exit()

    lives_between_B_and_G = input("Who lives between B and G?: ")
    if lives_between_B_and_G == 'F' or lives_between_B_and_G == 'f':
        print('correct!')
    elif lives_between_B_and_G != 'F' or lives_between_B_and_G != 'f':
        second_chance = input('Incorrect, Do you want a second chance, enter Y to continue or any key to exit: ')
        if second_chance == 'Y' or second_chance == 'y':
            lives_between_B_and_G = input("Who lives between B and G?: ")
            if lives_between_B_and_G != 'F' and lives_between_B_and_G != 'f':
                print('Good bye!')
                exit()
            else:
                print('correct!')
        else:
            print('Good bye!')
            exit()

    is_the_neighbor_of_A = input("Who is the neighbor of A?: ")
    if is_the_neighbor_of_A == 'E' or is_the_neighbor_of_A == 'e':
        print('correct!')
    elif is_the_neighbor_of_A != 'E' or is_the_neighbor_of_A != 'e':
        second_chance = input('Incorrect, Do you want a second chance, enter Y to continue or any key to exit: ')
        if second_chance == 'Y' or second_chance == 'y':
            is_the_neighbor_of_A = input("Who is the neighbor of A?: ")
            if is_the_neighbor_of_A != 'E' and is_the_neighbor_of_A != 'e':
                print('Good bye!')
                exit()
            else:
                print('correct!')
        else:
            print('Good bye!')
            exit()

    Num_of_houses_between_B_and_E = input("How many houses are there between B and E?: ")
    if Num_of_houses_between_B_and_E == '3':
        print('correct!')
        print('-------- You have answered all questions correctly --------')
    elif Num_of_houses_between_B_and_E != '3':
        second_chance = input('Incorrect, Do you want a second chance, enter Y to continue or any key to exit: ')
        if second_chance == 'Y' or second_chance == 'y':
            Num_of_houses_between_B_and_E = input("How many houses are there between B and E?: ")
            if Num_of_houses_between_B_and_E != '3':
                print('Good bye!')
                exit()
            else:
                print('correct!')
                print('-------- You have answered all questions correctly --------')
        else:
            print('Good bye!')
else:
    print("Good bye!")
