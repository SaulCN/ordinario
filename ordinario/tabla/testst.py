
import unittest
from unittest import result, TestCase, mock
from unittest.mock import patch, mock_open
from app import usuario
from app import ver_usario
from app import ver_usarios,ver
import mongomock
import requests_mock

class test_ver_usuarios_1_outlow(unittest.TestCase):
    var2=[{"_id":"000051","date":"2020-01-03","amount":"-51.13","type":"outflow","category":"groceries","user_email":"janedoe@email.com"},{"_id":"000053","date":"2020-01-10","amount":"-150.72","type":"outflow","category":"transfer","user_email":"janedoe@email.com"},{"_id":"000054","date":"2020-01-13","amount":"-560.00","type":"outflow","category":"rent","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll.find",return_value= var2)
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver_usarios(),str([{"user_email":"janedoe@email.com","total_inflow":'0',"total_outflow":"-761.85"}]))

class test_ver_usuarios_inflow_3(unittest.TestCase):  
    var=[{"_id":"000052","date":"2020-01-10","amount":"2500.72","type":"inflow","category":"salary","user_email":"janedoe@email.com"},{"_id":"000689","date":"2020-01-10","amount":"150.72","type":"inflow","category":"savings","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll.find",return_value= var)  
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver_usarios(),str([{"user_email":"janedoe@email.com","total_inflow":'2651.4399999999996',"total_outflow":'0'}]))

class test_ver_usuarios(unittest.TestCase):  
    var=[{"_id":"000051","date":"2020-01-03","amount":"-51.13","type":"outflow","category":"groceries","user_email":"janedoe@email.com"},{"_id":"000052","date":"2020-01-10","amount":"2500.72","type":"inflow","category":"salary","user_email":"janedoe@email.com"},{"_id":"000053","date":"2020-01-10","amount":"-150.72","type":"outflow","category":"transfer","user_email":"janedoe@email.com"},{"_id":"000054","date":"2020-01-13","amount":"-560.00","type":"outflow","category":"rent","user_email":"janedoe@email.com"},{"_id":"000689","date":"2020-01-10","amount":"150.72","type":"inflow","category":"savings","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll.find",return_value= var)  
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver_usarios(),str([{"user_email":"janedoe@email.com","total_inflow":'2651.4399999999996',"total_outflow":'-761.85'}]))


class test_ver(unittest.TestCase):  
    var=[{"_id":"000051","date":"2020-01-03","amount":"-51.13","type":"outflow","category":"groceries","user_email":"janedoe@email.com"},{"_id":"000052","date":"2020-01-10","amount":"2500.72","type":"inflow","category":"salary","user_email":"janedoe@email.com"},{"_id":"000053","date":"2020-01-10","amount":"-150.72","type":"outflow","category":"transfer","user_email":"janedoe@email.com"},{"_id":"000054","date":"2020-01-13","amount":"-560.00","type":"outflow","category":"rent","user_email":"janedoe@email.com"},{"_id":"000689","date":"2020-01-10","amount":"150.72","type":"inflow","category":"savings","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll",return_value= var)  
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver("user_email"),{"inflow":{"salary":"0","savings":"0"},"outflow":{"groceries":"0","rent":"0","transfer":"0"}})

class test_ver(unittest.TestCase):  
    var=[{"_id":"000051","date":"2020-01-03","amount":"-51.13","type":"outflow","category":"groceries","user_email":"janedoe@email.com"},{"_id":"000052","date":"2020-01-10","amount":"2500.72","type":"inflow","category":"salary","user_email":"janedoe@email.com"},{"_id":"000053","date":"2020-01-10","amount":"-150.72","type":"outflow","category":"transfer","user_email":"janedoe@email.com"},{"_id":"000054","date":"2020-01-13","amount":"-560.00","type":"outflow","category":"rent","user_email":"janedoe@email.com"},{"_id":"000689","date":"2020-01-10","amount":"150.72","type":"inflow","category":"savings","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll",return_value= var)  
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver("user_email"),{"inflow":{"salary":"0","savings":"0"},"outflow":{"groceries":"0","rent":"0","transfer":"0"}})

class test_ver_1(unittest.TestCase):  
    var=[{"_id":"000051","date":"2020-01-03","amount":"-51.13","type":"outflow","category":"groceries","user_email":"janedoe@email.com"},{"_id":"000052","date":"2020-01-10","amount":"2500.72","type":"inflow","category":"salary","user_email":"janedoe@email.com"},{"_id":"000053","date":"2020-01-10","amount":"-150.72","type":"outflow","category":"transfer","user_email":"janedoe@email.com"},{"_id":"000054","date":"2020-01-13","amount":"-560.00","type":"outflow","category":"rent","user_email":"janedoe@email.com"},{"_id":"000689","date":"2020-01-10","amount":"150.72","type":"inflow","category":"savings","user_email":"janedoe@email.com"}]
    @mock.patch("app.coll.find",return_value= var)  
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(ver("janedoe@email.com"),{"inflow":{"salary":"2500.72","savings":"150.72"},"outflow":{"groceries":"-51.13","rent":"-560.0","transfer":"-150.72"}})

if __name__ =='__main__':
 unittest.main()