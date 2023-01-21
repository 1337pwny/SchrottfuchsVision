import requests
class RestClient:
    def __init__(self, hostname="localhost", port="5000"):
        self.hostname = hostname
        self.port = port
    def setDistance(self, value):

        session = requests.session()
        try:
            resp = session.get(f"http://{self.hostname}:{self.port}/graph?name=distance,value={value}")
        except Exception:
            return
