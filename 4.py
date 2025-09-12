def solve_cryptarithmetic(equation):
    # Parse the equation
    left, right = equation.split('=')
    left1, left2 = left.split('+')
    
    # Get unique letters
    letters = set(left1 + left2 + right)
    
    # Try all possible assignments
    for i in range(10**(len(letters))):
        assignment = {}
        digits = [int(d) for d in str(i).zfill(len(letters))]
        for j, letter in enumerate(letters):
            assignment[letter] = digits[j]
        
        # Check if the assignment is valid
        if assignment[left1[0]] == 0 or assignment[left2[0]] == 0 or assignment[right[0]] == 0:
            continue
        
        # Calculate the values
        left1_value = sum(assignment[letter] * 10**i for i, letter in enumerate(reversed(left1)))
        left2_value = sum(assignment[letter] * 10**i for i, letter in enumerate(reversed(left2)))
        right_value = sum(assignment[letter] * 10**i for i, letter in enumerate(reversed(right)))
        
        # Check if the equation holds
        if left1_value + left2_value == right_value:
            return assignment
    
    return None

# Example usage
equation = "SEND+MORE=MONEY"
solution = solve_cryptarithmetic(equation)
if solution:
    print("Solution found:")
    for letter, value in solution.items():
        print(f"{letter} = {value}")
else:
    print("No solution found")
