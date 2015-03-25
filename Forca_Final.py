# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:33:03 2015

@author: Felipe
"""

import turtle
#Importa a biblioteca do turtle
window = turtle.Screen() 
#Define e importa a janela da biblioteca do turtle
window.bgcolor("orange")
#Definição da cor da janela
window.title("Jogo da Forca")
#Define o nome da janela do turtle
poste = turtle.Turtle()
#Definição do que define o lapis ( A própia tartaruga)

poste.speed(8)
poste.penup()
poste.setpos(-250,0)
poste.pendown()
poste.forward(80)
poste.back(40)
poste.left(90)
poste.forward(180)
poste.right(90)
poste.forward(80)
poste.right(90)
poste.forward(30)
window.exitonclick()

