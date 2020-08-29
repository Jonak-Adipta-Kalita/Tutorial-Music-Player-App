######################################## Imports ################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

######################################## root methods ################################
root = Tk()
root.geometry('1100x500+200+50')
root.title('Jak Music Player')
root.iconbitmap('Papirus-Team-Papirus-Apps-Enjoy-music-player.ico')
root.resizable(False,False)
root.configure(bg='powder blue')

######################################## functions ################################
def UnmuteMusic():
    global CurrentVol
    root.UnmuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(CurrentVol)
    AudioStatusLabel.configure(text='Playing...')

def MuteMusic():
    global CurrentVol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    CurrentVol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    AudioStatusLabel.configure(text='Mute...')

def ResumeMusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing...')

def StopMusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped...')

def VolumedownMusic():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def VolumeupMusic():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def PauseMusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused...')

def PlayMusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.set_volume(0.4)
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing...')

    song = MP3(ad)
    TotalSongLength = int(song.info.length)
    ProgressbarMusic['maximum'] = TotalSongLength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=TotalSongLength))))
    def ProgressbarMusicTick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic['value'] = CurrentSongLength
        ProgressbarMusic.after(2,ProgressbarMusicTick)
    ProgressbarMusicTick()

def MusicURL():
    try:
        dd = filedialog.askopenfilename(intialdir='F:\Hard-disk\Project\Works\JAK Music Player\Music',title='Select Audio File',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename()
    audiotrack.set(dd)

def createwidthes():
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel
######################################## Label #############################
    TrackLabel = Label(root,text='Select Audio Track: ',bg='powder blue',font=('times',15,' italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text='',bg='powder blue',font=('times',15,' italic bold'),width=7)
    AudioStatusLabel.grid(row=2,column=1)

######################################## Entry box #############################
    TrackLabelEntry = Entry(root,font=('times',16,' italic bold'),width=45,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

######################################## Buttons #############################
    BrowseButton = Button(root,text='Scearch',bg='pink',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=MusicURL)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root, text='Play',bg='green2',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=PlayMusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=ResumeMusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.PauseButton = Button(root,text='Pause',bg='yellow',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=PauseMusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.MuteButton = Button(root,text='Mute',font=('times',10,' italic bold'),width=20,bg='yellow',activebackground='violet',bd=8,command=MuteMusic)
    root.MuteButton.grid(row=5,column=2,padx=20,pady=20)
    root.MuteButton.grid_remove()

    root.UnmuteButton = Button(root,text='Unmute',font=('times',10,' italic bold'),width=20,bg='yellow',activebackground='violet',bd=8,command=UnmuteMusic)
    root.UnmuteButton.grid(row=5,column=2,padx=20,pady=20)
    root.UnmuteButton.grid_remove()

    VolumeUpButton = Button(root,text='VolumeUp',bg='Blue',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=VolumeupMusic)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',bg='Red',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=StopMusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton = Button(root,text='VolumeDown',bg='Blue',font=('times',12,' italic bold'),width=20,bd=8,activebackground='violet',command=VolumedownMusic)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

######################################## Progressbar Volume #############################
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,columnspan=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

######################################## Progressbar Music #############################
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)


######################################## Global Variables ################################
audiotrack = StringVar()
CurrentVol = 0
TotalSongLength = 0
count = 0
text = ''

######################################## Sliders ################################
ss = 'Developed by Jonak Adipta Kalita'
SliderLabel = Label(root,text=ss,bg='powder blue',font=('times',40,' italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)

def IntroLabelTrick():
    global count,text
    if (count >=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTrick)

######################################## Function Wrork ################################
IntroLabelTrick()
mixer.init()
createwidthes()

######################################## loop #######################################
root.mainloop()

######################################## End ########################################
