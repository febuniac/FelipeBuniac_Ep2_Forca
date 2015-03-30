# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:33:03 2015

@author: Felipe
"""

import turtle
import random
#Importa a biblioteca do turtle e do random
#import tkinter (funçao que pergunta se quer recomeçar)
space = '_____   ' 
#definição dos tracinhos das palavras
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



def tronco():
        poste = turtle.Turtle()
        poste.speed(8) # Constroi o Tronco 
        poste.pensize(10)
        poste.penup()
        poste.setpos(-180,65)
        poste.pendown()
        poste.right(90)
        poste.forward(100)
        poste.color('black')
        



def braco_esquerdo():
    
    poste=turtle.Turtle()         #Constroi o braço esquerdo
    poste.speed(8)
    poste.pensize(10)
    poste.penup()
    poste.setpos(-180, 35)
    poste.pendown()
    poste.right(135)
    poste.forward(40)
    poste.color("black")
    
braco_esquerdo()
def braco_direito():
    
    poste=turtle.Turtle()         #Constroi o braço direito
    poste.speed(8)
    poste.pensize(10)
    poste.penup()
    poste.setpos(-180, 35)
    poste.pendown()
    poste.right(400)
    poste.forward(40)
    poste.color("black")
    

def perna_direita():
    
    poste=turtle.Turtle()
    poste.speed(8)
    poste.pensize(10)
    poste.penup()
    poste.setpos(-180,-35)
    poste.pendown()
    poste.right(40)
    poste.forward(40)
    poste.color("black")
    
    
perna_direita()
    
def perna_esquerda():
    
    poste=turtle.Turtle()
    poste.speed(8)
    poste.pensize(10)
    poste.penup()
    poste.setpos(-180,-35)
    poste.pendown()
    poste.left(-140)
    poste.forward(40)
    poste.color("black")


arquivo = open("palavras_forca.txt", encoding='utf-8')
#Abre o arquivo (palavras_forca em formato text0(txt))e como ele esta codificado(utf-8)
ler=arquivo.readlines()

#Define ler como ler as linhas do arquivo
numero = random.randint(0, len(ler))
#escolhe palavras de forma aleatória de acordo com a posição na lista
#comprimento = len(arquivo)

poste.penup()
poste.setpos(5,-60)
poste.write(len(ler[numero])*space)
#Tira os erros da frase.
print(ler[numero])
#print a palvra escolhida(a palavra é escolhida como um numero da lista)
lista_limpa = []
for x in ler:
    y = x.strip()
    if y != "":
        lista_limpa.append(y)
ler = lista_limpa
poste.penup()
poste.setpos(5,-60)
poste.write(len(ler[numero])*space)
#Tira os erros da frase.
print(ler[numero])
#print a palvra escolhida(a palavra é escolhida como um numero da lista)
lista_limpa = []
errado = 0
certo = 0
while errado<6 and certo<len(ler[numero]):
    caixa =janela.textinput("Digite uma letra", "Digite uma letra")
    
    for i in range(len(ler[numero])):
        if caixa == ler[numero][i]:
            print(i)
            poste.setpos(5 + 20*(i),-60)
            poste.write(caixa,font=("Arial",30,"normal"))
    #i é a posicao da letra correta    
    # i é uma variavel que aumenta de 1 em 1 (i comeca em zero e se for menor que o tamanhao da palavra vai aumentando de 1 em 1 )
    if caixa not in ler[numero]:
        errado+=1
        if errado == 1:
            cabeca()
        elif errado == 2:
            tronco()
        elif errado == 3:
            braco_esquerdo()
        elif errado == 4:
            braco_direito()
        elif errado == 5:
            perna_direita()
        elif errado == 6:
            perna_esquerda()
    if errado==6:
        poste.write('O jogo acabou! ENFORCADO!!', align="center",font=("Arial",30) )
        break
            
 #from random import randint
#x = randint(0,15)
#palavra = arquivo[x]
#comprimento = len(arquivo)
#poste.setpos(-100,-200)
#poste.left(90)

#Para escrever os tracinhos das letras
#assina e assina
#for i in range (len(numero0)):
   # if guess == numero0[i]
    
 #   poste.speed(100)
  #  poste.color("black")
   # poste.pendown()
   # poste.forward(20)
    #poste.penup()
    #poste.forward(15)
    #poste.pendown()
    #acertos =[]
    #erros=[]
    #i=0   
    


janela.exitonclick()

arquivo = open('entrada.csv','r')
leitura=arquivo.read(1000)
lista = leitura.split(',')
import random
palavra = random.choice(lista)
print(palavra)


