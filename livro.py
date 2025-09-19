class Livro:
    titulo = ""
    autor = ""
    
    def definir_informacao(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacao(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}')




