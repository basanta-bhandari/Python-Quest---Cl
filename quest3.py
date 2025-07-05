
def prime_checker(n):
    if n < 2:
        return False
    
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False

# Testing the function
print(f"22 is {prime_checker(22)}")  # Should print False
print(f"23 is {prime_checker(23)}")  # Should print True
print(f"2 is {prime_checker(2)}")   # Should print True
print(f"1 is {prime_checker(1)}")   # Should print False      
v=int(input("Again enter an number:"))
print(f"{v} is {prime_checker(v)}")


