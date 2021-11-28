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
- Na página de Atualização de Bio, usa-se Ajax para indicar quantos caracteres foram digitados

### O que não foi desenvolvido
- Sistema de Resenhas
	- Usuários com cadastro podem publicar e atualizar notas e resenhas de jogos públicas (visitantes podem visualizar)
- Estatísticas anonimizadas gerais para visitantes

### Para Testar (Manual do Usuário)
- Fazer uma conta
	- Digitar um username válido (que ainda está disponível)
	- Digitar e confirmar senha (a senha precisa seguir algumas regras, conferir no settings do app)
	- Email (pode ser fictício)
	- Ao confirmar, o site vai para a tela de Login
	- Ao logar, o usuário tem a opção de completar o cadastro com uma bio, o botão fica na barra superior do site
	- Depois de logado, o usuário pode trocar a senha, clicando no botão presente na barra superior do site
- Incluir um jogo
	- Na visão da lista pessoal clicar em Acrescentar um Jogo
	- Inserir os dados atentando para Título, Desenvolvedor e Publicadora (campos obrigatórios)
	- Clicar no botão de confirmação (Essa operação pode demorar alguns segundos, pois o site busca a capa do jogo para salvar na plataforma)
- Atualizar ou remover um jogo
	- Clicar no botão referente na linha do jogo desejado, na lista pessoal
- Logout
	- Clicar no botão de Logout no canto superior direito
- Reset da senha via email
	- Seguir os passos dados em aula, capturando o link enviado pela console do IDE
- Botão Buscar
	- Sem necessidade de cadastro
	- Com título digitado: O site busca pelo jogo com o título digitado ou um título aproximado
	- Sem título: O site exibe todos os jogos da plataforma
