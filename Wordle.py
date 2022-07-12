from termcolor import colored
import random



class Game:
    def __init__(self):
        self.wordle = ''
        self.guesses = [[],[],[],[],[],[]]
        self.grey_letters = []
        self.green_letters = []
        self.yellow_letters = []
        self.guess1 =['','','','','']
        self.guess_counter = 0
        self.text_file = 'answers.txt'
        self.possible_guesses = 'possible_guesses.txt'
        self.win = False
        self.lose = False
        self.lines = []
        self.lines2 = []
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        self.create_possible_guesses_file()
        self.keyboard = []




    def create_keyboard(self):
        for letter in self.alphabet:
            self.keyboard.append(letter)

        #for letter in self.keyboard:
            #print(letter)

    def edit_keyboard(self):
        pass


    def create_word(self):
        '''opens the text file, strips unneeded characters, and randomly selects a word'''

        lines = open(self.text_file).read().splitlines()

        myline = random.choice(lines)
        #print(myline)
        myline = myline.replace('  ', '').replace('\'', '').replace(',', '') #removes white space and superfluous characters from word
        #print(myline)
        #print('plots')
        self.wordle = myline.upper()
        self.lines2 = lines

    def create_possible_guesses_file(self):
        '''opens the text file of possible guesses, and makes it a list so we can iterate through it for error checking'''
        lines = open(self.possible_guesses).read().splitlines()
        self.lines = lines #makes this variable global so we can interact with it later




    def win_sequence(self):
        pass

    def lose_sequence(self):
        pass

    def check_guess(self, guess):
        while guess.lower() not in self.lines and guess.lower() not in self.lines2:
            print('please enter a valid 5 letter word')
            guess = input('Input guess')

        guess = guess.upper()

        letter_count = 0
        current_progress = ['','','','','']
        index = -1
        counter_dict = dict()

        for l in self.wordle:
            if l in counter_dict.keys():
                counter_dict[l] += 1
            else:
                counter_dict[l] = 1


        for guess_letter, wordle_letter in zip(guess, self.wordle):
            index +=1

            counter_dict
            if guess_letter == wordle_letter:
                current_progress[index] = colored(guess_letter, 'green')
                counter_dict[guess_letter] -= 1

        index = -1
        for guess_letter, wordle_letter in zip(guess, self.wordle):
            index += 1
            letter_count = self.wordle.count(guess_letter)

            if guess_letter not in self.wordle:
                current_progress[index] = colored(guess_letter, 'grey')
                self.grey_letters.append(guess_letter)

            elif guess_letter != wordle_letter and guess_letter in self.wordle:
                if counter_dict[guess_letter] <= 0:
                    current_progress[index] = colored(guess_letter, 'grey')
                else:
                    current_progress[index] = colored(guess_letter, 'yellow')
                counter_dict[guess_letter] -= 1





        self.guesses[self.guess_counter] = current_progress
        #print(*current_progress)
        for prev in self.guesses:
            print(*prev)

        self.guess_counter += 1

        if guess == self.wordle:
            self.win = True

        elif self.guess_counter >= 6:
            self.lose = True

        #print(*self.guesses, sep = '\n')


if __name__ == '__main__':
    x = Game()
    x.create_keyboard()
    x.create_word()
    while x.win != True and x.lose != True:
        user_guess = input('Input guess')
        x.check_guess(user_guess)
    if x.win == True:
        print('Congrats, you won in {} guesses! The word was {}'.format(x.guess_counter, x.wordle))

    elif x.lose == True:
        print('Sorry, you used all 6 guesses. The word was {}'.format(x.wordle))
    #print('word: ', x.wordle)

#print(colored('correct', 'green'), colored('wrong', 'red'))

#y = colored('T', 'green')
#print(y)








