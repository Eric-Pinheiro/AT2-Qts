from locust import HttpUser, task, between
import random
import string

class ProvisioningUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def view_portal(self):
        self.client.get("/")

    @task(1)
    def provision_machine(self):
        hostname = "PC-" + "".join(random.choices(string.ascii_uppercase, k=6))
        self.client.post("/api/provision", json={
            "hostname": hostname,
            "os_version": "Win11_Pro_23H2"
        })