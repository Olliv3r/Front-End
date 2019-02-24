#!/usr/bin/env python3
# Descrição: Gerador De ScriptS Deface.
# Para Ataque [mass Deface]
# Autor: Olive. canal do YouTube [Tio olive].


# Modulos Importados
import subprocess
import sys
import time
import os

def Sfront():
    print('Gerador De ScriptS DefAce, Para Ataque [mass Deface]\n')
	 
def bn():
    clear('clear')
    print("""\033[0m]
   \033[01;94m|-------------------------------------------\033[01;94m|
   \033[01;94m|  \033[02;91m_____   _____   ____    _   _   _______  \033[01;94m|
   \033[01;94m| \033[02;91m/  ___| |  __ | / __ \  | | | | |__   __| \033[01;94m|
   \033[01;94m| \033[02;91m| |___  | |_ /  | | | | | .\| |    | |    \033[01;94m|
   \033[01;94m| \033[02;91m| |__/  | |\ \  | |_| | | |\  |    | |    \033[01;94m|
   \033[01;94m| \033[02;91m|_|     |_| \_\ \____/  |_| |_|    |_|    \033[01;94m|
   \033[01;94m|-------------------------------------------|\033[0m
      \t\t\033[01;96mVersão: \033[01;91mBETA\033[0m.
      \t\t\033[01;96mFront: \033[01;91mv1.0\033[0m.
      \t\t\033[01;96mAutor: \033[01;91molive\033[0m.
    """)
    Sfront()

clear = subprocess.run
tempo = time.sleep


exp, ht1, ht2, re1, re2, bo1, bo2 = '<!DOCTYPE html>','<html lang="pt-br">','</html>','<read>','</read>','<body>','</body>'

bn()

TITULO = str(input('\033[01;94mTÍTULO: \033[01;91m'))
print('')
colors = str(input('\033[01;94mCor Do Título\033[0m(\033[01;92mgreen\033[0m,\033[01;91mred\033[0m,\033[00;97mgray\033[0m,\033[02;93molive \033[0metc.): \033[01;91m'))
print('')
IMG_CENTER = str(input('\033[01;94mLINK DE UMA IMG PRO CENTRO: \033[01;91m'))
#IMG_BG = str(input('LINK DE UMA IMG DE FUNDO: '))
print('')
MSG = str(input('\033[01;94mMensagem: \033[01;91m'))
print('')
cor_msg = str(input('\033[01;94mCor Da Mensagem\033[0m(\033[01;94mblue\033[0m,\033[01;91mred\033[0m,\033[01;93myellow\033[0m,\033[01;95mcyan\033[0m): \033[01;91m'))
print('')
Autor = str(input('\033[01;94mAutor Do Script: \033[01;91m'))
print('')
cor_by = str(input('\033[01;94mCor Do Autor\033[0m(\033[02;92mlime\033[0m,\033[3;91mmaroon\033[0m,\033[00;96maqua\033[0m,\033[21;94mnavy \033[0metc\033[0m): \033[01;91m'))

# Tags
st1 = '<style>'
st2 = '</style>'

# Estilização
body = ('width: {}; border-style: {}; border-color: {}; border-width: {}; background-color: {};'.format('100%','solid','red','1px','black'))

h1_st = ('color: {};font-family: {}; font-weight: {}; text-align: {}; border-color: {}; border-style: {}; border-width: {};'.format(colors,'sans-serif','bold','center','red','solid','1px'))

img_center_st = ('border-color: {}; border-style:{};border-width: {}; text-align: {};'.format('red','solid','1.5','center'))

IMAGEM_WIDTH = ('width: {};'.format('650px'))

figure_init, figure_end, figcaption_init, figcaption_end, legenda_fig = ('<figure class="image">','</figure>','<figcaption>','</figcaption>','Conexão Falhou, acesso Negado, Impossível')

msg_st = ('color: {}; font-family: {}; text-align: {};'.format(cor_msg,'serif','center'))

fig_st = ('color: {}; font-family: {}; border-color: {}; border-style: {}; border-width: {}; text-align: {};'.format('red','sans-serif','red','solid','0.4px','center'))

# Título Da Página
titulo = ('<title>{}</title>'.format(TITULO))

# Codificação Selecionada 'UTF-8'
metachar = '<meta charset="UTF-8"/>'

# Classes
#h1 = ('<h1>{}</h1>'.format(titulo))
img = ('<img class="image" src="{}">'.format(IMG_CENTER))
P = ('<p class="mensagem">{}</p>'.format(MSG))

Ti = ('<h1>{}</h1>'.format(TITULO))

#IMG_CEN = ('<background-image: url({});'.format(IMG_BG))

# Estilização
by_st = ('color: {}; font-family: {}; text-align: {}; border-style: {}; border-color: {}; border-width: {}; text-transformation: {}; font-weight: {}; background-color: {};'.format(cor_by,'serif','center','solid','red','1px','uppercase','bold','blue'))

# Tags
p_by = ('<p class="autor">By: {}</p>'.format(Autor))

# Inicio Da Função
def script():
    print('Gerando index!')
    tempo(1.5)
    # Abrir Index Novo E Escrevendo Index
    linhas = open('script.html','x+t')
    linhas.write(exp+'\n')
    linhas.write(ht1+'\n')
    linhas.write(re1+'\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{} \n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n'.format(titulo, metachar, st1,'h1 {',h1_st,'}','.image {',img_center_st, '}','.autor {', msg_st,'}','body {',body,'}','figcaption {',fig_st,'}','.mensagem {',by_st,'}','img {', IMAGEM_WIDTH,'}',st2))
    linhas.write(re2+'\n')
    linhas.write(bo1+'\n\t{}\n\t{}\n\t\t{}\n\t\t{}{}{}\n\t{}\n\t{}\n\t{}\n'.format(Ti, figure_init, img, figcaption_init,legenda_fig, figcaption_end, figure_end, P, p_by))
    linhas.write(bo2+'\n')
    linhas.write(ht2+'\n')
    linhas.close()
    # Index Fechada
    
    

# Função Invocada.

script()
PATH = '/data/data/com.termux/files/home/Front-End'
if(os.path.exists(PATH+'/script.html') == True):
    print('\033[01;92mIndex\033[0m[\033[01;94m+\033[0m] \033[01;92mSalvo Em {}'.format(PATH+'/script.html'))
elif(os.path.exists(PATH+'/script.html') == False):
    print('Não Salvo Em {}'.format(PATH+'/scri...'))