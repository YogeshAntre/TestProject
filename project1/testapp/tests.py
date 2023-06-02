from django.test import TestCase
from django.db import transaction
# Create your tests here.
from rest_framework.test import APITestCase
from testapp.models import Product
import json
from rest_framework.test import APIClient
#from django.contrib.auth import get_user_model
from django.test import TestCase,RequestFactory
from django.contrib.auth.models import User


class Product_TestCase(TestCase):
    print('----------------------------Product UNIT Test CaSE--------------------------------')
    def setUp(self):
        self.args = {
            'name':'TELICOm',
            'desc':'ACC',
            'price':123.23,
            'qty':3
        }
        with transaction.atomic():
            pp=Product.objects.create( **self.args )
    def Test_01(self):
            
        response = self.client.get('/pro/data/1')
        self.assertEqual(response.status_code, 200)
        ss = json.loads(response.content)
        
        self.assertEqual(ss['id'], 1)
        

        response = self.client.get('/pro/data/3')
        self.assertEqual(response.status_code, 404)
    

    def Test_03(self):
        """
            Request all Product datastored in the backend 
        """
        response = self.client.get('/pro/data')
        self.assertEqual(response.status_code, 200)
        product = json.loads(response.content)
        self.assertEqual(len(product), 1)        

        self.assertTrue('id' in product[0].keys())
        self.assertTrue('name' in product[0].keys())
        self.assertTrue('desc' in product[0].keys())
        self.assertTrue('price' in product[0].keys())
        self.assertTrue('qty' in product[0].keys())
    

    def Test_04(self):
        """
            Request update the data values
        
        """
        self.factory = RequestFactory()
        self.admin_user = User.objects.create(username='admin',password='admin')
        self.client = APIClient()        
        test= self.client.force_authenticate(user=self.admin_user)
        self.args['id']=1 
        self.args['name']='example'        
        self.args['desc']='FR'
        self.args['price']=2234.45
        self.args['qty']=3


        response = self.client.patch('/pro/data/1', data=self.args, format='json')
        self.assertEqual(response.status_code, 200)
        #Verify the able to get updated name in the corresponding
        ss = json.loads(response.content)
        print(ss)
        self.assertEqual(ss['name'], 'example')
        response = self.client.get('/pro/data/1')
        self.assertEqual(response.status_code, 200)

    def test_05_delete(self):
        """
            Request delete the data stored in the backend 
        """
        self.factory = RequestFactory()
        self.admin_user = User.objects.create(username='admin',password='admin')
        self.client = APIClient()        
        test= self.client.force_authenticate(user=self.admin_user)        
        response = self.client.delete('/pro/data/1')
        self.assertEqual(response.status_code, 204)
        #Verify the able to get deleted systemsettings throws 404
        response = self.client.get('pro/data/1')
        self.assertEqual(response.status_code, 404)