#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:32:46 2020

@author: thanhquynh
"""

import pandas as pd
import numpy as np
import array as arr
class temp:
    a0 = []
    #df_tmp = pd.DataFrame()
    a1 = []
    a2 = []
    X = []
    #d = []
    #e = []
    
    def __init__(self):
        print("")
    def readFile(self):
        self.X = pd.ExcelFile('data.xlsx')
        #type(X)
        
    
    
    def getQueue(self):
        a0 = pd.read_excel(self.X, '2017')
        a1 = pd.read_excel(self.X, '2018')
        a2 = pd.read_excel(self.X, '2019')
        
        coldata0 = np.size(a0, 1)
        coldata1 = np.size(a1, 1)
        coldata2 = np.size(a2, 1)
        
        
        for i in range(0,coldata0-1):
                self.a0 = self.a0 + (a0['Th'+str(i+1)].values.tolist())
                
        for i in range(0,coldata1-1):
                self.a1 = self.a1 + (a1['Th'+str(i+1)].values.tolist())
                
        for i in range(0,coldata2-1):
                self.a2 = self.a2 + (a2['Th'+str(i+1)].values.tolist())
                
        self.a0 = [k for k in self.a0 if (str(k) != 'nan')]
        self.a1 = [k for k in self.a1 if (str(k) != 'nan')]
        self.a2 = [k for k in self.a2 if (str(k) != 'nan')]
        
    def getCondition(self, a):
        run.readFile()
        run.getQueue()
        i = 0
        queue = []
        e = []
        E = []
        eo = []
        upup = []
        upupdown = []
        f = []
        g = []
        #Y: 1 is check updown (consecutive), 
        #   2 is check even odd (consecutive)
        #   3 is check updown (broken) 
        #   4 is check even odd (broken)
        Y = int(input('input for method: '))
        n = int(input('input1: '))
        m = int(input('input2: '))
        ngay = int(input('input ngay: '))
        while i < len(a)-1:
            if len(queue) < ngay:
                queue.append(a[i])
                #print(queue)
            else:
                del queue[0]
                queue.append(a[i])
                #print(queue)
            
            if Y == 0:
                self.updown(i, m, n, queue, upup, upupdown, ngay, a)
            if Y == 1:
                self.evenodd(i, m, n, queue, e, eo, ngay, a)                
            if Y == 2:
                self.cutNdayupdown(i, n, queue, f, g, ngay, a)
            if Y == 3:
                self.cutNdayevenodd(i, n, queue, f, g, ngay, a)
            i = i + 1
            
        if Y == 0 and n == 1:
            Upup = np.asarray(upup)
            up = [k for k in Upup[:,ngay] if k >= 50]
            down = [k for k in Upup[:,ngay] if k < 50]
            #print(Upup)
            print(ngay, 'ngay up: ' + str(len(Upup)))
            print(ngay, 'ngay up, ngay tiep theo up: ' + str(len(up)))
            print(ngay, 'ngay up, ngay tiep theo down: ' + str(len(down)))
            
            Upupdown = np.asarray(upupdown)
            up1 = [k for k in Upupdown[:,ngay + 1] if k >= 50]
            down1 = [k for k in Upupdown[:,ngay + 1] if k < 50]
            print(ngay, 'ngay up, ngay tiep theo down, ngay sau do up: ' + str(len(up1)))
            print(ngay, 'ngay up, ngay tiep theo down, ngay sau do down: ' + str(len(down1)))
            #print(Upup)
            #print(Upupdown)
            
        if Y == 0 and n == 0:
            Upup = np.asarray(upup)
            up = [k for k in Upup[:,ngay] if k >= 50]
            down = [k for k in Upup[:,ngay] if k < 50]
            print(ngay, 'ngay down: ' + str(len(Upup)))
            print(ngay, 'ngay down, ngay tiep theo up: ' + str(len(up)))
            print(ngay, 'ngay down, ngay tiep theo down: ' + str(len(down)))
            #print(Upup)
            Upupdown = np.asarray(upupdown)
            up1 = [k for k in Upupdown[:,ngay + 1] if k >= 50]
            down1 = [k for k in Upupdown[:,ngay + 1] if k < 50]
            print(ngay, 'ngay down, ngay tiep theo up, ngay sau do up: ' + str(len(up1)))
            print(ngay, 'ngay down, ngay tiep theo up, ngay sau do down: ' + str(len(down1)))
            
        if Y == 1 and n == 0:   
            E = np.asarray(e)
            l = [k for k in E[:,ngay] if k%2 == 1]
            o = [k for k in E[:,ngay] if k%2 == 0]
            print(ngay, 'ngay chan: ' + str(len(e)))
            print(ngay, 'ngay chan, ngay tiep theo le: ' + str(len(l)))
            print(ngay, 'ngay chan, ngay tiep theo chan: ' + str(len(o)))
                
            EO = np.asarray(eo)
            l1 = [k for k in EO[:,ngay + 1] if k%2 == 1]
            o1 = [k for k in EO[:,ngay + 1] if k%2 == 0]
            print(ngay, 'ngay chan, ngay tiep theo le, ngay sau do le: ' + str(len(l1)))
            print(ngay, 'ngay chan, ngay tiep theo le, ngay sau do chan: ' + str(len(o1)))
            #print(EO)
            
        if Y == 1 and n == 1:   
            E = np.asarray(e)
            l = [k for k in E[:,ngay] if k%2 == 1]
            o = [k for k in E[:,ngay] if k%2 == 0]
            print(ngay, 'ngay le: ' + str(len(e)))
            print(ngay, 'ngay le, ngay tiep theo le: ' + str(len(l)))
            print(ngay, 'ngay le, ngay tiep theo chan: ' + str(len(o)))
                
            EO = np.asarray(eo)
            l1 = [k for k in EO[:,ngay + 1] if k%2 == 1]
            o1 = [k for k in EO[:,ngay + 1] if k%2 == 0]
            print(ngay, 'ngay le, ngay tiep theo chan, ngay sau do le: ' + str(len(l1)))
            print(ngay, 'ngay le, ngay tiep theo chan, ngay sau do chan: ' + str(len(o1)))
        
        if Y == 2 and n == 0:
            B = np.asarray(f)
            up = [x for x in B[:,ngay] if (x >= 50)]
            print(ngay, 'ngay down lien tiep: ' + str(len(g)))
            print('Ngay thu', ngay + 1 ,'up: ' + str(len(up)))
            
            
        if Y == 2 and n == 1:
            B = np.asarray(f)
            up = [x for x in B[:,ngay] if (x < 50)]
            print(ngay, 'ngay up lien tiep: ' + str(len(g)))
            print('Ngay thu', ngay + 1 ,'down: ' + str(len(up)))
            
         
        if Y == 3 and n == 1:
            B = np.asarray(f)
            up = [x for x in B[:,ngay] if (x%2 == 0)]
            print(ngay, 'ngay le lien tiep: ' + str(len(g)))
            print('Ngay thu', ngay + 1 ,'chan: ' + str(len(up)))
            
        if Y == 3 and n == 0:
            B = np.asarray(f)
            up = [x for x in B[:,ngay] if (x%2 == 1)]
            print(ngay, 'ngay chan lien tiep: ' + str(len(g)))
            print('Ngay thu', ngay + 1 ,'le: ' + str(len(up)))
            
    

    def evenodd(self, i, m, n, queue, e, eo, ngay, a):
        if len(queue) == ngay and len([x for x in queue if (x%2 == n)]) == ngay:
            queue.append(a[i+1])
            e.append(list(queue))
            if a[i+1]%2 == m and i < len(a) - 2:
                queue.append(a[i+2])
                eo.append(list(queue))
                del queue[len(queue)-1]
            del queue[len(queue)-1]
            
            
    def updown(self, i, m, n, queue, upup, upupdown, ngay, a):
        if len(queue) == ngay and len([x for x in queue if self.checkUpDown(x) == n]) == ngay:
            queue.append(a[i+1])
            upup.append(list(queue))
            if self.checkUpDown(a[i+1]) == m and i < len(a) - ngay:
                queue.append(a[i+2])
                upupdown.append(list(queue))
                del queue[len(queue) - 1]
            del queue[len(queue) - 1]
                
                
                
    def cutNdayupdown(self, i, n, queue, f, g, ngay, a):
        if len(queue) == ngay and len([x for x in queue if self.checkUpDown(x) == n]) == ngay:
            queue.append(a[i+1])
            f.append(list(queue))
            del queue[:(len(queue) - 1)]
            g.append(a[i+1])
            i = i + 1
           
    def cutNdayevenodd(self, i, n, queue, f, g, ngay, a):
        if len(queue) == ngay and len([x for x in queue if (x%2 == n)]) == ngay:
            queue.append(a[i+1])
            f.append(list(queue))
            del queue[:(len(queue) - 1)]
            g.append(a[i+1])
            i = i + 1
            
    def checkUpDown(self, x):
        if x>=50:
            return 1
        else:
            return 0


    
        
    
    
    
    def display(self):
        run.getQueue()
        
        #print(self.a2)
        #run.evenodd()
        run.getCondition(self.a0)
        run.getCondition(self.a1)
        run.getCondition(self.a2)
        #a = del self.a
        #print(a)
        
        
run = temp()
run.readFile()

run.display()