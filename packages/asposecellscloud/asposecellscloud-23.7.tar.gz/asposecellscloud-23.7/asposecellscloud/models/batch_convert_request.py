# coding: utf-8

"""
Copyright (c) 2022 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from pprint import pformat
from six import iteritems
import re


class BatchConvertRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_folder': 'str',
        'source_storage': 'str',
        'match_condition': 'MatchConditionRequest',
        'format': 'str',
        'out_folder': 'str',
        'out_storage': 'str',
        'save_options': 'SaveOptions'
    }

    attribute_map = {
        'source_folder': 'SourceFolder',
        'source_storage': 'SourceStorage',
        'match_condition': 'MatchCondition',
        'format': 'Format',
        'out_folder': 'OutFolder',
        'out_storage': 'OutStorage',
        'save_options': 'SaveOptions'
    }
    
    @staticmethod
    def get_swagger_types():
        return BatchConvertRequest.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return BatchConvertRequest.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, source_folder=None, source_storage=None, match_condition=None, format=None, out_folder=None, out_storage=None, save_options=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        BatchConvertRequest - a model defined in Swagger
        """

        self.container['source_folder'] = None
        self.container['source_storage'] = None
        self.container['match_condition'] = None
        self.container['format'] = None
        self.container['out_folder'] = None
        self.container['out_storage'] = None
        self.container['save_options'] = None

        if source_folder is not None:
          self.source_folder = source_folder
        if source_storage is not None:
          self.source_storage = source_storage
        if match_condition is not None:
          self.match_condition = match_condition
        if format is not None:
          self.format = format
        if out_folder is not None:
          self.out_folder = out_folder
        if out_storage is not None:
          self.out_storage = out_storage
        if save_options is not None:
          self.save_options = save_options

    @property
    def source_folder(self):
        """
        Gets the source_folder of this BatchConvertRequest.

        :return: The source_folder of this BatchConvertRequest.
        :rtype: str
        """
        return self.container['source_folder']

    @source_folder.setter
    def source_folder(self, source_folder):
        """
        Sets the source_folder of this BatchConvertRequest.

        :param source_folder: The source_folder of this BatchConvertRequest.
        :type: str
        """

        self.container['source_folder'] = source_folder

    @property
    def source_storage(self):
        """
        Gets the source_storage of this BatchConvertRequest.

        :return: The source_storage of this BatchConvertRequest.
        :rtype: str
        """
        return self.container['source_storage']

    @source_storage.setter
    def source_storage(self, source_storage):
        """
        Sets the source_storage of this BatchConvertRequest.

        :param source_storage: The source_storage of this BatchConvertRequest.
        :type: str
        """

        self.container['source_storage'] = source_storage

    @property
    def match_condition(self):
        """
        Gets the match_condition of this BatchConvertRequest.

        :return: The match_condition of this BatchConvertRequest.
        :rtype: MatchConditionRequest
        """
        return self.container['match_condition']

    @match_condition.setter
    def match_condition(self, match_condition):
        """
        Sets the match_condition of this BatchConvertRequest.

        :param match_condition: The match_condition of this BatchConvertRequest.
        :type: MatchConditionRequest
        """

        self.container['match_condition'] = match_condition

    @property
    def format(self):
        """
        Gets the format of this BatchConvertRequest.

        :return: The format of this BatchConvertRequest.
        :rtype: str
        """
        return self.container['format']

    @format.setter
    def format(self, format):
        """
        Sets the format of this BatchConvertRequest.

        :param format: The format of this BatchConvertRequest.
        :type: str
        """

        self.container['format'] = format

    @property
    def out_folder(self):
        """
        Gets the out_folder of this BatchConvertRequest.

        :return: The out_folder of this BatchConvertRequest.
        :rtype: str
        """
        return self.container['out_folder']

    @out_folder.setter
    def out_folder(self, out_folder):
        """
        Sets the out_folder of this BatchConvertRequest.

        :param out_folder: The out_folder of this BatchConvertRequest.
        :type: str
        """

        self.container['out_folder'] = out_folder

    @property
    def out_storage(self):
        """
        Gets the out_storage of this BatchConvertRequest.

        :return: The out_storage of this BatchConvertRequest.
        :rtype: str
        """
        return self.container['out_storage']

    @out_storage.setter
    def out_storage(self, out_storage):
        """
        Sets the out_storage of this BatchConvertRequest.

        :param out_storage: The out_storage of this BatchConvertRequest.
        :type: str
        """

        self.container['out_storage'] = out_storage

    @property
    def save_options(self):
        """
        Gets the save_options of this BatchConvertRequest.

        :return: The save_options of this BatchConvertRequest.
        :rtype: SaveOptions
        """
        return self.container['save_options']

    @save_options.setter
    def save_options(self, save_options):
        """
        Sets the save_options of this BatchConvertRequest.

        :param save_options: The save_options of this BatchConvertRequest.
        :type: SaveOptions
        """

        self.container['save_options'] = save_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BatchConvertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
