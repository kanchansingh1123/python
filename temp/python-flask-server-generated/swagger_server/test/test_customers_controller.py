# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_paged_list import CustomerPagedList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomersController(BaseTestCase):
    """CustomersController integration test stubs"""

    def test_delete_customer_v1(self):
        """Test case for delete_customer_v1

        Delete Customer By ID
        """
        response = self.client.open(
            '/v1/customers/{customerId}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_id_v1(self):
        """Test case for get_customer_by_id_v1

        Get Customer By ID
        """
        response = self.client.open(
            '/v1/customers/{customerId}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_customers_v1(self):
        """Test case for list_customers_v1

        List Customers
        """
        query_string = [('page_number', 1),
                        ('page_size', 25)]
        response = self.client.open(
            '/v1/customers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v1_customers_customer_id_put(self):
        """Test case for v1_customers_customer_id_put

        Update Customer
        """
        body = Customer()
        response = self.client.open(
            '/v1/customers/{customerId}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v1_customers_post(self):
        """Test case for v1_customers_post

        New Customer
        """
        body = Customer()
        response = self.client.open(
            '/v1/customers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
