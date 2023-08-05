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
from . import SaveOptions

class JsonSaveOptions(SaveOptions):
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
        'export_area': 'CellArea',
        'has_header_row': 'bool',
        'export_as_string': 'bool',
        'indent': 'str'
    }

    attribute_map = {
        'export_area': 'ExportArea',
        'has_header_row': 'HasHeaderRow',
        'export_as_string': 'ExportAsString',
        'indent': 'Indent'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(JsonSaveOptions.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(JsonSaveOptions.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, export_area=None, has_header_row=None, export_as_string=None, indent=None, **kw):
        super(JsonSaveOptions, self).__init__(**kw)
		    
        """
        JsonSaveOptions - a model defined in Swagger
        """

        self.container['export_area'] = None
        self.container['has_header_row'] = None
        self.container['export_as_string'] = None
        self.container['indent'] = None

        if export_area is not None:
          self.export_area = export_area
        if has_header_row is not None:
          self.has_header_row = has_header_row
        if export_as_string is not None:
          self.export_as_string = export_as_string
        if indent is not None:
          self.indent = indent

    @property
    def export_area(self):
        """
        Gets the export_area of this JsonSaveOptions.

        :return: The export_area of this JsonSaveOptions.
        :rtype: CellArea
        """
        return self.container['export_area']

    @export_area.setter
    def export_area(self, export_area):
        """
        Sets the export_area of this JsonSaveOptions.

        :param export_area: The export_area of this JsonSaveOptions.
        :type: CellArea
        """

        self.container['export_area'] = export_area

    @property
    def has_header_row(self):
        """
        Gets the has_header_row of this JsonSaveOptions.

        :return: The has_header_row of this JsonSaveOptions.
        :rtype: bool
        """
        return self.container['has_header_row']

    @has_header_row.setter
    def has_header_row(self, has_header_row):
        """
        Sets the has_header_row of this JsonSaveOptions.

        :param has_header_row: The has_header_row of this JsonSaveOptions.
        :type: bool
        """

        self.container['has_header_row'] = has_header_row

    @property
    def export_as_string(self):
        """
        Gets the export_as_string of this JsonSaveOptions.

        :return: The export_as_string of this JsonSaveOptions.
        :rtype: bool
        """
        return self.container['export_as_string']

    @export_as_string.setter
    def export_as_string(self, export_as_string):
        """
        Sets the export_as_string of this JsonSaveOptions.

        :param export_as_string: The export_as_string of this JsonSaveOptions.
        :type: bool
        """

        self.container['export_as_string'] = export_as_string

    @property
    def indent(self):
        """
        Gets the indent of this JsonSaveOptions.

        :return: The indent of this JsonSaveOptions.
        :rtype: str
        """
        return self.container['indent']

    @indent.setter
    def indent(self, indent):
        """
        Sets the indent of this JsonSaveOptions.

        :param indent: The indent of this JsonSaveOptions.
        :type: str
        """

        self.container['indent'] = indent

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
        if not isinstance(other, JsonSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
