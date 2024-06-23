
import sys # module in the system---it will allow to us emany things on the system 
import pygame # play song 
from PyQt6.QtWidgets import * #telling file to go to the folder.subfolder + * means a wild card and it imports everything from the PyQt6 widgets 
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import random 
from pygame import*
from mutagen.mp3 import MP3





class BringInWidgets(QMainWindow): # inheritance -- using the main window from the bottom to portray the widgets -- BRINGINWIDGETS is not stand alone, it is a QMAINWINDOW 
    y = True
    do= "assets/songs/DoubleTake.mp3"
    fa = "assets/songs/FallingFlower.mp3"
    sh = "assets/songs/Shino.mp3"
    wa = "assets/songs/WaterLofi.mp3"
    wi = "assets/songs/Willow.mp3"

    DO = 'assets/albumCovers/DoubleTakeImage.jpg'
    FA = 'assets/albumCovers/FallingFlower.jpg'
    SH = 'assets/albumCovers/Shino Image.jpg'
    WA = 'assets/albumCovers/Water Image.jpg'
    WI = 'assets/albumCovers/Willow Image.jpeg'

    

    coverList = [DO, FA, SH, WA, WI]
    
    x = [do, fa, sh, wa, wi]
    song1=["double take -- dhruv"]
    song2=["falling flower -- seventeen"]
    song3=["shinoga e-wa--fujii kaze "]
    song4=["Water Lofi--someone"]
    song5=["willow--taylor swift"]
    lala = 0
    song = ""
    def __init__(self):   #self is used to attach things into the object
        super().__init__()
        #QMainWindow.__init__(self)
        pygame.mixer.init() # intitializes the mixer to play songs 

        self.setFixedSize(800,600) #method --u can make it over and over 
        self.setWindowTitle("Niki's Music") # sets the title of the window (program title)
        self.setStyleSheet(   #kinda like css style
            """
                background-color: pink;
            """
        )  
        # input = QLineEdit(self) 
        # input.move(50,50)

        
        shuffleButton=QPushButton(self)
        shuffleButton.setGeometry(485,495,50,50)
        shuffleButton.setIcon(QIcon('assets/icons/shuffle.svg'))
        shuffleButton.setIconSize(QSize(50,50))
        shuffleButton.clicked.connect(lambda: self.shuffle(name, album))


    

        


        # layout = QVBoxLayout() #holds all the other widgets 

        name = QLabel(self) #absolute posistioning
        name.setGeometry(330,-35,200,150)
        name.setText("Niki's Song") # posistion
        name.setStyleSheet(
            """
            color: purple;
            font-size: 15px;
            
            """                                           

        )


        def nameOne(self):
            DoubleTake = QLabel("Double Take -- Dhruv", self)
            DoubleTake.setGeometry(330,100,200,150) # posistion
            DoubleTake.setStyleSheet(
            """
            color: purple;
            font-size: 10px;
            
            """

        )

        def nameTwo(self):
            FallingFlower = QLabel("Falling Flower -- Seventeen", self )
            FallingFlower.setGeometry(330,100,200,150)
            FallingFlower.setStyleSheet(
                """
                color: purple;
                font-size: 10px;
                """
            )

        def nameThree(self):
            Shino = QLabel("Shinunoga E-wa -- Fujii Kaze", self )
            Shino.setGeometry(330,100,200,150)
            Shino.setStyleSheet(
                """
                color: purple;
                font-size: 10px;
                """
            )

        def nameFour(self):
            WaterLofi = QLabel("WaterLofi", self )
            WaterLofi.setGeometry(330,100,200,150)
            WaterLofi.setStyleSheet(
                """
                color: purple;
                font-size: 10px;
                """
            )

        def nameFive(self):
            Willow = QLabel("Willow -- Taylor Swift", self )
            Willow.setGeometry(330,100,200,150)
            Willow.setStyleSheet(
                """
                color: purple;
                font-size: 10px;
                """
            )



        box = QFrame(self)
        box.setGeometry(285,100,250,250)
        box.setStyleSheet(
            """
                background-color: purple;
                border: 2px solid white;
            """
        )

        count = QLabel('Album', box)
        count.setGeometry(0,0,box.width(),box.height())
        count.setStyleSheet(
            """
            color:white;
            font-size:25px;
            text-align: center;
            """
        )





        name2 = QLabel('Music 1', self) #absolute posistioning
        name2.setGeometry(150,375,250,30) # posistion

        name2.setStyleSheet(
            """
            color:white;
            font-size: 25px;
            
            """
        )
       
        box2 = QPushButton('Double Take' ,self)
        box2.setGeometry(150,375,250,30)
        box2.clicked.connect(lambda: print('Music 1'))
        box2.clicked.connect(lambda: self.DoubleTake(name, album, Q))
        box2.setIcon(QIcon('assets/icons/play1.svg'))
        box2.setIconSize(QSize(25,25))
    
        # box2.setPixmap(QPixmap('assets/albumCovers/DoubleTakeImage.jpg').scaled(250,250))
        box2.setStyleSheet(
            """
                color: white;
                background-color: purple;
                
            """
        )

    
        box3 = QPushButton('Falling Flower',self)
        box3.setGeometry(150,410,250,30)
        box3.clicked.connect(lambda: print('Music 2'))
        box3.clicked.connect(lambda: self.FallingFlower(name, album, Q))
        # box3.setPixmap(QPixmap('assets/albumCovers/FallingFlower.jpg').scaled(250,250))
        box3.setIcon(QIcon('assets/icons/play1.svg'))
        box3.setIconSize(QSize(25,25))
        box3.setStyleSheet(
            """
                color: white;
                background-color: purple;
                
            """
        )
        box4 = QPushButton('Shino',self)
        box4.setGeometry(150,445,250,30)
        box4.clicked.connect(lambda: print('Music 3'))
        box4.clicked.connect(lambda: self.Shino(name, album, Q))
        box4.setIcon(QIcon('assets/icons/play1.svg'))
        box4.setIconSize(QSize(25,25))
        box4.setStyleSheet(
            """
                color: white;
                background-color: purple;
                
            """
        )
        box5 = QPushButton('WaterLofi',self)
        box5.setGeometry(150,480,250,30)
        box5.clicked.connect(lambda: print('Music 4'))
        box5.clicked.connect(lambda: self.WaterLofi(name, album, Q))
        box5.setIcon(QIcon('assets/icons/play1.svg'))
        box5.setIconSize(QSize(25,25))
        box5.setStyleSheet(
            """
                color: white;
                background-color: purple;
                
            """
        )

        

        box6 = QPushButton('Willow',self)
        box6.setGeometry(150,515,250,30)
        box6.clicked.connect(lambda: print('Music 5'))
        box6.clicked.connect(lambda: self.Willow(name, album, Q))
        box6.setIcon(QIcon('assets/icons/play1.svg'))
        box6.setIconSize(QSize(25,25))
        box6.setStyleSheet(
            """
                color: white;
                background-color: purple;
                
            """
        )


        # album cover
        album = QLabel(self)
        album.setGeometry(285,100,250,250)
        
    
        # Pause + restart from the spot that has been paused 
        stopButton=QPushButton(self)
        stopButton.setGeometry(425,375,50,50)
        stopButton.setIcon(QIcon('assets/icons/pause.svg'))
        stopButton.setIconSize(QSize(50,50))
        stopButton.clicked.connect(lambda: self.DoubleTakeStop()) # allows code for the actual thing to happen

        


        #Rewind
        rewindButton = QPushButton(self)
        rewindButton.setGeometry(485,375,50,50)
        rewindButton.setIcon(QIcon('assets/icons/rewind.png'))
        rewindButton.setIconSize(QSize(50,50))
        rewindButton.clicked.connect(lambda: self.DoubleTakeRewind())


        #Volume Up 
        volumeUpButton = QPushButton(self)
        volumeUpButton.setGeometry(425, 435, 50, 50)
        volumeUpButton.setIcon(QIcon('assets/icons/volumeUp.svg'))
        volumeUpButton.setIconSize(QSize(50,50))
        volumeUpButton.clicked.connect(lambda: self.DoubleTakeVolumeUp())


        #volume down
        volumeDownButton = QPushButton(self)
        volumeDownButton.setGeometry(485, 435, 50, 50)
        volumeDownButton.setIcon(QIcon('assets/icons/volumeDown.svg'))
        volumeDownButton.setIconSize(QSize(50,50))
        volumeDownButton.clicked.connect(lambda: self.DoubleTakeVolumeDown())

        #STOP
        StopButton=QPushButton(self)
        StopButton.setGeometry(425,495,50,50)
        StopButton.setIcon(QIcon('assets/icons/stop.svg'))
        StopButton.setIconSize(QSize(50,50))
        StopButton.clicked.connect(lambda: self.DStop()) 

        #Fast Forward
        fastforward = QPushButton(self)
        fastforward.setGeometry(550,435,50,50)
        fastforward.setIcon(QIcon('assets/icons/fastforward.svg'))
        fastforward.setIconSize(QSize(50,50))
        fastforward.clicked.connect(lambda: self.lenght())


        self.remainButton = QPushButton(self)
        self.remainButton.setGeometry(620,350,200,20)
        self.remainButton.setText('Double Take Time')
        self.remainButton.clicked.connect(lambda: self.songLengthD(Q))

        self.remainFButton = QPushButton(self)
        self.remainFButton.setGeometry(620,400,200,20)
        self.remainFButton.setText('Falling Flower Time')
        self.remainFButton.clicked.connect(lambda: self.songLengthF(Q))

        self.remainSButton = QPushButton(self)
        self.remainSButton.setGeometry(620,450,200,20)
        self.remainSButton.setText('Shino Time')
        self.remainSButton.clicked.connect(lambda: self.songLengthS(Q))

        self.remainWLButton = QPushButton(self)
        self.remainWLButton.setGeometry(620,500,200,20)
        self.remainWLButton.setText('Water Lofi Time')
        self.remainWLButton.clicked.connect(lambda: self.songLengthWL(Q))

        self.remainWButton = QPushButton(self)
        self.remainWButton.setGeometry(620,550,200,20)
        self.remainWButton.setText('Willow Time')
        self.remainWButton.clicked.connect(lambda: self.songLengthW(Q))


        
        self.remainButton.hide()
        self.remainFButton.hide()
        self.remainSButton.hide()
        self.remainWLButton.hide()
        self.remainWButton.hide()

        Q = QLabel(self)
        Q.setGeometry(25,100,250,100)
        Q.setText('')

        

    def lenght(self):
        currentSong = pygame.mixer.music.get_pos()//100
        self.lala = currentSong + 5
        pygame.mixer.music.set_pos(self.lala)
        print(currentSong)

        
    
    def songLengthD(self, Q):
        if pygame.mixer.music.get_busy():
            song = MP3('assets/songs/DoubleTake.mp3')
            songTotalD = int(song.info.length)
            print(songTotalD)
            songLengthD = self.lala + (pygame.mixer.music.get_pos()//1000)
            print(songLengthD)
            Q.setText(str(songLengthD)+ "/" +str(songTotalD) + "secs")
            self.remainButton.show()
            self.remainFButton.hide()
            self.remainSButton.hide()
            self.remainWLButton.hide()
            self.remainWButton.hide()

    def songLengthF(self, Q):
        if pygame.mixer.music.get_busy():
            song = MP3('assets/songs/FallingFlower.mp3')
            songTotalF = int(song.info.length)
            print(songTotalF)
            songLengthF = self.lala + (pygame.mixer.music.get_pos()//1000)
            print(songLengthF)
            Q.setText(str(songLengthF)+ "/" +str(songTotalF) + "secs")
            self.remainButton.hide()
            self.remainFButton.show()
            self.remainSButton.hide()
            self.remainWLButton.hide()
            self.remainWButton.hide()
            

    def songLengthS(self, Q):
        if pygame.mixer.music.get_busy():
            song = MP3('assets/songs/Shino.mp3')
            songTotalS = int(song.info.length)
            print(songTotalS)
            songLengthS = self.lala + (pygame.mixer.music.get_pos()//1000)
            print(songLengthS)
            Q.setText(str(songLengthS)+ "/" +str(songTotalS) + "secs")
            self.remainButton.hide()
            self.remainFButton.hide()
            self.remainSButton.show()
            self.remainWLButton.hide()
            self.remainWButton.hide()
    
    def songLengthWL(self, Q):
        if pygame.mixer.music.get_busy():
            song = MP3('assets/songs/WaterLofi.mp3')
            songTotalWL = int(song.info.length)
            print(songTotalWL)
            songLengthWL = self.lala + (pygame.mixer.music.get_pos()//1000)
            print(songLengthWL)
            Q.setText(str(songLengthWL)+ "/" +str(songTotalWL) + "secs")
            self.remainButton.hide()
            self.remainFButton.hide()
            self.remainSButton.hide()
            self.remainWLButton.show()
            self.remainWButton.hide()

    def songLengthW(self, Q):
        if pygame.mixer.music.get_busy():
            song = MP3('assets/songs/Willow.mp3')
            songTotalW = int(song.info.length)
            print(songTotalW)
            songLengthW = self.lala + (pygame.mixer.music.get_pos()//1000)
            print(songLengthW)
            Q.setText(str(songLengthW)+ "/" +str(songTotalW) + "secs")
            self.remainButton.hide()
            self.remainFButton.hide()
            self.remainSButton.hide()
            self.remainWLButton.hide()
            self.remainWButton.show()

    
    
    def DoubleTake(self, name, album, Q):
        # load the song 
        pygame.mixer.music.load('assets/songs/DoubleTake.mp3')
        # play the song 
        pygame.mixer.music.play()
        # song = MP3('assets/songs/DoubleTake.mp3')
        # songLength = int((song.info.length))
        # print(songLength)
        # if pygame.mixer.music.get_busy():
        #     songremains = songLength - pygame.mixer.music.get_pos()
        #     print(songremains)
        name.setText("Double Take -- Dhruv")
        album.setPixmap(QPixmap('assets/albumCovers/DoubleTakeImage.jpg').scaled(300,300))
        print('playing a song')
        self.lala = 0
        self.songLengthD(Q)
        
    def FallingFlower(self, name, album,Q):
        # load the song 
        pygame.mixer.music.load('assets/songs/FallingFlower.mp3')
        # play the song 
        # song = MP3('assets/songs/FallingFlower.mp3')
        # songLength = song.info.length
        # print(songLength)
        pygame.mixer.music.play()
        name.setText("Falling Flower -- Seventeen")
        album.setPixmap(QPixmap('assets/albumCovers/FallingFlower.jpg').scaled(300,300))
        print('playing a song')
        self.lala = 0
        self.songLengthF(Q)
    def Shino(self, name, album,Q):
        # load the song 
        pygame.mixer.music.load('assets/songs/Shino.mp3')
        # play the song 
        pygame.mixer.music.play()
        print('playing a song')
        name.setText("Shinunoga E-wa -- Fujii Kaze")
        album.setPixmap(QPixmap('assets/albumCovers/Shino Image.jpg').scaled(300,300))
        self.lala = 0
        self.songLengthS(Q)
    def WaterLofi(self, name, album,Q):
        # load the song 
        pygame.mixer.music.load('assets/songs/WaterLofi.mp3')
        # play the song 
        pygame.mixer.music.play()
        album.setPixmap(QPixmap('assets/albumCovers/Water Image.jpg').scaled(300,300))
        print('playing a song')
        name.setText("WaterLofi -- Lexin Music")
        self.lala = 0
        self.songLengthWL(Q)
    def Willow(self, name, album,Q):
        # load the song 
        pygame.mixer.music.load('assets/songs/Willow.mp3')
        # play the song 
        pygame.mixer.music.play()
        print('playing a song')
        album.setPixmap(QPixmap('assets/albumCovers/Willow Image.jpeg').scaled(300,300))
        name.setText("Willow -- Taylor Swift")
        self.lala = 0
        self.songLengthW(Q)


    def DStop(self):
        pygame.mixer.music.stop()
    def FStop(self):
        pygame.mixer.music.stop()
    def SStop(self):
        pygame.mixer.music.stop()
    def WStop(self):
        pygame.mixer.music.stop()
    def WiStop(self):
        pygame.mixer.music.stop()\
        

    def DoubleTakeStop(self):
        if self.y:
            pygame.mixer.music.pause()
            self.y = False
        else:
            pygame.mixer.music.unpause()
            self.y = True
    def FallingFlowerStop(self):
        if self.y:
            pygame.mixer.music.pause()
            self.y = False
        else:
            pygame.mixer.music.unpause()
            self.y = True
    def ShinoStop(self):
        if self.y:
            pygame.mixer.music.pause()
            self.y = False
        else:
            pygame.mixer.music.unpause()
            self.y = True
    def WaterLofiStop(self):
        if self.y:
            pygame.mixer.music.pause()
            self.y = False
        else:
            pygame.mixer.music.unpause()
            self.y = True
    def WillowStop(self):
        if self.y:
            pygame.mixer.music.pause()
            self.y = False
        else:
            pygame.mixer.music.unpause()
            self.y = True


    def DoubleTakeRewind(self):
        pygame.mixer.music.play()
        self.lala = 0
    def FallingFlowerRewind(self):
        pygame.mixer.music.play()
        self.lala = 0
    def ShinoRewind(self):
        pygame.mixer.music.play()
        self.lala = 0
    def WaterLofiRewind(self):
        pygame.mixer.music.play()
        self.lala = 0
    def WillowRewind(self):
        pygame.mixer.music.play()
        self.lala = 0


    # volume up and down
    def DoubleTakeVolumeUp(self):
        pygame.mixer.music.set_volume(1.3)
    def FallingFlowerVolumeUp(self):
        pygame.mixer.music.set_volume(1.3)
    def ShinoRewind(self):
        pygame.mixer.music.set_volume(1.3)
    def WaterLofiVolumeUp(self):
        pygame.mixer.music.set_volume(1.3)
    def WillowVolumeUp(self):
        pygame.mixer.music.set_volume(1.3)

    def DoubleTakeVolumeDown(self):
        pygame.mixer.music.set_volume(0.3)
    def FallingFlowerVolumeDown(self):
        pygame.mixer.music.set_volume(0.3)
    def ShinoVolumeDown(self):
        pygame.mixer.music.set_volume(0.3)
    def WaterLofiVolumeDown(self):
        pygame.mixer.music.set_volume(0.3)
    def WillowVolumeDown(self):
        pygame.mixer.music.set_volume(0.3)

    

    def stopSong(self):
        pygame.mixer.music.pause()
        print('stopping a song')


    def shuffle(self, name, album):
            pygame.mixer.music.stop()
            gaga = random.randint(0,4)
            self.lala = 0
            if gaga == 0:
                
                pygame.mixer.music.load(self.x[0])
                pygame.mixer.music.play()
                name.setText("Double Take -- Dhruv")
                album.setPixmap(QPixmap(self.coverList[0]).scaled(300,300))
                self.remainButton.show()
                self.remainFButton.hide()
                self.remainSButton.hide()
                self.remainWLButton.hide()
                self.remainWButton.hide()
            elif gaga == 1:
                pygame.mixer.music.load(self.x[1])
                pygame.mixer.music.play()
                name.setText("Falling Flower -- Seventeen")
                album.setPixmap(QPixmap(self.coverList[1]).scaled(300,300))
                self.remainButton.hide()
                self.remainFButton.show()
                self.remainSButton.hide()
                self.remainWLButton.hide()
                self.remainWButton.hide()
            elif gaga == 2:
                pygame.mixer.music.load(self.x[2])
                pygame.mixer.music.play()
                name.setText("Shinunoga E-wa -- Fujii Kaze")
                album.setPixmap(QPixmap(self.coverList[2]).scaled(300,300))
                self.remainButton.hide()
                self.remainFButton.hide()
                self.remainSButton.show()
                self.remainWLButton.hide()
                self.remainWButton.hide()
            elif gaga == 3:
                pygame.mixer.music.load(self.x[3])
                pygame.mixer.music.play()
                name.setText("WaterLofi")
                album.setPixmap(QPixmap(self.coverList[3]).scaled(300,300))
                self.remainButton.hide()
                self.remainFButton.hide()
                self.remainSButton.hide()
                self.remainWLButton.show()
                self.remainWButton.hide()
            elif gaga == 4:
                pygame.mixer.music.load(self.x[4])
                pygame.mixer.music.play()
                name.setText("Willow -- Taylor Swift")
                album.setPixmap(QPixmap(self.coverList[4]).scaled(300,300))
                self.remainButton.hide()
                self.remainFButton.hide()
                self.remainSButton.hide()
                self.remainWLButton.hide()
                self.remainWButton.show()
            print(gaga)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BringInWidgets()
    window.show()
    sys.exit(app.exec())
    