import requests

BASE_URL = "http://localhost:3000"
ENDPOINT = "/profissionais/1/associar-aluno"
HEADERS = {"Content-Type": "application/json"}
DATA = {"alunoId": 2749}

def test_associar_aluno():
    # Enviar requisição POST
    response = requests.post(BASE_URL + ENDPOINT, json=DATA, headers=HEADERS)

    # Verificar status da resposta
    assert response.status_code == 200, f"Status code esperado: 200, obtido: {response.status_code}"

    # Verificar mensagem de sucesso
    assert response.json() == "Aluno associado ao profissional com sucesso!", \
        f"Mensagem esperada: 'Aluno associado ao profissional com sucesso!', obtida: {response.json()}"

    print("Teste passou: Aluno associado ao profissional com sucesso.")

if __name__ == "__main__":
    test_associar_aluno()