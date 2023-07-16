import random

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class FlashcardSet:
    def __init__(self, name):
        self.name = name
        self.flashcards = []

    def add_flashcard(self, front, back):
        flashcard = Flashcard(front, back)
        self.flashcards.append(flashcard)

    def study(self):
        random.shuffle(self.flashcards)
        for flashcard in self.flashcards:
            input(f"Front: {flashcard.front}\nPress Enter to see the answer.")
            print(f"Back: {flashcard.back}")
            print("----------------------")

def create_flashcards():
    flashcard_set = FlashcardSet("Vocabulary Flashcards")
    vocabulary = [
        "Hello", "Goodbye", "Yes", "No", "Thank you", "Please", "Sorry", "Excuse me", "Help", "I",
        "You", "He", "She", "We", "They", "It", "This", "That", "Here", "There", "Who", "What", "Where",
        "When", "Why", "How", "Name", "Age", "Number", "Time", "Day", "Week", "Month", "Year", "Today",
        "Tomorrow", "Yesterday", "Now", "Always", "Sometimes", "Never", "Very", "Big", "Small", "Good",
        "Bad", "Happy", "Sad", "Like", "Dislike", "Eat", "Drink", "Sleep", "Walk", "Run", "Talk", "Listen",
        "Read", "Write", "Learn", "Understand", "Speak", "Know", "Want", "Need", "Love", "Hate", "See",
        "Hear", "Touch", "Smell", "Taste", "Hot", "Cold", "High", "Low", "Far", "Near", "Up", "Down",
        "Right", "Left", "Good morning", "Good afternoon", "Good evening", "Good night", "Exciting",
        "Interesting", "Difficult", "Easy", "Beautiful", "Ugly", "Friend", "Family", "Home", "School",
        "Work", "Food", "Water", "Air"
    ]
    for word in vocabulary:
        front = word
        back = input(f"What does '{word}' mean? ")
        flashcard_set.add_flashcard(front, back)
    return flashcard_set

def main():
    flashcard_set = create_flashcards()
    flashcard_set.study()

if __name__ == "__main__":
    main()
