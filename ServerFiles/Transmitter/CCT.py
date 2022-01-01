from pygame.locals import *
import pygame
import os





pygame.init()
pygame.joystick.init()
screen=pygame.display.set_mode((100,100),DOUBLEBUF,32)
with open("config.cctf") as configfile:
    configfile=configfile.readlines()
    for commands in configfile:
        exec(str(commands))
Controller = pygame.joystick.Joystick(0)
Controller.init()



def logs_sent_to_panel():
    LogsFile=open("CCTP.log","w")
    LogsFile.write(Controller.get_name()+"\n")
    LogsFile.write(commands[0])
    LogsFile.write(commands[1])
    LogsFile.write(commands[2])
    LogsFile.write(commands[3])
    
    LogsFile.close()
def commands_sent_to_server():
    SegmentFile=open("../ServerSender/index.html","w")
    SegmentFile.writelines(commands)
    SegmentFile.close()
               

commands = ["NULL\n","NULL\n","NULL\n","NULL\n"]
while(True):
    commands_sent_to_server()
    logs_sent_to_panel()
    for event_get in pygame.event.get():
        number_of_axes = Controller.get_numaxes()
        os.system("cls")
        for i in range(len(commands)):
            commands[i]="NULL\n"
        for move in range(number_of_axes):
            CurrentAxisPosition=Controller.get_axis(move)
            if move==0 and Controller.get_button(3)==True:
                if (CurrentAxisPosition>0):
                    commands[move] = "RIGHT\n"
                else:
                    commands[move] = "LEFT\n"
            if move==1 and Controller.get_button(3)==True :
                if (CurrentAxisPosition>0):
                    commands[move]="DOWN\n"
                else:
                    commands[move]="UP\n"
            if move==2 and Controller.get_button(3)==True :
                commands[move]="NULL\n"
            if move==3 and Controller.get_button(2)==True:
                if(CurrentAxisPosition>0):
                    commands[move]="LEFT\n"
                else:
                    commands[move]="RIGHT\n"
            if move==4 and Controller.get_button(3)==True :
                pass

        
    
    
