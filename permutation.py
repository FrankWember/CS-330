# Tower of Hanoi Recursive Function

def tower_of_hanoi(n, source, target, auxiliary, step):
    """
    Function to solve the Tower of Hanoi problem.
    :param n: Number of disks
    :param source: The source peg
    :param target: The target peg
    :param auxiliary: The auxiliary peg
    :param step: List holding the step counter
    """
    if n == 1:
        step[0] += 1
        return
    else:
        # Move n-1 disks from source to auxiliary
        tower_of_hanoi(n - 1, source, auxiliary, target, step)
        
        # Move nth disk from source to target
        step[0] += 1
        
        # Move n-1 disks from auxiliary to target
        tower_of_hanoi(n - 1, auxiliary, target, source, step)


# Main program to test the Tower of Hanoi function for values of n from 3 to 35
if __name__ == "__main__":
    for num_of_disks in range(3, 36):  # Loop from 3 to 35 disks
        # Using a list to store step count as a mutable reference
        step = [0]
        
        # Function call
        tower_of_hanoi(num_of_disks, 'A', 'C', 'B', step)
        
        # Print the number of steps for the current number of disks
        print(f"Number of disks: {num_of_disks}, Total steps: {step[0]}")
