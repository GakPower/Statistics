#
# Author: GakPower
#
# Date: 22-Feb-2018 (6:39 PM)
#

import texttable as tt
from math import log, ceil


def pos(number):  # Returns the position in string from the given number

    if number <= 0:
        raise ValueError("Invalid input! Only POSITIVE input is acceptable")
    elif number == 1:
        return "1st"
    elif number == 2:
        return "2nd"
    elif number == 3:
        return "3rd"
    else:
        return str(number) + "th"


def fill_lists(list_of_v, sum_, control_str):  # Creates f, f% and if needed the F and F% lists

    f_list, f_list_, num_of_x, count = [], [], len(list_of_v), 0

    if control_str == "F":  # F == Float

        N_list, F_list, F_list_ = [], [], []

        for i in range(num_of_x):
            count += list_of_v[i]
            N_list.append(count)
            # ================= Creating the f list =================
            f_list.append(round(list_of_v[i] / sum_, 2))
            # ================= Creating the f% list =================
            f_list_.append(round(f_list[i] * 100))
            # ================= Creating the F list =================
            F_list.append(round(N_list[i] / sum_, 2))
            # ================= Creating the F% list =================
            F_list_.append(round(F_list[i] * 100))

        result = [N_list, f_list, f_list_, F_list, F_list_]

    else:
        N_list = []

        for i in range(num_of_x):
            count += list_of_v[i]
            N_list.append(count)
            # ================= Creating the f list =================
            f_list.append(round(list_of_v[i] / sum_, 2))
            # ================= Creating the f% list =================
            f_list_.append(round(f_list[i] * 100))

        result = [N_list, f_list, f_list_]

    return result


def type_1():
    # ================= Initialization =================
    x_list, v_list, x, v_sum, input_type = [], [], 0, 0, " "

    # ================= Creating the x and v lists =================
    while True:

        xis = input("Enter " + pos(x + 1) + " x (Press \"Enter\" when done)" + input_type + ": ")

        if x == 0:
            try:
                xis = float(xis)
                input_type = " (NUMERIC)"
                str_gen_type = "NUMERIC"
            except ValueError:
                if xis == "":
                    pass
                else:
                    input_type = " (WORD)"
                    str_gen_type = "a WORD"
            finally:
                gen_type = type(xis)
                curr_type = gen_type

        else:
            try:
                xis = float(xis)
                str_curr_type = "NUMERIC"
            except ValueError:
                str_curr_type = "a WORD"
            finally:
                curr_type = type(xis)

# ================= Invalid Input Error Handling =================
        if curr_type != gen_type and xis != "":
            print("""
        +===================================================+
        | Invalid type of input!                            |
        |                                                   |
        | Based on your first input, the supported type for |
        | the current execution is                          |
        | {0} while your last entry is {1} !         |
        |                                                   |
        | Please enter an input with a valid type...        |
        +===================================================+
        """.format(str_curr_type, str_gen_type))
            continue
# ================================================================

        if xis != "":  # Checks if input is empty (User just pressed ENTER) if so it exit else create/add to lists

            if xis not in x_list:
                x_list.append(xis)
                v_list.append(1)
                x += 1
            else:
                position = x_list.index(xis)
                v_list[position] += 1
                x += 1
        else:
            if x == 0:
                print("""
                +==================================================================+
                |                                                                  |
                |                    Invalid EMPTY input!                          |
                |             Please try again with a valid one...                 |
                |                                                                  |
                +==================================================================+
                """)
                continue
            v_sum = sum(v_list)  # Calculates the v
            x_list, v_list = zip(*sorted(zip(x_list, v_list)))  # Sorts x and v lists based on x
            break

    if type(x_list[0]) == float:  # Checks for the type of input

        # ================= Filling lists =================
        N_list, f_list, f_list_, F_list, F_list_ = fill_lists(v_list, v_sum, "F")
        data_array = [x_list, v_list, N_list, f_list, f_list_, F_list, F_list_]
        name_array = ['Xi', 'vi', 'Ni', 'fi', 'fi%', 'Fi', 'Fi%']
        output(name_array, data_array, 'cm')
    else:

        # ================= Filling lists =================
        N_list, f_list, f_list_ = fill_lists(v_list, v_sum, "W")
        data_array = [x_list, v_list, N_list, f_list, f_list_]
        name_array = ['Xi', 'vi', 'Ni', 'fi', 'fi%']
        output(name_array, data_array, 'cm')


def type_2():
    # ================= Initialization =================
    x_list, v_list, x, v_sum, input_type = [], [], 0, 0, " "

    # ================= Creating the x and v lists =================
    while True:

        xis = input("Enter " + pos(x + 1) + " x (Press \"Enter\" when done): ")

        try:
            xis = float(xis)
        except ValueError:
            if xis != "":  # Non-numeric input error handling
                print("""
                +===================================================+
                | Invalid type of input!                            |
                |                                                   |
                | You are allowed to enter only numeric values!     |
                |                                                   |
                |                                                   |
                | Please enter an input with a numeric type...      |
                +===================================================+
                """)
                continue

        if xis != "":  # Checks if input is empty (User just pressed ENTER) if so it exit else create/add to lists

            if xis not in x_list:
                x_list.append(xis)
                v_list.append(1)
                x += 1
            else:
                position = x_list.index(xis)
                v_list[position] += 1
                x += 1
        else:
            if x == 0:
                print("""
                +==================================================================+
                |                                                                  |
                |                    Invalid EMPTY input!                          |
                |             Please try again with a valid one...                 |
                |                                                                  |
                +==================================================================+
                """)
                continue
            v_sum = sum(v_list)  # Calculates the v
            x_list, v_list = zip(*sorted(zip(x_list, v_list)))  # Sorts x and v lists based on x
            break

    numofclasses = 1 if v_sum == 1 else int(ceil(log(v_sum, 2)))  # Calculates the number of classes
    intervalofclasses = ceil((max(x_list) - min(x_list)) / numofclasses)  # Calculates the interval of classes

    # Initialization
    maxclasses = []
    temp = x_list[0]
    v_list_classes = [0 for _ in range(numofclasses)]

    # Creates a list with the limits of the classes
    for _ in range(numofclasses):
        temp += intervalofclasses
        maxclasses.append(temp)

    tempclasses = [(x_list[0], maxclasses[0])]  # Complete the list of limits

    for i in range(numofclasses-1):
        tempclasses.append((maxclasses[i], maxclasses[i+1]))

    classes = tuple(tempclasses)  # Convert list to tuple

    if v_sum != 1:
        for z in range(len(x_list)):
            for y in range(numofclasses):
                if z == len(x_list)-1:  # if it is the last item
                    if classes[y][0] <= x_list[z] < classes[y][1]:
                        v_list_classes[y] += v_list[z]
                elif classes[y][0] <= x_list[z] < classes[y][1]:
                    v_list_classes[y] += v_list[z]
    else:
        v_list_classes[0] = 1

    # ============================ Filling Lists ======================================
    N_list, f_list, f_list_, F_list, F_list_ = fill_lists(v_list_classes, v_sum, "F")
    data_array = [classes, v_list_classes, N_list, f_list, f_list_, F_list, F_list_]
    name_array = ['Xi', 'vi', 'Ni', 'fi', 'fi%', 'Fi', 'Fi%']
    output(name_array, data_array, 'cm')


def output(name_array, data_array, align):  # Creates the table of the Statistical info

    # Initialization
    tab, x, num_of_xs, num_of_data = tt.Texttable(), [[]], len(name_array), len(data_array[0])

    for i in range(num_of_data):
        x.append([data_array[h][i] for h in range(num_of_xs)])  # adds data to a new row

    tab.add_rows(x)  # adds rows with the above data

    tab.set_cols_align([align[0] for _ in range(num_of_xs)])  # horizontal alignment
    tab.set_cols_valign([align[1] for _ in range(num_of_xs)])  # vertical alignment

    tab.header(name_array)  # creating the header

    print("\n" * 100)  # Let empty space after the inputs
    print(tab.draw())
    print("\n" * 3)  # Let empty space after the output


if __name__ == "__main__":
    while True:

        Type = int(input("""
What type of input are you about to enter?

Enter the number representing the preferred type of input: 
1) Few numbers(no need for classification)
2) A lot of numbers different with each other(classification is needed)
\n==> """))

        if Type == 1:
            type_1()
            break
        elif Type == 2:
            type_2()
            break
        else:
            print("Invalid input!! Please TRY AGAIN...\n")

    input('Press ENTER to exit')
