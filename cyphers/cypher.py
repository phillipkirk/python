def encrypt(input_string):
    # Function to encrypt a string
    print(f"\n Input: {input_string}")
    input_ascii = []
    # Convert characters to ASCII    
    for char in input_string:
        input_ascii.append(ord(char))

    output_ascii = []
    for num_in in input_ascii:
        # Exclude punctuation
        if num_in > 64 and num_in not in range(91, 96)  and num_in < 123:
            # Apply encryption to lower case letters
            if num_in in range(97, 123):
                num_out = num_in + 15
                if num_out > 122:
                     num_out = 96 + (num_out  - 122)
                output_ascii.append(num_out)
            # Apply encryption to upper case letters
            elif num_in in range(65, 91):
                num_out = num_in + 15
                if num_out > 90:
                     num_out = 65 + (num_out  - 90)
                output_ascii.append(num_out)
        # Pass punctuatiion through
        else:
            output_ascii.append(num_in)

    # Build output string
    output_string = ''
    for num in output_ascii:
        output_string +=chr(num)

    # Return strint to user
    print(f"Output: {output_string}\n")

def main():
    # Main program loop
    print("To exit enter 'quit'")
    while True:
        user_string = input("Please enter a string: ")
        while user_string.lower() != "quit":
            try:
                encrypt(user_string)
            except ValueError as e:
                print(e)
            break
        if user_string == "quit":
            break

main()
