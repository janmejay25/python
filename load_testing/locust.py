# locustfile.py
from locust import HttpUser, task, between

class MyWebsiteUser(HttpUser):
    wait_time = between(1, 3)  # seconds between tasks

    @task
    def load_home_page(self):
        self.client.get("/")  # Replace with your endpoint
