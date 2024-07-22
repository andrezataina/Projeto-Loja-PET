import biblioteca_reprograma as pr

def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{PetLândia}\nLoja 01\nTerminal de Vendas', sv=2, tamanho=100, margem=5, cor_texto='azul', cor_barra='amarelo')
    pr.separador(108, cor_texto='cinza')
    if(erro != ''):
        pr.imprimir(erro, tamanho =100, alinhar='centro', cor_texto='vermelho negrito')
        pr.separador(108, cor_texto='ciano')
    erro = ''