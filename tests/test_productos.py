import unittest

from flask import request

from tests.base import BaseTestCase
from clikpik import Producto



class TestProductos(BaseTestCase):


    def test_productos(self):
        result = self.client.get("/productos")
        self.assertEqual(result.status_code, 200)
        pass

    def test_putproducto(self):
        result = self.client.put("/productos", data={"nombre": 'test1', "ubicacion": 'test2' })
        self.assertEqual(result.status_code, 200)
        pass
if __name__ == '__main__':
    unittest.main()