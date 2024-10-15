class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(self):
        return self.word + '(' + self.meaning + ')'
    
flash = []
print("Welcome to flashcard application.")

while True:
    word = input("Enter a word :")
    meaning = input("Enter the meaning :")
    flash.append(flashcard(word,meaning))
    option = int(input("Do you want to continue? \n If yes then 1 else 0"))
    if not option:
        break

for c in flash:
    print(c)