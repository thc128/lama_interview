import os
import unittest

from src.app import app


def file_reader(path):
    with open(path, 'r') as input_file:
        return input_file.read()


def examples_reader():
    examples_dir = os.path.join("src", "request_examples")
    files = [os.path.join(examples_dir, file) for file in os.listdir(examples_dir)]
    examples = [file_reader(path) for path in sorted(files)]
    return examples
    
    
class ApplicationMatchTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.examples = examples_reader()
        self.headers = {"Content-Type": "application/json"}
        
    def test_first(self):
        response = self.client.post("/applicationMatch", headers=self.headers, data=self.examples[0])
        assert response.status_code == 200
        assert response.json == []
        
    def test_second(self):
        response = self.client.post("/applicationMatch", headers=self.headers, data=self.examples[1])
        assert response.status_code == 200
        assert response.json == ["First Lama Bank", "Lama International Bank"]
        
    def test_third(self):
        response = self.client.post("/applicationMatch", headers=self.headers, data=self.examples[2])
        assert response.status_code == 200
        assert response.json == ["Bank HaPoalama", "First Lama Bank"]
        
        

if __name__ == "__main__":
    unittest.main()