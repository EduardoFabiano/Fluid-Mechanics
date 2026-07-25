# CONSTANTE GRAVITACIONAL
G = 9.81  

# FUNÇÕES DE CÁLCULO
def calcular_densidade(massa, volume):
    return massa / volume

def calcular_pressao_geral(forca, area):
    return forca / area

def calcular_pressao_hidrostatica(densidade, profundidade):
    return densidade * G * profundidade

def calcular_empuxo(densidade_fluido, volume_submerso):
    return densidade_fluido * volume_submerso * G

def calcular_bernoulli_constante(pressao, velocidade, altura, densidade):
    termo_pressao = pressao
    termo_cinetico = 0.5 * densidade * (velocidade ** 2)
    termo_potencial = densidade * G * altura
    return termo_pressao + termo_cinetico + termo_potencial

# FUNÇÃO AUXILIAR PARA VALIDAR ENTRADAS
def ler_numero(mensagem):
    """Garante que o usuário digite apenas números válidos."""
    while True:
        try:
            entrada = input(mensagem).replace(',', '.')
            return float(entrada)
        except ValueError:
            print(" Erro: Digite apenas números! Letras ou espaços em branco não são aceitos.")

# INTERFACE PRINCIPAL COM LOOP CONTÍNUO
def executar_calculadora():
    while True:
        print("\nCALCULADORA DE MECÂNICA DOS FLUIDOS")
        print("1. Densidade (m / V)")
        print("2. Pressão Geral (F / A)")
        print("3. Pressão Hidrostática (ρ * g * h)")
        print("4. Empuxo (ρ * V * g)")
        print("5. Constante de Bernoulli")
        print("6. Sair do programa")
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        print("-" * 40)
        
        # Condição de saída do loop
        if opcao == '6':
            print("Encerrando o programa...")
            break
            
        try:
            if opcao == '1':
                m = ler_numero("Digite a massa (kg): ")
                v = ler_numero("Digite o volume (m³): ")
                res = calcular_densidade(m, v)
                print(f"\nDensidade: {res:.2f} kg/m³")
                
            elif opcao == '2':
                f = ler_numero("Digite a força (N): ")
                a = ler_numero("Digite a área (m²): ")
                res = calcular_pressao_geral(f, a)
                print(f"\nPressão Geral: {res:.2f} Pa")
                
            elif opcao == '3':
                d = ler_numero("Digite a densidade do fluido (kg/m³): ")
                h = ler_numero("Digite a profundidade/altura (m): ")
                res = calcular_pressao_hidrostatica(d, h)
                print(f"\nPressão Hidrostática: {res:.2f} Pa")
                
            elif opcao == '4':
                d = ler_numero("Digite a densidade do fluido (kg/m³): ")
                v = ler_numero("Digite o volume submerso (m³): ")
                res = calcular_empuxo(d, v)
                print(f"\nForça de Empuxo: {res:.2f} N")
                
            elif opcao == '5':
                p = ler_numero("Digite a pressão (Pa): ")
                v = ler_numero("Digite a velocidade (m/s): ")
                h = ler_numero("Digite a altura/posição (m): ")
                d = ler_numero("Digite a densidade do fluido (kg/m³): ")
                res = calcular_bernoulli_constante(p, v, h, d)
                print(f"\nConstante de Bernoulli: {res:.2f} J/m³")
                
            else:
                print("\nOpção inválida! Escolha um número de 1 a 6.")
                
        except ZeroDivisionError:
            print("\nErro Matemático: Divisão por zero detectada (ex: volume ou área não podem ser 0).")
            
        print("\n" + "." * 40)
        
if __name__ == "__main__":
    executar_calculadora()
    
    print("\n" + "="*40)
    input("Programa finalizado com sucesso. Pressione ENTER para fechar a tela...")
