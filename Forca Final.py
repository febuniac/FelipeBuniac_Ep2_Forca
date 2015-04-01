# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:33:03 2015

@author: Felipe
"""

import turtle
import random
import time
recomecar = True or False
while recomecar == True:
    placar_certo = turtle.Turtle()
    placar_errado = turtle.Turtle()
    #Importa a biblioteca do turtle, do random, tkinter e time
    space = '_ ' 
    #definição dos tracinhos das palavras
    janela = turtle.Screen()
     #Define e importa a janela da biblioteca do turtle
    janela.bgcolor("orange") 
    #Definição da cor da janela
    janela.title("Jogo da Forca")
    #Define o nome da janela do turtle
    
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
        
            poste = turtle.Turtle()      #Constroi o Tronco
            poste.speed(8)
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
        
        poste=turtle.Turtle()     #Constroi a perna direita
        poste.speed(8)
        poste.pensize(10)
        poste.penup()
        poste.setpos(-180,-35)
        poste.pendown()
        poste.right(40)
        poste.forward(40)
        poste.color("black")
        
        
    
        
    def perna_esquerda():
        
        poste=turtle.Turtle()     #Constroi a perna esquerda
        poste.speed(8)
        poste.pensize(10)
        poste.penup()
        poste.setpos(-180,-35)
        poste.pendown()
        poste.left(-140)
        poste.forward(40)
        poste.color("black")
    
    
    
    
    
    
    poste = turtle.Turtle()                               
    #Definição do que define o lapis ( A própia tartaruga)
    poste.hideturtle()
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
    #Define ler como Ler as linhas do arquivo
    lista_limpa = []
    #define lista_limpa como uma lista vazia
    for x in ler:
    #Se x estiver na lista de palavras entra no for
        y = x.strip()
    #passa por todos os caracteres da lista ler
        if y != "":
           y = y.replace ('ã','a')
           y = y.replace ('á','a')
           y = y.replace ('â','a')
           y = y.replace ('ó','o')
           y = y.replace ('õ','o')
           y = y.replace ('ô','o')
           y = y.replace ('í','i')
           y = y.replace ('ê','e')
           y = y.replace ('é','e')
           y = y.replace ('ú','u')
    #Trocando letras acentuadas por letras sem acentuo
           lista_limpa.append(y.upper())
    #A lista passa a ser inteira em letras maiusculas
    ler = lista_limpa
    # iguala a lista ler a lista_limpa
    numero = random.randint(0, len(ler)-1)
    #escolhe palavras de forma aleatória de acordo com a posição na lista
    #comprimento = len(arquivo)
    poste.penup()
    poste.setpos(-140,-60)
    for i in ler[numero]:
        if i == " ":
            poste.penup()
            poste.setheading(0)
            poste.forward(36)
            
        else:
            poste.write(space,move = True, font=("Monaco",30,"normal"))
    #Tira os erros da frase.
    print(ler[numero])
    #print a palvra escolhida(a palavra é escolhida como um numero da lista)
    
    tentativas = []
    #numero de tentativas
    tentturtle = turtle.Turtle()
    tentturtle.hideturtle()
    errado = 0
    certo = 0
    
    while errado<6 and certo<len(ler[numero]):
        caixa =janela.textinput("Digite uma letra", "Digite uma letra:")
        caixa = caixa.upper()
        if len(caixa)>1:
             tentturtle.penup()
             tentturtle.setpos(60,50)
             tentturtle.write("Não ponha mais de uma letra!", False, align="center",font=("Arial",36))
             time.sleep(1)
             tentturtle.clear()
             continue
        if caixa in tentativas:
            tentturtle.write("Ja inserido", False, align="center",font=("Arial",36))
            time.sleep(1)
            tentturtle.clear()
            continue
       
        else:
            tentativas.append(caixa)
        poste.setpos(80,50)
        poste.write("Erros:",True, font=("Monaco",30,"normal"))
        for i in tentativas:
            if i not in ler[numero]:
                poste.write(i,True, font=("Monaco",30,"normal"))     
        for i in range(len(ler[numero])):
            if caixa == ler[numero][i]:
                certo+=1
                poste.setpos(-140 + 36*(i),-60)
                poste.write(caixa,font=("Monaco",30,"normal"))
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
            poste.setpos(100,30)
            #poste.pensize(20)
            poste.write('O jogo acabou! ENFORCADO!!', align="center",font=("Monaco",50) )
            
        if certo==len(ler[numero]):
            poste.setpos(100,30)
            #poste.pensize(20)
            poste.write('Parabens!!! Você ganhou o jogo!',align="center",font=("Monaco",50))
            
        #x = janela.textinput("Deseja jogar Novamente", "Deseja Jogar Novamente?")
        #if x == "sim": 
            #errado = 7
            #certo = len(ler[numero])+1 
        else:
            
            placar_certo.penup()
            placar_errado.penup()
            placar_certo.hideturtle()
            placar_errado.hideturtle()
    
    
            poste.penup()
            poste.setpos(160,180)
            poste.pensize(10)
            poste.write("ERROS:")
            
            placar_errado.reset()
            placar_errado.penup()
            placar_errado.setpos(210,180)
            placar_errado.write(errado-y.count(" "))
            placar_errado.hideturtle()
            
            poste.penup()
            poste.setpos(155,190)
            poste.pensize(10)
            poste.write("ACERTOS:")
        
            placar_certo.reset()
            placar_certo.penup()
            placar_certo.setpos(210,190)
            placar_certo.write(certo-y.count(" "))
            placar_certo.hideturtle()
            poste.penup()
            poste.setpos(160,180)
            poste.pensize(10)
            
        if errado==6 or certo == len(ler[numero]):
                    jogarnovamente = janela.textinput("Fim do jogo", "Quer jogar novamente? True(sim) ou False?(não)")
                    if jogarnovamente == True:
                        recomecar = True
                        acertos = 7
                        erros = 7
                        placar_errado.reset()
                        placar_certo.reset()
                        poste.reset()
         
                   
                    if jogarnovamente == False:
                        recomecar = False
                        poste.reset()
                        poste.penup()
                        poste.setpos(-200,180)
                        poste.pensize(10)
                        poste.write("Clique na tela para terminar",font=("Arial", 28))
                        break
          
    print(errado)
    
    print(certo)           
    janela.exitonclick()
         
    
            
    
        
            