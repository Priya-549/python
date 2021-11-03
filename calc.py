# CommandLineCalc

# ----------------
# Functions
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def power(a,b):
    return a**b

def mod(a,b):
    return a%b

# ----------------

if __name__ == "__main__":
    print("""
    Addition: 1
    Subtraction: 2
    Divide: 3
    Multiplication: 4
    Power: 5
    MOD: 6
    """)
    choice = int(input("Choice: "))

    a, b = input("values: ").split()
    if choice ==1: print(add(int(a),int(b)))
    if choice ==2: print(sub(int(a),int(b)))
    if choice ==3: print(div(int(a),int(b)))
    if choice ==4: print(mul(int(a),int(b)))
    if choice ==5: print(power(int(a),int(b)))
    if choice ==6: print(mod(int(a),int(b)))


