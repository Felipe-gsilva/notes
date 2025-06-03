Nos referimos ao requerente ou usuário no contexto da autenticação como `agente`. 
Toda estrutura de dados usada para o gerenciamento de permissões e decisões como esta são chamados de `credenciais`.
Tais credencias dão informações importante para que o SO decida se o agente pode ou não acessar um `objeto` da requisição.

Empiricamente, sabemos que usuários e programas tem privilégios de acesso a objetos distintos e o escopo deste acesso tem que ser gerenciado pelo SO. Para endereçar esse problema, podemos escrever cada processo com sua identidade própria, associado ao ID do usuário também.

Entretanto, como podemos autenticar o usuário? "confirmar que ele é quem diz ser"

# Autenticação 

- Autenticação baseada no que se sabe, ou seja, apenas usar uma senha (algo que o usuário sabe) -> criptografia:
- Autenticação baseada no que você tem
- Autenticação baseada no que você é
