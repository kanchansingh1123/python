# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BeerOrderLine(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, beer_id: str=None, upc: str=None, order_quantity: int=None, quantity_allocated: int=None):  # noqa: E501
        """BeerOrderLine - a model defined in Swagger

        :param id: The id of this BeerOrderLine.  # noqa: E501
        :type id: str
        :param beer_id: The beer_id of this BeerOrderLine.  # noqa: E501
        :type beer_id: str
        :param upc: The upc of this BeerOrderLine.  # noqa: E501
        :type upc: str
        :param order_quantity: The order_quantity of this BeerOrderLine.  # noqa: E501
        :type order_quantity: int
        :param quantity_allocated: The quantity_allocated of this BeerOrderLine.  # noqa: E501
        :type quantity_allocated: int
        """
        self.swagger_types = {
            'id': str,
            'beer_id': str,
            'upc': str,
            'order_quantity': int,
            'quantity_allocated': int
        }

        self.attribute_map = {
            'id': 'id',
            'beer_id': 'beerId',
            'upc': 'upc',
            'order_quantity': 'orderQuantity',
            'quantity_allocated': 'quantityAllocated'
        }
        self._id = id
        self._beer_id = beer_id
        self._upc = upc
        self._order_quantity = order_quantity
        self._quantity_allocated = quantity_allocated

    @classmethod
    def from_dict(cls, dikt) -> 'BeerOrderLine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BeerOrderLine of this BeerOrderLine.  # noqa: E501
        :rtype: BeerOrderLine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BeerOrderLine.


        :return: The id of this BeerOrderLine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BeerOrderLine.


        :param id: The id of this BeerOrderLine.
        :type id: str
        """

        self._id = id

    @property
    def beer_id(self) -> str:
        """Gets the beer_id of this BeerOrderLine.


        :return: The beer_id of this BeerOrderLine.
        :rtype: str
        """
        return self._beer_id

    @beer_id.setter
    def beer_id(self, beer_id: str):
        """Sets the beer_id of this BeerOrderLine.


        :param beer_id: The beer_id of this BeerOrderLine.
        :type beer_id: str
        """

        self._beer_id = beer_id

    @property
    def upc(self) -> str:
        """Gets the upc of this BeerOrderLine.


        :return: The upc of this BeerOrderLine.
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc: str):
        """Sets the upc of this BeerOrderLine.


        :param upc: The upc of this BeerOrderLine.
        :type upc: str
        """
        if upc is None:
            raise ValueError("Invalid value for `upc`, must not be `None`")  # noqa: E501

        self._upc = upc

    @property
    def order_quantity(self) -> int:
        """Gets the order_quantity of this BeerOrderLine.


        :return: The order_quantity of this BeerOrderLine.
        :rtype: int
        """
        return self._order_quantity

    @order_quantity.setter
    def order_quantity(self, order_quantity: int):
        """Sets the order_quantity of this BeerOrderLine.


        :param order_quantity: The order_quantity of this BeerOrderLine.
        :type order_quantity: int
        """
        if order_quantity is None:
            raise ValueError("Invalid value for `order_quantity`, must not be `None`")  # noqa: E501

        self._order_quantity = order_quantity

    @property
    def quantity_allocated(self) -> int:
        """Gets the quantity_allocated of this BeerOrderLine.


        :return: The quantity_allocated of this BeerOrderLine.
        :rtype: int
        """
        return self._quantity_allocated

    @quantity_allocated.setter
    def quantity_allocated(self, quantity_allocated: int):
        """Sets the quantity_allocated of this BeerOrderLine.


        :param quantity_allocated: The quantity_allocated of this BeerOrderLine.
        :type quantity_allocated: int
        """

        self._quantity_allocated = quantity_allocated
