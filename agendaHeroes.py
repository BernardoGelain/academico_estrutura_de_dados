class Superhero:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class AgendaHeroes:
    def __init__(self):
        # Inicializa uma lista vazia com 26 elementos para representar a tabela hash.
        self.table = [None] * 26

    def _hash_function(self, char):
        # Calcula o índice da tabela hash para a letra dada.
        return ord(char.upper()) - ord('A')

    def add_contact(self, superhero):
        index = self._hash_function(superhero.name[0])
        # Verifica se o índice está vazio; se sim, cria uma lista e adiciona o super-herói.
        if self.table[index] is None:
            self.table[index] = [superhero]
        else:
            # Se o índice já possui uma lista, adiciona o super-herói a essa lista.
            self.table[index].append(superhero)

    def search_contact(self, name):
        index = self._hash_function(name[0])
        contacts = self.table[index]
        if contacts is None:
            return []
        # Retorna uma lista de super-heróis cujos nomes correspondem à pesquisa.
        return [hero for hero in contacts if hero.name == name]

    def list_contacts_by_letter(self, letter):
        index = self._hash_function(letter)
        contacts = self.table[index]
        if contacts is None:
            return []
        # Retorna uma lista de nomes de super-heróis cujos nomes começam com a letra dada.
        return [hero.name for hero in contacts]

    def remove_contact(self, name):
        index = self._hash_function(name[0])
        contacts = self.table[index]
        if contacts is None:
            return
        # Remove o super-herói da lista de contatos no índice correspondente.
        self.table[index] = [hero for hero in contacts if hero.name != name]

    def import_contacts_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, contact = line.strip().split(',')
                # Adiciona cada super-herói lido do arquivo à tabela hash.
                self.add_contact(Superhero(name, contact))

    def export_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            for contacts in self.table:
                if contacts is not None:
                    # Escreve os detalhes de contato de cada super-herói no arquivo.
                    for hero in contacts:
                        file.write(f"{hero.name},{hero.contact}\n")


def main():
    agenda = AgendaHeroes()

    while True:
        # Menu interativo para escolher as opções.
        print("Menu:")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar contatos por letra")
        print("4. Remover contato")
        print("5. Importar contatos do arquivo")
        print("6. Exportar contatos para o arquivo")
        print("7. Sair")
