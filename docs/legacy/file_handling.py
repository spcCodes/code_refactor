# file_handling.py

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            return data
    except IOError, e:
        return "Error reading file: {}".format(e)

def write_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
            return "Write successful"
    except IOError, e:
        return "Error writing to file: {}".format(e)

if __name__ == "__main__":
    file_name = "example.txt"
    data = "This is a sample text for file handling in Python 2."

    write_result = write_file(file_name, data)
    print write_result

    read_result = read_file(file_name)
    print read_result
