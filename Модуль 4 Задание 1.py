import os

text = input()

def write_and_read(text):
    # YOUR CODE HERE
    file_path = os.path.join(os.path.abspath('/tmp'), 'my_file.txt')
    with open(file_path, 'w') as file:
        file.write(text)
    with open(file_path, 'r') as file:
        result = file.read()
    return result

print(write_and_read(text))