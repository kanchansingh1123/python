# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.beer_order import BeerOrder  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrderServiceController(BaseTestCase):
    """OrderServiceController integration test stubs"""

    def test_v1_customers_customer_id_orders_post(self):
        """Test case for v1_customers_customer_id_orders_post

        
        """
        body = BeerOrder()
        response = self.client.open(
            '/v1/customers/{customerId}/orders'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
