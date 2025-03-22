# Gestorin - Teste Automatizado

Este repositório contém testes automatizados para a API Gestorin, com foco na funcionalidade de associação de alunos a profissionais.

## Estrutura do Repositório

- `caso_de_teste.md`: Descrição detalhada do caso de teste
- `teste_automatizado.py`: Script Python para automação do teste
- `resultados.md`: Resultados da execução do teste

## Caso de Teste: Associar Aluno a Profissional

O teste verifica se o endpoint `POST /profissionais/:profissionalId/associar-aluno` associa corretamente um aluno a um profissional, preenchendo automaticamente o campo `data_inicio` no banco de dados.

### Pré-condição
- O banco de dados deve conter um profissional com id = 1
- O banco de dados deve conter um aluno com id = 2749
- O campo data_inicio deve ser configurado para ser preenchido automaticamente no backend

### Procedimento
O teste envia uma requisição POST para o endpoint e verifica se:
1. A API retorna a resposta esperada
2. O registro foi criado corretamente no banco de dados

### Execução do Teste
Para executar o teste automatizado:

```bash
python teste_automatizado.py
```

## Resultados

Os resultados da execução do teste estão documentados no arquivo `resultados.md`.