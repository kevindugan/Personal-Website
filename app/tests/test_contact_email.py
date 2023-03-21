from ..contact import EmailContact
from azure.communication.email import EmailClient
import pytest

def test_get_form_data_full():
    
    contactor = EmailContact(admin_email="admin@domain.com", azure_email="azure@domain.com")
    form = {
        "name": "test name",
        "email": "test@domain.com",
        "message": "Hey there\n some other text"
    }

    result = contactor.generateMessageObject(form)
    assert result["content"]["subject"] == "Contact from Website"
    assert result["content"]["plainText"] == f"Name: {form['name']}\nEmail: {form['email']}\n\n{form['message']}"
    assert len(result["recipients"]["to"]) == 1
    assert result["recipients"]["to"][0]["address"] == "admin@domain.com"
    assert result["senderAddress"] == "azure@domain.com"

def test_send_message(monkeypatch):
    monkeypatch.setattr(EmailClient, "from_connection_string", lambda x: MockEmailClient(x))

    contactor = EmailContact(connection="testConnectionString")
    form = {
        "name": "test",
        "email": "test@domain.com",
        "message": "testing"
    }

    try:
        contactor.sendContactEmail(form)
    except Exception as e:
        pytest.fail(f"Exception Raised: {e}")

def test_send_timeout(monkeypatch):
    monkeypatch.setattr(EmailClient, "from_connection_string", lambda x: MockEmailClient(x))

    contactor = EmailContact(wait=12, timeout=24)
    form = {
        "name": "test",
        "email": "test@domain.com",
        "message": "testing"
    }

    with pytest.raises(RuntimeError) as ex:
        contactor.sendContactEmail(form)
    assert "timed out" in str(ex.value)

#========================================================================================
# Mock Objects
#========================================================================================

class MockEmailClient:
    def __init__(self, connection):
        self.connection_string = connection
        print(f"Mock Client: {self.connection_string}")

    def begin_send(self, message):
        print("Mock Start Send")
        return MockEmailPoller()
    
class MockEmailPoller:
    def __init__(self):
        self.query = 0

    def done(self):
        self.query += 1
        return True if self.query > 5 else False
    
    def status(self):
        return "Succeeded" if self.query > 5 else "InProgress"
    
    def wait(self, time):
        pass

    def result(self):
        return {"id": "1234", "error": None}