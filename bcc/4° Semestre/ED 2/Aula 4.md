
disclaimer: arquivo de índices contém todos os índices que referenciam registros dentro dos arquivos de dados.
# Index
Fornece mecanismos para localizar informações. É representado por vetores (maps, nesse caso) que contém as #keys e os campos de referencia. Deve-se criar uma chave primária para acesso à um campo ou guardar a referência ao seu endereço (apenas em runtime).

> Um índice, em geral, tem tamanho fixo e estão em outros arquivos. Tendo 2 campos fixos, a chave e o endereço (lógico ou físico).

### Características 
- Índices devem estar ordenados.
- pode ser usada a busca binária em memória principal.
- registro de tamanho fixo impõem um limite ao tamanho da chave primária.

## Operações
- inserção de registros (de preferencia, mantendo o arquivo de indices na memória interna)
	- inserir no final do arquivo de indices
	- remoção: busca-se o registro em qualquer lugar e remove do jeito que quiser
		- remove o valor do endereço no arquivo de dados
		- ao se retornar, remova a [key](#keys).

### Cuidados
 é importante garantir que os índices que estão em memória principal sejam escritos de volta na memória secundária (write-through ou write-back).
 - pode-se manter uma ==**status flag**== no arquivo de indices que indica que um arquivo está sendo utilizado pela memória principal.
 - flag no header do arquivo de dados.
- reconstrói-se o índice a partir do arquivo de dados, que sempre é atualizado.

# Chave Primárias
 #keys 
### Solução de repetição chave secundária
- associar uma lista de tamanho fixo a cada chave secundária (salvar repetição)
- lista invertidas -> salvar uma lista com as chaves secundárias e garantir a repetição desta associando a posição da próxima repetição, salvando em outro arquivo de índices esta repetição.
# Associação do índice ao endereço físico
- em indices primários 
	- binding -> criado no momento que um arquivo é criado.
- em índices secundários
	- late binding
	

