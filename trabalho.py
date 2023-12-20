class Endereco:
    def __init__(self, rua, casa, municipio, provincia, pais):
        self.rua = rua
        self.casa = casa
        self.municipio = municipio
        self.provincia = provincia
        self.pais = pais

class Contato:
    def __init__(self, nome, telefone, email=None, codigo_postal=None, endereco=None, bi=None, nif=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.codigo_postal = codigo_postal
        self.endereco = endereco
        self.bi = bi
        self.nif = nif

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def editar_contato(self, nome, novo_contato):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.__dict__.update(novo_contato.__dict__)
                return True
        return False

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def pesquisa(self,nome):
    self.vet.append(nome)
    if nome in self.vet:
        print("Nome<",nome,">encontrado")
    else:
        print("nome não encontrado na agenda")
   resultado=agenda("joao",123)
   resultado.pesquisa("joao")
