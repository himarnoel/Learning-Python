
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days* 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsuported units"


def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            my_var = days_to_units(
                user_input_number, days_and_unit_dictionary["units"])
            print(my_var)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid ")
    except ValueError:
        print("your input is not a number")


user_input_message = "Hey user, enter number of days and conversion: \n"
