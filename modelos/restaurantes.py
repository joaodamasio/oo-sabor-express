class Restaurante:
    
    restaurantes = []
    
    # metodo construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    #metodo para mostrar o conteudo do objeto
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
    
    
restaurante_praca = Restaurante('Praca','Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()
