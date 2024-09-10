# Henry Roeser
# 09/10/24
# f-String Greeting Card 

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information for a greeting card you're making:

     - the first name of the person the greeting card is for 
     - the occasion (e.g., birthday, graduation, etc.) 
     - the custom message

3. Assign each piece of information collected to a variable with a short, specific name.



4. Use the `print( )` function  and an f-string to display your personalized greeting card on the screen.

'print()

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''
# Get the three pieces of info from the user
# Use the input ( ) function three times to do this
first_name = input("Enter the person's name: (Example:David)\n") 

occasion = input('Enter the occasion: (Example:Birthday\n')

custom_message = input('Enter the greeting message: (Example: Dear David, Have a happy birthday!\n')

# Build the greeting card using a Python f-string
# An f-string is like a fill-in-the-blank sentence in English
print(f"{first_name} is having a {occasion} party on Saturday! {custom_message}, {first_name}!")
