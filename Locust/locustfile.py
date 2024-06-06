from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def call_api(self):
        self.client.post("/dynamodbmanager", json={"id": "12345"})
