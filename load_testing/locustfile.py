from locust import HttpUser, task, between

class MyAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_image(self):
        # Tester le GET /generated_images/default2.jpg
        self.client.get("/generated_images/default2.jpg")

    @task
    def generate_meme(self):
        # Tester le POST /generate_meme
        user_input = {"user_input": "Hello World"}
        self.client.post("/generate_meme", json=user_input)
