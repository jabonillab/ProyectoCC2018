import unittest
import json
from flask import request

from tests.base import BaseTestCase
from clikpik import Producto



class TestProductos(BaseTestCase):


    def test_productos(self):
        result = self.client.get("/productos")
        self.assertEqual(result.status_code, 200)
        pass

    def test_putproducto(self):
        data = {
            "ubicacion": "lat,test",
            "nombre": "test1"
        }
        datos = json.dumps(data)
        headers = {'content-type': 'application/json'}
        result = self.client.put("/productos", data=datos, headers=headers)
        self.assertEqual(result.status_code, 200)
        pass
if __name__ == '__main__':
    unittest.main()