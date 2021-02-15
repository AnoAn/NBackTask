# coding=utf-8

from psychopy import visual, data, core, event, gui
import random
import datetime #library to get the current date
import pyglet
import csv
import itertools

tmpData = str(datetime.datetime.now())[0:10] #get the current date
tmpOra = str(datetime.datetime.now())[11:19]

correctCount = 0

def nBackTaskProva(win, datafile, datafileAll, clock, fix, letter, stimPool, trialType, memLoad, subj, age, gender, condition='', keys=['j','f'], RT=0, rGiven=0, stop=0, choice=0, correct=None, trialNum=0):
    global tmpData, tmpOra, correctCount
    for l in stimPool:
        rGiven=0
        if stop==1:
            break
        event.clearEvents()
        letter.setText(l[0])
        trialNum+=1
        if trialNum==31:
            break
        timeS=clock.getTime()
        recordKeyPress=1
        
        if memLoad==1:
            if trialNum==1:
                letter.draw()
                win.flip()
                core.wait(1.5)
                correct=2
                rGiven=1
        elif memLoad==2:
            if trialNum<=2:
                letter.draw()
                win.flip()
                core.wait(1.5)
                correct=2
                rGiven=1
        
        while True:
            letter.draw()
            win.flip()
            if int(l[1])==1 and event.getKeys(keyList=keys[1]) or int(l[1])==0 and event.getKeys(keyList=keys[0]):
                rGiven=1
                correct=1
                correctCount+=1
                RT=str(round(float(clock.getTime()-timeS),4)).replace('.',',')
                print correct, RT
            if int(l[1])==0 and event.getKeys(keyList=keys[1]) or int(l[1])==1 and event.getKeys(keyList=keys[0]):
                rGiven=1
                correct=0
                RT=str(round(float(clock.getTime()-timeS),4)).replace('.',',')
                print correct, RT
            if rGiven==1:
                if correct==0:
                    letter.setColor("red")
                    if int(l[1])==0:
                        choice=1
                    elif int(l[1])==1:
                        choice=0
                elif correct==1:
                    letter.setColor("green")
                    if int(l[1])==0:
                        choice=0
                    elif int(l[1])==1:
                        choice=1
                letter.draw()
                win.flip()
                core.wait(0.5)
                datafile.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                datafileAll.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                win.flip()
                core.wait(0.5)
                letter.setColor("white")
                break
            if event.getKeys(keyList=['escape']):
                stop = 1
                datafile.close()
                datafileAll.close()
                break
            else:
                continue
            break





def nBackTask(win, datafile, datafileAll, clock, fix, letter, stimPool, trialType, memLoad, subj, age, gender, condition='', keys=['f','j'], RT=0, rGiven=0, stop=0, choice=0, correct=None, correctCount=0, trialNum=0):
    trialNum=0
    stop=0
    for l in stimPool:
        rGiven=0
        if stop==1:
            break
        event.clearEvents()
        letter.setText(l[0])
        trialNum+=1
        #if trialNum==11:
            #break
        timeS=clock.getTime()
        recordKeyPress=1
        while True:
            if clock.getTime()-timeS <=.05:
                letter.draw()
            win.flip()
            if recordKeyPress==1:
                if int(l[1])==1 and event.getKeys(keyList=keys[1]) or int(l[1])==0 and event.getKeys(keyList=keys[0]):
                    rGiven=1
                    correct=1
                    correctCount+=1
                    RT=str(round(float(clock.getTime()-timeS),4)).replace('.',',')
                    recordKeyPress=0
                    print correct, RT
                if int(l[1])==0 and event.getKeys(keyList=keys[1]) or int(l[1])==1 and event.getKeys(keyList=keys[0]):
                    rGiven=1
                    correct=0
                    RT=str(round(float(clock.getTime()-timeS),4)).replace('.',',')
                    recordKeyPress=0
                    print correct, RT
            if clock.getTime()-timeS >=2.5:
                if rGiven==0:
                    correct=2
                    RT="2,5"
                    choice=2
                    print correct
                if correct==0:
                    if int(l[1])==0:
                        choice=1
                    elif int(l[1])==1:
                        choice=0
                elif correct==1:
                    if int(l[1])==0:
                        choice=0
                    elif int(l[1])==1:
                        choice=1
                if memLoad==1:
                    datafile.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                    datafileAll.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                    break
                elif memLoad==2:
                    datafile.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                    datafileAll.write("%s;%s;%s;%s;%s;%s;%i;%i;%s;%s;%i;%i;%i;%s;\n"%(subj, age, gender, tmpData, tmpOra, condition, memLoad,trialNum,trialType,l[0],int(l[1]),choice,correct, RT))
                    break
            if event.getKeys(keyList=['escape']):
                stop = 1
                datafile.close()
                datafileAll.close()
                break
            else:
                continue
            break
            