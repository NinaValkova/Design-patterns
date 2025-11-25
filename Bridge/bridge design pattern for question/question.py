from abc import abstractmethod


class Question:
    @abstractmethod
    def next_question(self):
        pass
    
    @abstractmethod
    def previous_question(self):
        pass
    
    @abstractmethod
    def new_question(self, question: str):
        pass
    
    @abstractmethod
    def delete_question(self, question: str):
        pass
    
    @abstractmethod
    def display_question(self):
        pass
    
    @abstractmethod
    def display_all_questions(self):
        pass