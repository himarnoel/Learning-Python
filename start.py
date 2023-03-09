import helper
user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, enter number of days and conversion:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {
        "days": days_and_unit[0],
        "units": days_and_unit[1]
    }
   
    helper.validate_and_execute(days_and_unit_dictionary)
