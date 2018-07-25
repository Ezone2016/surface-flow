#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

# create a new 'Calculator'
calculator2 = Calculator(Input=contour1)
calculator2.Function = ''

# find source
solution = FindSource('solution-*')

# find source
calculator1 = FindSource('Calculator1')

# Properties modified on calculator2
calculator2.ResultArrayName = '112'
calculator2.Function = 'abs(Normals_X*1/2.45+Normals_Y*1/2.45+Normals_Z*2/2.45)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [519, 678]

# get color transfer function/color map for 'a112'
a112LUT = GetColorTransferFunction('a112')

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', '112']
calculator2Display.LookupTable = a112LUT
calculator2Display.OSPRayScaleArray = '112'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = '112'
calculator2Display.ScaleFactor = 10.161299896240235
calculator2Display.SelectScaleArray = '112'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = '112'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# find source
isoVolume1 = FindSource('IsoVolume1')

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume2 = IsoVolume(Input=calculator2)
isoVolume2.InputScalars = ['POINTS', '112']
isoVolume2.ThresholdRange = [0.0003270105439789339, 0.9974419219153267]

# Properties modified on isoVolume2
isoVolume2.ThresholdRange = [0.90, 1.0]

# get opacity transfer function/opacity map for 'a112'
a112PWF = GetOpacityTransferFunction('a112')

# show data in view
isoVolume2Display = Show(isoVolume2, renderView1)
# trace defaults for the display properties.
isoVolume2Display.Representation = 'Surface'
isoVolume2Display.ColorArrayName = ['POINTS', '112']
isoVolume2Display.LookupTable = a112LUT
isoVolume2Display.OSPRayScaleArray = '112'
isoVolume2Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume2Display.SelectOrientationVectors = '112'
isoVolume2Display.ScaleFactor = 8.804088973999024
isoVolume2Display.SelectScaleArray = '112'
isoVolume2Display.GlyphType = 'Arrow'
isoVolume2Display.GlyphTableIndexArray = '112'
isoVolume2Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume2Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume2Display.ScalarOpacityFunction = a112PWF
isoVolume2Display.ScalarOpacityUnitDistance = 22.93779351713065

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
isoVolume2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(isoVolume1)

# get color transfer function/color map for 'a001'
a001LUT = GetColorTransferFunction('a001')

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
isoVolume1Display.ScaleFactor = 8.871219253540039
isoVolume1Display.SelectScaleArray = '001'
isoVolume1Display.GlyphType = 'Arrow'
isoVolume1Display.GlyphTableIndexArray = '001'
isoVolume1Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume1Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume1Display.ScalarOpacityFunction = a001PWF
isoVolume1Display.ScalarOpacityUnitDistance = 13.332701092177238

# show color bar/color legend
isoVolume1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(isoVolume1, renderView1)

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator3 = Calculator(Input=contour1)
calculator3.Function = ''

# Properties modified on calculator3
calculator3.ResultArrayName = '-112'
calculator3.Function = '-Normals_X*1/2.45+Normals_Y*1/2.45+Normals_Z*2/2.45'

# show data in view
calculator3Display = Show(calculator3, renderView1)
# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', '-112']
calculator3Display.LookupTable = a112LUT
calculator3Display.OSPRayScaleArray = '-112'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = '-112'
calculator3Display.ScaleFactor = 10.161299896240235
calculator3Display.SelectScaleArray = '-112'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = '-112'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume3 = IsoVolume(Input=calculator3)
isoVolume3.InputScalars = ['POINTS', '-112']
isoVolume3.ThresholdRange = [-0.997441885422687, 0.9974419219153267]

# Properties modified on isoVolume3
isoVolume3.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume3Display = Show(isoVolume3, renderView1)
# trace defaults for the display properties.
isoVolume3Display.Representation = 'Surface'
isoVolume3Display.ColorArrayName = ['POINTS', '-112']
isoVolume3Display.LookupTable = a112LUT
isoVolume3Display.OSPRayScaleArray = '-112'
isoVolume3Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume3Display.SelectOrientationVectors = '-112'
isoVolume3Display.ScaleFactor = 4.336886596679688
isoVolume3Display.SelectScaleArray = '-112'
isoVolume3Display.GlyphType = 'Arrow'
isoVolume3Display.GlyphTableIndexArray = '-112'
isoVolume3Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume3Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume3Display.ScalarOpacityFunction = a112PWF
isoVolume3Display.ScalarOpacityUnitDistance = 12.859344224463152

# hide data in view
Hide(calculator3, renderView1)

# show color bar/color legend
isoVolume3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator4 = Calculator(Input=contour1)
calculator4.Function = ''

# Properties modified on calculator4
calculator4.ResultArrayName = '1-12'
calculator4.Function = ''

# show data in view
calculator4Display = Show(calculator4, renderView1)
# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = [None, '']
calculator4Display.OSPRayScaleArray = 'Normals'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'None'
calculator4Display.ScaleFactor = 10.161299896240235
calculator4Display.SelectScaleArray = 'None'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'None'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume4 = IsoVolume(Input=calculator4)
isoVolume4.InputScalars = ['POINTS', 'f_tot']
isoVolume4.ThresholdRange = [0.00790392979979515, 0.07748670130968094]

# set active source
SetActiveSource(calculator4)

# destroy isoVolume4
Delete(isoVolume4)
del isoVolume4

# Properties modified on calculator4
calculator4.Function = 'Normals_X*1/2.45-Normals_Y*1/2.45+Normals_Z*2/2.45'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume4 = IsoVolume(Input=calculator4)
isoVolume4.InputScalars = ['POINTS', '1-12']
isoVolume4.ThresholdRange = [-0.997441885422687, 0.9974419219153267]

# Properties modified on isoVolume4
isoVolume4.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume4Display = Show(isoVolume4, renderView1)
# trace defaults for the display properties.
isoVolume4Display.Representation = 'Surface'
isoVolume4Display.ColorArrayName = ['POINTS', '1-12']
isoVolume4Display.LookupTable = a112LUT
isoVolume4Display.OSPRayScaleArray = '1-12'
isoVolume4Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume4Display.SelectOrientationVectors = '1-12'
isoVolume4Display.ScaleFactor = 4.336886596679688
isoVolume4Display.SelectScaleArray = '1-12'
isoVolume4Display.GlyphType = 'Arrow'
isoVolume4Display.GlyphTableIndexArray = '1-12'
isoVolume4Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume4Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume4Display.ScalarOpacityFunction = a112PWF
isoVolume4Display.ScalarOpacityUnitDistance = 12.859344224463152

# hide data in view
Hide(calculator4, renderView1)

# show color bar/color legend
isoVolume4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator5 = Calculator(Input=contour1)
calculator5.Function = ''

# Properties modified on calculator5
calculator5.ResultArrayName = '-1-12'
calculator5.Function = '-Normals_X*1/2.45-Normals_Y*1/2.45+Normals_Z*2/2.45'

# show data in view
calculator5Display = Show(calculator5, renderView1)
# trace defaults for the display properties.
calculator5Display.Representation = 'Surface'
calculator5Display.ColorArrayName = ['POINTS', '-1-12']
calculator5Display.LookupTable = a112LUT
calculator5Display.OSPRayScaleArray = '-1-12'
calculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator5Display.SelectOrientationVectors = '-1-12'
calculator5Display.ScaleFactor = 10.161299896240235
calculator5Display.SelectScaleArray = '-1-12'
calculator5Display.GlyphType = 'Arrow'
calculator5Display.GlyphTableIndexArray = '-1-12'
calculator5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator5Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume5 = IsoVolume(Input=calculator5)
isoVolume5.InputScalars = ['POINTS', '-1-12']
isoVolume5.ThresholdRange = [-0.9974418732584738, 0.997441885422687]

# Properties modified on isoVolume5
isoVolume5.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume5Display = Show(isoVolume5, renderView1)
# trace defaults for the display properties.
isoVolume5Display.Representation = 'Surface'
isoVolume5Display.ColorArrayName = ['POINTS', '-1-12']
isoVolume5Display.LookupTable = a112LUT
isoVolume5Display.OSPRayScaleArray = '-1-12'
isoVolume5Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume5Display.SelectOrientationVectors = '-1-12'
isoVolume5Display.ScaleFactor = 4.336886215209961
isoVolume5Display.SelectScaleArray = '-1-12'
isoVolume5Display.GlyphType = 'Arrow'
isoVolume5Display.GlyphTableIndexArray = '-1-12'
isoVolume5Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume5Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume5Display.ScalarOpacityFunction = a112PWF
isoVolume5Display.ScalarOpacityUnitDistance = 12.859343660650289

# hide data in view
Hide(calculator5, renderView1)

# show color bar/color legend
isoVolume5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator6 = Calculator(Input=contour1)
calculator6.Function = ''

# Properties modified on calculator6
calculator6.ResultArrayName = '11-2'
calculator6.Function = 'Normals_X*1/2.45+Normals_Y*1/2.45-Normals_Z*2/2.45'

# show data in view
calculator6Display = Show(calculator6, renderView1)
# trace defaults for the display properties.
calculator6Display.Representation = 'Surface'
calculator6Display.ColorArrayName = ['POINTS', '11-2']
calculator6Display.LookupTable = a112LUT
calculator6Display.OSPRayScaleArray = '11-2'
calculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator6Display.SelectOrientationVectors = '11-2'
calculator6Display.ScaleFactor = 10.161299896240235
calculator6Display.SelectScaleArray = '11-2'
calculator6Display.GlyphType = 'Arrow'
calculator6Display.GlyphTableIndexArray = '11-2'
calculator6Display.DataAxesGrid = 'GridAxesRepresentation'
calculator6Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume6 = IsoVolume(Input=calculator6)
isoVolume6.InputScalars = ['POINTS', '11-2']
isoVolume6.ThresholdRange = [-0.997441885422687, 0.9974418732584738]

# Properties modified on isoVolume6
isoVolume6.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume6Display = Show(isoVolume6, renderView1)
# trace defaults for the display properties.
isoVolume6Display.Representation = 'Surface'
isoVolume6Display.ColorArrayName = ['POINTS', '11-2']
isoVolume6Display.LookupTable = a112LUT
isoVolume6Display.OSPRayScaleArray = '11-2'
isoVolume6Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume6Display.SelectOrientationVectors = '11-2'
isoVolume6Display.ScaleFactor = 4.336886596679688
isoVolume6Display.SelectScaleArray = '11-2'
isoVolume6Display.GlyphType = 'Arrow'
isoVolume6Display.GlyphTableIndexArray = '11-2'
isoVolume6Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume6Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume6Display.ScalarOpacityFunction = a112PWF
isoVolume6Display.ScalarOpacityUnitDistance = 12.859344788275992

# hide data in view
Hide(calculator6, renderView1)

# show color bar/color legend
isoVolume6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator7 = Calculator(Input=contour1)
calculator7.Function = ''

# Properties modified on calculator7
calculator7.ResultArrayName = '-11-2'
calculator7.Function = '-Normals_X*1/2.45+Normals_Y*1/2.45-Normals_Z*2/2.45'

# show data in view
calculator7Display = Show(calculator7, renderView1)
# trace defaults for the display properties.
calculator7Display.Representation = 'Surface'
calculator7Display.ColorArrayName = ['POINTS', '-11-2']
calculator7Display.LookupTable = a112LUT
calculator7Display.OSPRayScaleArray = '-11-2'
calculator7Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator7Display.SelectOrientationVectors = '-11-2'
calculator7Display.ScaleFactor = 10.161299896240235
calculator7Display.SelectScaleArray = '-11-2'
calculator7Display.GlyphType = 'Arrow'
calculator7Display.GlyphTableIndexArray = '-11-2'
calculator7Display.DataAxesGrid = 'GridAxesRepresentation'
calculator7Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator7Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume7 = IsoVolume(Input=calculator7)
isoVolume7.InputScalars = ['POINTS', '-11-2']
isoVolume7.ThresholdRange = [-0.9974419219153265, 0.997441885422687]

# Properties modified on isoVolume7
isoVolume7.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume7Display = Show(isoVolume7, renderView1)
# trace defaults for the display properties.
isoVolume7Display.Representation = 'Surface'
isoVolume7Display.ColorArrayName = ['POINTS', '-11-2']
isoVolume7Display.LookupTable = a112LUT
isoVolume7Display.OSPRayScaleArray = '-11-2'
isoVolume7Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume7Display.SelectOrientationVectors = '-11-2'
isoVolume7Display.ScaleFactor = 4.336886596679688
isoVolume7Display.SelectScaleArray = '-11-2'
isoVolume7Display.GlyphType = 'Arrow'
isoVolume7Display.GlyphTableIndexArray = '-11-2'
isoVolume7Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume7Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume7Display.ScalarOpacityFunction = a112PWF
isoVolume7Display.ScalarOpacityUnitDistance = 12.859344224463152

# hide data in view
Hide(calculator7, renderView1)

# show color bar/color legend
isoVolume7Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator8 = Calculator(Input=contour1)
calculator8.Function = ''

# Properties modified on calculator8
calculator8.ResultArrayName = '1-1-2'
calculator8.Function = 'Normals_X*1/2.45-Normals_Y*1/2.45-Normals_Z*2/2.45'

# show data in view
calculator8Display = Show(calculator8, renderView1)
# trace defaults for the display properties.
calculator8Display.Representation = 'Surface'
calculator8Display.ColorArrayName = ['POINTS', '1-1-2']
calculator8Display.LookupTable = a112LUT
calculator8Display.OSPRayScaleArray = '1-1-2'
calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator8Display.SelectOrientationVectors = '1-1-2'
calculator8Display.ScaleFactor = 10.161299896240235
calculator8Display.SelectScaleArray = '1-1-2'
calculator8Display.GlyphType = 'Arrow'
calculator8Display.GlyphTableIndexArray = '1-1-2'
calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
calculator8Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator8Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume8 = IsoVolume(Input=calculator8)
isoVolume8.InputScalars = ['POINTS', '1-1-2']
isoVolume8.ThresholdRange = [-0.9974419219153267, 0.997441885422687]

# Properties modified on isoVolume8
isoVolume8.ThresholdRange = [0.90, 1.0]

# show data in view
isoVolume8Display = Show(isoVolume8, renderView1)
# trace defaults for the display properties.
isoVolume8Display.Representation = 'Surface'
isoVolume8Display.ColorArrayName = ['POINTS', '1-1-2']
isoVolume8Display.LookupTable = a112LUT
isoVolume8Display.OSPRayScaleArray = '1-1-2'
isoVolume8Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume8Display.SelectOrientationVectors = '1-1-2'
isoVolume8Display.ScaleFactor = 4.336886596679688
isoVolume8Display.SelectScaleArray = '1-1-2'
isoVolume8Display.GlyphType = 'Arrow'
isoVolume8Display.GlyphTableIndexArray = '1-1-2'
isoVolume8Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume8Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume8Display.ScalarOpacityFunction = a112PWF
isoVolume8Display.ScalarOpacityUnitDistance = 12.859344224463152

# hide data in view
Hide(calculator8, renderView1)

# show color bar/color legend
isoVolume8Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide color bar/color legend
isoVolume8Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-179.4439209358293, 381.2254392030468, -48.41511092552713]
renderView1.CameraFocalPoint = [100.00000381469727, 100.00000381469727, 100.0]
renderView1.CameraViewUp = [0.2826772370002286, -0.2127279982635163, -0.9353290214874731]
renderView1.CameraParallelScale = 111.11618786996414

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).