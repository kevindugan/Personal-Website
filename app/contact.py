from azure.communication.email import EmailClient
from flask import flash

class EmailContact:

    def __init__(self,
                 admin_email=None,
                 azure_email=None,
                 connection=None,
                 wait=10,
                 timeout=200):
        self.admin_email = admin_email
        self.azure_email = azure_email
        self.connection_string = connection

        self.poll_wait = wait
        self.send_timeout = timeout

    def generateMessageObject(self, form_data):
        return {
            "content": {
                "subject": "Contact from Website",
                "plainText": f"Name: {form_data['name']}\n"
                             f"Email: {form_data['email']}\n\n"
                             f"{form_data['message']}"
            },
            "recipients": {
                "to": [
                    {
                        "address": self.admin_email,
                        "displayName": "Admin"
                    }
                ]
            },
            "senderAddress": self.azure_email
        }

    def sendContactEmail(self, form_data):
        message = self.generateMessageObject(form_data)
        email_client = EmailClient.from_connection_string(self.connection_string)
        
        try:
            self.waitForSend( email_client.begin_send(message) )
            # self.waitForSend(Poller())
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def waitForSend(self, poller):
        elapsed_time = 0
        while not poller.done():
            print(f"Email send poller status: {poller.status()}")
            poller.wait(self.poll_wait)

            elapsed_time += self.poll_wait
            if elapsed_time > self.send_timeout:
                raise RuntimeError("Email send timed out.")

        if poller.status() == "Succeeded":
            print(f"Successfully sent the email (operation id: {poller.result()['id']})")
        else:
            raise RuntimeError(str(poller.result()["error"]))


# from time import time, sleep
# class Poller:
#     def __init__(self):
#         self.live_time = time()
#         self.finish = self.live_time + 30

#     def done(self):
#         return time() > self.finish
    
#     def status(self):
#         return "Succeeded" if self.done() else "InProgress"
    
#     def wait(self, duration):
#         sleep(duration)

#     def result(self):
#         return {"id": "2134"}