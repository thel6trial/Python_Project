import random

words = ['hanoi', 'blackpink', 'saigon']

class Hangman:
    # Khởi tạo gồm từ cần đoán, từ hiển thị và số lần đoán
    def __init__(self):
        self.word = random.choice(words)
        self.display = ['_' for i in list(self.word)]
        self.guesses = 0
    # Hàm hiển thị ra từ cần hiển thị
    def show(self):
        display1 = ' '.join(self.display)
        print("The word is: {display1}")
    # Hàm lấy ra chỉ số của chữ cái khi đoán đúng
    def get_word_index(self, guess):
        vitri = []

        for index, char in enumerate(list(self.word)):
            if char == guess:
                vitri.append(index)
    #Hàm thay vị trí của những từ đoán đúng cho dấu gạch
    def update(self, vitri, letter):
        for i in vitri:
            self.display[i] = letter
    #Hàm kiểm tra xem có đoán đúng không
    def check(self, guess):
        if guess in self.word:
            vitri = self.get_word_index(guess)
            self.update(vitri, guess)
    # Hàm kiểm tra chiến thắng không
    def check_for_win(self):
        display1 = " ".join(self.display)
        word = self.word
        if display1 == word:
            print("You win !!!")

def game():
    word = Hangman()
    while True:
        a = input("Nhập từ cần đoán: ")
        word.check(a)
        word.show()
        word.guesses += 1
        if word.check_for_win():
            print("Bạn đã đoán đúng trong {word.guesses} lần")
            break

def ask():
    while True:
        ask = input("Bạn có muốn chơi game không ?")
        if ask == 'no':
            break
        game()
