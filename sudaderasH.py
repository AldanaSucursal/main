import flet as ft
import modelo
def main(page:ft.Page):
    tabla=[]
    registros=modelo.Prendas.select().where(modelo.Prendas.id_categoria==5)
    for r in registros:
        cel1=ft.DataCell(ft.Text(r.id_proveedor.nombre))
        cel2=ft.DataCell(ft.Text(r.cantidad))
        cel3=ft.DataCell(ft.Text(r.talla))
        cel4=ft.DataCell(ft.Text(r.color))
        cel5=ft.DataCell(ft.Text(r.id_categoria.categoria))
        fila=ft.DataRow(cells=[cel1,cel2,cel3,cel4,cel5])
        tabla.append(fila)


    encabezado=[ft.DataColumn(ft.Text('Proveedor')),
                ft.DataColumn(ft.Text('Cantidad')),
                ft.DataColumn(ft.Text('Talla')),
                ft.DataColumn(ft.Text('Color')),
                ft.DataColumn(ft.Text('Categoria'))]
        
    tblcategoria=ft.DataTable(columns=encabezado,
                                rows=tabla,
                                heading_row_color=ft.colors.TRANSPARENT,
                                border=ft.border.all(5,"blue"),
                                border_radius=15)
    return tblcategoria
if __name__=='__main__':
    ft.app(target=main)