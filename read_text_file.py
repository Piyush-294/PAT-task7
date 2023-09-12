def read_text_file(file_name):

    try:
        # Attempt to open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Display the content to the console
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"File '{file_name}' not found.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Prompt the user to enter the name of the text file
    file_name = input("Enter the name of the text file: ")

    # Call the function to read and display the file content
    read_text_file(file_name)

