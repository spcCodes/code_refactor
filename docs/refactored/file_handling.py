def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except OSError as e:
        raise ValueError(f"Error reading file: {e}")

def write_file(file_name: str, data: str) -> str:
    try:
        with open(file_name, 'w') as file:
            file.write(data)
            return "Write successful"
    except OSError as e:
        raise ValueError(f"Error writing to file: {e}")

if __name__ == "__main__":
    file_name = "example.txt"
    data = "This is a sample text for file handling in Python 2."

    write_result = write_file(file_name, data)
    print(write_result)

    read_result = read_file(file_name)
    print(read_result)