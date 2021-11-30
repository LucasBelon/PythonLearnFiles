def save_to_file(content, filename):
    with open(filename,'w') as file:
        file.write(content)
        del file
def read_file(filename):
    with open(filename,'r') as file:
        return file.read()

print('__name__ do file_operations.py: ', __name__)