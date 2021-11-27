# INF1407-2021.2 
PUC-Rio - INF1407 - Programação para a Web - 2021.2
---
## Trabalho 2 - Site de Tracking de Jogos
## Membro do grupo: Felipe Holanda Bezerra - 1810238

### Descrição Breve
Usuários cadastrados podem alimentar a plataforma com dados sobre os games que estão jogando.
Usuários não cadastrados podem apenas fazer buscas e visualizar os games e dados brutos anonimizados sobre estes.

### O que foi desenvolvido
- Cadastro de Usuários
	- Username
	- Senha
	- Email
	- Bio (opcional)
- Login / Logout de Usuários
	- Recuperar senha por email (via link da console)
	- Usuários logados: 
		- Cadastrar jogos
		- Trocar senha
		- Digitar / Atualizar bio (curta biografia de até 150 caracteres)
		- Visualizar a lista pessoal de jogos
			- Título
			- Desenvolvedor
			- Publicador
			- Tempo de jogo
			- Status (ainda jogando, complecionista, completou o principal ou apenas partes)
- Operações CRUD no banco:
	- Jogos
	- Usuários
- Usuários visitantes podem visualizar todos os jogos (clicando no botão Buscar sem digitar um título) ou buscar por um jogo específico (digitando um título e clicando no botão Buscar)
	- Para fins de demonstração, cada jogo exibe apenas dados de Título, Desenvolvedor e Publicador	
- Cadastro de Usuários usa Ajax para checar se já existe o username
- Atualização de bio usa Ajax para indicar quantos caracteres foram digitados

### O que não foi desenvolvido
- Sistema de Resenhas
- Estatísticas anonimizados gerais para visitantes