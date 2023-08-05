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


class ShadowEffect(object):
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
        'distance': 'float',
        'angle': 'float',
        'preset_type': 'str',
        'color': 'CellsColor',
        'transparency': 'float',
        'blur': 'float',
        'size': 'float'
    }

    attribute_map = {
        'distance': 'Distance',
        'angle': 'Angle',
        'preset_type': 'PresetType',
        'color': 'Color',
        'transparency': 'Transparency',
        'blur': 'Blur',
        'size': 'Size'
    }
    
    @staticmethod
    def get_swagger_types():
        return ShadowEffect.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ShadowEffect.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, distance=None, angle=None, preset_type=None, color=None, transparency=None, blur=None, size=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ShadowEffect - a model defined in Swagger
        """

        self.container['distance'] = None
        self.container['angle'] = None
        self.container['preset_type'] = None
        self.container['color'] = None
        self.container['transparency'] = None
        self.container['blur'] = None
        self.container['size'] = None

        if distance is not None:
          self.distance = distance
        if angle is not None:
          self.angle = angle
        if preset_type is not None:
          self.preset_type = preset_type
        if color is not None:
          self.color = color
        if transparency is not None:
          self.transparency = transparency
        if blur is not None:
          self.blur = blur
        if size is not None:
          self.size = size

    @property
    def distance(self):
        """
        Gets the distance of this ShadowEffect.

        :return: The distance of this ShadowEffect.
        :rtype: float
        """
        return self.container['distance']

    @distance.setter
    def distance(self, distance):
        """
        Sets the distance of this ShadowEffect.

        :param distance: The distance of this ShadowEffect.
        :type: float
        """

        self.container['distance'] = distance

    @property
    def angle(self):
        """
        Gets the angle of this ShadowEffect.

        :return: The angle of this ShadowEffect.
        :rtype: float
        """
        return self.container['angle']

    @angle.setter
    def angle(self, angle):
        """
        Sets the angle of this ShadowEffect.

        :param angle: The angle of this ShadowEffect.
        :type: float
        """

        self.container['angle'] = angle

    @property
    def preset_type(self):
        """
        Gets the preset_type of this ShadowEffect.

        :return: The preset_type of this ShadowEffect.
        :rtype: str
        """
        return self.container['preset_type']

    @preset_type.setter
    def preset_type(self, preset_type):
        """
        Sets the preset_type of this ShadowEffect.

        :param preset_type: The preset_type of this ShadowEffect.
        :type: str
        """

        self.container['preset_type'] = preset_type

    @property
    def color(self):
        """
        Gets the color of this ShadowEffect.

        :return: The color of this ShadowEffect.
        :rtype: CellsColor
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this ShadowEffect.

        :param color: The color of this ShadowEffect.
        :type: CellsColor
        """

        self.container['color'] = color

    @property
    def transparency(self):
        """
        Gets the transparency of this ShadowEffect.

        :return: The transparency of this ShadowEffect.
        :rtype: float
        """
        return self.container['transparency']

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency of this ShadowEffect.

        :param transparency: The transparency of this ShadowEffect.
        :type: float
        """

        self.container['transparency'] = transparency

    @property
    def blur(self):
        """
        Gets the blur of this ShadowEffect.

        :return: The blur of this ShadowEffect.
        :rtype: float
        """
        return self.container['blur']

    @blur.setter
    def blur(self, blur):
        """
        Sets the blur of this ShadowEffect.

        :param blur: The blur of this ShadowEffect.
        :type: float
        """

        self.container['blur'] = blur

    @property
    def size(self):
        """
        Gets the size of this ShadowEffect.

        :return: The size of this ShadowEffect.
        :rtype: float
        """
        return self.container['size']

    @size.setter
    def size(self, size):
        """
        Sets the size of this ShadowEffect.

        :param size: The size of this ShadowEffect.
        :type: float
        """

        self.container['size'] = size

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
        if not isinstance(other, ShadowEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
