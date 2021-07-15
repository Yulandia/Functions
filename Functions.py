def function1():
    print('"More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"')
#list of benefits
list_benefits = [function1()]

def function2():
    print(' is a benefit of functions!')
#build a sentence
build_sentence = [function2()]

# Modify this function to return a list of strings as defined above


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


# Modify this function to concatenate to each benefit - " is a benefit of functions!"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()

    print(build_sentence(list_of_benefits[0]))

    print(build_sentence(list_of_benefits[1]))

    print(build_sentence(list_of_benefits[2]))

    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()