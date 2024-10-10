import pyautogui as auto
import time
import pandas as pd

auto.PAUSE = 0.5

auto.press("win")
auto.write("chrome")
auto.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
auto.write(link)
auto.press("enter")
#auto.click(2038, 38, clicks=2)
#auto.press("f11")
time.sleep(3)

auto.click(1646,382)

auto.write("teste@teste.com.br")

time.sleep(1)

auto.press("tab")

time.sleep(0.5)
#auto.click(1477, 527)
auto.write('dsfsdfdsfsdfasfdaf')

auto.click(1937, 545)

time.sleep(2)


table = pd.read_csv('produtos.csv')
print(table)


#pegar dados

for linha in table.index:
    auto.click(1634, 262)

    #codigo
    codigo = table.loc[linha, "codigo"]
    auto.write(str(codigo))
    auto.press("tab")

    #marca

    marca = table.loc[linha, "marca"]
    auto.write(str(marca))

    #tipo
    tipo = table.loc[linha, "tipo"]
    auto.write(str(tipo))
    auto.press("tab")

    #categoria
    categoria = table.loc[linha, "categoria"]
    auto.write(str(categoria))
    auto.press("tab")

    # preco_unitario

    preco_unitario = table.loc[linha, "preco_unitario"]
    auto.write(str(preco_unitario))
    auto.press("tab")

    # custo

    custo = table.loc[linha, "custo"]
    auto.write(str(custo))
    auto.press("tab")

    # obs

    obs = table.loc[linha, "obs"]
    if not pd.isna(obs):
        auto.write(str(obs))
    
    auto.press("tab")

    auto.press("enter")
    auto.scroll(5000)
