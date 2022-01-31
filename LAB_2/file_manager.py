class FileManager:
    def __init__(self,file_name):
        self.file_name=file_name
    def read_file(text_data):
        f = open(text_data, 'r')
        file_contents = f.read()
        print(file_contents)
        f.close()
    def update_file(text_data):
        f = open(text_data, "a")
        f.write("test")
        f.close()