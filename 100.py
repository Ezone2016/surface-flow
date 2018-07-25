#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator9 = Calculator(Input=contour1)
calculator9.Function = ''

# find source
calculator4 = FindSource('Calculator4')

# set active source
SetActiveSource(calculator4)

# find source
calculator5 = FindSource('Calculator5')

# set active source
SetActiveSource(calculator5)

# get color transfer function/color map for 'a112'
a112LUT = GetColorTransferFunction('a112')

# set active source
SetActiveSource(calculator9)

# find source
solution = FindSource('solution-*')

# find source
calculator1 = FindSource('Calculator1')

# find source
isoVolume2 = FindSource('IsoVolume2')

# find source
calculator3 = FindSource('Calculator3')

# find source
isoVolume3 = FindSource('IsoVolume3')

# find source
calculator2 = FindSource('Calculator2')

# find source
isoVolume1 = FindSource('IsoVolume1')

# find source
isoVolume4 = FindSource('IsoVolume4')

# find source
isoVolume5 = FindSource('IsoVolume5')

# find source
calculator6 = FindSource('Calculator6')

# find source
isoVolume6 = FindSource('IsoVolume6')

# find source
calculator7 = FindSource('Calculator7')

# find source
isoVolume7 = FindSource('IsoVolume7')

# find source
calculator8 = FindSource('Calculator8')

# find source
isoVolume8 = FindSource('IsoVolume8')

# Properties modified on calculator9
calculator9.ResultArrayName = '010'
calculator9.Function = 'abs(Normals_X*0+Normals_Y*1+Normals_Z*0)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1072, 678]

# get color transfer function/color map for 'a010'
a010LUT = GetColorTransferFunction('a010')

# show data in view
calculator9Display = Show(calculator9, renderView1)
# trace defaults for the display properties.
calculator9Display.Representation = 'Surface'
calculator9Display.ColorArrayName = ['POINTS', '010']
calculator9Display.LookupTable = a010LUT
calculator9Display.OSPRayScaleArray = '010'
calculator9Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator9Display.SelectOrientationVectors = '010'
calculator9Display.ScaleFactor = 10.17312355041504
calculator9Display.SelectScaleArray = '010'
calculator9Display.GlyphType = 'Arrow'
calculator9Display.GlyphTableIndexArray = '010'
calculator9Display.DataAxesGrid = 'GridAxesRepresentation'
calculator9Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator9Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
a112LUT.RescaleTransferFunction(-0.999397112399, 0.999591338391)

# get opacity transfer function/opacity map for 'a112'
a112PWF = GetOpacityTransferFunction('a112')

# Rescale transfer function
a112PWF.RescaleTransferFunction(-0.999397112399, 0.999591338391)

# create a new 'Iso Volume'
isoVolume9 = IsoVolume(Input=calculator9)
isoVolume9.InputScalars = ['POINTS', '010']
isoVolume9.ThresholdRange = [0.0, 1.0]

# Properties modified on isoVolume9
isoVolume9.ThresholdRange = [0.95, 1.0]

# get opacity transfer function/opacity map for 'a010'
a010PWF = GetOpacityTransferFunction('a010')

# show data in view
isoVolume9Display = Show(isoVolume9, renderView1)
# trace defaults for the display properties.
isoVolume9Display.Representation = 'Surface'
isoVolume9Display.ColorArrayName = ['POINTS', '010']
isoVolume9Display.LookupTable = a010LUT
isoVolume9Display.OSPRayScaleArray = '010'
isoVolume9Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume9Display.SelectOrientationVectors = '010'
isoVolume9Display.ScaleFactor = 10.17312355041504
isoVolume9Display.SelectScaleArray = '010'
isoVolume9Display.GlyphType = 'Arrow'
isoVolume9Display.GlyphTableIndexArray = '010'
isoVolume9Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume9Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume9Display.ScalarOpacityFunction = a010PWF
isoVolume9Display.ScalarOpacityUnitDistance = 20.758479867058284

# hide data in view
Hide(calculator9, renderView1)

# show color bar/color legend
isoVolume9Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on isoVolume9
isoVolume9.ThresholdRange = [0.9, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# hide color bar/color legend
isoVolume9Display.SetScalarBarVisibility(renderView1, False)

# Properties modified on a010LUT
a010LUT.Discretize = 0

# Properties modified on a010LUT
a010LUT.NanColor = [0.6666666666666666, 0.6666666666666666, 1.0]

# Properties modified on a010LUT
a010LUT.EnableOpacityMapping = 1

# Properties modified on a010LUT
a010LUT.EnableOpacityMapping = 0

# Properties modified on a010LUT
a010LUT.Discretize = 1

# Properties modified on a010LUT
a010LUT.NumberOfTableValues = 1

# Properties modified on a010LUT
a010LUT.EnableOpacityMapping = 1

# Properties modified on a010LUT
a010LUT.EnableOpacityMapping = 0

# set active source
SetActiveSource(isoVolume7)

# set active source
SetActiveSource(calculator8)

# set active source
SetActiveSource(isoVolume7)

# Properties modified on isoVolume7
isoVolume7.ThresholdRange = [0.9, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator10 = Calculator(Input=contour1)
calculator10.Function = ''

# Properties modified on calculator10
calculator10.ResultArrayName = '100'
calculator10.Function = 'abs(Normals_X*1+Normals_Y*0+Normals_Z*0)'

# get color transfer function/color map for 'a100'
a100LUT = GetColorTransferFunction('a100')

# show data in view
calculator10Display = Show(calculator10, renderView1)
# trace defaults for the display properties.
calculator10Display.Representation = 'Surface'
calculator10Display.ColorArrayName = ['POINTS', '100']
calculator10Display.LookupTable = a100LUT
calculator10Display.OSPRayScaleArray = '100'
calculator10Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator10Display.SelectOrientationVectors = '100'
calculator10Display.ScaleFactor = 10.172604370117188
calculator10Display.SelectScaleArray = '100'
calculator10Display.GlyphType = 'Arrow'
calculator10Display.GlyphTableIndexArray = '100'
calculator10Display.DataAxesGrid = 'GridAxesRepresentation'
calculator10Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator10Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume10 = IsoVolume(Input=calculator10)
isoVolume10.InputScalars = ['POINTS', '100']
isoVolume10.ThresholdRange = [0.0, 1.0]

# Properties modified on isoVolume10
isoVolume10.ThresholdRange = [0.9, 1.0]

# get opacity transfer function/opacity map for 'a100'
a100PWF = GetOpacityTransferFunction('a100')

# show data in view
isoVolume10Display = Show(isoVolume10, renderView1)
# trace defaults for the display properties.
isoVolume10Display.Representation = 'Surface'
isoVolume10Display.ColorArrayName = ['POINTS', '100']
isoVolume10Display.LookupTable = a100LUT
isoVolume10Display.OSPRayScaleArray = '100'
isoVolume10Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume10Display.SelectOrientationVectors = '100'
isoVolume10Display.ScaleFactor = 10.172604370117188
isoVolume10Display.SelectScaleArray = '100'
isoVolume10Display.GlyphType = 'Arrow'
isoVolume10Display.GlyphTableIndexArray = '100'
isoVolume10Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume10Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume10Display.ScalarOpacityFunction = a100PWF
isoVolume10Display.ScalarOpacityUnitDistance = 13.133344672110272

# hide data in view
Hide(calculator10, renderView1)

# show color bar/color legend
isoVolume10Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on a100LUT
a100LUT.NumberOfTableValues = 1

# Properties modified on a100LUT
a100LUT.NanColor = [0.6666666666666666, 0.6666666666666666, 1.0]

# hide color bar/color legend
isoVolume10Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-270.45165998979695, 155.11707059901278, -97.31034870710167]
renderView1.CameraFocalPoint = [100.00000141845098, 100.00000478724824, 99.99999911234194]
renderView1.CameraViewUp = [0.43476577946060924, -0.2114965466104527, -0.8753558863581495]
renderView1.CameraParallelScale = 111.11618786996414

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).