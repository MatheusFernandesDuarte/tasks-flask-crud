import pytest, requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# CRUD
def test_create_task():
    new_task_data = {
        "title": "Estudar Python",
        "description": "No curso"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200

    response_json = response.json()
    assert 'message' in response_json
    assert 'id' in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200

    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        
        assert response.status_code == 200

        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Teste de nova descrição",
            "title": "Teste de novo título"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        
        response.status_code == 200

        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa específica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        
        assert response.status_code == 200

        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        
        response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404