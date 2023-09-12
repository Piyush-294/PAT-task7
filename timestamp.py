import datetime


def create_timestamp_file():
    # Get the current timestamp as a string
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Create a filename based on the current timestamp
    file_name = f'timestamp_{current_time}.txt'

    # Create and write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(current_time)


if __name__ == "__main__":
    create_timestamp_file()
    print("Timestamp file created successfully.")
