user_input = input("want to run the program : ")

def input_check(user_input: str) -> None:
    if user_input in ("", None):
        raise ValueError("'user_input' nothing passed")
    elif user_input.strip().lower() not in ("yes", "no"):
        raise ValueError("'user_input' bad value")
    return None

input_check(user_input)

while user_input.strip().lower() == "yes":
    print("program running")
    user_input = input("still want to run the program : ")
    input_check(user_input)