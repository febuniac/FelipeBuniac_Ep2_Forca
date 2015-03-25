# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:33:03 2015

@author: Felipe
"""

import turtle
#Importa a biblioteca do turtle
janela = turtle.Screen() 
#Define e importa a janela da biblioteca do turtle
janela.bgcolor("orange") 
#Definição da cor da janela
janela.title("Jogo da Forca")
#Define o nome da janela do turtle
poste = turtle.Turtle()
#Definição do que define o lapis ( A própia tartaruga)
poste.pensize(20)
#Define a grossura do meu lapis
poste.speed(8)
#definindo a velocidade do lapis do turtle
poste.penup()
#penup tira o lapis do papel e não desenha nada
poste.setpos(-300,-60)
#definição de onde o lapis irá começar a desenhar
poste.pendown()
#pendown põe o lapis de volta no papel para desenhar
poste.forward(80)
#Poste desenha para frente 80 unidades
poste.back(40)
#Lapis volta para o meio da base da forca para desenhar para cima
poste.left(90)
#lapis desenha vira 90 unidades para esquerda (vai para cima)
poste.forward(180)
#lapis desenha 180 unidades para cima
poste.right(90)
#lapis vira 90 unidades para direita
poste.forward(80)
#lapis desenha 80 unidades para frente
poste.right(90)
#lapis vira 90 unidades para direita
poste.forward(30)
#lapis desenha 30 unidades para baixo
arquivo = open("palavras_forca.txt","r+", encoding='utf-8')
prinr(arquivo)
janela.exitonclick()
