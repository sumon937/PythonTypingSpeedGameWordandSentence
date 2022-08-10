from tkinter import *
from tkinter import messagebox
import pygame
from pygame.locals import *
import sys
import time
import random


class SentenceGame:

    def __init__(self):
        self.w = 850
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500, 750))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Speed test')

        self.run()

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if (not self.end):
            # Calculate time
            self.total_time = time.time() - self.time_start

            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100

            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:' + str(round(self.total_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()

        self.running = True
        while (self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                        # position of reset box
                    if (x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()


                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        # drawing heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        # draw the sentence string
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

        pygame.display.update()


class WordGame:
    def __init__(self):
        global count, sliderWrod
        global score, miss
        self.root = Tk()
        self.root.geometry('800x700+300+50')
        self.root.resizable(False, False)
        self.root.title('Typing Speed Game')
        # root.iconbitmap('icon.ico')
        self.root.configure(bg='black')
        self.words = ['Science', 'Ipsum', 'Simply', 'dummy', 'printing', 'typesetting', 'Program', 'Computer',
                 'Industry',
                 'Action', 'software', 'versions', 'NeedSpeed']
        random.shuffle(self.words)

        self.score = 0
        self.miss = 0
        self.timeLeft = 60
        self.count = 0
        self.sliderWrod = ''

        ############## label section
        self.titleLabel = Label(self.root, text='', bg='black', fg='green', font=('arial', 30, 'italic bold'), width=33)
        self.titleLabel.place(x=10, y=10)

        self.text = 'Welcome To Typing Speed Testing Game'
        if (self.count >= len(self.text)):
            self.count = 0
            self.sliderWrod = ''
        self.sliderWrod += self.text[self.count]
        self.count += 1
        #self.titleLabel.configure(text=self.sliderWrod)
        self.titleLabel.configure(text="Welcome to Word Game")

        #self.titleLabel.after(150, self.welcomeLabel)

        self.scoreLabel = Label(self.root, text='Your Score :', bg='black', fg='white', font=('arial', 25, 'italic bold'))
        self.scoreLabel.place(x=10, y=100)
        self.scoreCountLabel = Label(self.root, text=self.score, bg='black', fg='white', font=('arial', 25, 'italic bold'))
        self.scoreCountLabel.place(x=80, y=180)

        self.timeLabel = Label(self.root, text='Time Left :', bg='black', fg='white', font=('arial', 25, 'italic bold'))
        self.timeLabel.place(x=600, y=100)
        self.timeCountLabel = Label(self.root, text=self.timeLeft, bg='black', fg='white', font=('arial', 25, 'italic bold'))
        self.timeCountLabel.place(x=680, y=180)

        self.wordLabel = Label(self.root, text=self.words[0], bg='black', fg='blue', font=('arial', 35, 'italic bold'))
        self.wordLabel.place(x=250, y=200)

        ############## Entry Section
        self.wordEntry = Entry(self.root, font=('arial', 25, 'italic bold'), bd=10, justify='center')
        self.wordEntry.place(x=200, y=300)
        self.wordEntry.focus_set()

        ######## game play detail label
        self.gamePlayDetailLabel = Label(self.root, text='Type Word And Hit Enter Button', bg='black', fg='powder blue',
                                    font=('arial', 30, 'italic bold'))
        self.gamePlayDetailLabel.place(x=100, y=450)

        self.root.bind('<Return>', self.startGame)
        self.root.mainloop()

    def time(self):

            if (self.timeLeft >= 11):
                pass
            else:
                self.timeCountLabel.configure(fg='red')
            if (self.timeLeft > 0):
                self.timeLeft -= 1
                self.timeCountLabel.configure(text=self.timeLeft)
                self.timeCountLabel.after(1000, self.time)
            else:
                self.gamePlayDetailLabel.configure(
                    text='Hit = {} | Miss = {} | Total Score = {}'.format(self.score, self.miss, self.score - self.miss))
                self.notific = messagebox.askretrycancel('Notification', 'For Play Again Please Hit The Retry Button!')
                if (self.notific == True):
                    self.score = 0
                    self.timeLeft = 60
                    self.miss = 0
                    self.timeCountLabel.configure(text=self.timeLeft)
                    self.wordLabel.configure(text=self.words[0])
                    self.scoreCountLabel.configure(text=self.score)


    def startGame(self,event):

                if (self.timeLeft == 60):
                    self.time()
                self.gamePlayDetailLabel.configure(text='Enjoy The Game')
                if (self.wordEntry.get() == self.wordLabel['text']):
                    self.score += 1
                    self.scoreCountLabel.configure(text=self.score)
                else:
                    self.miss += 1
                random.shuffle(self.words)
                self.wordLabel.configure(text=self.words[0])
                self.wordEntry.delete(0, END)



def runSentenceGame():
    home.destroy()
    SentenceGame()

def runWordGame():
    home.destroy()
    WordGame()



if __name__ == '__main__':
    home = Tk()
    home.geometry('800x600+300+50')
    home.title('Typing Game')
    home.configure(bg='black')
    home.resizable(False,False)

    titleLable = Label(home, text='Please choose a game type!', bg='black', fg='white', font=('arial', 25, 'italic bold'))
    titleLable.place(x=200,y=100)

    wordButton = Button(home, text='WORD', bg='black', fg='white',font=('arial', 25, 'italic bold'),command=runWordGame)
    wordButton.place(x=200, y=300)

    sentButton = Button(home, text='SENTENCE', bg='black', fg='white', font=('arial', 25, 'italic bold'),command=runSentenceGame)
    sentButton.place(x=400, y=300)

    home.mainloop()


