# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 03:00:18 2019

@author: MohamedElfatih
"""

from GameManager_3 import GameManager
from Grid_3       import Grid
from ComputerAI_3 import ComputerAI
from PlayerAI_3   import PlayerAI
from Displayer_3  import Displayer
from random       import randint
import time

def main():
    w_0 = [.2,.5,1]
    w_1 = [.1,.4,.7]
    w_2 = [.02,.04,.06]
    
    max0 = 0
    w0_max = -1
    w1_max = -1
    w2_max = -1
    for i in w_0:
        for j in w_1:
            for k in w_2:
                gameManager = GameManager()
                playerAI  	= PlayerAI()
                playerAI.w0 = i
                playerAI.w1 = j
                playerAI.w2 = k
                computerAI  = ComputerAI()
                displayer 	= Displayer()
            
                gameManager.setDisplayer(displayer)
                gameManager.setPlayerAI(playerAI)
                gameManager.setComputerAI(computerAI)
            
                v = gameManager.start()
                if v > max0:
                    max0 = v;
                    w0_max = i
                    w1_max = j
                    w2_max = k
    print(max0)
    print(w0_max)
    print(w1_max)
    print(w2_max)
                    

if __name__ == '__main__':
    main()
