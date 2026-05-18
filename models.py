# arquivo so pra nao ficar dando erro de importacao

class Move: #IA
    def __init__(self, name, move_type, power, accuracy, pp):
        self.name = name          # "Lança-Chamas"
        self.move_type = move_type  # "Fogo"
        self.power = power        # 90  (quão forte é)
        self.accuracy = accuracy  # 100 (% de chance de acertar)
        self.pp = pp              # 15  (quantas vezes pode usar)
        self.current_pp = pp      # PP atual (vai diminuindo)

    def use(self):
        if self.current_pp > 0:
            self.current_pp -= 1
            return True
        return False  # sem PP, não pode usar
    
def pega_ataques(nome, dic):
    pokemon_data = None
    for i in dic:
        if i['name'] == nome:
            pokemon_data = i
            break
    
    if pokemon_data == None:
        return []

    lista_ataques = pokemon_data['moves']
    for i in range(0,len(lista_ataques)):
        ataque = lista_ataques[i]
        lista_ataques[i] = Move(ataque['name'], ataque['type'], ataque['power'], ataque['accuracy'], ataque['pp'])
    return lista_ataques