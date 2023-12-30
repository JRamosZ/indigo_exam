from classes import Library
from os import system

def library_management():
    library = Library()
    option = 0
    while option != '6':
        system("clear")
        print(
            "Menú\n1. Agregar libro\n2. Buscar libro\n3. Prestar libro\n4. Devolver libro\n5. Mostrar inventario\n6. Salir del programa/n")
        option = input("Selecciona una de las opciones: ")
        if option == '1':
            library.register_book()
        elif option == '2':
            library.search_book()
        elif option == '3':
            library.lend_book()
        elif option == '4':
            library.turn_back_book()
        elif option == '5':
            library.show_inventory()
        elif option == '6':
            library.exit()
        else:
            print("Opción no válida, vuelva a intentar\n\n")
    print("Gracias! Vuelva pronto")


# new_book = Book("El negociador", "Arturo Elias", 5, 4)
# session.add(new_book)
#
# new_book2 = Book("Los Rompecabezas", "Ravenburguers", 2, 2)
# session.add(new_book2)
# session.commit()

# result = session.query(Book).filter(Book.author == "Arturo Elias")
# for r in result:
#     print(r)