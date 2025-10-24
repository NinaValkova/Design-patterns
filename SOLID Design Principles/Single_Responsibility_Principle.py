#single responsibility principle - class should have a single reason to change

# journal primary responsibility is to keep the entries
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
        
    def remove_entry(self, pos):
        del self.entries[pos]        
    
    def __str__(self):
        return '\n'.join(self.entries)    

# separation of concerns
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w') 
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I cried today.')
j.add_entry("I ate a bug.")

file = r'C:\Users\Lenovo\Desktop\Design patterns\SOLID Design Principles/journal.txt'
PersistenceManager.save_to_file(j, file)

# Why use with open(...)?
# It’s the recommended way to work with files in Python.
# You don’t need to call fh.close() manually.
# fh.read() Reads the entire file at once as a single string.
with open(file) as fh:
    print(fh.read())
    
    
    
    