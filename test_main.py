import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from datetime import datetime
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Teste do endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "greeting": "Hello, World!",
        "message": "Welcome to FastAPI!"
    }

@patch('main.requests.get')
def test_datas_indisponiveis_success(mock_get):
    """Teste do endpoint de datas indisponíveis com sucesso"""
    # Mock da resposta do calendário iCal
    mock_ical_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Test//Test//EN
BEGIN:VEVENT
DTSTART:20240115T140000Z
DTEND:20240117T110000Z
SUMMARY:Test Event
END:VEVENT
END:VCALENDAR"""
    
    mock_response = Mock()
    mock_response.text = mock_ical_content
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    response = client.get("/datas-indisponiveis")
    assert response.status_code == 200
    
    data = response.json()
    assert "datas_indisponiveis" in data
    assert isinstance(data["datas_indisponiveis"], list)

@patch('main.requests.get')
def test_datas_indisponiveis_request_error(mock_get):
    """Teste do endpoint com erro de requisição"""
    mock_get.side_effect = Exception("Connection error")
    
    response = client.get("/datas-indisponiveis")
    assert response.status_code == 200
    
    data = response.json()
    assert "error" in data
    assert "Connection error" in data["error"]

@patch('main.requests.get')
def test_datas_indisponiveis_empty_calendar(mock_get):
    """Teste com calendário vazio"""
    mock_ical_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Test//Test//EN
END:VCALENDAR"""
    
    mock_response = Mock()
    mock_response.text = mock_ical_content
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    response = client.get("/datas-indisponiveis")
    assert response.status_code == 200
    
    data = response.json()
    assert "datas_indisponiveis" in data
    assert data["datas_indisponiveis"] == []

@patch('main.requests.get')
def test_datas_indisponiveis_multiple_events(mock_get):
    """Teste com múltiplos eventos"""
    mock_ical_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Test//Test//EN
BEGIN:VEVENT
DTSTART:20240115T140000Z
DTEND:20240116T110000Z
SUMMARY:Test Event 1
END:VEVENT
BEGIN:VEVENT
DTSTART:20240120T140000Z
DTEND:20240122T110000Z
SUMMARY:Test Event 2
END:VEVENT
END:VCALENDAR"""
    
    mock_response = Mock()
    mock_response.text = mock_ical_content
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    response = client.get("/datas-indisponiveis")
    assert response.status_code == 200
    
    data = response.json()
    assert "datas_indisponiveis" in data
    assert len(data["datas_indisponiveis"]) > 0

def test_health_check():
    """Teste básico de saúde da API"""
    response = client.get("/")
    assert response.status_code == 200 