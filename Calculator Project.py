def calculator():
    while True:
        print("\n")
        first_input = input("Please enter your first number (or type 'exit' to quit): ")
        if first_input.lower() == "exit":
            return False
        try:
            num1 = float(first_input)
            second_input = input(
                "Please enter your second number (or type 'exit' to quit): "
            )
            if second_input.lower() == "exit":
                return False
            num2 = float(second_input)
        except ValueError as ERROR:
            print("Invalid number input\n")
            print(ERROR)
            print("\nTry again")
            continue
        opp = input("Please enter your operation +-*/   ")
        if opp == "+":
            answer = num1 + num2
        elif opp == "-":
            answer = num1 - num2
        elif opp == "*":
            answer = num1 * num2
        elif opp == "/":
            try:
                answer = num1 / num2
            except ZeroDivisionError as ERROR:
                print("Invalid equation\n")
                print(ERROR)
                print("\nTry again")
                continue

        else:
            print("Invalid operation\nTry again")
            continue

        print(f"answer is {answer}")
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != "yes":
            break


while True:
    if not calculator():
        break
