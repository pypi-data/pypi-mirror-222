# coding: utf-8

"""
Copyright (c) 2021 Aspose.Cells Cloud
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
from . import TaskParameter

class ConvertWorksheetTaskParameter(TaskParameter):
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
        'workbook': 'FileSource',
        'sheet': 'str',
        'target': 'FileSource',
        'format': 'str',
        'area': 'str',
        'page_index': 'int',
        'vertical_resolution': 'int',
        'horizontal_resolution': 'int'
    }

    attribute_map = {
        'workbook': 'Workbook',
        'sheet': 'Sheet',
        'target': 'Target',
        'format': 'Format',
        'area': 'Area',
        'page_index': 'PageIndex',
        'vertical_resolution': 'VerticalResolution',
        'horizontal_resolution': 'HorizontalResolution'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ConvertWorksheetTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ConvertWorksheetTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, workbook=None, sheet=None, target=None, format=None, area=None, page_index=None, vertical_resolution=None, horizontal_resolution=None, **kw):
        super(ConvertWorksheetTaskParameter, self).__init__(**kw)
		    
        """
        ConvertWorksheetTaskParameter - a model defined in Swagger
        """

        self.container['workbook'] = None
        self.container['sheet'] = None
        self.container['target'] = None
        self.container['format'] = None
        self.container['area'] = None
        self.container['page_index'] = None
        self.container['vertical_resolution'] = None
        self.container['horizontal_resolution'] = None

        if workbook is not None:
          self.workbook = workbook
        if sheet is not None:
          self.sheet = sheet
        if target is not None:
          self.target = target
        if format is not None:
          self.format = format
        if area is not None:
          self.area = area
        if page_index is not None:
          self.page_index = page_index
        if vertical_resolution is not None:
          self.vertical_resolution = vertical_resolution
        if horizontal_resolution is not None:
          self.horizontal_resolution = horizontal_resolution

    @property
    def workbook(self):
        """
        Gets the workbook of this ConvertWorksheetTaskParameter.

        :return: The workbook of this ConvertWorksheetTaskParameter.
        :rtype: FileSource
        """
        return self.container['workbook']

    @workbook.setter
    def workbook(self, workbook):
        """
        Sets the workbook of this ConvertWorksheetTaskParameter.

        :param workbook: The workbook of this ConvertWorksheetTaskParameter.
        :type: FileSource
        """

        self.container['workbook'] = workbook

    @property
    def sheet(self):
        """
        Gets the sheet of this ConvertWorksheetTaskParameter.

        :return: The sheet of this ConvertWorksheetTaskParameter.
        :rtype: str
        """
        return self.container['sheet']

    @sheet.setter
    def sheet(self, sheet):
        """
        Sets the sheet of this ConvertWorksheetTaskParameter.

        :param sheet: The sheet of this ConvertWorksheetTaskParameter.
        :type: str
        """

        self.container['sheet'] = sheet

    @property
    def target(self):
        """
        Gets the target of this ConvertWorksheetTaskParameter.

        :return: The target of this ConvertWorksheetTaskParameter.
        :rtype: FileSource
        """
        return self.container['target']

    @target.setter
    def target(self, target):
        """
        Sets the target of this ConvertWorksheetTaskParameter.

        :param target: The target of this ConvertWorksheetTaskParameter.
        :type: FileSource
        """

        self.container['target'] = target

    @property
    def format(self):
        """
        Gets the format of this ConvertWorksheetTaskParameter.

        :return: The format of this ConvertWorksheetTaskParameter.
        :rtype: str
        """
        return self.container['format']

    @format.setter
    def format(self, format):
        """
        Sets the format of this ConvertWorksheetTaskParameter.

        :param format: The format of this ConvertWorksheetTaskParameter.
        :type: str
        """

        self.container['format'] = format

    @property
    def area(self):
        """
        Gets the area of this ConvertWorksheetTaskParameter.

        :return: The area of this ConvertWorksheetTaskParameter.
        :rtype: str
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this ConvertWorksheetTaskParameter.

        :param area: The area of this ConvertWorksheetTaskParameter.
        :type: str
        """

        self.container['area'] = area

    @property
    def page_index(self):
        """
        Gets the page_index of this ConvertWorksheetTaskParameter.

        :return: The page_index of this ConvertWorksheetTaskParameter.
        :rtype: int
        """
        return self.container['page_index']

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this ConvertWorksheetTaskParameter.

        :param page_index: The page_index of this ConvertWorksheetTaskParameter.
        :type: int
        """

        self.container['page_index'] = page_index

    @property
    def vertical_resolution(self):
        """
        Gets the vertical_resolution of this ConvertWorksheetTaskParameter.

        :return: The vertical_resolution of this ConvertWorksheetTaskParameter.
        :rtype: int
        """
        return self.container['vertical_resolution']

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """
        Sets the vertical_resolution of this ConvertWorksheetTaskParameter.

        :param vertical_resolution: The vertical_resolution of this ConvertWorksheetTaskParameter.
        :type: int
        """

        self.container['vertical_resolution'] = vertical_resolution

    @property
    def horizontal_resolution(self):
        """
        Gets the horizontal_resolution of this ConvertWorksheetTaskParameter.

        :return: The horizontal_resolution of this ConvertWorksheetTaskParameter.
        :rtype: int
        """
        return self.container['horizontal_resolution']

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """
        Sets the horizontal_resolution of this ConvertWorksheetTaskParameter.

        :param horizontal_resolution: The horizontal_resolution of this ConvertWorksheetTaskParameter.
        :type: int
        """

        self.container['horizontal_resolution'] = horizontal_resolution

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
        if not isinstance(other, ConvertWorksheetTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
