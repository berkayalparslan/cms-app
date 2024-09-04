from locust import HttpUser, task,between
import time

class TestUser(HttpUser):
    host = 'http://localhost:8000'
    wait_time = between(1,5)
    @task
    def display_posts(self):
        self.client.get('/posts')

    @task
    def display_single_post(self):
        for post in range(2):
            self.client.get('/posts/test-title1725477731357605/')