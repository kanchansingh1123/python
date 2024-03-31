# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.beer import Beer  # noqa: E501
from swagger_server.models.beer_paged_list import BeerPagedList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBeersController(BaseTestCase):
    """BeersController integration test stubs"""

    def test_delete_beer_v1(self):
        """Test case for delete_beer_v1

        Delete Beer by Id
        """
        response = self.client.open(
            '/v1/beers/{beerId}'.format(beer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_beer_by_id_v1(self):
        """Test case for get_beer_by_id_v1

        Get Beer by ID
        """
        response = self.client.open(
            '/v1/beers/{beerId}'.format(beer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_beers_v1(self):
        """Test case for list_beers_v1

        List Beers
        """
        query_string = [('page_number', 1),
                        ('page_size', 25)]
        response = self.client.open(
            '/v1/beers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_beer_by_id_v1(self):
        """Test case for update_beer_by_id_v1

        Update Beer by ID
        """
        body = Beer()
        response = self.client.open(
            '/v1/beers/{beerId}'.format(beer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v1_beers_post(self):
        """Test case for v1_beers_post

        New Beer
        """
        body = Beer()
        response = self.client.open(
            '/v1/beers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
