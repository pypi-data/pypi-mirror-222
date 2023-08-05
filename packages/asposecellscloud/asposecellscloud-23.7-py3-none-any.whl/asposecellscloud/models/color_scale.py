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


class ColorScale(object):
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
        'max_cfvo': 'ConditionalFormattingValue',
        'mid_color': 'Color',
        'min_color': 'Color',
        'mid_cfvo': 'ConditionalFormattingValue',
        'min_cfvo': 'ConditionalFormattingValue',
        'max_color': 'Color'
    }

    attribute_map = {
        'max_cfvo': 'MaxCfvo',
        'mid_color': 'MidColor',
        'min_color': 'MinColor',
        'mid_cfvo': 'MidCfvo',
        'min_cfvo': 'MinCfvo',
        'max_color': 'MaxColor'
    }
    
    @staticmethod
    def get_swagger_types():
        return ColorScale.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ColorScale.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, max_cfvo=None, mid_color=None, min_color=None, mid_cfvo=None, min_cfvo=None, max_color=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ColorScale - a model defined in Swagger
        """

        self.container['max_cfvo'] = None
        self.container['mid_color'] = None
        self.container['min_color'] = None
        self.container['mid_cfvo'] = None
        self.container['min_cfvo'] = None
        self.container['max_color'] = None

        if max_cfvo is not None:
          self.max_cfvo = max_cfvo
        if mid_color is not None:
          self.mid_color = mid_color
        if min_color is not None:
          self.min_color = min_color
        if mid_cfvo is not None:
          self.mid_cfvo = mid_cfvo
        if min_cfvo is not None:
          self.min_cfvo = min_cfvo
        if max_color is not None:
          self.max_color = max_color

    @property
    def max_cfvo(self):
        """
        Gets the max_cfvo of this ColorScale.
        Get or set this ColorScale's max value object.  Cannot set null or CFValueObject     with type FormatConditionValueType.Min to it.

        :return: The max_cfvo of this ColorScale.
        :rtype: ConditionalFormattingValue
        """
        return self.container['max_cfvo']

    @max_cfvo.setter
    def max_cfvo(self, max_cfvo):
        """
        Sets the max_cfvo of this ColorScale.
        Get or set this ColorScale's max value object.  Cannot set null or CFValueObject     with type FormatConditionValueType.Min to it.

        :param max_cfvo: The max_cfvo of this ColorScale.
        :type: ConditionalFormattingValue
        """

        self.container['max_cfvo'] = max_cfvo

    @property
    def mid_color(self):
        """
        Gets the mid_color of this ColorScale.
        Get or set the mid value object's corresponding color.             

        :return: The mid_color of this ColorScale.
        :rtype: Color
        """
        return self.container['mid_color']

    @mid_color.setter
    def mid_color(self, mid_color):
        """
        Sets the mid_color of this ColorScale.
        Get or set the mid value object's corresponding color.             

        :param mid_color: The mid_color of this ColorScale.
        :type: Color
        """

        self.container['mid_color'] = mid_color

    @property
    def min_color(self):
        """
        Gets the min_color of this ColorScale.
        Get or set the min value object's corresponding color.

        :return: The min_color of this ColorScale.
        :rtype: Color
        """
        return self.container['min_color']

    @min_color.setter
    def min_color(self, min_color):
        """
        Sets the min_color of this ColorScale.
        Get or set the min value object's corresponding color.

        :param min_color: The min_color of this ColorScale.
        :type: Color
        """

        self.container['min_color'] = min_color

    @property
    def mid_cfvo(self):
        """
        Gets the mid_cfvo of this ColorScale.
        Get or set this ColorScale's mid value object.  Cannot set CFValueObject    with type FormatConditionValueType.Max or FormatConditionValueType.Min to    it.             

        :return: The mid_cfvo of this ColorScale.
        :rtype: ConditionalFormattingValue
        """
        return self.container['mid_cfvo']

    @mid_cfvo.setter
    def mid_cfvo(self, mid_cfvo):
        """
        Sets the mid_cfvo of this ColorScale.
        Get or set this ColorScale's mid value object.  Cannot set CFValueObject    with type FormatConditionValueType.Max or FormatConditionValueType.Min to    it.             

        :param mid_cfvo: The mid_cfvo of this ColorScale.
        :type: ConditionalFormattingValue
        """

        self.container['mid_cfvo'] = mid_cfvo

    @property
    def min_cfvo(self):
        """
        Gets the min_cfvo of this ColorScale.
        Get or set this ColorScale's min value object.  Cannot set null or CFValueObject    with type FormatConditionValueType.Max to it.             

        :return: The min_cfvo of this ColorScale.
        :rtype: ConditionalFormattingValue
        """
        return self.container['min_cfvo']

    @min_cfvo.setter
    def min_cfvo(self, min_cfvo):
        """
        Sets the min_cfvo of this ColorScale.
        Get or set this ColorScale's min value object.  Cannot set null or CFValueObject    with type FormatConditionValueType.Max to it.             

        :param min_cfvo: The min_cfvo of this ColorScale.
        :type: ConditionalFormattingValue
        """

        self.container['min_cfvo'] = min_cfvo

    @property
    def max_color(self):
        """
        Gets the max_color of this ColorScale.
        Get or set the max value object's corresponding color.

        :return: The max_color of this ColorScale.
        :rtype: Color
        """
        return self.container['max_color']

    @max_color.setter
    def max_color(self, max_color):
        """
        Sets the max_color of this ColorScale.
        Get or set the max value object's corresponding color.

        :param max_color: The max_color of this ColorScale.
        :type: Color
        """

        self.container['max_color'] = max_color

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
        if not isinstance(other, ColorScale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
