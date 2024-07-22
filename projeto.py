import biblioteca_reprograma as pr
from datetime import datetime

produtos =  [
    {'codigo': 1, 'nome': 'Ração para cães (10kg)', 'valor': 80.00},
    {'codigo': 2, 'nome': 'Ração para gatos (5kg)', 'valor': 60.00},
    {'codigo': 3, 'nome': 'Petisco de carne para cães', 'valor': 15.00},
    {'codigo': 4, 'nome': 'Petisco de frango para cães', 'valor': 12.00},
    {'codigo': 5, 'nome': 'Areia sanitária para gatos (5kg)', 'valor': 25.00},
    {'codigo': 6, 'nome': 'Shampoo neutro para pets', 'valor': 20.00},
    {'codigo': 7, 'nome': 'Condicionador para pets', 'valor': 18.00},
    {'codigo': 8, 'nome': 'Escova de pelos para cães e gatos', 'valor': 15.00},
    {'codigo': 9, 'nome': 'Coleira ajustável para cães', 'valor': 30.00},
    {'codigo': 10, 'nome': 'Coleira antipulgas para cães', 'valor': 40.00},
    {'codigo': 11, 'nome': 'Brinquedo bola para cães', 'valor': 10.00},
    {'codigo': 12, 'nome': 'Brinquedo de corda para cães', 'valor': 12.00},
    {'codigo': 13, 'nome': 'Brinquedo interativo para gatos', 'valor': 15.00},
    {'codigo': 14, 'nome': 'Casinha de plástico para cães', 'valor': 80.00},
    {'codigo': 15, 'nome': 'Cama acolchoada para cães (porte médio)', 'valor': 70.00},
    {'codigo': 16, 'nome': 'Cama confortável para gatos', 'valor': 50.00},
    {'codigo': 17, 'nome': 'Bebedouro automático para pets', 'valor': 35.00},
    {'codigo': 18, 'nome': 'Comedouro automático para pets', 'valor': 40.00},
    {'codigo': 19, 'nome': 'Colete salva-vidas para cães', 'valor': 60.00},
    {'codigo': 20, 'nome': 'Caixa de transporte para gatos', 'valor': 55.00},
    {'codigo': 21, 'nome': 'Guia retrátil para cães', 'valor': 25.00},
    {'codigo': 22, 'nome': 'Roupa de inverno para cães (tamanho M)', 'valor': 45.00},
    {'codigo': 23, 'nome': 'Roupa de verão para cães (tamanho P)', 'valor': 30.00},
    {'codigo': 24, 'nome': 'Peitoral confortável para gatos', 'valor': 20.00},
    {'codigo': 25, 'nome': 'Tapete higiênico descartável (pacote com 50 unidades)', 'valor': 40.00},
    {'codigo': 26, 'nome': 'Arranhador para gatos', 'valor': 50.00},
    {'codigo': 27, 'nome': 'Caminha suspensa para gatos', 'valor': 65.00},
    {'codigo': 28, 'nome': 'Bolsa de transporte para pets', 'valor': 60.00},
    {'codigo': 29, 'nome': 'Escada para cães e gatos', 'valor': 55.00},
    {'codigo': 30, 'nome': 'Focinheira para cães', 'valor': 15.00},
    {'codigo': 31, 'nome': 'Gaiola espaçosa para hamsters', 'valor': 40.00},
    {'codigo': 32, 'nome': 'Aquário completo (20 litros)', 'valor': 120.00},
    {'codigo': 33, 'nome': 'Toca para roedores', 'valor': 25.00},
    {'codigo': 34, 'nome': 'Comedouro para pássaros', 'valor': 8.00},
    {'codigo': 35, 'nome': 'Brinquedo mastigável para cães', 'valor': 12.00},
    {'codigo': 36, 'nome': 'Areia de sílica para gatos (3kg)', 'valor': 30.00},
    {'codigo': 37, 'nome': 'Capa de chuva para cães (tamanho G)', 'valor': 25.00},
    {'codigo': 38, 'nome': 'Portão de segurança para cães', 'valor': 70.00},
    {'codigo': 39, 'nome': 'Tapete gelado para pets', 'valor': 35.00},
    {'codigo': 40, 'nome': 'Cobertor térmico para gatos', 'valor': 45.00},
    {'codigo': 41, 'nome': 'Escova dental para pets', 'valor': 18.00},
    {'codigo': 42, 'nome': 'Gel dental para cães e gatos', 'valor': 15.00},
    {'codigo': 43, 'nome': 'Roupa de banho para cães (tamanho P)', 'valor': 20.00},
    {'codigo': 44, 'nome': 'Ossinho de couro para cães', 'valor': 8.00},
    {'codigo': 45, 'nome': 'Arranhador para gatos com túnel', 'valor': 55.00},
    {'codigo': 46, 'nome': 'Peitoral para cães com luz LED', 'valor': 40.00},
    {'codigo': 47, 'nome': 'Comedouro elevado para cães', 'valor': 50.00},
    {'codigo': 48, 'nome': 'Porta de entrada para gatos', 'valor': 30.00},
    {'codigo': 49, 'nome': 'Tigela de inox para pets', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Brinquedo interativo para cães (dispenser de petiscos)', 'valor': 25.00},
    {'codigo': 51, 'nome': 'Cama ortopédica para cães (porte grande)', 'valor': 100.00},
    {'codigo': 52, 'nome': 'Cama térmica para gatos', 'valor': 60.00},
    {'codigo': 53, 'nome': 'Capa de assento para pets', 'valor': 35.00},
    {'codigo': 54, 'nome': 'Rede para pássaros', 'valor': 15.00},
    {'codigo': 55, 'nome': 'Corda dental para cães', 'valor': 12.00},
    {'codigo': 56, 'nome': 'Peitoral para cães com coleira retrátil', 'valor': 45.00},
    {'codigo': 57, 'nome': 'Bebedouro automático para gatos', 'valor': 30.00},
    {'codigo': 58, 'nome': 'Roupa de proteção solar para cães (tamanho M)', 'valor': 35.00},
    {'codigo': 59, 'nome': 'Caixa de transporte para cães', 'valor': 80.00},
    {'codigo': 60, 'nome': 'Bolsa de transporte para gatos', 'valor': 55.00},
    {'codigo': 61, 'nome': 'Comedouro automático para gatos', 'valor': 45.00},
    {'codigo': 62, 'nome': 'Ração úmida para cães (pack com 12 unidades)', 'valor': 25.00},
    {'codigo': 63, 'nome': 'Comedouro duplo para pets', 'valor': 20.00},
    {'codigo': 64, 'nome': 'Brinquedo mordedor para filhotes', 'valor': 15.00},
    {'codigo': 65, 'nome': 'Tigela antiformiga para cães', 'valor': 18.00},
    {'codigo': 66, 'nome': 'Bolsa de transporte para roedores', 'valor': 25.00},
    {'codigo': 67, 'nome': 'Coleira refletiva para cães', 'valor': 22.00},
    {'codigo': 68, 'nome': 'Arranhador para gatos com pelúcia', 'valor': 60.00},
    {'codigo': 69, 'nome': 'Comedouro para aves', 'valor' : 75.00},
]

# Imprimir cabeçalho
def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{PetLândia}\nLoja 01\nTerminal de Vendas', sv=2, tamanho=100, margem=5, cor_texto='azul', cor_barra='amarelo')
    pr.separador(108, cor_texto='cinza')
    if(erro != ''):
        pr.imprimir(erro, tamanho =100, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(108, cor_texto='ciano')
    erro = ''

# Imprimir Rodapé
def imprimir_rodape():
    pr.imprimir('[A] Ajuda ', '[S] Sair ',caracter='=', tamanho=105, alinhar='fim', end='⁜')

    return input().lower()

# Opções de Ajuda do Sistema
def imprimir_ajuda():
    pr.pular_linha(quantidade=3)
    pr.imprimir('[A]   >> Ajuda com o Sistema', alinhar='centro', tamanho=120)  
    pr.imprimir('[S]   >> Sair da Tela ou Sistema', alinhar='centro', tamanho=120) 
    pr.imprimir('[N]   >> Cria uma Nova Compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[F]   >> Fechar a Compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[P]   >> Confirmar que a compra foi paga', alinhar='centro', tamanho=120)  
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra', alinhar='centro', tamanho=120)  
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado', alinhar='centro', tamanho=120)  
    pr.imprimir('[E]   >> Encerar caixa', alinhar='centro', tamanho=120)  
    pr.pular_linha(quantidade=3)

def produto_codigo(codigo):
    for produto in produto:
        if produto['codigo'] == codigo:
            return produto
        else:
            return ('Produto inexistente!')
        
def novo_produto(produto, quantidade):
    return {
        'codigo': produto['codigo'],
        'nome': produto['nome'],
        'valor': produto['valor'],
        'quantidade': quantidade
                              }

def imprime_fechamento_caixa(compras):
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=20, alinhar='centro') 

    total = 0

    for compra in compras:
        total += compra['total']
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim')
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')
    pr.separador(120, caracter='-')
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')

def imprime_compra_fechada(compra, total):
    total_compra = 0

    pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')
    pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
    pr.imprimir('valor', tamanho=12, alinhar='centro')

    for produto in compra:
        imprimir_produto(produto)
        total_compra += produto['valor'] * produto['quantidade']

    pr.separador(120, caracter='-') 
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim')
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito')
    pr.limpar_formatacao()
    pr.pular_linha()
    pr.pular_linha()

def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')

def imprime_compra(compra):

    if len(compra) > 0:
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro', end='|') 
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')

        for produto in compra:
            total += produto['valor'] * produto['quantiade']
        pr.separador(120, caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim')
    else:
       pr.imprimir('Não há itens na lista!', tamanho=120, alinhar='center')

    pr.pular_linha()
    pr.pular_linha()

def calcula_total_desconto(compra):
    total = 0

    for produto in compra:
        total += produto['valor'] * produto['quantidade']
    if total < 100:
        return total
    elif total > 100:
        aplica_desconto = total * 0.9
        return aplica_desconto
    
    return total

def menu():
    opcao = ''
    erro = ''
    tela = ''
    compra = []
    compras = []
    total = []

    while opcao != 's':
        imprimir_cabecalho(erro)
        if tela == '':
            pr.pular_linha(quantidade=4)
        elif tela == 'ajuda':
            imprimir_ajuda()
            tela = ''
        elif tela == 'compra':
            imprime_compra(compra)
        elif tela == 'fechar':
            imprime_compra_fechada(compra, total)
        elif tela == 'encerrar':
            imprime_fechamento_caixa(compras)
            compras = []
            tela = ''
            pr.pular_linha(quantidade=4)

        opcao = imprimir_rodape()
        if opcao == 'a':
            tela = 'ajuda'
        elif opcao == 'n':
            tela = 'compra'
        elif opcao == 'f':
            total = calcula_total_desconto(compra)
            tela = 'fechar'
        elif opcao == 'e':
            tela = 'encerrar'
        elif 'p' in opcao:
            compras.append({'itens': compra, 'total': total, 'data': datetime.now()})
            compra = []
            tela = ''
        else:
            try:
                codigo = int(opcao)
                produto = produto_codigo(codigo)
                compra.append(novo_produto(produto, 1))
            except ValueError:
                erro = 'A opção selecionada não existe no sistema!'
            except TypeError:
                erro = 'O código do produto não existe!'


