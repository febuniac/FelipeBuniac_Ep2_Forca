# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:33:03 2015

@author: Felipe
"""

import turtle
import random
#Importa a biblioteca do turtle
janela = turtle.Screen() 
#Define e importa a janela da biblioteca do turtle
janela.bgcolor("orange") 
#Definição da cor da janela
janela.title("Jogo da Forca")
#Define o nome da janela do turtle
poste = turtle.Turtle()
#Definição do que define o lapis ( A própia tartaruga)
poste.pensize(15)
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
poste.forward(200)
#lapis desenha 180 unidades para cima
poste.right(90)
#lapis vira 90 unidades para direita
poste.forward(80)
#lapis desenha 80 unidades para frente
poste.right(90)
#lapis vira 90 unidades para direita
poste.forward(30)
#lapis desenha 30 unidades para baixo
arquivo = open("palavras_forca.txt", encoding='utf-8')
#Abre o arquivo (palavras_forca em formato text0(txt))e como ele esta codificado(utf-8)
ler=arquivo.readlines()
#Define ler como ler as linhas do arquivo
numero = random.randint(0, len(ler))
#escolhe palavras de forma aleatória de acordo com a posição na lista
print(ler[numero])
#print a palvra escolhida(a palavra é escolhida como um numero da lista)
def cabeca():   
        poste = turtle.Turtle()          #Constroi a cabeca
        poste.speed(8)
        poste.pensize(10)
        poste.penup()
        poste.setpos(-180,105)
        poste.left(180)
        poste.pendown()
        poste.circle(20)
        poste.color("black")
cabeca()


janela.exitonclick()

