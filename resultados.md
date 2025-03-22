
# Resultados do Teste

## Data e Hora da Execução

- Data: 2025-03-21  
- Hora: 14:30 (UTC)

## Configuração do Ambiente

- Servidor Backend: Rodando em http://localhost:3000.
- Banco de Dados: Populado com os seguintes dados:

  - Profissional:  

    ```json
    {
      "id": 1,
      "nome": "Dr. João",
      "especialidade": "Fisioterapeuta",
      "contato": "joao@example.com"
    }
    ```

  - Aluno:  

    ```json
    {
      "id": 2749,
      "nome": "Maria Oliveira",
      "tipo_deficiencia": "Visual",
      "necessidades": "Material em braille"
    }
    ```

## Requisição Enviada

- Endpoint: `POST /profissionais/1/associar-aluno`
- Corpo da Requisição:

  ```json
  {
    "alunoId": 2749
  }
  ```

## Resposta da API

- Status Code: 200 OK
- Corpo da Resposta:

"Aluno associado ao profissional com sucesso!"

## Validação no Banco de Dados

Após a execução do teste, foi verificado que o registro foi inserido corretamente na tabela atendimento com os seguintes valores:

```json
{
  "id": 1,
  "profissional_id": 1,
  "aluno_id": 2749,
  "data_inicio": "2025-03-21T14:30:00Z"
}
```

## Pós-condição

### Estado do Banco de Dados:

Um novo registro foi adicionado à tabela atendimento com os valores corretos:

- profissional_id = 1
- aluno_id = 2749
- data_inicio preenchido automaticamente com a data e hora da execução do teste.

### Impacto no Sistema:

- O profissional com id = 1 agora está associado ao aluno com id = 2749.
- Nenhum outro dado foi alterado no banco de dados.

## Conclusão:

O teste foi bem-sucedido. O endpoint `POST /profissionais/:profissionalId/associar-aluno` está funcionando conforme o esperado, associando o aluno ao profissional e preenchendo automaticamente o campo data_inicio.