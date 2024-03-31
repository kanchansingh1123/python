# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.address import Address  # noqa: F401,E501
from swagger_server import util


class Customer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, first_name: str=None, last_name: str=None, address: Address=None):  # noqa: E501
        """Customer - a model defined in Swagger

        :param id: The id of this Customer.  # noqa: E501
        :type id: str
        :param first_name: The first_name of this Customer.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Customer.  # noqa: E501
        :type last_name: str
        :param address: The address of this Customer.  # noqa: E501
        :type address: Address
        """
        self.swagger_types = {
            'id': str,
            'first_name': str,
            'last_name': str,
            'address': Address
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'address': 'address'
        }
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Customer.


        :param id: The id of this Customer.
        :type id: str
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Customer.


        :return: The first_name of this Customer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Customer.


        :return: The last_name of this Customer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def address(self) -> Address:
        """Gets the address of this Customer.


        :return: The address of this Customer.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address: Address):
        """Sets the address of this Customer.


        :param address: The address of this Customer.
        :type address: Address
        """

        self._address = address
