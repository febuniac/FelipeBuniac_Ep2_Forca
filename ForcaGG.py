# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:39:47 2015

@author: Felipe
"""


import turtle
import random
import time


o = open("palavras_forca.txt", encoding="utf-8") # abre arquivo entrada.txt

p = o.readlines()  # le o arquivo e coloca em lista p 

lista = []
for ln in p:
    c = ln.strip()
    if c != "":
        lista.append(c) #limpando

print(lista)

n= len(lista) - 1
pn = random.randint(0,n)
palavra = lista[pn] #escolha palavra

palavram = palavra.upper()

print(palavra) 

x= len(palavra)#qnts espaços



espaco = []

start = 0
while start != -1:
    start = palavra.find(" ", start)
    espaco.append(start)
    if start!= -1:
        start += 1
        
    

del espaco[-1]



del lista[pn]
tela = turtle.Screen() 
tela.bgcolor("orange")



tortugal = turtle.Turtle()

tortugal.pen(shown =False,fillcolor="blue",pencolor="black")
tortugal.penup()

#########################################33

tortuga = turtle.Turtle()
tortuga.speed(50)


tortuga.pen(shown =False,fillcolor="blue",pencolor="black")
tortuga.penup()

tortuga.setpos(-350,100)
####################################################

tartarugaf = turtle.Turtle()
tartarugaf.penup()


tartarugaf.pen(shown =False,fillcolor="black",pencolor="black")
tartarugaf.pensize(8)
tartarugaf.setpos(-250 , -250)
tartarugaf.pendown()
tartarugaf.left(90)
tartarugaf.forward(400)
tartarugaf.right(90)
tartarugaf.forward(100)
tartarugaf.right(90)
tartarugaf.forward(95)
tartarugaf.penup()
tartarugaf.pen(shown =False,fillcolor="red",pencolor="black")


tortugam = turtle.Turtle()
tortugam.pen(shown =False,fillcolor="red",pencolor="red")


tartarugac = turtle.Turtle()
tartarugac.penup()
tartarugac.pen(shown =False,fillcolor="red",pencolor="red")


tortuga.color("red")

f = 0#finalizar
i = 0#qntdade de _

letras = []

t = 0

while t != x: #x = len(palavra)
    letras.append(palavra[t].upper()) #letras
    t += 1




while i != x: #x = len(palavra)
    
    
    tortuga.setpos(i*35-x*17.5,-300)
    if palavra[i] == " " :
        
        tortuga.write(" ", False, align="left",font=("Arial",30))
    else:
        tortuga.write("_ ", False, align="left",font=("Arial",30))
    i +=1



acertos = 0
erros = 0

tentativas = []

teste = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Â","Á","À","Ã","É","Í","Ó","Õ","Ô","Ò","Ú"]
teste2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

e1 = 0
e2 = 0
e3 = 0
e4 = 0        
e5 = 0        
e6 = 0 
while acertos < x-len(espaco) and erros != 6: #x = len(palavra)

    if erros != 6:
    
        
        chute = tela.textinput("Chute", "Qual seu chute?")
        chutee = chute.upper()

        w = 0

        while w < len(palavra):

                        if letras[w] == "Ã" and chutee == "A":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("Ã", False, align="center",font=("Arial",25))
                        
                            acertos += 1
                        
                        
                        
                        if letras[w] == "Á" and chutee == "A":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("Á", False, align="center",font=("Arial",25))
                            
                            acertos += 1
                            
                                            
                            
                        if letras[w] == "Â" and chutee == "A":
                            tortugal.setpos(w*35-x*16,-290)
        
                            tortugal.write("Â", False, align="center",font=("Arial",25))
        
                            acertos += 1        
        
        
                        if letras[w] == "À" and chutee == "A":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("À", False, align="center",font=("Arial",25))                    
        
                            acertos += 1        
                            
        
                        if letras[w] == "É" and chutee == "E":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("É", False, align="center",font=("Arial",25))
                            
                            acertos += 1
        
                        if letras[w] == "Í" and chutee == "I":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("Í", False, align="center",font=("Arial",25))
        
                            acertos += 1
        
                        if letras[w] == "Ó" and chutee == "O":
                            tortugal.setpos(w*35-x*16,-290)
                
                            tortugal.write("Ó", False, align="center",font=("Arial",25))
                            
                            acertos += 1
                        
                        if letras[w] == "Ô" and chutee == "O":
                            tortugal.setpos(w*35-x*16,-290)
                        
                            tortugal.write("Ô", False, align="center",font=("Arial",25))
                        
                            acertos += 1
                        
                        
                        if letras[w] == "Ò" and chutee == "O":
                            tortugal.setpos(w*35-x*16,-290)
                        
                            tortugal.write("Ò", False, align="center",font=("Arial",25))
                        
                            acertos += 1
                        
                        if letras[w] == "Õ" and chutee == "O":
                            tortugal.setpos(w*35-x*16,-290)
                        
                            tortugal.write("Õ", False, align="center",font=("Arial",25))
                        
                            acertos += 1
                        
                        if letras[w] == "Ú" and chutee == "U":
                            tortugal.setpos(w*35-x*16,-290)
                        
                            tortugal.write("Ú", False, align="center",font=("Arial",25))
                        
                            acertos += 1

                        w +=1




        
        if chutee in tentativas:
            
            
               tortugam.write("Ja inserido", False, align="center",font=("Arial",40))
               time.sleep(1)
               tortugam.clear()
                       
                   
        if chutee in letras and chutee in teste and len(chute) == 1 and chutee not in tentativas:
                
                tentativas.append(chutee)
                n = 0        
                
                iguais = []
                
                
                
                print("Parabéns você acertou ")
                
                while n < len(palavra):              
                    
                    if letras[n] == chutee:

                       
                        
                        
            
            
                        tortugal.setpos(n*34-x*16,-290)
                
                        tortugal.write(chutee, False, align="center",font=("Arial",25))
            
                        acertos += 1
                               
                     
                    
                    n +=1
                    
        elif chutee not in tentativas and chute  in teste2:
                erros += 1
                tentativas.append(chutee)
                print("Que burro da 0 pra ele ")
                print(erros)        

               
        
        
        
        
        if erros == 1 and e1 == 0: 
            tartarugac.penup()
            tartarugac.setpos(-150 , 55)
            tartarugac.pendown()
            tartarugac.circle(20)
            e1 = 1
    
        if erros == 2 and e2 == 0:
            tartarugac.penup()
            tartarugac.setpos(-150 , 55)
            tartarugac.pendown()
            tartarugac.right(90)
            tartarugac.forward(80)
            e2 = 1            
            
        if erros == 3 and e3 == 0:
            tartarugac.penup()
            tartarugac.setpos(-150 , 40)
            tartarugac.pendown()
            tartarugac.right(30)
            tartarugac.forward(30)
            e3 = 1
            
            
        if erros == 4 and e4 == 0:
            
            tartarugac.penup()
            tartarugac.setpos(-150 , 40)
            tartarugac.pendown()
            tartarugac.left(80)
            tartarugac.forward(30)
            e4 = 1
        if erros == 5 and e5 == 0:
            tartarugac.penup()
            tartarugac.setpos(-150 , -25)
            tartarugac.pendown()
            tartarugac.right(80)
            tartarugac.forward(30)
        
            e5 = 1
            
        if erros == 6 and e6 == 0:
            tartarugac.penup()
            tartarugac.setpos(-150 , -25)
            tartarugac.pendown()
            tartarugac.left(60)
            tartarugac.forward(30)
            e6 = 1
            
            
            
if acertos == x-len(espaco):
    tortugam.write("Venceu", False, align="center",font=("Arial",70))
    
    
    




if erros > 5:
    
    print("Morreu")
    tortugam.write("Wasted", False, align="center",font=("Arial",80))
   

           
tela.exitonclick()

arquivo = open('entrada.csv','r')
leitura=arquivo.read(1000)
lista = leitura.split(',')
import random
palavra = random.choice(lista)
print(palavra)

arquivo = open('Pasta2.csv','r')
leitura=arquivo.read(1000)
lista = leitura.split(';')
palavra = random.choice(lista)
print(palavra)