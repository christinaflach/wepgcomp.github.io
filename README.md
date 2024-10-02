# Site do WEPGCOMP

Este repositório contém o código-fonte do site do Workshop de Estudantes de Pós-Graduação em Ciência da Computação (WEPGCOMP) do Programa de Pós-Graduação em Computação (PGCOMP) do Instituto de Computação da Universidade Federal da Bahia (UFBA).

## Guidelines para organizadores

[Consulte aqui](./_organizacao.md) as orientações para organizadores do WEPGCOMP.

## Configuração

O site é construído com [Jekyll](https://jekyllrb.com/), um gerador de sites estáticos. Para rodar o site localmente, você precisará do Ruby 3.0.5.

Para **baixar as dependências** do repositório, execute o seguinte comando:

```bash
bundle install
```

Para **rodar o site** localmente, execute o seguinte comando:

```bash
bundle exec jekyll serve -i
```

## Criação de página para uma nova edição do evento

Para criar uma nova edição do evento, você precisará criar cópias de arquivos e pastas de uma edição anterior e editar os arquivos copiados.

A seguir, um exemplo de como criar uma nova edição do evento para o ano de 2024. Primeiramnente, crie uma cópia das pastas relevantes:

```bash
cp -r 2023 2024
cp -r _layouts/2023 _layouts/2024
```

A seguir, edite os seguintes arquivos:

- `index.html`: atualizar ano
- `2024/index.md`: atualizar informações
- `_layouts/2024/event.html`: atualizar links do menu
- `2024/*.md`: atualizar informações


## Publicação

Para publicar suas alterações, envie-as para o repositório do GitHub. O site é publicado automaticamente pelo GitHub Pages.
