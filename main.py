too_much_problems= "The number of problems can't be more than 5."
too_much_digits= "The number can only contain 4 digits."
wrong_operator= "The operator can only be '+' or '-'."
only_digits= "The input can only be digits."
arranged_problems= ""
def arithmetic_formatter (problems, val= False):
    operator= list(map(lambda x: x.split()[1], problems))
    numbers= []
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all (list(map(lambda i: i.isdigit(), numbers))):
        print("The input can only be digits.")
        return (only_digits)

    elif not all (list(map( lambda i: len(i)< 4, numbers))):
        print("The number can only contain 4 digits.")
        return(too_much_digits)

    elif (len(problems)>5):
        print("The number of problems can't be more than 5.")
        return(too_much_problems)

    elif set(operator)!= {"+", "-"} and len(set(operator)!= 2):
        print("The operator can only be '+' or '-'.")
        return(wrong_operator)
    first_line= ""
    dashes= ""
    results= list(map(lambda x: eval(x), problems))
    solutions= ""
    for i in range (0, len(numbers), 2):

        space_width= max(len(numbers[i]), len(numbers[i+1]))
        space_width+=2

        first_line += numbers [i].rjust(space_width)

        dashes+= "-"* space_width
        solutions += str(results[i // 2]).rjust(space_width)
        if i != len(numbers)-2:
            first_line += " "* 4
            dashes+= " "* 4
            solutions+= " "* 4
    second_line= ""
    for i in range(1, len(numbers), 2):
        space_width= max(len(numbers[i]), len(numbers[i-1]))
        space_width += 1
        second_line+= operator[i//2]
        second_line+= numbers[i].rjust(space_width)
        if i != len(numbers)-1:
            second_line+= " " * 4
    if val:
        arranged_problems = "\n".join((first_line, second_line, dashes, solutions))
    else:
        arranged_problems= "\n". join ((first_line, second_line,dashes))
    print(arranged_problems)
    return arranged_problems


arithmetic_formatter( ["34 + 53", "45 - 35", "345 + 34", "45 + 45"], val= True)


