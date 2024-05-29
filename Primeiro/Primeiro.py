import flet as ft

def main(page: ft.Page):
    # Lista para armazenar as linhas dos produtos
    rows = []

    # Definindo as colunas da tabela
    columns = [
        ft.DataColumn(ft.Text("Nome do Produto")),
        ft.DataColumn(ft.Text("Data de Vencimento")),
        ft.DataColumn(ft.Text("Preço")),
    ]

    data_table = ft.DataTable(columns=columns, rows=rows)

    # Função para adicionar um novo produto
    def add_product(e):
        product_name = product_name_input.value
        product_date = product_date_input.value
        product_price = product_price_input.value

        if product_name and product_date and product_price:
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

    PaginaAdicional = product_name_input, product_date_input, product_price_input, submit_button

    # Guias
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tabela",
                content=data_table
            ),

            ft.Tab(
                text="Adicionar Produto",
                icon=ft.icons.SETTINGS,
                content= submit_button
            ),
        ],
        expand=1,
    )
    page.add(t)


ft.app(target=main)