print("Recursive Printing")

# Design a recursive function that accepts an integer argument, n, and prints the numbers 1 up through n. 


#Function using recursion to print numbers from 1 to n
def recursive_print(n):

    # if n is less than or equal to zero, print "The End"
   if n <= 0:
     print("The End")
   else:
       print(n)
       recursive_print(n - 1)
       # 1 is subtracted from current number
 
 # Allows user to enter a random number
user_num = int(input("Enter a non-negative integer: "))
recursive_print(user_num)
# The recursive_print function is called with the number entered by user 

   