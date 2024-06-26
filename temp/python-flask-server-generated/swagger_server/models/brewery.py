# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Brewery(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, location: str=None):  # noqa: E501
        """Brewery - a model defined in Swagger

        :param name: The name of this Brewery.  # noqa: E501
        :type name: str
        :param location: The location of this Brewery.  # noqa: E501
        :type location: str
        """
        self.swagger_types = {
            'name': str,
            'location': str
        }

        self.attribute_map = {
            'name': 'name',
            'location': 'location'
        }
        self._name = name
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'Brewery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Brewery of this Brewery.  # noqa: E501
        :rtype: Brewery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Brewery.


        :return: The name of this Brewery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Brewery.


        :param name: The name of this Brewery.
        :type name: str
        """

        self._name = name

    @property
    def location(self) -> str:
        """Gets the location of this Brewery.


        :return: The location of this Brewery.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Brewery.


        :param location: The location of this Brewery.
        :type location: str
        """

        self._location = location
