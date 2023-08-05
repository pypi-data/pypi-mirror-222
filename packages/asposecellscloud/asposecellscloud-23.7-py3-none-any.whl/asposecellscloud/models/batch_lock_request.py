# coding: utf-8
"""
<copyright company="Aspose" file="BatchLockRequestpy.cs">
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

class BatchLockRequest(object):

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
        'source_folder' : 'str',
        'source_storage' : 'str',
        'match_condition' : 'MatchConditionRequest',
        'password' : 'str',
        'out_folder' : 'str',
        'out_storage' : 'str'
    }

    attribute_map = {
        'source_folder' : 'SourceFolder' ,
        'source_storage' : 'SourceStorage' ,
        'match_condition' : 'MatchCondition' ,
        'password' : 'Password' ,
        'out_folder' : 'OutFolder' ,
        'out_storage' : 'OutStorage' 
    }

    @staticmethod
    def get_swagger_types():
        return BatchLockRequest.swagger_types

    @staticmethod
    def get_attribute_map():
        return BatchLockRequest.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,source_folder=None ,source_storage=None ,match_condition=None ,password=None ,out_folder=None ,out_storage=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        BatchLockRequest - a model defined in Swagger
        """
        self.container['source_folder'] = None 
        self.container['source_storage'] = None 
        self.container['match_condition'] = None 
        self.container['password'] = None 
        self.container['out_folder'] = None 
        self.container['out_storage'] = None 
        params = locals()
        self.source_folder = source_folder
        if 'source_folder' in params:
            self.source_folder = params["source_folder"]


             
        self.source_storage = source_storage
        if 'source_storage' in params:
            self.source_storage = params["source_storage"]


             
        self.match_condition = match_condition
        if 'match_condition' in params:
            self.match_condition = params["match_condition"]


             
        self.password = password
        if 'password' in params:
            self.password = params["password"]


             
        self.out_folder = out_folder
        if 'out_folder' in params:
            self.out_folder = params["out_folder"]


             
        self.out_storage = out_storage
        if 'out_storage' in params:
            self.out_storage = params["out_storage"]


             

    @property
    def source_folder(self):
        return self.container['source_folder']

    @source_folder.setter
    def source_folder(self, source_folder):
        self.container['source_folder'] = source_folder 
    @property
    def source_storage(self):
        return self.container['source_storage']

    @source_storage.setter
    def source_storage(self, source_storage):
        self.container['source_storage'] = source_storage 
    @property
    def match_condition(self):
        return self.container['match_condition']

    @match_condition.setter
    def match_condition(self, match_condition):
        self.container['match_condition'] = match_condition 
    @property
    def password(self):
        return self.container['password']

    @password.setter
    def password(self, password):
        self.container['password'] = password 
    @property
    def out_folder(self):
        return self.container['out_folder']

    @out_folder.setter
    def out_folder(self, out_folder):
        self.container['out_folder'] = out_folder 
    @property
    def out_storage(self):
        return self.container['out_storage']

    @out_storage.setter
    def out_storage(self, out_storage):
        self.container['out_storage'] = out_storage 

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
        if not isinstance(other, BatchLockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    