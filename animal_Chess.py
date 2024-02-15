from tkinter import*
import random
from PIL import ImageTk, Image
import os

root = Tk()
path = os.path.dirname(os.path.abspath(__file__))
canvas = Canvas(root, width=540, height=600)
canvas.grid(columnspan=5, rowspan=4)
subor = Image.open(path + '//whoEatWho.png')
picture = subor.resize((540, 60), Image.LANCZOS)
subor = ImageTk.PhotoImage(picture)
canvas.create_image((0, 540), image=subor, anchor=NW)

def animal(event):
    mouseX = event.x
    mouseY = event.y
    for policko in policka:
        if mouseX >= policko.x and mouseX <= policko.x + 134:
            if mouseY >= policko.y and mouseY <= policko.y + 134:
                policko.changeMyCard()

def changeTitle():
    global title, allowed
    if allowed == 1:
        if title == 'blue':
            title = 'red'
        else:
            title = 'blue'
        root.title(title)
    
def remains(animalsRemain1, animalsRemain2, group):
    global title
    if 'elephant' in animalsRemain1:
            if 'mouse' in animalsRemain2:
                root.title(f'{group} win!!!')
            else:
                root.title(f'{group} win!!!')
    if 'lion' in animalsRemain1:
        root.title(f'{group} win!!!')
    if 'tiger' in animalsRemain1 and not 'lion' in animalsRemain2:
        root.title(f'{group} win!!!')
    if 'puma' in animalsRemain1 and not 'lion' in animalsRemain2 and not 'tiger' in animalsRemain2:
        root.title(f'{group} win!!!')
    if 'wolf' in animalsRemain1 and not 'lion' in animalsRemain2 and not 'tiger' in animalsRemain2 and not 'puma' in animalsRemain2:
        root.title(f'{group} win!!!')
    if 'dog' in animalsRemain1 and not 'lion' in animalsRemain2  and not 'tiger' in animalsRemain2  and not 'puma' in animalsRemain2  and not 'wolf' in animalsRemain2:
        root.title(f'{group} win!!!')
    if 'cat' in animalsRemain1 and not 'lion' in animalsRemain2 and not 'tiger' in animalsRemain2 and not 'puma' in animalsRemain2 and not 'wolf' in animalsRemain2 and not 'dog' in animalsRemain2:
        root.title(f'{group} win!!!')
            
def someoneKilled(index):
    global title, allowed
    animalsRemain[index] = 0
    if animalsRemain[::2].count(0) >= 7 and animalsRemain[1::2].count(0) >= 7 or animalsRemain[::2].count(0) == 8 or animalsRemain[1::2].count(0) == 8:
        allowed = 0
        if animalsRemain[::2] == animalsRemain[1::2]:
            root.title('Draw!!!')
        else:
            remains(animalsRemain[::2], animalsRemain[1::2], 'blue')
            remains(animalsRemain[1::2], animalsRemain[::2], 'red')
        

class Policko():
    path = os.path.dirname(os.path.abspath(__file__))
    filesAnimalsnotUsed = [path + '//blueMouse.png',
                            path + '//redMouse.png',
                            path + '//blueCat.png',
                            path + '//redCat.png',
                            path + '//blueDog.png',
                            path + '//redDog.png',
                            path + '//blueWolf.png',
                            path + '//redWolf.png',
                            path + '//bluePuma.png',
                            path + '//redPuma.png',
                            path + '//blueTiger.png',
                            path + '//redTiger.png',
                            path + '//blueLion.png',
                            path + '//redLion.png',
                            path + '//blueElephant.png',
                            path + '//redElephant.png',
                            -1]

    filesAnimals = [path + '//blueMouse.png',
                    path + '//redMouse.png',
                    path + '//blueCat.png',
                    path + '//redCat.png',
                    path + '//blueDog.png',
                    path + '//redDog.png',
                    path + '//blueWolf.png',
                    path + '//redWolf.png',
                    path + '//bluePuma.png',
                    path + '//redPuma.png',
                    path + '//blueTiger.png',
                    path + '//redTiger.png',
                    path + '//blueLion.png',
                    path + '//redLion.png',
                    path + '//blueElephant.png',
                    path + '//redElephant.png']

    animalNames = ['mouse',
                    'mouse',
                    'cat',
                    'cat',
                    'dog',
                    'dog',
                    'wolf',
                    'wolf',
                    'puma',
                    'puma',
                    'tiger',
                    'tiger',
                    'lion',
                    'lion',
                    'elephant',
                    'elephant']

    def __init__(self, x, y, me) -> None:
        self.killer = -1
        self.x = x
        self.y = y
        self.pos = me
        self.animalObjectIndex = me
        self.animalFileIndex = -1
        self.animalName = ''
        self.group = ''
        self.__policko = canvas.create_rectangle(self.x, self.y, self.x + 135, self.y + 135)
        animals.append(Animal(self.animalObjectIndex, self.x, self.y))
        self.owner = animals[self.animalObjectIndex]

    def changeMyCard(self):
        global title
        if not self.owner == -1 or not self.killer == -1:
            if self.animalFileIndex == -1 and self.killer == -1:
                while self.filesAnimalsnotUsed[self.animalFileIndex] == -1:
                    self.animalFileIndex = random.randint(0, len(self.filesAnimalsnotUsed) - 1)

                self.animalName = self.animalNames[self.animalFileIndex]
                self.owner.animalFileIndex = self.animalFileIndex
                self.owner.resizePicture(135)
                self.filesAnimalsnotUsed[self.animalFileIndex] = -1
                self.group = self.owner.getGroup()
                changeTitle()

            elif self.killer == -1 and title == self.group and not self.owner == -1:
                self.owner.resizePicture(155)
                self.killer = self.owner.animalObjectIndex
                self.__setVariables()

            elif not self.owner == -1 and self.killer == self.owner.animalObjectIndex and title == self.group:
                self.killer = -1
                self.__setVariables()
                self.owner.resizePicture(135)

            elif not self.killer == -1 and not title == self.group and not self.group == '' and not self.owner == -1:
                if animals[self.killer].y == self.y + 135 and animals[self.killer].x == self.x or animals[self.killer].y == self.y - 135 and animals[self.killer].x == self.x or animals[self.killer].x == self.x - 135 and animals[self.killer].y == self.y or animals[self.killer].x == self.x + 135 and animals[self.killer].y == self.y:
                    if policka[self.killer].animalName == self.animalName:
                        someoneKilled(self.owner.animalFileIndex)
                        someoneKilled(animals[self.killer].animalFileIndex)
                        self.owner.animalObjectIndex = -1
                        animals[self.killer].animalObjectIndex = -1
                        canvas.delete(self.owner.animal)
                        canvas.delete(animals[self.killer].animal)
                        self.owner = -1
                        policka[self.killer].owner = -1
                        self.killer = -1
                        self.__setVariables()
                        changeTitle()

                    elif policka[self.killer].animalName == 'elephant' and not self.animalName == 'mouse':
                        self.killProcess()

                    elif policka[self.killer].animalName == 'elephant' and self.animalName == 'mouse':
                        someoneKilled(self.owner.animalFileIndex)

                    elif policka[self.killer].animalName == 'mouse' and self.animalName == 'elephant':
                        self.killProcess()

                    elif policka[self.killer].animalFileIndex > self.animalFileIndex:
                        animals[self.killer].x = self.owner.x
                        animals[self.killer].y = self.owner.y
                        self.pos = (animals[self.killer].y / 135) * 4 + (animals[self.killer].x / 135)
                        someoneKilled(self.owner.animalFileIndex)
                        canvas.delete(self.owner.animal)
                        animals[self.killer].resizePicture(135)

                        animals[self.killer].animalObjectIndex = self.animalObjectIndex
                        animals[self.animalObjectIndex] = animals[self.killer]
                        self.group = animals[self.animalObjectIndex].group
                        animals[self.animalObjectIndex].animalFileIndex = animals[self.killer].animalFileIndex
                        self.animalFileIndex = animals[self.animalObjectIndex].animalFileIndex
                        self.animalName = policka[self.killer].animalName
                        self.owner = animals[self.animalObjectIndex]
                        animals[self.killer].animalObjectIndex = self.animalObjectIndex

                        policka[self.killer].owner = -1
                        policka[self.killer].animalFileIndex = -1
                        policka[self.killer].animalName = ''
                        policka[self.killer].group = ''

                        self.killer = -1
                        self.__setVariables()
                        changeTitle()

            elif not self.killer == -1 and self.owner == -1:
                if animals[self.killer].y == self.y + 135 and animals[self.killer].x == self.x or animals[self.killer].y == self.y - 135 and animals[self.killer].x == self.x or animals[self.killer].x == self.x - 135 and animals[self.killer].y == self.y or animals[self.killer].x == self.x + 135 and animals[self.killer].y == self.y:
                    animals[self.killer].x = policka[self.animalObjectIndex].x
                    animals[self.killer].y = policka[self.animalObjectIndex].y
                    self.pos = (animals[self.killer].y / 135) * 4 + (animals[self.killer].x / 135)
                    animals[self.killer].resizePicture(135)

                    animals[self.killer].animalObjectIndex = self.animalObjectIndex
                    animals[self.animalObjectIndex] = animals[self.killer]
                    self.group = animals[self.animalObjectIndex].group
                    animals[self.animalObjectIndex].animalFileIndex = animals[self.killer].animalFileIndex
                    self.animalFileIndex = animals[self.animalObjectIndex].animalFileIndex
                    self.animalName = policka[self.killer].animalName
                    self.owner = animals[self.animalObjectIndex]
                    animals[self.killer].animalObjectIndex = self.animalObjectIndex

                    policka[self.killer].owner = -1
                    policka[self.killer].animalFileIndex = -1
                    policka[self.killer].animalName = ''
                    policka[self.killer].group = ''

                    self.killer = -1
                    self.__setVariables()
                    changeTitle()

    def __setVariables(self):
        for policko in policka:
            policko.killer = self.killer
            
    def killProcess(self):
        someoneKilled(self.owner.animalFileIndex)
        animals[self.killer].x = self.owner.x
        animals[self.killer].y = self.owner.y
        self.pos = (animals[self.killer].y / 135) * 4 + (animals[self.killer].x / 135)
        canvas.delete(self.owner.animal)
        animals[self.killer].resizePicture(135)

        animals[self.killer].animalObjectIndex = self.animalObjectIndex
        animals[self.animalObjectIndex] = animals[self.killer]
        self.group = animals[self.animalObjectIndex].group
        animals[self.animalObjectIndex].animalFileIndex = animals[self.killer].animalFileIndex
        self.animalFileIndex = animals[self.animalObjectIndex].animalFileIndex
        self.animalName = policka[self.killer].animalName
        self.owner = animals[self.animalObjectIndex]
        animals[self.killer].animalObjectIndex = self.animalObjectIndex

        policka[self.killer].owner = -1
        policka[self.killer].animalFileIndex = -1
        policka[self.killer].animalName = ''
        policka[self.killer].group = ''

        self.killer = -1
        self.__setVariables()
        changeTitle()

class Animal():
    path = os.path.dirname(os.path.abspath(__file__))
    redAnimals = [path + '//redMouse.png',
                    path + '//redCat.png',
                    path + '//redDog.png',
                    path + '//redWolf.png',
                    path + '//redPuma.png',
                    path + '//redTiger.png',
                    path + '//redLion.png',
                    path + '//redElephant.png']

    blueAnimals = [path + '//blueMouse.png',
                    path + '//blueCat.png',
                    path + '//blueDog.png',
                    path + '//blueWolf.png',
                    path + '//bluePuma.png',
                    path + '//blueTiger.png',
                    path + '//blueLion.png',
                    path + '//blueElephant.png']

    def __init__(self, me, x, y) -> None:
        self.x = x
        self.y = y
        self.animalObjectIndex = me
        self.animalFileIndex = -1
        self.__animalSubor = Image.open(self.path + '//policko.png')
        self.__resizedPic = self.__animalSubor.resize((135, 135), Image.LANCZOS)
        self.__animalSubor = ImageTk.PhotoImage(self.__resizedPic)
        self.animal = canvas.create_image((self.x, self.y), image=self.__animalSubor, anchor=NW)

    def getGroup(self):
        for zviera in self.redAnimals:
            if self.__subor == zviera:
                self.group = 'red'
                break
            elif not self.__subor == zviera:
                self.group = 'blue'
        return self.group

    def resizePicture(self, size):
        canvas.delete(self.animal)
        self.__subor = policka[1].filesAnimals[self.animalFileIndex]
        self.__biggerSubor = Image.open(self.__subor)
        self.__resizedPic = self.__biggerSubor.resize((size, size), Image.LANCZOS)
        self.__biggerSubor = ImageTk.PhotoImage(self.__resizedPic)
        self.animal = canvas.create_image((self.x, self.y), image=self.__biggerSubor, anchor=NW)

starterTitle = random.randint(0, 1)
title = ''
if starterTitle == 0:
    title = 'blue'
    root.title(title)
else:
    title = 'red'
    root.title(title)

animals = []
policka = []
allowed = 1
animalsRemain = ['mouse',
                'mouse',
                'cat',
                'cat',
                'dog',
                'dog',
                'wolf',
                'wolf',
                'puma',
                'puma',
                'tiger',
                'tiger',
                'lion',
                'lion',
                'elephant',
                'elephant']

index = 0
for y in range(4):
    for x in range(4):
        policka.append(Policko(x * 135, y * 135, index))
        index += 1

root.bind('<Button-1>', animal)
root.mainloop()