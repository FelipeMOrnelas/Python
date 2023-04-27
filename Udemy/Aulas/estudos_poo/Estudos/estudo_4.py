class BancodeDados:
    def __init__(self):
        self._dados = {}

    def iserir_clientes(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
    def excluir_clientes(self, id):
        del self._dados['clientes'][id]

bd = BancodeDados()
bd.iserir_clientes(1, 'Felipe')
bd.iserir_clientes(2, 'Osvaldo')
bd.iserir_clientes(3, 'Talita')
bd.excluir_clientes(2)
bd.lista_clientes()
