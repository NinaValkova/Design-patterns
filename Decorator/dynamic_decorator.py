# FileWithLogging wraps a real file object
# Decorator / Wrapper pattern for Python file objects.
class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    def __iter__(self):
        return self.file.__iter__()

    # iter  allows:
    #     for line in file:
    #      ...
    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, item):
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):  # Forward attribute assignments
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.file, key, value)

    def __delattr__(self, item):  # Forward attribute deletion
        # del file.some_attribute - delete the attribute from the real file object, not the wrapper
        delattr(self.__dict__["file"], item)
        # The delattr(object, attribute) function will delete the specified attribute from the specified object.


if __name__ == "__main__":
    file = FileWithLogging(open("hello.txt", "w"))
    file.writelines(["hello", "world"])
    file.write("testing")
    file.close()
