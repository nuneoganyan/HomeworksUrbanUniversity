calls = 0
def count_calls() :
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list) :
    count_calls()
    for i in list :
        i.casefold()
    if string.casefold() in list :
        return True
    else :
        return False
print(string_info("Nune"))
print(string_info("paruyr"))
print(is_contains("NuNe", ["nune", "Artur", "gayanE"]))
print(is_contains("paruyr", ["Nune", "Artur", "gayanE"]))
print(calls)