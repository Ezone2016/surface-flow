#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

# create a new 'Calculator'
calculator1 = Calculator(Input=contour1)
calculator1.Function = ''

# find source
solution = FindSource('solution-*')

# Properties modified on calculator1
calculator1.ResultArrayName = '001'
calculator1.Function = 'abs(Normals_X*0+Normals_Y*0+Normals_Z*1)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [519, 678]

# get color transfer function/color map for 'a001'
a001LUT = GetColorTransferFunction('a001')

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', '001']
calculator1Display.LookupTable = a001LUT
calculator1Display.OSPRayScaleArray = '001'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = '001'
calculator1Display.ScaleFactor = 10.161299896240235
calculator1Display.SelectScaleArray = '001'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = '001'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(Input=calculator1)
isoVolume1.InputScalars = ['POINTS', '001']
isoVolume1.ThresholdRange = [0.0, 1.0]

# Properties modified on isoVolume1
isoVolume1.ThresholdRange = [0.95, 1.0]

# get opacity transfer function/opacity map for 'a001'
a001PWF = GetOpacityTransferFunction('a001')

# show data in view
isoVolume1Display = Show(isoVolume1, renderView1)
# trace defaults for the display properties.
isoVolume1Display.Representation = 'Surface'
isoVolume1Display.ColorArrayName = ['POINTS', '001']
isoVolume1Display.LookupTable = a001LUT
isoVolume1Display.OSPRayScaleArray = '001'
isoVolume1Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume1Display.SelectOrientationVectors = '001'
isoVolume1Display.ScaleFactor = 9.104409790039062
isoVolume1Display.SelectScaleArray = '001'
isoVolume1Display.GlyphType = 'Arrow'
isoVolume1Display.GlyphTableIndexArray = '001'
isoVolume1Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume1Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume1Display.ScalarOpacityFunction = a001PWF
isoVolume1Display.ScalarOpacityUnitDistance = 12.073835969555603

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
isoVolume1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide color bar/color legend
isoVolume1Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-92.67985379072978, 209.46707736035933, -162.49726332630382]
renderView1.CameraFocalPoint = [100.00000164117833, 100.00000203561724, 100.00000173914523]
renderView1.CameraViewUp = [0.6687053785352756, -0.3697814053178461, -0.6450541287358393]
renderView1.CameraParallelScale = 90.17153799043486

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).