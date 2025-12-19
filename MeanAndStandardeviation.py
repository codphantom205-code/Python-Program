import numpy as np
try:
    user_input = input("Enter numbers separated by spaces: ")
    user_numbers = list(map(float, user_input.strip().split()))
    user_array = np.array(user_numbers)

    mean_user = np.mean(user_array)
    std_user = np.std(user_array)

    print("User Array:", user_array)
    print("Mean :", mean_user)
    print("Standard Deviation :", std_user)
except ValueError:
    print("Invalid input. Please enter numbers only.")
