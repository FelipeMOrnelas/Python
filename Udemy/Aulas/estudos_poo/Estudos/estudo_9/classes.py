class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'Info: {msg}')

    def log_error(self, msg):
        self.write(f'Error: {msg}')

class Celular(Eletronico, LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f'{self._nome} já está conectado!'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} agora está conectado!'
        print(info)
        self.log_info(info)
        self._conectado = True


    def desconectado(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado!'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} foi desligado com sucesso!'
        print(info)
        self.log_info(info)
        self._conectado = False


