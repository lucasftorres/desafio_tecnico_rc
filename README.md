# Esta é a documentação do meu projeto

[Meu projeto](https://lucasftorres.github.io/desafio_tecnico_rc/)
# Extração


# Checagem e Processamento:

## Informações:


### Tabela Vendas.csv
Linhas: 51,290  
Colunas: 6

| Pedido | Cliente | Produto | Valor Venda | Quantidade Venda | Custo Envio |
|--------|---------|---------|-------------|------------------|-------------|

---

### Tabela Clientes.csv
Linhas: 1,590  
Colunas: 8

| ID Cliente | Nome Cliente | Segmento | Cidade | Estado | País | Mercado | Região |
|------------|--------------|----------|--------|--------|------|---------|--------|

---

### Tabela Produtos.csv
Linhas: 10,292  
Colunas: 4

| ID Produto | Categoria | SubCategoria | Nome Produto |
|------------|-----------|--------------|--------------|

---

### Tabela Pedidos.csv
Linhas: 25,036  
Colunas: 7

| Local Pedido | Ano | ID Pedido | Data Pedido | Data Envio | Modo Envio | Prioridade Pedido |
|--------------|-----|-----------|-------------|------------|------------|------------------|

-----------------------------------------------------------------------------------------

 - Itens duplicados tabela Produtos.csv:

    |   | ID Produto         | Categoria   | SubCategoria | Nome Produto                                           |
    |---|--------------------|-------------|--------------|--------------------------------------------------------|
    | 0 | TEC-AC-10003033    | Tecnologia  | Accessories  | Plantronics CS510 - Over-the-Head monaural Wir...      |
    | 1 | TEC-AC-10003033    | Tecnologia  | Accessories  | Plantronics CS510 - Over-the-Head monaural Wir...      |


    Observação:
    Produtos que possuem o mesmo nome para vários ID's diferentes:

    | | nome_produto |	Quantidade |
    | ------ | ---- | -------- |
    | 0	| Staples	| 45 |
    | 1	| Stockwell Paper Clips, Assorted Sizes	| 16 |
    | 2	| Acco Index Tab, Clear	| 12 |
    | 3	| Bush Stackable Bookrack, Pine	| 11 |
    | 4	| Stockwell Thumb Tacks, Metal	| 11 |
    ...	...	...
    | 1933 | Advantus Light Bulb, Black	| 2 |
    | 1934 | Panasonic Inkjet, Durable | 2 |
    | 1935 | Hon Computer Table, with Bottom Storage | 2 |
    | 1936 | Prang Drawing Pencil Set | 2 |

    Total de 1938 itens representando 18.8% do total

    Porém somente 2 produtos estão cadastrados em subcategorias diferentes:


    | Subcategorias | Produto |
    |------------|--------------------------------------------|
    | 2          | Harbour Creations Executive Leather Armchair|
    | 10         | Staples                                    |



-----------------------------------------------------------------------------------------

- Itens duplicados tabela Clientes.csv
       
    Foi encontrada uma quantidade significativa de nomes repetidos, 
    mas com diferentes cidades/estados/regiões, o que indica homônimos 
    ou diferentes pessoas. Caso fosse feito um merge/junção apenas 
    pelo nome, haveria risco de misturar perfis distintos.
    Nomes iguais com outros atributos diferentes geralmente 
    representam pessoas diferentes (homônimos), ou dependendo do contexto do 
    negócio, podem ser a mesma pessoa com múltiplos cadastros 
    (por exemplo, mudou de cidade, atua em segmentos diferentes etc).

-----------------------------------------------------------------------------------------


 - Itens duplicados tabela Pedidos.csv

    |   | Local Pedido | Ano | ID Pedido | Data Pedido | Data Envio | Modo Envio | Prioridade Pedido |
    |---|--------------|-----|-----------|-------------|------------|------------|------------------|
    | 0 | CA           | 2012| 124891    | 31/07/2012  | 31/07/2012 | Mesmo Dia  | Critico          |
    | 1 | CA           | 2012| 124891    | 31/07/2012  | 31/07/2012 | Mesmo Dia  | Critico          |


    Observação: 3518 Pedidos possuem o mesmo pedido_num


-----------------------------------------------------------------------------------------

 - Itens Duplicados tabela Vendas.csv

    Após a padronização dos ID's na tabela produtos e checagem na tabela vendas, 
    foi identificado 32281 vendas que possuiam id_produto
    diferentes para o mesmo nome_produto representando aproximadamente 63% do total.
    Em contextos reais esse percentual deveria ser investigado.

-----------------------------------------------------------------------------------------

# Transformação:

## 1 - Tratamentos Gerais:
    - Conversão de Datas da tabela pedidos;
    - Renomear colunas;
    - Conversão de Tipos textual para numérico da tabela vendas;
    - Criação de novas colunas 'valor_unit' na tabela vendas e 'id_pedido' na tabela pedidos;
## 2 - Tabela dim_produtos
    - Unificação dos ID's dos produtos que possuiam o mesmo nome para ID's diferentes;
        - Redução de 10292 para 3660 produtos
    - Checagem comparativa da tabela produto x vendas;
    - Criação da surrogate key da tabela produtos sk_produto;
## 3 - Tabela dim_clientes
    - Criação da surrogate key da tabela clientes sk_cliente;
## 4 - Tabela dim_pedidos
    - Criação da surrogate key da tabela pedidos sk_pedido;
## 5 - Tabela dim_data
    - Criação da Tabela;
    - Associação a tabela pedidos;
## 6 - Organização das Colunas
    - Remoção de colunas temporárias;
    - Reordenação;
    - Merge final da tabela fato_vendas;
## 7 - Outliers
    - Para valor_venda, foram encontrados 5.655 registros considerados outliers;
    - Para custo_envio, foram 5.022 registros identificados como outliers;

        - Eles podem distorcer análises estatísticas;
        - Podem sinalizar oportunidades de investigação, ajustes ou limpeza de dados;
        - Ajudam a deixar relatórios e modelos preditivos mais consistentes e realistas;









# desafio_tecnico_rc
