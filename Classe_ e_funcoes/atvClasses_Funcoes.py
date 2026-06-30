class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


l1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
l2 = Livro("Cinderela", "Walt Disney", 1950)
l3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

livros = [l1, l2, l3]

def mostrar_livro(l):
    print(f"Titulo: {l.titulo} | Autor: {l.autor} | Ano: {l.ano_publicacao}")


for l in livros:
    mostrar_livro(l)


def verificar_duplicados(lista):
    vistos = set()

    for l in lista:
        chave = (l.titulo, l.autor)

        if chave in vistos:
            print("Duplicado encontrado:", chave)
        else:
            vistos.add(chave)


verificar_duplicados(livros)
