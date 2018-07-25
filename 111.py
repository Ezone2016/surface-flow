#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

# create a new 'Calculator'
calculator17 = Calculator(Input=contour1)
calculator17.Function = ''

# find source
solution = FindSource('solution-*')

# find source
text1 = FindSource('Text1')

# find source
isoVolume3 = FindSource('IsoVolume3')

# find source
isoVolume1 = FindSource('IsoVolume1')

# find source
isoVolume2 = FindSource('IsoVolume2')

# Properties modified on calculator17
calculator17.ResultArrayName = '111'
calculator17.Function = 'abs(Normals_X*1/sqrt(3)+Normals_Y*1/sqrt(3)+Normals_Z*1/sqrt(3))'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1072, 707]

# get color transfer function/color map for 'a111'
a111LUT = GetColorTransferFunction('a111')

# show data in view
calculator17Display = Show(calculator17, renderView1)
# trace defaults for the display properties.
calculator17Display.Representation = 'Surface'
calculator17Display.ColorArrayName = ['POINTS', '111']
calculator17Display.LookupTable = a111LUT
calculator17Display.OSPRayScaleArray = '111'
calculator17Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator17Display.SelectOrientationVectors = '111'
calculator17Display.ScaleFactor = 10.172604370117188
calculator17Display.SelectScaleArray = '111'
calculator17Display.GlyphType = 'Arrow'
calculator17Display.GlyphTableIndexArray = '111'
calculator17Display.DataAxesGrid = 'GridAxesRepresentation'
calculator17Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator17Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator17Display.SetScalarBarVisibility(renderView1, True)

# find source
calculator16 = FindSource('Calculator16')

# find source
isoVolume15 = FindSource('IsoVolume15')

# find source
calculator15 = FindSource('Calculator15')

# find source
calculator13 = FindSource('Calculator13')

# find source
isoVolume12 = FindSource('IsoVolume12')

# find source
calculator12 = FindSource('Calculator12')

# find source
isoVolume13 = FindSource('IsoVolume13')

# find source
calculator11 = FindSource('Calculator11')

# find source
isoVolume10 = FindSource('IsoVolume10')

# find source
isoVolume14 = FindSource('IsoVolume14')

# find source
calculator10 = FindSource('Calculator10')

# find source
isoVolume9 = FindSource('IsoVolume9')

# find source
calculator9 = FindSource('Calculator9')

# find source
isoVolume11 = FindSource('IsoVolume11')

# find source
isoVolume8 = FindSource('IsoVolume8')

# find source
isoVolume7 = FindSource('IsoVolume7')

# find source
calculator8 = FindSource('Calculator8')

# find source
calculator7 = FindSource('Calculator7')

# find source
calculator6 = FindSource('Calculator6')

# find source
isoVolume6 = FindSource('IsoVolume6')

# find source
isoVolume16 = FindSource('IsoVolume16')

# find source
calculator14 = FindSource('Calculator14')

# find source
calculator4 = FindSource('Calculator4')

# find source
isoVolume5 = FindSource('IsoVolume5')

# find source
isoVolume4 = FindSource('IsoVolume4')

# find source
calculator2 = FindSource('Calculator2')

# find source
calculator1 = FindSource('Calculator1')

# find source
calculator3 = FindSource('Calculator3')

# find source
calculator5 = FindSource('Calculator5')

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume17 = IsoVolume(Input=calculator17)
isoVolume17.InputScalars = ['POINTS', '111']
isoVolume17.ThresholdRange = [0.0012553429883580547, 0.9999638486561773]

# Properties modified on isoVolume17
isoVolume17.ThresholdRange = [0.9, 0.9999638486561773]

# get opacity transfer function/opacity map for 'a111'
a111PWF = GetOpacityTransferFunction('a111')

# show data in view
isoVolume17Display = Show(isoVolume17, renderView1)
# trace defaults for the display properties.
isoVolume17Display.Representation = 'Surface'
isoVolume17Display.ColorArrayName = ['POINTS', '111']
isoVolume17Display.LookupTable = a111LUT
isoVolume17Display.OSPRayScaleArray = '111'
isoVolume17Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume17Display.SelectOrientationVectors = '111'
isoVolume17Display.ScaleFactor = 9.429016876220704
isoVolume17Display.SelectScaleArray = '111'
isoVolume17Display.GlyphType = 'Arrow'
isoVolume17Display.GlyphTableIndexArray = '111'
isoVolume17Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume17Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume17Display.ScalarOpacityFunction = a111PWF
isoVolume17Display.ScalarOpacityUnitDistance = 14.38561644453019

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
isoVolume17Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator17, renderView1)

# show color bar/color legend
isoVolume17Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator18 = Calculator(Input=contour1)
calculator18.Function = ''

# Properties modified on calculator18
calculator18.ResultArrayName = '-111'
calculator18.Function = 'abs(-Normals_X*1/sqrt(3)+Normals_Y*1/sqrt(3)+Normals_Z*1/sqrt(3))'

# show data in view
calculator18Display = Show(calculator18, renderView1)
# trace defaults for the display properties.
calculator18Display.Representation = 'Surface'
calculator18Display.ColorArrayName = ['POINTS', '-111']
calculator18Display.LookupTable = a111LUT
calculator18Display.OSPRayScaleArray = '-111'
calculator18Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator18Display.SelectOrientationVectors = '-111'
calculator18Display.ScaleFactor = 10.172604370117188
calculator18Display.SelectScaleArray = '-111'
calculator18Display.GlyphType = 'Arrow'
calculator18Display.GlyphTableIndexArray = '-111'
calculator18Display.DataAxesGrid = 'GridAxesRepresentation'
calculator18Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator18Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator18Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume18 = IsoVolume(Input=calculator18)
isoVolume18.InputScalars = ['POINTS', '-111']
isoVolume18.ThresholdRange = [0.0012553429883580547, 0.9999638486561773]

# Properties modified on isoVolume18
isoVolume18.ThresholdRange = [0.9, 0.9999638486561773]

# show data in view
isoVolume18Display = Show(isoVolume18, renderView1)
# trace defaults for the display properties.
isoVolume18Display.Representation = 'Surface'
isoVolume18Display.ColorArrayName = ['POINTS', '-111']
isoVolume18Display.LookupTable = a111LUT
isoVolume18Display.OSPRayScaleArray = '-111'
isoVolume18Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume18Display.SelectOrientationVectors = '-111'
isoVolume18Display.ScaleFactor = 9.429016876220704
isoVolume18Display.SelectScaleArray = '-111'
isoVolume18Display.GlyphType = 'Arrow'
isoVolume18Display.GlyphTableIndexArray = '-111'
isoVolume18Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume18Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume18Display.ScalarOpacityFunction = a111PWF
isoVolume18Display.ScalarOpacityUnitDistance = 14.38561644453019

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
isoVolume18Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator18, renderView1)

# show color bar/color legend
isoVolume18Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator19 = Calculator(Input=contour1)
calculator19.Function = ''

# Properties modified on calculator19
calculator19.Function = 'abs(Normals_X*1/sqrt(3)-Normals_Y*1/sqrt(3)+Normals_Z*1/sqrt(3))'

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')

# show data in view
calculator19Display = Show(calculator19, renderView1)
# trace defaults for the display properties.
calculator19Display.Representation = 'Surface'
calculator19Display.ColorArrayName = ['POINTS', 'Result']
calculator19Display.LookupTable = resultLUT
calculator19Display.OSPRayScaleArray = 'Result'
calculator19Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator19Display.SelectOrientationVectors = 'None'
calculator19Display.ScaleFactor = 10.172604370117188
calculator19Display.SelectScaleArray = 'Result'
calculator19Display.GlyphType = 'Arrow'
calculator19Display.GlyphTableIndexArray = 'Result'
calculator19Display.DataAxesGrid = 'GridAxesRepresentation'
calculator19Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator19Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator19Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume19 = IsoVolume(Input=calculator19)
isoVolume19.InputScalars = ['POINTS', 'Result']
isoVolume19.ThresholdRange = [0.0012553429883580547, 0.9999638486561773]

# Properties modified on isoVolume19
isoVolume19.ThresholdRange = [0.9, 0.9999638486561773]

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')

# show data in view
isoVolume19Display = Show(isoVolume19, renderView1)
# trace defaults for the display properties.
isoVolume19Display.Representation = 'Surface'
isoVolume19Display.ColorArrayName = ['POINTS', 'Result']
isoVolume19Display.LookupTable = resultLUT
isoVolume19Display.OSPRayScaleArray = 'Result'
isoVolume19Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume19Display.SelectOrientationVectors = 'None'
isoVolume19Display.ScaleFactor = 9.429016876220704
isoVolume19Display.SelectScaleArray = 'Result'
isoVolume19Display.GlyphType = 'Arrow'
isoVolume19Display.GlyphTableIndexArray = 'Result'
isoVolume19Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume19Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume19Display.ScalarOpacityFunction = resultPWF
isoVolume19Display.ScalarOpacityUnitDistance = 14.38561644453019

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
isoVolume19Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator19, renderView1)

# show color bar/color legend
isoVolume19Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on resultLUT
resultLUT.NumberOfTableValues = 1

# Properties modified on resultLUT
resultLUT.NanColor = [0.0, 0.0, 1.0]

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator20 = Calculator(Input=contour1)
calculator20.Function = ''

# Properties modified on calculator20
calculator20.ResultArrayName = '11-1'
calculator20.Function = 'abs(Normals_X*1/sqrt(3)+Normals_Y*1/sqrt(3)-Normals_Z*1/sqrt(3))'

# show data in view
calculator20Display = Show(calculator20, renderView1)
# trace defaults for the display properties.
calculator20Display.Representation = 'Surface'
calculator20Display.ColorArrayName = ['POINTS', '11-1']
calculator20Display.LookupTable = a111LUT
calculator20Display.OSPRayScaleArray = '11-1'
calculator20Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator20Display.SelectOrientationVectors = '11-1'
calculator20Display.ScaleFactor = 10.172604370117188
calculator20Display.SelectScaleArray = '11-1'
calculator20Display.GlyphType = 'Arrow'
calculator20Display.GlyphTableIndexArray = '11-1'
calculator20Display.DataAxesGrid = 'GridAxesRepresentation'
calculator20Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator20Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator20Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume20 = IsoVolume(Input=calculator20)
isoVolume20.InputScalars = ['POINTS', '11-1']
isoVolume20.ThresholdRange = [0.0012553429883580547, 0.9999638142434195]

# Properties modified on isoVolume20
isoVolume20.ThresholdRange = [0.9, 0.9999638142434195]

# show data in view
isoVolume20Display = Show(isoVolume20, renderView1)
# trace defaults for the display properties.
isoVolume20Display.Representation = 'Surface'
isoVolume20Display.ColorArrayName = ['POINTS', '11-1']
isoVolume20Display.LookupTable = a111LUT
isoVolume20Display.OSPRayScaleArray = '11-1'
isoVolume20Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume20Display.SelectOrientationVectors = '11-1'
isoVolume20Display.ScaleFactor = 9.429016876220704
isoVolume20Display.SelectScaleArray = '11-1'
isoVolume20Display.GlyphType = 'Arrow'
isoVolume20Display.GlyphTableIndexArray = '11-1'
isoVolume20Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume20Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume20Display.ScalarOpacityFunction = a111PWF
isoVolume20Display.ScalarOpacityUnitDistance = 14.38561644453019

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
isoVolume20Display.OSPRayScaleFunction.Points = [0.999999935136943, 0.0, 0.5, 0.0, 1.0000000473773563, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator20, renderView1)

# show color bar/color legend
isoVolume20Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-194.0803466746444, 113.88237493786538, 282.13007423015864]
renderView1.CameraFocalPoint = [51.53446493494764, 102.28785884571431, 130.01571241170572]
renderView1.CameraViewUp = [0.5276021997492523, 0.07384192124669375, 0.8462761307554098]
renderView1.CameraParallelScale = 111.11618786996414

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).