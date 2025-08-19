import pandas as pd
import numpy as np

# Extracao
vendas = pd.read_csv('dados/Vendas.csv', sep=';')
clientes = pd.read_csv('dados/Clientes.csv', sep=';')
pedidos = pd.read_csv('dados/Pedidos.csv', sep=';')
produtos = pd.read_csv('dados/Produtos.csv', sep=';')


vendas.info()
def verificar_valores_ausentes(df):
    """
    Recebe um DataFrame pandas e retorna um resumo dos valores ausentes.
    """
    # Número de valores ausentes por coluna
    ausentes_por_coluna = df.isnull().sum()
    # Porcentagem de valores ausentes por coluna
    perc_ausentes = (df.isnull().mean() * 100).round(2)
    
    # Juntando em um novo DataFrame de resumo
    resumo = pd.DataFrame({
        'Valores Ausentes': ausentes_por_coluna,
        'Percentual (%)': perc_ausentes
    })

    return resumo[resumo['Valores Ausentes'] > 0].sort_values(by='Valores Ausentes', ascending=False)

# Verificando valores ausentes
# print(verificar_valores_ausentes(clientes))
# print(verificar_valores_ausentes(pedidos))
# print(verificar_valores_ausentes(produtos))
# print(verificar_valores_ausentes(vendas))


def remover_espacos_vazios(df):
    """
    Remove espaços em branco no início e no final dos textos
    de todas as colunas do tipo string em um DataFrame pandas.
    Retorna o DataFrame limpo.
    """
    # Apenas para colunas de texto: aplica strip() removendo espaços no início/fim
    df_limpo = df.copy()
    colunas_objeto = df_limpo.select_dtypes(include=['object', 'string']).columns
    for col in colunas_objeto:
        df_limpo[col] = df_limpo[col].astype(str).str.strip()
    return df_limpo

# Remocao de espacos
clientes = remover_espacos_vazios(clientes)
pedidos = remover_espacos_vazios(pedidos)
produtos = remover_espacos_vazios(produtos)
vendas = remover_espacos_vazios(vendas)


# Conversao de datas
pedidos['Data Pedido'] = pd.to_datetime(pedidos['Data Pedido'], dayfirst=True)
pedidos['Data Envio'] = pd.to_datetime(pedidos['Data Envio'], dayfirst=True)

# Renomear colunas

vendas = vendas.rename(columns={'Pedido': 'id_pedido',
                                 'Cliente': 'id_cliente',
                                 'Produto': 'id_produto',
                                 'Valor Venda': 'valor_venda',
                                 'Quantidade Vendida': 'qtd_vendida',
                                 'Custo Envio': 'custo_envio'})

pedidos = pedidos.rename(columns={'Local Pedido': 'local_pedido',
                                  'Ano': 'ano',
                                  'ID Pedido': 'id_pedido_num',
                                   'Data Pedido': 'data_pedido',
                                   'Data Envio': 'data_envio',
                                   'Modo Envio': 'modo_envio',
                                   'Prioridade Pedido': 'prioridade'})

clientes = clientes.rename(columns={'ID Cliente': 'id_cliente',
                                    'Nome Cliente': 'nome_cliente',
                                    'Segmento': 'segmento',
                                    'Cidade': 'cidade',
                                    'Estado': 'estado',
                                    'Pais': 'pais',
                                    'Mercado': 'mercado',
                                    'Regiao': 'regiao'})

produtos = produtos.rename(columns={'ID Produto': 'id_produto',
                                    'Categoria': 'categoria',
                                    'SubCategoria': 'subcategoria',
                                    'Nome Produto': 'nome_produto'})


# Remocao do prefixo dos ids do cliente
clientes['id_cliente'] = clientes['id_cliente'].str.split('-', n=1).str[1]
vendas['id_cliente'] = vendas['id_cliente'].str.split('-', n=1).str[1]

# Verificacao se há id de clientes apos a remocao do prefixo 
duplicadas_clientes = clientes[clientes.duplicated(subset='id_cliente', keep=False)]

# print(duplicadas_clientes.head())


### DATASET PEDIDOS

# Substituindo a abreviacao dos Prefixos dos locais do pedidos por nomes
mapa_locais = {
    'CA': 'Canada',
    'IN': 'India',
    'ES': 'Espanha',
    'SG': 'Singapura',
    'ID': 'Indonesia',
    'SA': 'Arabia Saudita',
    'MX': 'Mexico',
    'TZ': 'Tanzania',
    'PL': 'Polonia',
    'US': 'Estados Unidos',
    'CG': 'Congo',
    'IT': 'Italia',
    'IR': ' Ira',
    'MZ': 'Mocambique',
    'UP': 'Desconhecido',
    'MO': 'Macau',
    'SO': 'Somalia',
    'BO': 'Bolivia',
    'SF': 'Finlandia',    # SF = Finlandia (antigo, atualmente FI)
    'RS': 'Servia',
    'EG': 'Egito',
    'AJ': 'Desconhecido',
    'LH': 'Desconhecido',
    'LT': 'Lituania',
    'RO': 'Romenia',
    'TU': 'Tunisia',
    'CM': 'Camaroes',
    'HU': 'Hungria',
    'AO': 'Angola',
    'GH': 'Gana',
    'ZA': 'Africa do Sul',
    'IZ': 'Iraque',
    'LI': 'Liechtenstein',
    'GG': 'Guernsey',
    'AL': 'Albania',
    'CD': 'Republica Democratica do Congo',
    'MW': 'Malawi',
    'WA': 'Desconhecido',
    'MA': 'Marrocos',
    'AU': 'Australia',
    'QA': 'Catar',
    'CF': 'Republica Centro-Africana',
    'AG': 'Antigua e Barbuda',
    'NI': 'Nicaragua',
    'EN': 'Desconhecido',
    'IV': 'Costa do Marfim',
    'EZ': 'Desconhecido',
    'CT': 'Desconhecido',
    'BN': 'Brunei',
    'SY': 'Siria',
    'LE': 'Libano',
    'KE': 'Quenia',
    'ML': 'Mali',
    'LY': 'Libia',
    'BU': 'Burundi',
    'IS': 'Islandia',
    'SI': 'Eslovenia',
    'TO': 'Togo', # Obs: TO tambem pode ser Tonga, confirme o seu caso
    'MR': 'Mauritania',
    'GV': 'Guine',
    'RW': 'Ruanda',
    'NG': 'Nigeria',
    'MG': 'Madagascar',
    'SU': 'Desconhecido',
    'SL': 'Serra Leoa',
    'BK': 'Desconhecido',
    'PU': 'Desconhecido',
    'DJ': 'Djibuti',
    'TS': 'Desconhecido',
    'HR': 'Croacia',
    'KG': 'Quirguistao',
    'ZI': 'Zimbabue',
    'UZ': 'Uzbequistao',
    'OD': 'Desconhecido',
    'GB': 'Reino Unido',
    'BA': 'Bosnia e Herzegovina',
    'YM': 'Iemen',
    'JO': 'Jordania',
    'AE': 'Emirados Arabes Unidos',
    'MD': 'Moldavia',
    'WZ': 'Eswatini',
    'TX': 'Desconhecido',
    'KZ': 'Cazaquistao',
    'ET': 'Etiopia',
    'UG': 'Uganda',
    'LO': 'Desconhecido',
    'TI': 'Desconhecido',
    'BY': 'Bielorrussia',
    'MK': 'Macedonia do Norte',
    'ER': 'Eritreia',
    'EK': 'Desconhecido',
    'AM': 'Armenia'
}

def substituir_prefixo_local(df, coluna_codigo, nova_coluna='pais', mapa=mapa_locais):
    """
    Extrai o prefixo da coluna de código e substitui pelo nome do país.
    Cria/atualiza uma coluna com o nome do país.
    """
    df = df.copy()
    # Extrai o prefixo ANTES do primeiro hífen
    df[nova_coluna] = df[coluna_codigo].str.extract(r'^([A-Z]{2})', expand=False)
    # Substitui a sigla pelo país
    df[nova_coluna] = df[nova_coluna].map(mapa)
    return df

pedidos = substituir_prefixo_local(pedidos, 'local_pedido', 'pais')

# Move a coluna 'pais' para o início do DataFrame
colunas = pedidos.columns.tolist()
colunas.remove('pais')
# Nova ordem: 'pais' + demais colunas
nova_ordem = ['pais'] + colunas
pedidos = pedidos[nova_ordem]


### DATASET PRODUTOS

# # linhas_duplicadas = produtos[produtos.duplicated(keep=False)]
produtos = produtos.drop_duplicates()


# Cria uma coluna auxiliar com apenas a parte numérica de 'ID Produto'
produtos['id_num'] = produtos['id_produto'].str.split('-', n=3).str[2]


# Conversao de valores numéricos
vendas['valor_venda'] = vendas['valor_venda'].str.replace(',', '.').astype(float)
vendas['custo_envio'] = vendas['custo_envio'].str.replace(',', '.').astype(float)


# Valor unitário já calculado antes:
vendas['valor_unit'] = vendas['valor_venda'] / vendas['qtd_vendida']
# pedidos_por_produto = vendas.groupby('Produto')['Pedido'].count().reset_index()

# Cria uma coluna auxiliar com apenas a parte numérica de 'ID Produto'
vendas['id_pedido_num'] = vendas['id_pedido'].str.split('-', n=3).str[2]

# # 1. Cria um novo id para cada nome_produto único, sequenciado a partir de 1
novo_id = {nome: idx for idx, nome in enumerate(produtos['nome_produto'].unique(), 1)}

# # 2. Mapeia o novo ID na base
produtos['id_num_novo'] = produtos['nome_produto'].map(novo_id)

# produtos = produtos.drop_duplicates(subset=['nome_produto'])

# Padronização de categorias e subcategorias
categoria_padrao = produtos.groupby('nome_produto')['categoria'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
subcategoria_padrao = produtos.groupby('nome_produto')['subcategoria'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])

# Mapear a categoria padronizada para o DataFrame
produtos['categoria_padronizada'] = produtos['nome_produto'].map(categoria_padrao)
produtos['subcategoria_padronizada'] = produtos['nome_produto'].map(subcategoria_padrao)


### DATASET VENDAS

vendas_novo = vendas.merge(
    produtos[['id_produto', 'id_num_novo', 'nome_produto', 'categoria_padronizada']],
    on='id_produto',
    how='left'
)


tabelao = vendas_novo.merge(
    clientes[['id_cliente', 'cidade', 'estado', 'pais']],
    on='id_cliente',
    how='left'
)

tabelao['id_pedido_num'] = tabelao['id_pedido_num'].astype(str)
pedidos['id_pedido_num'] = pedidos['id_pedido_num'].astype(str)


vendas_clientes_pedidos = tabelao.merge(
    pedidos[['id_pedido_num', 'modo_envio', 'prioridade', 'local_pedido']],
    on='id_pedido_num',
    how='left'
)


# Agora, vendas_novo terá a coluna 'id_num_novo'
colunas_agrup = [
    'id_num_novo',    # ID padronizado do produto
    'nome_produto',
    'cidade',
    'pais',
    'modo_envio',
    'prioridade'
]

analise_envio = (
    vendas_clientes_pedidos
        .groupby(colunas_agrup)['custo_envio']
        .agg(['count', 'min', 'max', 'mean', 'std'])
        .reset_index()
)

# Filtro: apenas onde há mais de 1 pedido naquele agrupamento
varios_pedidos = analise_envio[analise_envio['count'] > 1]

colunas = [
    'id_pedido_num',
    'id_cliente',
    'local_pedido',
    'pais',
    'categoria_padronizada', 
    'id_num_novo', # ID padronizado do produto
    'valor_venda',
    'custo_envio',
    'cidade',
    'modo_envio',
    'prioridade'
]

