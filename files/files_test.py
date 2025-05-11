import typing

class ReadFiles:
    def __init__(self, path:str, mode:str) -> None:
        self.path = path
        self.mode = mode

    def read_files(self) -> typing.Union[int, str]:
        if self.mode == 'r':
            my_file = open(self.path, self.mode)
            my_data = my_file.read()
            my_file.close()
            return my_data
        elif self.mode == 'w':
            data = input("Enter : ")
            my_file = open(self.path, self.mode)
            my_data = my_file.write(data)
            my_file.close()
            return my_data

user_path = input("Enter path, mode of the file to be processed : ")
user_path = user_path.split(',')

file_ops = ReadFiles(user_path[0], user_path[1])

my_file = file_ops.read_files()
print(my_file)

