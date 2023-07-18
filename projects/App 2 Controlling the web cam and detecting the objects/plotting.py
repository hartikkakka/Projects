from app_2 import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


# Create a ColumnDataSource object using the df variable
cds = ColumnDataSource(df)

# Create a figure object with specified attributes
p = figure(x_axis_type="datetime", height=600, width=1000, title="Motion Graph")

"""
x_axis_type="datetime": This sets the type of the x-axis to display dates and times.
height="100": This sets the height of the figure to 100 pixels.
width=500: This sets the width of the figure to 500 pixels.
 sizing_mode attribute is set to "stretch_both", allowing the plot to resize and 
 fill both the height and width of the available space
title="Motion Graph": This sets the title of the figure to "Motion Graph".
"""

# Customize the y-axis ticks
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1


# Create a HoverTool object for displaying tooltips
hover = HoverTool(tooltips=[("Start","@Start"),("End","@End")])
p.add_tools(hover)

# Create a quad glyph to represent the motion events
q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)


# Specify the output file for saving the graph
output_file("Graph.html")

# Display the figure
show(p)



