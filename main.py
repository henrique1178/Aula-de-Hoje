import flet as ft #importanto o flet e nomeando ele como ft para facilitar a sintaxe

def main(page: ft.Page): #receita de bolo, pois isso é a sintaxe padrão da biblioteca
    def ChecarIdade(e): #esse 'e' siginifica 'evento'
        if int(entrada_idade.value) >= 18:
            resultado.value = "Maior de Idade"
        else:
            resultado.value = "Menor de idade"
        resultado.update() #update serve para atualizar la na caixa vazia cada valor que for alterado aqui dentro com base no 'input' de usuário
            
            
    page.title = "Checando Idade" #'title' serve ´para gerarmos um titulo, seguido do parametro page
    titulo = ft.Text(value="PROGRAMA PARA CHECAR IDADE", size=28) #Text vai adicionar uma 
    entrada_idade = ft.TextField(label="Idade", keyboard_type=ft.KeyboardType.NUMBER)
    botao = ft.ElevatedButton("Checar Idade", on_click=ChecarIdade)
    resultado = ft.Text(value="", size=18)
    page.add(titulo,entrada_idade,botao,resultado)
    

ft.app(target=main) #receita de bolo, pois isso é a sintaxe padrão da biblioteca





def main(page: ft.Page):
    page.title = "Seja bem vindo ao flet"
    page.add(
        ft.Text(value="MENSAGEM DE SAUDAÇÃO", size=30),
        ft.ElevatedButton("Bom dia!", on_click=lambda _: page.add(ft.Text(value="Olá tenha um bom dia"))),
        ft.ElevatedButton("Boa tarde!", on_click=lambda _: page.add(ft.Text(value="Olá tenha uma boa tarde"))),
        ft.ElevatedButton("Boa noite!", on_click=lambda _: page.add(ft.Text(value="Olá tenha uma boa noite")))
    )

ft.app(target=main)



# LAYOUT EM LINHA
def main(page: ft.Page):
    page.title = "Seja bem vindo ao flet"
    layout_linha = ft.Row(
        controls=[
            ft.Text(value="Texto da linha"),
            ft.ElevatedButton("Primeiro botão da linha"),
            ft.ElevatedButton("Segundo botão da linha"),
            ft.ElevatedButton("Terceiro botão da linha"),
        ]
    )
    page.add(layout_linha)

ft.app(target=main)