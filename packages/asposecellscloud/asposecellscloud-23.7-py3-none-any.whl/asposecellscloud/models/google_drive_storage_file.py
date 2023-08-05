# coding: utf-8
"""
<copyright company="Aspose" file="GoogleDriveStorageFilepy.cs">
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

class GoogleDriveStorageFile(object):

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
        'mime_type' : 'str',
        'name' : 'str',
        'is_folder' : 'bool',
        'modified_date' : 'datetime',
        'size' : 'int',
        'path' : 'str'
    }

    attribute_map = {
        'mime_type' : 'MimeType' ,
        'name' : 'Name' ,
        'is_folder' : 'IsFolder' ,
        'modified_date' : 'ModifiedDate' ,
        'size' : 'Size' ,
        'path' : 'Path' 
    }

    @staticmethod
    def get_swagger_types():
        return GoogleDriveStorageFile.swagger_types

    @staticmethod
    def get_attribute_map():
        return GoogleDriveStorageFile.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,mime_type=None ,name=None ,is_folder=None ,modified_date=None ,size=None ,path=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        GoogleDriveStorageFile - a model defined in Swagger
        """
        self.container['mime_type'] = None 
        self.container['name'] = None 
        self.container['is_folder'] = None 
        self.container['modified_date'] = None 
        self.container['size'] = None 
        self.container['path'] = None 
        params = locals()
        self.mime_type = mime_type
        if 'mime_type' in params:
            self.mime_type = params["mime_type"]


             
        self.name = name
        if 'name' in params:
            self.name = params["name"]


             
        self.is_folder = is_folder
        if 'is_folder' in params:
            self.is_folder = params["is_folder"]


             
        self.modified_date = modified_date
        if 'modified_date' in params:
            self.modified_date = params["modified_date"]


             
        self.size = size
        if 'size' in params:
            self.size = params["size"]


             
        self.path = path
        if 'path' in params:
            self.path = params["path"]


             

    @property
    def mime_type(self):
        return self.container['mime_type']

    @mime_type.setter
    def mime_type(self, mime_type):
        self.container['mime_type'] = mime_type 
    @property
    def name(self):
        return self.container['name']

    @name.setter
    def name(self, name):
        self.container['name'] = name 
    @property
    def is_folder(self):
        return self.container['is_folder']

    @is_folder.setter
    def is_folder(self, is_folder):
        self.container['is_folder'] = is_folder 
    @property
    def modified_date(self):
        return self.container['modified_date']

    @modified_date.setter
    def modified_date(self, modified_date):
        self.container['modified_date'] = modified_date 
    @property
    def size(self):
        return self.container['size']

    @size.setter
    def size(self, size):
        self.container['size'] = size 
    @property
    def path(self):
        return self.container['path']

    @path.setter
    def path(self, path):
        self.container['path'] = path 

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
        if not isinstance(other, GoogleDriveStorageFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    