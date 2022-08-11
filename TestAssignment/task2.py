#Recursive super digit function
def super_digit(input_number):
    # Type check for input 
    if type(input_number) is not int or input_number < 0 : return "Invalid Input"

    #break statement
    if  input_number < 10 : return input_number
    #recursion
    else:
        input_numbers_list = [int(x) for x in list(str(input_number))] # type conversion comphered list
        input_number = sum(input_numbers_list)
        return super_digit(input_number)
    