import csv

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

f=solution.PointData.GetArray('f_tot')

da = []
with open('data.txt') as inf:
    data = csv.reader(inf, delimiter=" ")
    for row in data:
         da.append(row)

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(Input=contour1)
pythonAnnotation1.Expression = '"t=%4.0f" % (da(t_value))'

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).


