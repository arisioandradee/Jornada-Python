# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa(https://dlp.hashtagtreinamentos.com/python/intensivao/login)
import pyautogui
import time

    # pyautogui.write = escrever um texto
    # pyautogui.press = apertar 1 tecla do teclado
    # pyautogui.click = clicar em algum lugar da tela
    # pyautogui.hotkey = combinação de teclas

pyautogui.PAUSE = 0.5 #dando pausa para o código esperar o computador

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)

# Entrando no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2) #usando biblioteca time para dar uma pausa de 2s

# Passo 2: Fazer login
# Selecionando o campo email
pyautogui.click(x=515, y=388) #usando arquivo auxilir para localizar o campo

# Escrevendo email
pyautogui.write("arisioandrade@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("senha 123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importando a base de daddos do arquivo local
import pandas as pd

tabela = pd.read_csv( 'lista.csv', sep=',', header=0, encoding='iso-8859-1')

# Passo 4: Cadastrando produto

for indice, linha in tabela.iterrows():
    pyautogui.click(x=453, y=275) #clicando no campo de código
    codigo = linha["codigo"] #pegar na tabela o valor que queremos preencher
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(linha["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["custo"]))
    pyautogui.press("tab")
    obs = linha["obs"] 
    
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
