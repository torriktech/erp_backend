# 1. ValueError
# 2. TypeError
# 3. FileNotFoundError
# 4. Exception
# 5. ZeroDivisionError

def div(filename):
    try:
        file = open(filename, "r")
        print(file.readline())
        
    except FileNotFoundError as e:
        print(f'Error ->>> {e}')
    finally:
        print("exception triggger or not")

# a = 20
# b = "z" 
div("text.txt")