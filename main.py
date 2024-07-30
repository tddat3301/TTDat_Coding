# 1 Write code to print out the numbers 1 to 10:
def print_numbers_1_to_10():
    for i in range(1, 11):
        print(i)

# 2 Print out the numbers 1 to 10, but print 'a' instead if the number divisible by 2:
def print_numbers_with_a_for_2():
    for i in range(1, 11):
        if i % 2 == 0:
            print('a')
        else:
            print(i)

# 3 Print out the numbers 1 to 10, but print 'a' instead if the number divisible by 2 and print 'b' instead if the number divisible by 3:
def print_numbers_with_a_and_b():
    for i in range(1, 11):
        if i % 3 == 0:
            print('b')
        elif i % 2 == 0:
            print('a')
        else:
            print(i)

# 4 Print out the numbers 1 to 10, but print 'a' instead if the number divisible by 2, print 'b' instead if the number divisible by 3 and print 'ab' instead if the number divisible by both 2 and 3:
def print_numbers_with_a_b_ab():
    for i in range(1, 11):
        if i % 2 == 0 and i % 3 == 0:
            print('ab')
        elif i % 3 == 0:
            print('b')
        elif i % 2 == 0:
            print('a')
        else:
            print(i)

# 5 Write a fuction which takes the input of a time in 24-hour format, and covers it to 12-hour format. Note: do not use a datetime library
def convert_to_12h(time_24h):
    # Split the time into hours and minutes
    hours, minutes = map(int, time_24h.split(':'))

    # Determine the period (AM/PM)
    period = 'AM' if hours < 12 else 'PM'

    # Convert hours from 24-hour to 12-hour format
    hours = hours % 12
    if hours == 0:
        hours == 12
    
    time_12h = f'{hours}:{minutes:02d} {period}'
    return time_12h

#Example usage
# a24 = '00:45'
# print(convert_to_12h(a24)) output 0:45 AM

def menu():
    while True:
        print("Menu:")
        print("1. Print numbers 1 to 10")
        print("2. Print numbers 1 to 10, but print 'a' instead if the number is divisible by 2")
        print("3. Print numbers 1 to 10, but print 'a' if divisible by 2 and 'b' if divisible by 3")
        print("4. Print numbers 1 to 10, print 'a' if divisible by 2, 'b' if divisible by 3, and 'ab' if divisible by both")
        print("5. Convert 24-hour time to 12-hour format")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print_numbers_1_to_10()
        elif choice == '2':
            print_numbers_with_a_for_2()
        elif choice == '3':
            print_numbers_with_a_and_b()
        elif choice == '4':
            print_numbers_with_a_b_ab()
        elif choice == '5':
            time_24h = input("Enter time in 24-hour format (HH:MM): ")
            print("12-hour format:", convert_to_12h(time_24h))
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()