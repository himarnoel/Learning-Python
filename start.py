
calulation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days*calulation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return


def validate_and_execute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print(my_var)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid ")
    except ValueError:
        print("your input is not a number")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, enter number of days and conversion:\n")
    days_and_unit = user_input.split(":")
    print(days_to_units)
    days_and_unit_dictionary = {
        "days": days_and_unit[0],
        "units": days_and_unit[1]
    }
    print(days_and_unit_dictionary)
    validate_and_execute()
