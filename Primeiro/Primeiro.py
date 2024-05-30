import flet as ft

def main(page: ft.Page):
    page.title = "Tabela de Produtos"
    page.window_min_height = 100
    page.window_min_width = 100
    # Lista para armazenar as linhas dos produtos
    rows = []

    # Definindo as colunas da tabela
    columns = [
        ft.DataColumn(ft.Text("Nome do Produto")),
        ft.DataColumn(ft.Text("Data de Vencimento")),
        ft.DataColumn(ft.Text("Preço")),
    ]

    # Criando a tabela
    data_table = ft.DataTable(columns=columns, rows=rows)

    # Função para navegar para a página de adição
    def go_to_add_product_page(e):
        page.views.append(add_product_page)
        page.update()

    # Botão para navegar para a página de adição
    add_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=go_to_add_product_page, bgcolor=ft.colors.BLUE_300)

    # Página principal com a tabela e botão de adicionar
    main_page = ft.View(
        "/",
        [
            add_button,
            data_table
        ]
    )

    # Função para adicionar um novo produto
    def add_product(e):
        product_name = product_name_input.value
        product_date = product_date_input.value
        product_price = product_price_input.value

        if product_name != None and product_date != None and product_price != None:
            new_row = ft.DataRow(cells=[
                ft.DataCell(ft.Text(product_name)),
                ft.DataCell(ft.Text(product_date)),
                ft.DataCell(ft.Text(product_price)),
            ])
            rows.append(new_row)
            data_table.rows = rows
            product_name_input.value = ""
            product_date_input.value = ""
            product_price_input.value = ""
            # Voltar para a página principal após adicionar o produto
            page.views.pop()
            page.update()


    # Campos de entrada para adicionar novos produtos
    product_name_input = ft.TextField(label="Nome do Produto")
    product_date_input = ft.TextField(label="Data de Vencimento")
    product_price_input = ft.TextField(label="Preço")

    # Botão para adicionar novos produtos
    submit_button = ft.ElevatedButton(text="Adicionar", on_click=add_product)

    # Ação do Botão voltar
    def go_back(e):
        page.views.pop()
        page.update()

    # Botão voltar
    menubar = ft.MenuBar(
        controls=[
                ft.MenuItemButton(
                    content= ft.Text("Back"),
                    on_click= go_back,
                    leading=ft.Icon(name='arrow_back')
                 )
        ]
    )


    # Página de adição de produtos
    add_product_page = ft.View(
        "/add",
        [
            menubar,
            product_name_input,
            product_date_input,
            product_price_input,
            submit_button
        ]
    )
    
    page.views.append(main_page)

    page.add(main_page)

ft.app(target=main)