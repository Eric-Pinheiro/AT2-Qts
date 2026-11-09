import pytest

@pytest.mark.integration
def test_provision_workstation_success(client, workstation_factory, mocker):
    # Arrange
    payload = workstation_factory()
    mock_notify = mocker.patch("src.main.notify_inventory_system", return_value=True)
    
    # Act
    response = client.post("/api/provision", json=payload)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["hostname"] == payload["hostname"]
    mock_notify.assert_called_once_with(payload["hostname"])

@pytest.mark.integration
def test_provision_workstation_inventory_failure(client, workstation_factory, mocker):
    # Arrange
    payload = workstation_factory()
    mocker.patch("src.main.notify_inventory_system", return_value=False)
    
    # Act
    response = client.post("/api/provision", json=payload)
    
    # Assert
    assert response.status_code == 503
    assert response.json()["detail"] == "Falha ao sincronizar com sistema de inventário"