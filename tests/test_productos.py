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
        headers = {'content-type': 'application/json'}
        result = self.client.put("/productos", data={"ubicacion":"test1","nombre":"test2"}, headers=headers)
        self.assertEqual(result.status_code, 200)
        pass
if __name__ == '__main__':
    unittest.main()