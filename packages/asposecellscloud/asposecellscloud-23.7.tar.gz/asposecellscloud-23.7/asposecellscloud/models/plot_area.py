# coding: utf-8
"""
<copyright company="Aspose" file="PlotAreapy.cs">
  Copyright (c) 2023 Aspose.Cells Cloud
</copyright>
<summary>
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
 SOFTWARE.
</summary>
"""

from pprint import pformat
from six import iteritems
import re

class PlotArea(object):

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
        'inner_height' : 'int',
        'inner_width' : 'int',
        'inner_x' : 'int',
        'inner_y' : 'int',
        'area' : 'Area',
        'auto_scale_font' : 'bool',
        'background_mode' : 'str',
        'border' : 'Line',
        'font' : 'Font',
        'is_automatic_size' : 'bool',
        'is_inner_mode' : 'bool',
        'shadow' : 'bool',
        'shape_properties' : 'list[LinkElement]',
        'width' : 'int',
        'height' : 'int',
        'x' : 'int',
        'y' : 'int'
    }

    attribute_map = {
        'inner_height' : 'InnerHeight' ,
        'inner_width' : 'InnerWidth' ,
        'inner_x' : 'InnerX' ,
        'inner_y' : 'InnerY' ,
        'area' : 'Area' ,
        'auto_scale_font' : 'AutoScaleFont' ,
        'background_mode' : 'BackgroundMode' ,
        'border' : 'Border' ,
        'font' : 'Font' ,
        'is_automatic_size' : 'IsAutomaticSize' ,
        'is_inner_mode' : 'IsInnerMode' ,
        'shadow' : 'Shadow' ,
        'shape_properties' : 'ShapeProperties' ,
        'width' : 'Width' ,
        'height' : 'Height' ,
        'x' : 'X' ,
        'y' : 'Y' 
    }

    @staticmethod
    def get_swagger_types():
        return PlotArea.swagger_types

    @staticmethod
    def get_attribute_map():
        return PlotArea.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,inner_height=None ,inner_width=None ,inner_x=None ,inner_y=None ,area=None ,auto_scale_font=None ,background_mode=None ,border=None ,font=None ,is_automatic_size=None ,is_inner_mode=None ,shadow=None ,shape_properties=None ,width=None ,height=None ,x=None ,y=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        PlotArea - a model defined in Swagger
        """
        self.container['inner_height'] = None 
        self.container['inner_width'] = None 
        self.container['inner_x'] = None 
        self.container['inner_y'] = None 
        self.container['area'] = None 
        self.container['auto_scale_font'] = None 
        self.container['background_mode'] = None 
        self.container['border'] = None 
        self.container['font'] = None 
        self.container['is_automatic_size'] = None 
        self.container['is_inner_mode'] = None 
        self.container['shadow'] = None 
        self.container['shape_properties'] = None 
        self.container['width'] = None 
        self.container['height'] = None 
        self.container['x'] = None 
        self.container['y'] = None 
        params = locals()
        self.inner_height = inner_height
        if 'inner_height' in params:
            self.inner_height = params["inner_height"]


             
        self.inner_width = inner_width
        if 'inner_width' in params:
            self.inner_width = params["inner_width"]


             
        self.inner_x = inner_x
        if 'inner_x' in params:
            self.inner_x = params["inner_x"]


             
        self.inner_y = inner_y
        if 'inner_y' in params:
            self.inner_y = params["inner_y"]


             
        self.area = area
        if 'area' in params:
            self.area = params["area"]


             
        self.auto_scale_font = auto_scale_font
        if 'auto_scale_font' in params:
            self.auto_scale_font = params["auto_scale_font"]


             
        self.background_mode = background_mode
        if 'background_mode' in params:
            self.background_mode = params["background_mode"]


             
        self.border = border
        if 'border' in params:
            self.border = params["border"]


             
        self.font = font
        if 'font' in params:
            self.font = params["font"]


             
        self.is_automatic_size = is_automatic_size
        if 'is_automatic_size' in params:
            self.is_automatic_size = params["is_automatic_size"]


             
        self.is_inner_mode = is_inner_mode
        if 'is_inner_mode' in params:
            self.is_inner_mode = params["is_inner_mode"]


             
        self.shadow = shadow
        if 'shadow' in params:
            self.shadow = params["shadow"]


             
        self.shape_properties = shape_properties
        if 'shape_properties' in params:
            self.shape_properties = params["shape_properties"]


             
        self.width = width
        if 'width' in params:
            self.width = params["width"]


             
        self.height = height
        if 'height' in params:
            self.height = params["height"]


             
        self.x = x
        if 'x' in params:
            self.x = params["x"]


             
        self.y = y
        if 'y' in params:
            self.y = params["y"]


             

    @property
    def inner_height(self):
        return self.container['inner_height']

    @inner_height.setter
    def inner_height(self, inner_height):
        self.container['inner_height'] = inner_height 
    @property
    def inner_width(self):
        return self.container['inner_width']

    @inner_width.setter
    def inner_width(self, inner_width):
        self.container['inner_width'] = inner_width 
    @property
    def inner_x(self):
        return self.container['inner_x']

    @inner_x.setter
    def inner_x(self, inner_x):
        self.container['inner_x'] = inner_x 
    @property
    def inner_y(self):
        return self.container['inner_y']

    @inner_y.setter
    def inner_y(self, inner_y):
        self.container['inner_y'] = inner_y 
    @property
    def area(self):
        return self.container['area']

    @area.setter
    def area(self, area):
        self.container['area'] = area 
    @property
    def auto_scale_font(self):
        return self.container['auto_scale_font']

    @auto_scale_font.setter
    def auto_scale_font(self, auto_scale_font):
        self.container['auto_scale_font'] = auto_scale_font 
    @property
    def background_mode(self):
        return self.container['background_mode']

    @background_mode.setter
    def background_mode(self, background_mode):
        self.container['background_mode'] = background_mode 
    @property
    def border(self):
        return self.container['border']

    @border.setter
    def border(self, border):
        self.container['border'] = border 
    @property
    def font(self):
        return self.container['font']

    @font.setter
    def font(self, font):
        self.container['font'] = font 
    @property
    def is_automatic_size(self):
        return self.container['is_automatic_size']

    @is_automatic_size.setter
    def is_automatic_size(self, is_automatic_size):
        self.container['is_automatic_size'] = is_automatic_size 
    @property
    def is_inner_mode(self):
        return self.container['is_inner_mode']

    @is_inner_mode.setter
    def is_inner_mode(self, is_inner_mode):
        self.container['is_inner_mode'] = is_inner_mode 
    @property
    def shadow(self):
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        self.container['shadow'] = shadow 
    @property
    def shape_properties(self):
        return self.container['shape_properties']

    @shape_properties.setter
    def shape_properties(self, shape_properties):
        self.container['shape_properties'] = shape_properties 
    @property
    def width(self):
        return self.container['width']

    @width.setter
    def width(self, width):
        self.container['width'] = width 
    @property
    def height(self):
        return self.container['height']

    @height.setter
    def height(self, height):
        self.container['height'] = height 
    @property
    def x(self):
        return self.container['x']

    @x.setter
    def x(self, x):
        self.container['x'] = x 
    @property
    def y(self):
        return self.container['y']

    @y.setter
    def y(self, y):
        self.container['y'] = y 

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
        if not isinstance(other, PlotArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    