# coding: utf-8
"""
<copyright company="Aspose" file="Seriespy.cs">
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

class Series(object):

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
        'area' : 'Area',
        'bar3_d_shape_type' : 'str',
        'border' : 'Line',
        'bubble_scale' : 'int',
        'bubble_sizes' : 'str',
        'count_of_data_values' : 'int',
        'data_labels' : 'LinkElement',
        'display_name' : 'str',
        'doughnut_hole_size' : 'int',
        'down_bars' : 'LinkElement',
        'drop_lines' : 'Line',
        'explosion' : 'int',
        'first_slice_angle' : 'int',
        'gap_width' : 'int',
        'has3_d_effect' : 'bool',
        'has_drop_lines' : 'bool',
        'has_hi_lo_lines' : 'bool',
        'has_leader_lines' : 'bool',
        'has_radar_axis_labels' : 'bool',
        'has_series_lines' : 'bool',
        'has_up_down_bars' : 'bool',
        'hi_lo_lines' : 'Line',
        'is_auto_split' : 'bool',
        'is_color_varied' : 'bool',
        'leader_lines' : 'Line',
        'legend_entry' : 'LinkElement',
        'line' : 'Line',
        'marker' : 'Marker',
        'name' : 'str',
        'overlap' : 'int',
        'plot_on_second_axis' : 'bool',
        'points' : 'LinkElement',
        'second_plot_size' : 'int',
        'series_lines' : 'Line',
        'shadow' : 'bool',
        'shape_properties' : 'LinkElement',
        'show_negative_bubbles' : 'bool',
        'size_represents' : 'str',
        'smooth' : 'bool',
        'split_type' : 'str',
        'split_value' : 'float',
        'trend_lines' : 'LinkElement',
        'type' : 'str',
        'up_bars' : 'LinkElement',
        'values' : 'str',
        'x_error_bar' : 'LinkElement',
        'x_values' : 'str',
        'y_error_bar' : 'LinkElement',
        'link' : 'Link'
    }

    attribute_map = {
        'area' : 'Area' ,
        'bar3_d_shape_type' : 'Bar3DShapeType' ,
        'border' : 'Border' ,
        'bubble_scale' : 'BubbleScale' ,
        'bubble_sizes' : 'BubbleSizes' ,
        'count_of_data_values' : 'CountOfDataValues' ,
        'data_labels' : 'DataLabels' ,
        'display_name' : 'DisplayName' ,
        'doughnut_hole_size' : 'DoughnutHoleSize' ,
        'down_bars' : 'DownBars' ,
        'drop_lines' : 'DropLines' ,
        'explosion' : 'Explosion' ,
        'first_slice_angle' : 'FirstSliceAngle' ,
        'gap_width' : 'GapWidth' ,
        'has3_d_effect' : 'Has3DEffect' ,
        'has_drop_lines' : 'HasDropLines' ,
        'has_hi_lo_lines' : 'HasHiLoLines' ,
        'has_leader_lines' : 'HasLeaderLines' ,
        'has_radar_axis_labels' : 'HasRadarAxisLabels' ,
        'has_series_lines' : 'HasSeriesLines' ,
        'has_up_down_bars' : 'HasUpDownBars' ,
        'hi_lo_lines' : 'HiLoLines' ,
        'is_auto_split' : 'IsAutoSplit' ,
        'is_color_varied' : 'IsColorVaried' ,
        'leader_lines' : 'LeaderLines' ,
        'legend_entry' : 'LegendEntry' ,
        'line' : 'Line' ,
        'marker' : 'Marker' ,
        'name' : 'Name' ,
        'overlap' : 'Overlap' ,
        'plot_on_second_axis' : 'PlotOnSecondAxis' ,
        'points' : 'Points' ,
        'second_plot_size' : 'SecondPlotSize' ,
        'series_lines' : 'SeriesLines' ,
        'shadow' : 'Shadow' ,
        'shape_properties' : 'ShapeProperties' ,
        'show_negative_bubbles' : 'ShowNegativeBubbles' ,
        'size_represents' : 'SizeRepresents' ,
        'smooth' : 'Smooth' ,
        'split_type' : 'SplitType' ,
        'split_value' : 'SplitValue' ,
        'trend_lines' : 'TrendLines' ,
        'type' : 'Type' ,
        'up_bars' : 'UpBars' ,
        'values' : 'Values' ,
        'x_error_bar' : 'XErrorBar' ,
        'x_values' : 'XValues' ,
        'y_error_bar' : 'YErrorBar' ,
        'link' : 'link' 
    }

    @staticmethod
    def get_swagger_types():
        return Series.swagger_types

    @staticmethod
    def get_attribute_map():
        return Series.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,area=None ,bar3_d_shape_type=None ,border=None ,bubble_scale=None ,bubble_sizes=None ,count_of_data_values=None ,data_labels=None ,display_name=None ,doughnut_hole_size=None ,down_bars=None ,drop_lines=None ,explosion=None ,first_slice_angle=None ,gap_width=None ,has3_d_effect=None ,has_drop_lines=None ,has_hi_lo_lines=None ,has_leader_lines=None ,has_radar_axis_labels=None ,has_series_lines=None ,has_up_down_bars=None ,hi_lo_lines=None ,is_auto_split=None ,is_color_varied=None ,leader_lines=None ,legend_entry=None ,line=None ,marker=None ,name=None ,overlap=None ,plot_on_second_axis=None ,points=None ,second_plot_size=None ,series_lines=None ,shadow=None ,shape_properties=None ,show_negative_bubbles=None ,size_represents=None ,smooth=None ,split_type=None ,split_value=None ,trend_lines=None ,type=None ,up_bars=None ,values=None ,x_error_bar=None ,x_values=None ,y_error_bar=None ,link=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        Series - a model defined in Swagger
        """
        self.container['area'] = None 
        self.container['bar3_d_shape_type'] = None 
        self.container['border'] = None 
        self.container['bubble_scale'] = None 
        self.container['bubble_sizes'] = None 
        self.container['count_of_data_values'] = None 
        self.container['data_labels'] = None 
        self.container['display_name'] = None 
        self.container['doughnut_hole_size'] = None 
        self.container['down_bars'] = None 
        self.container['drop_lines'] = None 
        self.container['explosion'] = None 
        self.container['first_slice_angle'] = None 
        self.container['gap_width'] = None 
        self.container['has3_d_effect'] = None 
        self.container['has_drop_lines'] = None 
        self.container['has_hi_lo_lines'] = None 
        self.container['has_leader_lines'] = None 
        self.container['has_radar_axis_labels'] = None 
        self.container['has_series_lines'] = None 
        self.container['has_up_down_bars'] = None 
        self.container['hi_lo_lines'] = None 
        self.container['is_auto_split'] = None 
        self.container['is_color_varied'] = None 
        self.container['leader_lines'] = None 
        self.container['legend_entry'] = None 
        self.container['line'] = None 
        self.container['marker'] = None 
        self.container['name'] = None 
        self.container['overlap'] = None 
        self.container['plot_on_second_axis'] = None 
        self.container['points'] = None 
        self.container['second_plot_size'] = None 
        self.container['series_lines'] = None 
        self.container['shadow'] = None 
        self.container['shape_properties'] = None 
        self.container['show_negative_bubbles'] = None 
        self.container['size_represents'] = None 
        self.container['smooth'] = None 
        self.container['split_type'] = None 
        self.container['split_value'] = None 
        self.container['trend_lines'] = None 
        self.container['type'] = None 
        self.container['up_bars'] = None 
        self.container['values'] = None 
        self.container['x_error_bar'] = None 
        self.container['x_values'] = None 
        self.container['y_error_bar'] = None 
        self.container['link'] = None 
        params = locals()
        self.area = area
        if 'area' in params:
            self.area = params["area"]


             
        self.bar3_d_shape_type = bar3_d_shape_type
        if 'bar3_d_shape_type' in params:
            self.bar3_d_shape_type = params["bar3_d_shape_type"]


             
        self.border = border
        if 'border' in params:
            self.border = params["border"]


             
        self.bubble_scale = bubble_scale
        if 'bubble_scale' in params:
            self.bubble_scale = params["bubble_scale"]


             
        self.bubble_sizes = bubble_sizes
        if 'bubble_sizes' in params:
            self.bubble_sizes = params["bubble_sizes"]


             
        self.count_of_data_values = count_of_data_values
        if 'count_of_data_values' in params:
            self.count_of_data_values = params["count_of_data_values"]


             
        self.data_labels = data_labels
        if 'data_labels' in params:
            self.data_labels = params["data_labels"]


             
        self.display_name = display_name
        if 'display_name' in params:
            self.display_name = params["display_name"]


             
        self.doughnut_hole_size = doughnut_hole_size
        if 'doughnut_hole_size' in params:
            self.doughnut_hole_size = params["doughnut_hole_size"]


             
        self.down_bars = down_bars
        if 'down_bars' in params:
            self.down_bars = params["down_bars"]


             
        self.drop_lines = drop_lines
        if 'drop_lines' in params:
            self.drop_lines = params["drop_lines"]


             
        self.explosion = explosion
        if 'explosion' in params:
            self.explosion = params["explosion"]


             
        self.first_slice_angle = first_slice_angle
        if 'first_slice_angle' in params:
            self.first_slice_angle = params["first_slice_angle"]


             
        self.gap_width = gap_width
        if 'gap_width' in params:
            self.gap_width = params["gap_width"]


             
        self.has3_d_effect = has3_d_effect
        if 'has3_d_effect' in params:
            self.has3_d_effect = params["has3_d_effect"]


             
        self.has_drop_lines = has_drop_lines
        if 'has_drop_lines' in params:
            self.has_drop_lines = params["has_drop_lines"]


             
        self.has_hi_lo_lines = has_hi_lo_lines
        if 'has_hi_lo_lines' in params:
            self.has_hi_lo_lines = params["has_hi_lo_lines"]


             
        self.has_leader_lines = has_leader_lines
        if 'has_leader_lines' in params:
            self.has_leader_lines = params["has_leader_lines"]


             
        self.has_radar_axis_labels = has_radar_axis_labels
        if 'has_radar_axis_labels' in params:
            self.has_radar_axis_labels = params["has_radar_axis_labels"]


             
        self.has_series_lines = has_series_lines
        if 'has_series_lines' in params:
            self.has_series_lines = params["has_series_lines"]


             
        self.has_up_down_bars = has_up_down_bars
        if 'has_up_down_bars' in params:
            self.has_up_down_bars = params["has_up_down_bars"]


             
        self.hi_lo_lines = hi_lo_lines
        if 'hi_lo_lines' in params:
            self.hi_lo_lines = params["hi_lo_lines"]


             
        self.is_auto_split = is_auto_split
        if 'is_auto_split' in params:
            self.is_auto_split = params["is_auto_split"]


             
        self.is_color_varied = is_color_varied
        if 'is_color_varied' in params:
            self.is_color_varied = params["is_color_varied"]


             
        self.leader_lines = leader_lines
        if 'leader_lines' in params:
            self.leader_lines = params["leader_lines"]


             
        self.legend_entry = legend_entry
        if 'legend_entry' in params:
            self.legend_entry = params["legend_entry"]


             
        self.line = line
        if 'line' in params:
            self.line = params["line"]


             
        self.marker = marker
        if 'marker' in params:
            self.marker = params["marker"]


             
        self.name = name
        if 'name' in params:
            self.name = params["name"]


             
        self.overlap = overlap
        if 'overlap' in params:
            self.overlap = params["overlap"]


             
        self.plot_on_second_axis = plot_on_second_axis
        if 'plot_on_second_axis' in params:
            self.plot_on_second_axis = params["plot_on_second_axis"]


             
        self.points = points
        if 'points' in params:
            self.points = params["points"]


             
        self.second_plot_size = second_plot_size
        if 'second_plot_size' in params:
            self.second_plot_size = params["second_plot_size"]


             
        self.series_lines = series_lines
        if 'series_lines' in params:
            self.series_lines = params["series_lines"]


             
        self.shadow = shadow
        if 'shadow' in params:
            self.shadow = params["shadow"]


             
        self.shape_properties = shape_properties
        if 'shape_properties' in params:
            self.shape_properties = params["shape_properties"]


             
        self.show_negative_bubbles = show_negative_bubbles
        if 'show_negative_bubbles' in params:
            self.show_negative_bubbles = params["show_negative_bubbles"]


             
        self.size_represents = size_represents
        if 'size_represents' in params:
            self.size_represents = params["size_represents"]


             
        self.smooth = smooth
        if 'smooth' in params:
            self.smooth = params["smooth"]


             
        self.split_type = split_type
        if 'split_type' in params:
            self.split_type = params["split_type"]


             
        self.split_value = split_value
        if 'split_value' in params:
            self.split_value = params["split_value"]


             
        self.trend_lines = trend_lines
        if 'trend_lines' in params:
            self.trend_lines = params["trend_lines"]


             
        self.type = type
        if 'type' in params:
            self.type = params["type"]


             
        self.up_bars = up_bars
        if 'up_bars' in params:
            self.up_bars = params["up_bars"]


             
        self.values = values
        if 'values' in params:
            self.values = params["values"]


             
        self.x_error_bar = x_error_bar
        if 'x_error_bar' in params:
            self.x_error_bar = params["x_error_bar"]


             
        self.x_values = x_values
        if 'x_values' in params:
            self.x_values = params["x_values"]


             
        self.y_error_bar = y_error_bar
        if 'y_error_bar' in params:
            self.y_error_bar = params["y_error_bar"]


             
        self.link = link
        if 'link' in params:
            self.link = params["link"]


             

    @property
    def area(self):
        return self.container['area']

    @area.setter
    def area(self, area):
        self.container['area'] = area 
    @property
    def bar3_d_shape_type(self):
        return self.container['bar3_d_shape_type']

    @bar3_d_shape_type.setter
    def bar3_d_shape_type(self, bar3_d_shape_type):
        self.container['bar3_d_shape_type'] = bar3_d_shape_type 
    @property
    def border(self):
        return self.container['border']

    @border.setter
    def border(self, border):
        self.container['border'] = border 
    @property
    def bubble_scale(self):
        return self.container['bubble_scale']

    @bubble_scale.setter
    def bubble_scale(self, bubble_scale):
        self.container['bubble_scale'] = bubble_scale 
    @property
    def bubble_sizes(self):
        return self.container['bubble_sizes']

    @bubble_sizes.setter
    def bubble_sizes(self, bubble_sizes):
        self.container['bubble_sizes'] = bubble_sizes 
    @property
    def count_of_data_values(self):
        return self.container['count_of_data_values']

    @count_of_data_values.setter
    def count_of_data_values(self, count_of_data_values):
        self.container['count_of_data_values'] = count_of_data_values 
    @property
    def data_labels(self):
        return self.container['data_labels']

    @data_labels.setter
    def data_labels(self, data_labels):
        self.container['data_labels'] = data_labels 
    @property
    def display_name(self):
        return self.container['display_name']

    @display_name.setter
    def display_name(self, display_name):
        self.container['display_name'] = display_name 
    @property
    def doughnut_hole_size(self):
        return self.container['doughnut_hole_size']

    @doughnut_hole_size.setter
    def doughnut_hole_size(self, doughnut_hole_size):
        self.container['doughnut_hole_size'] = doughnut_hole_size 
    @property
    def down_bars(self):
        return self.container['down_bars']

    @down_bars.setter
    def down_bars(self, down_bars):
        self.container['down_bars'] = down_bars 
    @property
    def drop_lines(self):
        return self.container['drop_lines']

    @drop_lines.setter
    def drop_lines(self, drop_lines):
        self.container['drop_lines'] = drop_lines 
    @property
    def explosion(self):
        return self.container['explosion']

    @explosion.setter
    def explosion(self, explosion):
        self.container['explosion'] = explosion 
    @property
    def first_slice_angle(self):
        return self.container['first_slice_angle']

    @first_slice_angle.setter
    def first_slice_angle(self, first_slice_angle):
        self.container['first_slice_angle'] = first_slice_angle 
    @property
    def gap_width(self):
        return self.container['gap_width']

    @gap_width.setter
    def gap_width(self, gap_width):
        self.container['gap_width'] = gap_width 
    @property
    def has3_d_effect(self):
        return self.container['has3_d_effect']

    @has3_d_effect.setter
    def has3_d_effect(self, has3_d_effect):
        self.container['has3_d_effect'] = has3_d_effect 
    @property
    def has_drop_lines(self):
        return self.container['has_drop_lines']

    @has_drop_lines.setter
    def has_drop_lines(self, has_drop_lines):
        self.container['has_drop_lines'] = has_drop_lines 
    @property
    def has_hi_lo_lines(self):
        return self.container['has_hi_lo_lines']

    @has_hi_lo_lines.setter
    def has_hi_lo_lines(self, has_hi_lo_lines):
        self.container['has_hi_lo_lines'] = has_hi_lo_lines 
    @property
    def has_leader_lines(self):
        return self.container['has_leader_lines']

    @has_leader_lines.setter
    def has_leader_lines(self, has_leader_lines):
        self.container['has_leader_lines'] = has_leader_lines 
    @property
    def has_radar_axis_labels(self):
        return self.container['has_radar_axis_labels']

    @has_radar_axis_labels.setter
    def has_radar_axis_labels(self, has_radar_axis_labels):
        self.container['has_radar_axis_labels'] = has_radar_axis_labels 
    @property
    def has_series_lines(self):
        return self.container['has_series_lines']

    @has_series_lines.setter
    def has_series_lines(self, has_series_lines):
        self.container['has_series_lines'] = has_series_lines 
    @property
    def has_up_down_bars(self):
        return self.container['has_up_down_bars']

    @has_up_down_bars.setter
    def has_up_down_bars(self, has_up_down_bars):
        self.container['has_up_down_bars'] = has_up_down_bars 
    @property
    def hi_lo_lines(self):
        return self.container['hi_lo_lines']

    @hi_lo_lines.setter
    def hi_lo_lines(self, hi_lo_lines):
        self.container['hi_lo_lines'] = hi_lo_lines 
    @property
    def is_auto_split(self):
        return self.container['is_auto_split']

    @is_auto_split.setter
    def is_auto_split(self, is_auto_split):
        self.container['is_auto_split'] = is_auto_split 
    @property
    def is_color_varied(self):
        return self.container['is_color_varied']

    @is_color_varied.setter
    def is_color_varied(self, is_color_varied):
        self.container['is_color_varied'] = is_color_varied 
    @property
    def leader_lines(self):
        return self.container['leader_lines']

    @leader_lines.setter
    def leader_lines(self, leader_lines):
        self.container['leader_lines'] = leader_lines 
    @property
    def legend_entry(self):
        return self.container['legend_entry']

    @legend_entry.setter
    def legend_entry(self, legend_entry):
        self.container['legend_entry'] = legend_entry 
    @property
    def line(self):
        return self.container['line']

    @line.setter
    def line(self, line):
        self.container['line'] = line 
    @property
    def marker(self):
        return self.container['marker']

    @marker.setter
    def marker(self, marker):
        self.container['marker'] = marker 
    @property
    def name(self):
        return self.container['name']

    @name.setter
    def name(self, name):
        self.container['name'] = name 
    @property
    def overlap(self):
        return self.container['overlap']

    @overlap.setter
    def overlap(self, overlap):
        self.container['overlap'] = overlap 
    @property
    def plot_on_second_axis(self):
        return self.container['plot_on_second_axis']

    @plot_on_second_axis.setter
    def plot_on_second_axis(self, plot_on_second_axis):
        self.container['plot_on_second_axis'] = plot_on_second_axis 
    @property
    def points(self):
        return self.container['points']

    @points.setter
    def points(self, points):
        self.container['points'] = points 
    @property
    def second_plot_size(self):
        return self.container['second_plot_size']

    @second_plot_size.setter
    def second_plot_size(self, second_plot_size):
        self.container['second_plot_size'] = second_plot_size 
    @property
    def series_lines(self):
        return self.container['series_lines']

    @series_lines.setter
    def series_lines(self, series_lines):
        self.container['series_lines'] = series_lines 
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
    def show_negative_bubbles(self):
        return self.container['show_negative_bubbles']

    @show_negative_bubbles.setter
    def show_negative_bubbles(self, show_negative_bubbles):
        self.container['show_negative_bubbles'] = show_negative_bubbles 
    @property
    def size_represents(self):
        return self.container['size_represents']

    @size_represents.setter
    def size_represents(self, size_represents):
        self.container['size_represents'] = size_represents 
    @property
    def smooth(self):
        return self.container['smooth']

    @smooth.setter
    def smooth(self, smooth):
        self.container['smooth'] = smooth 
    @property
    def split_type(self):
        return self.container['split_type']

    @split_type.setter
    def split_type(self, split_type):
        self.container['split_type'] = split_type 
    @property
    def split_value(self):
        return self.container['split_value']

    @split_value.setter
    def split_value(self, split_value):
        self.container['split_value'] = split_value 
    @property
    def trend_lines(self):
        return self.container['trend_lines']

    @trend_lines.setter
    def trend_lines(self, trend_lines):
        self.container['trend_lines'] = trend_lines 
    @property
    def type(self):
        return self.container['type']

    @type.setter
    def type(self, type):
        self.container['type'] = type 
    @property
    def up_bars(self):
        return self.container['up_bars']

    @up_bars.setter
    def up_bars(self, up_bars):
        self.container['up_bars'] = up_bars 
    @property
    def values(self):
        return self.container['values']

    @values.setter
    def values(self, values):
        self.container['values'] = values 
    @property
    def x_error_bar(self):
        return self.container['x_error_bar']

    @x_error_bar.setter
    def x_error_bar(self, x_error_bar):
        self.container['x_error_bar'] = x_error_bar 
    @property
    def x_values(self):
        return self.container['x_values']

    @x_values.setter
    def x_values(self, x_values):
        self.container['x_values'] = x_values 
    @property
    def y_error_bar(self):
        return self.container['y_error_bar']

    @y_error_bar.setter
    def y_error_bar(self, y_error_bar):
        self.container['y_error_bar'] = y_error_bar 
    @property
    def link(self):
        return self.container['link']

    @link.setter
    def link(self, link):
        self.container['link'] = link 

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
        if not isinstance(other, Series):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    