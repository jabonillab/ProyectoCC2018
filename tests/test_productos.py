import unittest

from flask import request

from tests.base import BaseTestCase
from clikpik import Producto



class TestProductos(BaseTestCase):


    def test_productos(self):
        result = self.client.get("/productos")
        self.assertEqual(result.status_code, 200)
        pass

    def test_postproducto(self):
        result = self.client.post("/productos/test1/test1")
        self.assertEqual(result.status_code, 200)
        pass
if __name__ == '__main__':
    unittest.main()