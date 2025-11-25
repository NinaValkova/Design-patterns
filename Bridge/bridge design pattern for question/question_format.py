from question_manager import QuestionManager

class QuestionFormat(QuestionManager):
    def display_all(self):
        print("\n----------------------------------------------")
        super().display()
        print("------------------------------------------------")