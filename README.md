# Sistema de Recomendação de Filmes - Projeto NoSQL

## Descrição

Este projeto tem como objetivo implementar um sistema de recomendação de filmes usando um banco de dados NoSQL, inspirado na plataforma Letterboxd. A aplicação permite que usuários avaliem filmes e, com base em suas avaliações, sugere filmes que outros usuários com gostos semelhantes também apreciaram. A lógica de recomendação se baseia em identificar usuários que deram notas semelhantes ao mesmo filme, oferecendo recomendações personalizadas.

## Funcionalidades

- **Avaliação de filmes**: Usuários podem avaliar filmes com uma nota de 1 a 10.
- **Recomendação de filmes**: Se o usuário A e o usuário B derem uma nota semelhante a um filme X, o sistema recomenda a A outros filmes que B avaliou com uma nota semelhante.
- **Recomendação por similaridade de nota**: Filmes com notas próximas também podem ser recomendados, expandindo as opções de recomendação.
- **Filtro por gênero**: Os usuários podem optar por refinar as recomendações com base no gênero do filme.

## Como os usuários podem utilizá-lo

- **Registrar-se**: O usuário pode criar um perfil no sistema.
- **Avaliar filmes**: Após o registro, o usuário pode buscar por filmes e dar notas de 1 a 10.
- **Receber recomendações**: Com base nas notas atribuídas, o sistema sugerirá novos filmes para assistir, recomendando aqueles avaliados por outros usuários com gostos semelhantes.
- **Refinar recomendações**: O usuário pode utilizar filtros, como gêneros de filmes, para personalizar ainda mais suas recomendações.

## Onde os usuários podem encontrar ajuda sobre o projeto

Para obter ajuda, os usuários podem:

- **Consultar a documentação**: Dentro do repositório do projeto, haverá uma documentação técnica detalhada explicando como usar as funcionalidades e resolver problemas comuns.

---

## Mapeamento de Coleções e Atributos

### Coleção `usuarios`
- **Atributos**:
  - `usuario_id` (chave primária)
  - `nome`
  - `email`
  - `senha`

### Coleção `filmes`
- **Atributos**:
  - `filme_id` (chave primária)
  - `titulo`
  - `genero`
  - `ano`

### Coleção `avaliacoes`
- **Atributos**:
  - `avaliacao_id` (chave primária)
  - `usuario_id` (chave estrangeira para `usuarios`)
  - `filme_id` (chave estrangeira para `filmes`)
  - `nota` (de 1 a 10)

---

## Relacionamento Entre as Coleções

### Relacionamento `usuarios` - `avaliacoes`
- **Tipo de relacionamento**: Um para muitos (um usuário pode ter várias avaliações).
- **Chave de relacionamento**: O campo `usuario_id` na coleção `avaliacoes` faz referência ao campo `usuario_id` na coleção `usuarios`.

### Relacionamento `filmes` - `avaliacoes`
- **Tipo de relacionamento**: Um para muitos (um filme pode ter várias avaliações).
- **Chave de relacionamento**: O campo `filme_id` na coleção `avaliacoes` faz referência ao campo `filme_id` na coleção `filmes`.

---

## Diagrama de Relações

```plaintext
   usuarios              avaliacoes             filmes
+--------------+       +----------------+     +--------------+
| usuario_id   | <-----| usuario_id      |     | filme_id     |
| nome         |       | filme_id        |---->| titulo       |
| email        |       | nota            |     | genero       |
| senha        |       +----------------+     | ano          |
+--------------+                             +--------------+
