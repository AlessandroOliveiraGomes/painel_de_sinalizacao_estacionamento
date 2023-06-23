class Fila:
    def __init__(self):
        self.fila = []
    
    def adicionar(self, elemento):
        self.fila.append(elemento)
    
    def remover(self):
        if self.vazia():
            return None
        return self.fila.pop(0)
    
    def vazia(self):
        return len(self.fila) == 0
    
    def tamanho(self):
        return len(self.fila)

class PainelSinalizacao:
    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.vagas_disponiveis = 0
    
    def atualizar_vagas_disponiveis(self, vagas):
        self.vagas_disponiveis = vagas
        self.exibir()
    
    def exibir(self):
        print(f"Painel de sinalização em {self.localizacao}: {self.vagas_disponiveis} vagas disponíveis")

class Estacionamento:
    def __init__(self, setor):
        self.setor = setor
        self.painel = PainelSinalizacao(setor)
        self.vagas_disponiveis = 10
    
    def registrar_entrada(self):
        if self.vagas_disponiveis > 0:
            self.vagas_disponiveis -= 1
            print("Entrada registrada")
            self.painel.atualizar_vagas_disponiveis(self.vagas_disponiveis)
        else:
            print("O setor está lotado. Não é possível registrar entrada.")
    
    def registrar_saida(self):
        if self.vagas_disponiveis < 10:
            self.vagas_disponiveis += 1
            print("Saída registrada")
            self.painel.atualizar_vagas_disponiveis(self.vagas_disponiveis)
        else:
            print("Não há veículos para saída.")

# Exemplo de utilização:
setor_estacionamento = "Setor 1"
estacionamento = Estacionamento(setor_estacionamento)

while True:
    print("1. Atualizar painel")
    print("2. Registrar entrada de veículo")
    print("3. Registrar saída de veículo")
    print("4. Encerrar programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        estacionamento.painel.atualizar_vagas_disponiveis(estacionamento.vagas_disponiveis)
    elif opcao == "2":
        print("Registro de entrada de veículo")
        estacionamento.registrar_entrada()
    elif opcao == "3":
        print("Registro de saída de veículo")
        estacionamento.registrar_saida()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
