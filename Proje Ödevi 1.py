#220501009 Betül Canol
#220501001 Hatice Reyhan Çalışkan 

import tkinter as tk
from tkinter import simpledialog
from tkinter import font
import sys

# 1st function (finding the x. smallest element of given list)
def x_smallest_element(x, lst):
    try:
        x = int(x)
    except ValueError:
        return None
    
    if x <= 0 or x > len(sorted(lst)): # error handling here
        return None 
    
    sorted_list = sorted(lst)
    result = sorted_list[x - 1]
    return result

# 2nd function (finding the closest pair)
def closest_pairs_to_x(x, lst):
    closest_sum = float('inf')
    result = None

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            current_sum = lst[i] + lst[j]

            if abs(x - current_sum) < abs(x - closest_sum):
                closest_sum = current_sum
                result = (lst[i], lst[j])

    return result

# 3rd function (finding repeating elements in a list)
def repeating_elements(lst):
    element_count = {}
    repeating_elements = []

    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    for element, count in element_count.items():
        if count > 1:
            repeating_elements.append(element)

    return repeating_elements

# 4th function (matrix multiplication)
def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        return "Matrices cannot be multiplied. Inner dimensions must match."

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            result[i][j] = sum([A[i][k] * B[k][j] for k in range(len(A[0]))])
    
    return result

# 5th function (word frequency)
def word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            words = text.split()
            result_word_frequency = {}

            for word in words:
                word = word.lower()
                word = word.strip('.,!?;:"()[]{}')  # clear the chars

                if word:
                    if word in result_word_frequency:
                        result_word_frequency[word] += 1  # if the word is not in the list
                    else:
                        result_word_frequency[word] = 1  # if the word is already in the list

        if result_word_frequency:
            sorted_word_frequency = sorted(result_word_frequency.items(), key = lambda x: x[1])

            output_str = "Word frequency analysis results (sorted from smallest to largest):\n"
            for word, count in sorted_word_frequency:
                output_str += f"The word '{word}' has been used {count} times.\n"
            return output_str
        else:
            return "No words were found in the text."
    except FileNotFoundError:
        return f"No file found with the name '{file_path}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# 6th function (finding the smallest value in the list)
def smallest_value(lst):
    if not lst:
        return None

    if len(lst) == 1:
        return lst[0]

    smallest = smallest_value(lst[1:])

    if lst[0] < smallest:
        return lst[0]
    else:
        return smallest

# 7th function (squareroot babylon) 
def sqrt(N, x0):
    if x0 < N and x0 > 0:
        tol = 1e-10 # fault tolerance "10^(-10)" can also be expressed this way "1e-10","0.0000000001
        maxiter = 10 # maximum number of iterations is used to determine how many times a loop or algorithm will repeat (u can change that)

        for i in range(maxiter):
            xn = 0.5 * (x0 + N / x0)
            error = abs(xn * xn - N)
             # loop as much as maxiter 
             # because if the tolerance level is too low for calculate to result or the initial estimate is chosen incorrectly 
             # (maybe even greater than the N), it will directly tell that the N value is incorrect
            if error < tol:
                return xn # return the result when it is acceptable (acceptable = if error < tol)

            x0 = xn # if an acceptable result is still not given, replace our first guess with the last number and continue the loop

        return f"{maxiter} No result was reached in the iteration. Increase max iteration."
    return "N and x0 must satisfy 0 < x0 < N"

# 8th function (greatest common divisor)
def greatest_common_divisor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return greatest_common_divisor(num2, num1 % num2)

# 9th function (prime number checker)
def prime_or_not(number):
    if number < 2: # the given number is not prime if it is less than two or negative
        return False
    i = 2 # this part starts checking the numbers to be given after two, we skipped the check three cuz three is already prime
    while i*i <= number:
        if number % i == 0:
            return False
        i = i + 1 
    return True

# 10th function (faster fibonacci)
def fibonacci(n, k, fibk, fibk1):
    if n < 0:
        return "Invalid input. The number 'n' cannot be negative."

    if n < 2:
        result = fibk if k == n else fibk1 if k == n - 1 else "Invalid input. The number 'k' should be less than or equal to 'n'."
        return result

    while k < n:
        fibk, fibk1 = fibk + fibk1, fibk
        k += 1

    return fibk 


#EXECUTE FUNCTIONS
# execute 1 
def execute_1():
    x = simpledialog.askinteger("Input", "Enter the x: ")
    lst = simpledialog.askstring("Input", "Enter a list (comma-separated): ")

    try:
        if x is None:
            raise ValueError("Invalid input. Please enter a valid value for x.")

        if x <= 0:
            raise ValueError("x must be a positive integer")

        if not lst.strip("[]"):
            raise ValueError("Invalid input. List cannot be empty.")

        lst_list = [int(item.strip()) for item in lst.strip("[]").split(',') if item.strip()]
        
        if not lst_list:
            raise ValueError("Invalid input. List cannot be empty.")

        result = x_smallest_element(x, lst_list)
        
        if result is not None:
            output_label.config(text = f"The {x}th smallest number in the list {lst_list} is: {result}")
        else:
            output_label.config(text = "Invalid input. List cannot be smaller than x.")
    except ValueError as e:
        error_message = f"Error: {str(e)}"
        output_label.config(text = error_message)

# execute 2
def execute_2():
    x = simpledialog.askinteger("Input", "Enter x: ")
    lst = simpledialog.askstring("Input", "Enter a list (comma-separated): ")

    try:
        lst = lst.strip('[]')
        lst_list = [int(item.strip()) for item in lst.split(',') if item.strip()]
        
        if len(lst_list) < 2:
            output_label.config(text = "At least two elements are needed for a pair.")
            return

        result = closest_pairs_to_x(x, lst_list)

        if result:
            output_label.config(text = f"The closest pair to {x} is {result}.")
        else:
            output_label.config(text = f"No pair found with the closest distance to {x}.")
    except ValueError:
        output_label.config(text = "Invalid input. Please enter valid parameters.")

# execute 3
def execute_3():
    lst = simpledialog.askstring("Input", "Enter a list (comma-separated, with or without square brackets): ")

    if lst is not None:
        lst = lst.strip('[]')
        lst = lst.replace(" ", "")
        elements = lst.split(',')
        try:
            lst_list = [int(item) for item in elements if item]
            result = repeating_elements(lst_list)

            if result:
                output_label.config(text = f"The repeating elements in the list [{lst}] are: {result}")
            else:
                output_label.config(text = "No repeating elements found.")
        except ValueError:
            output_label.config(text = "Invalid input. Please enter valid parameters.")
    else:
        output_label.config(text = "No input provided.")

# execute 4
def execute_4():
    while True:
        matrix1_str = simpledialog.askstring("Input", "Enter the first matrix ( format ex: [[x, y, z],[a, b, c]] ): ")
        matrix2_str = simpledialog.askstring("Input", "Enter the second matrix ( format ex: [[x, y], [a, b], [j, k]]: ")

        if matrix1_str is None or matrix2_str is None:
            output_label.config(text = "Input is missing. Please enter valid matrices.")
            return

        try:
            # evaluate the input strings to obtain matrices
            matrix1 = eval(matrix1_str)
            matrix2 = eval(matrix2_str)

            if not isinstance(matrix1, list) or not isinstance(matrix2, list):
                raise ValueError("Invalid input. Please enter valid matrices.")

            # check if the matrixes are multiplicapable (?)
            if len(matrix1[0]) != len(matrix2):
                raise ValueError("Matrix dimensions do not match. First matrix columns must be equal to the second matrix rows.")

            result = matrix_multiplication(matrix1, matrix2)

            # this prepares strings for A, B, and the result
            matrix1_str = "\n".join([str(row) for row in matrix1])
            matrix2_str = "\n".join([str(row) for row in matrix2])
            result_str = "\n".join([str(row) for row in result])

            output_label.config(text = f"Matrix A:\n{matrix1_str}\n\nMatrix B:\n{matrix2_str}\n\nResult:\n{result_str}") #display A B Result
            break  # if the input is invalid 
        except ValueError as e:
            output_label.config(text = f"Invalid input. Error: {str(e)}")

# execute 5
def execute_5():
    file_path = simpledialog.askstring("Input", "Enter the file path: ")

    try:
        result = word_frequency(file_path)
        output_label.config(text = result)
    except Exception as e:
        output_label.config(text = f"An error occurred: {str(e)}")

# execute 6
def execute_6():
    lst = simpledialog.askstring("Input", "Enter a list of integers (e.g., [1, 2, 3]): ")

    try:
        if '[' in lst and ']' in lst:
            lst_content = lst[lst.index('[') + 1:lst.index(']')]
            lst_list = [int(item.strip()) for item in lst_content.split(',') if item.strip()]
        else:
            lst_list = [int(item.strip()) for item in lst.split(',') if item.strip()]
        
        if not lst_list:
            output_label.config(text = "The list is empty. Please enter a list of integers.")
        else:
            result = smallest_value(lst_list)
            output_label.config(text = f"The smallest value in the list {lst} is: {result}")
    except ValueError:
        output_label.config(text = "Invalid input. Please enter a valid list of integers.")

# execute 7
def execute_7():
    N = simpledialog.askfloat("Input", "Enter N: ")
    x0 = simpledialog.askfloat("Input", "Enter the initial estimate (x0): ")

    result = sqrt(N, x0)

    if isinstance(result, str):  # this checks if the result is a string !
        output_label.config(text = result)
    else:
        output_label.config(text = f"Square root of {N} is approximately: {result}")

# execute 8
def execute_8():
    num1 = simpledialog.askinteger("Input", "Enter the first number: ")
    num2 = simpledialog.askinteger("Input", "Enter the second number: ")

    if num1 is not None and num2 is not None:
        result = greatest_common_divisor(num1, num2)
        output_label.config(text = f"The greatest common divisor of {num1} and {num2} is: {result}")
    else:
        output_label.config(text = "Invalid input. Please enter valid numbers.")

# execute 9
def execute_9():
    number = simpledialog.askinteger("Input", "Enter a number: ")
    if number is not None:
        result = prime_or_not(number)
        output_label.config(text = f"The number {number} is prime: {result}")
    else:
        output_label.config(text = "Invalid input. Please enter a valid number.")

# execute 10
def execute_10():
    n = simpledialog.askinteger("Input", "Enter n (the index of the fib num): ")
    k = simpledialog.askinteger("Input", "Enter k (the starting index): ")
    fibk = simpledialog.askinteger("Input", "Enter F(k) (kth fib num): ")
    fibk1 = simpledialog.askinteger("Input", "Enter F(k-1) ((k-1)th fib num): ")
    
    if n is not None and k is not None and fibk is not None and fibk1 is not None:
        result = fibonacci(n, k, fibk, fibk1)
        output_label.config(text = f"Fib({n}) = {result}") 
    else:
        output_label.config(text = "Invalid input. Please enter valid numbers.")


# MAIN MENU
def main_menu():
    global output_label  # declare output_label as a global variable !!
    functions = [
        ("Xth Smallest Element", execute_1),
        ("Closest Pairs to X", execute_2),
        ("Repeating Elements in a List", execute_3),
        ("Matrix Multiplication", execute_4),
        ("Word Frequency", execute_5),
        ("Smallest Value in a List", execute_6),
        ("Babylon Square Root", execute_7),
        ("Greatest Common Divisor", execute_8),
        ("Prime Number Checker", execute_9),
        ("Faster Fibonacci", execute_10),
        ("Exit", sys.exit)
    ]

#INTERFACE LOOK
    menu_window = tk.Tk()
    menu_window.title("Console")
    menu_window.geometry("800x700")  # window size

    # bg colour for the whole win
    menu_window.configure(bg = "light pink")

    # button bg
    button_frame = tk.Frame(menu_window, bg = "#a6a8ea")  #button bg colour
    button_frame.pack(side = "left", fill = "both", expand = True)

    output_label = tk.Label(menu_window, text = "", width = 80, height = 10, bg = "#8eb9f5", font = ("Consolas", 20)) # output bg colour
    output_label.pack(side = "right", fill = "both", expand = True)

    for i, (function_name, function_handler) in enumerate(functions):
        button = tk.Button(button_frame, text = function_name, width = 25, height = 2, command = function_handler, bg = "light blue")
        button.pack(side = "top", pady = 10, anchor = "n")
        button.pack_configure(anchor = "center")  # center the button horizontally

    
    button_frame.pack_propagate(True)  # enable frame auto-resizing
    button_frame.pack(side = "left", fill = "both", expand = True, padx = 10) # center the buttons vertically by adding padding at the top and bottom

    menu_window.mainloop()

main_menu()