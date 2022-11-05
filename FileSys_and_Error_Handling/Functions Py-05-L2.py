def returned_list(first, second):
    return [first, second]

def returned_dict(first, second):
    return {first: second}

def returned_tup(first, second):
    return (first, second)

def returned_none(first, second):
    return first, second

def main():
    first_val = input("Please enter a value: ")
    second_val = input("Please enter another value: ")
    list_res = returned_list(first_val, second_val)
    dict_res = returned_dict(first_val, second_val)
    tup_res = returned_tup(first_val, second_val)
    none_res = returned_none(first_val, second_val)
    print(f"{} and its type is: {}") (list_res, type(list_res))
    print(f"{} and its type is: {}") (dict_res, type(dict_res))
    print(f"{} and its type is: {}") (tup_res, type(tup_res))
    print(f"{} and its type is: {}") (none_res, type(none_res))

main()
