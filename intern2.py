# Word Counter Program in Python

def count_words(text):
    """
    This function counts the number of words in the input text.
    It uses the split() method to separate the words by whitespace and returns the length of the resulting list.
    """
    # Split the text into a list of words using whitespace as the delimiter
    words = text.split()
    
    # Return the number of words in the list
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    It includes error handling for invalid inputs.
    """
    try:
        # Display a welcoming message
        print("Welcome to the Word Counter Program!")
        
        # Get user input (text to count words)
        text_input = input("Please enter the text you want to count the words for: ")
        
        # Check if the input text is empty
        if not text_input.strip():
            raise ValueError("Input cannot be empty. Please provide a valid text.")
        
        # Call the count_words function to get the word count
        word_count = count_words(text_input)
        
        # Display the word count result to the user
        print(f"The number of words in the provided text is: {word_count}")
    
    except ValueError as e:
        # Handle invalid input errors and display the error message
        print(f"Error: {e}")
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    
    finally:
        # Optional: Goodbye message
        print("\nThank you for using the Word Counter Program!")

# Run the main function to start the program
if __name__ == "__main__":
    main()
