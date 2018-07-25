#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
contour1 = FindSource('Contour1')

# create a new 'Calculator'
calculator11 = Calculator(Input=contour1)
calculator11.Function = ''

# find source
solution = FindSource('solution-*')

# find source
calculator2 = FindSource('Calculator2')

# find source
isoVolume2 = FindSource('IsoVolume2')

# find source
calculator8 = FindSource('Calculator8')

# find source
calculator3 = FindSource('Calculator3')

# find source
isoVolume3 = FindSource('IsoVolume3')

# find source
isoVolume4 = FindSource('IsoVolume4')

# find source
calculator4 = FindSource('Calculator4')

# find source
calculator6 = FindSource('Calculator6')

# find source
calculator5 = FindSource('Calculator5')

# find source
isoVolume6 = FindSource('IsoVolume6')

# find source
isoVolume7 = FindSource('IsoVolume7')

# find source
calculator7 = FindSource('Calculator7')

# find source
isoVolume10 = FindSource('IsoVolume10')

# find source
isoVolume8 = FindSource('IsoVolume8')

# Properties modified on calculator11
calculator11.ResultArrayName = '101'
calculator11.Function = 'abs(Normals_X*1+Normals_Y*0+Normals_Z*1)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1072, 678]

# get color transfer function/color map for 'a101'
a101LUT = GetColorTransferFunction('a101')

# show data in view
calculator11Display = Show(calculator11, renderView1)
# trace defaults for the display properties.
calculator11Display.Representation = 'Surface'
calculator11Display.ColorArrayName = ['POINTS', '101']
calculator11Display.LookupTable = a101LUT
calculator11Display.OSPRayScaleArray = '101'
calculator11Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator11Display.SelectOrientationVectors = '101'
calculator11Display.ScaleFactor = 10.17312355041504
calculator11Display.SelectScaleArray = '101'
calculator11Display.GlyphType = 'Arrow'
calculator11Display.GlyphTableIndexArray = '101'
calculator11Display.DataAxesGrid = 'GridAxesRepresentation'
calculator11Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator11Display.SetScalarBarVisibility(renderView1, True)

# find source
isoVolume9 = FindSource('IsoVolume9')

# find source
isoVolume1 = FindSource('IsoVolume1')

# find source
calculator10 = FindSource('Calculator10')

# find source
calculator1 = FindSource('Calculator1')

# find source
calculator9 = FindSource('Calculator9')

# find source
isoVolume5 = FindSource('IsoVolume5')

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'a112'
a112LUT = GetColorTransferFunction('a112')

# Rescale transfer function
a112LUT.RescaleTransferFunction(-0.999397112399, 0.999591338391)

# get opacity transfer function/opacity map for 'a112'
a112PWF = GetOpacityTransferFunction('a112')

# Rescale transfer function
a112PWF.RescaleTransferFunction(-0.999397112399, 0.999591338391)

# create a new 'Iso Volume'
isoVolume11 = IsoVolume(Input=calculator11)
isoVolume11.InputScalars = ['POINTS', '101']
isoVolume11.ThresholdRange = [0.0, 1.4110935926437378]

# set active source
SetActiveSource(calculator11)

# destroy isoVolume11
Delete(isoVolume11)
del isoVolume11

# Properties modified on calculator11
calculator11.Function = 'abs(Normals_X*1/sqrt(2)+Normals_Y*0/sqrt(2)+Normals_Z*1/sqrt(2))'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume11 = IsoVolume(Input=calculator11)
isoVolume11.InputScalars = ['POINTS', '101']
isoVolume11.ThresholdRange = [0.0, 0.9977938482472746]

# Properties modified on isoVolume11
isoVolume11.ThresholdRange = [0.1, 0.1]

# get opacity transfer function/opacity map for 'a101'
a101PWF = GetOpacityTransferFunction('a101')

# show data in view
isoVolume11Display = Show(isoVolume11, renderView1)
# trace defaults for the display properties.
isoVolume11Display.Representation = 'Surface'
isoVolume11Display.ColorArrayName = ['POINTS', '101']
isoVolume11Display.LookupTable = a101LUT
isoVolume11Display.OSPRayScaleArray = '101'
isoVolume11Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume11Display.SelectOrientationVectors = '101'
isoVolume11Display.ScaleFactor = 10.128280639648438
isoVolume11Display.SelectScaleArray = '101'
isoVolume11Display.GlyphType = 'Arrow'
isoVolume11Display.GlyphTableIndexArray = '101'
isoVolume11Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume11Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume11Display.ScalarOpacityFunction = a101PWF
isoVolume11Display.ScalarOpacityUnitDistance = 23.82707180130548

# hide data in view
Hide(calculator11, renderView1)

# show color bar/color legend
isoVolume11Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide color bar/color legend
isoVolume11Display.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'a001'
a001LUT = GetColorTransferFunction('a001')

# get color legend/bar for a001LUT in view renderView1
a001LUTColorBar = GetScalarBar(a001LUT, renderView1)

# change scalar bar placement
a001LUTColorBar.WindowLocation = 'AnyLocation'
a001LUTColorBar.Position = [0.8917910447761194, 0.6533923303834808]
a001LUTColorBar.ScalarBarLength = 0.33000000000000007

# Properties modified on a101LUT
a101LUT.NumberOfTableValues = 1

# Properties modified on a101LUT
a101LUT.NanColor = [1.0, 0.3333333333333333, 1.0]

# Properties modified on a101LUT
a101LUT.EnableOpacityMapping = 1

# Properties modified on a101LUT
a101LUT.EnableOpacityMapping = 0

# Properties modified on a101LUT
a101LUT.EnableOpacityMapping = 1

# Properties modified on a101LUT
a101LUT.EnableOpacityMapping = 0

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToFirst()

# hide data in view
Hide(isoVolume10, renderView1)

# hide data in view
Hide(isoVolume9, renderView1)

# hide data in view
Hide(isoVolume8, renderView1)

# hide data in view
Hide(isoVolume7, renderView1)

# hide data in view
Hide(isoVolume6, renderView1)

# hide data in view
Hide(isoVolume5, renderView1)

# hide data in view
Hide(isoVolume4, renderView1)

# hide data in view
Hide(isoVolume3, renderView1)

# hide data in view
Hide(isoVolume1, renderView1)

# hide data in view
Hide(isoVolume2, renderView1)

animationScene1.GoToLast()

animationScene1.GoToFirst()

# set active source
SetActiveSource(isoVolume1)

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

# set active source
SetActiveSource(isoVolume2)

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

# show color bar/color legend
isoVolume2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume3)

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

# show color bar/color legend
isoVolume3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume4)

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

# show color bar/color legend
isoVolume4Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume5)

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

# show color bar/color legend
isoVolume5Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume6)

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

# show color bar/color legend
isoVolume6Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume7)

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

# show color bar/color legend
isoVolume7Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume8)

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

# show color bar/color legend
isoVolume8Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume9)

# get color transfer function/color map for 'a010'
a010LUT = GetColorTransferFunction('a010')

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

# show color bar/color legend
isoVolume9Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(isoVolume10)

# get color transfer function/color map for 'a100'
a100LUT = GetColorTransferFunction('a100')

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

# show color bar/color legend
isoVolume10Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(isoVolume11, renderView1)

# set active source
SetActiveSource(isoVolume11)

# show data in view
isoVolume11Display = Show(isoVolume11, renderView1)

# show color bar/color legend
isoVolume11Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(isoVolume11, renderView1)

# show data in view
isoVolume11Display = Show(isoVolume11, renderView1)

# show color bar/color legend
isoVolume11Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for a101LUT in view renderView1
a101LUTColorBar = GetScalarBar(a101LUT, renderView1)

# change scalar bar placement
a101LUTColorBar.WindowLocation = 'AnyLocation'
a101LUTColorBar.Position = [0.0018656716417910502, 0.2566371681415929]
a101LUTColorBar.ScalarBarLength = 0.33000000000000007

# set active source
SetActiveSource(calculator11)

# set active source
SetActiveSource(isoVolume11)

# set active source
SetActiveSource(calculator11)

# hide data in view
Hide(isoVolume11, renderView1)

# show data in view
calculator11Display = Show(calculator11, renderView1)

# show color bar/color legend
calculator11Display.SetScalarBarVisibility(renderView1, True)

# destroy isoVolume11
Delete(isoVolume11)
del isoVolume11

# create a new 'Iso Volume'
isoVolume11 = IsoVolume(Input=calculator11)
isoVolume11.InputScalars = ['POINTS', '101']
isoVolume11.ThresholdRange = [0.0, 0.9997951070551174]

# Properties modified on isoVolume11
isoVolume11.ThresholdRange = [0.1, 0.1]

# show data in view
isoVolume11Display = Show(isoVolume11, renderView1)
# trace defaults for the display properties.
isoVolume11Display.Representation = 'Surface'
isoVolume11Display.ColorArrayName = ['POINTS', '101']
isoVolume11Display.LookupTable = a101LUT
isoVolume11Display.OSPRayScaleArray = '101'
isoVolume11Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume11Display.SelectOrientationVectors = '101'
isoVolume11Display.ScaleFactor = 9.9894775390625
isoVolume11Display.SelectScaleArray = '101'
isoVolume11Display.GlyphType = 'Arrow'
isoVolume11Display.GlyphTableIndexArray = '101'
isoVolume11Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume11Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume11Display.ScalarOpacityFunction = a101PWF
isoVolume11Display.ScalarOpacityUnitDistance = 22.448393841606563

# hide data in view
Hide(calculator11, renderView1)

# show color bar/color legend
isoVolume11Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on isoVolume11
isoVolume11.ThresholdRange = [0.9, 1.0]

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# Properties modified on isoVolume11
isoVolume11.ThresholdRange = [0.8, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on isoVolume11
isoVolume11.ThresholdRange = [0.9, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator12 = Calculator(Input=contour1)
calculator12.Function = ''

# Properties modified on calculator12
calculator12.ResultArrayName = '011'
calculator12.Function = 'abs(Normals_X*0+Normals_Y*1/sqrt(2)+Normals_Z*1/sqrt(2))'

# get color transfer function/color map for 'a011'
a011LUT = GetColorTransferFunction('a011')

# show data in view
calculator12Display = Show(calculator12, renderView1)
# trace defaults for the display properties.
calculator12Display.Representation = 'Surface'
calculator12Display.ColorArrayName = ['POINTS', '011']
calculator12Display.LookupTable = a011LUT
calculator12Display.OSPRayScaleArray = '011'
calculator12Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator12Display.SelectOrientationVectors = '011'
calculator12Display.ScaleFactor = 10.164659881591797
calculator12Display.SelectScaleArray = '011'
calculator12Display.GlyphType = 'Arrow'
calculator12Display.GlyphTableIndexArray = '011'
calculator12Display.DataAxesGrid = 'GridAxesRepresentation'
calculator12Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator12Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume12 = IsoVolume(Input=calculator12)
isoVolume12.InputScalars = ['POINTS', '011']
isoVolume12.ThresholdRange = [0.0, 0.9971184449998876]

# Properties modified on isoVolume12
isoVolume12.ThresholdRange = [0.9, 1.0]

# get opacity transfer function/opacity map for 'a011'
a011PWF = GetOpacityTransferFunction('a011')

# show data in view
isoVolume12Display = Show(isoVolume12, renderView1)
# trace defaults for the display properties.
isoVolume12Display.Representation = 'Surface'
isoVolume12Display.ColorArrayName = ['POINTS', '011']
isoVolume12Display.LookupTable = a011LUT
isoVolume12Display.OSPRayScaleArray = '011'
isoVolume12Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume12Display.SelectOrientationVectors = '011'
isoVolume12Display.ScaleFactor = 9.348189163208009
isoVolume12Display.SelectScaleArray = '011'
isoVolume12Display.GlyphType = 'Arrow'
isoVolume12Display.GlyphTableIndexArray = '011'
isoVolume12Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume12Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume12Display.ScalarOpacityFunction = a011PWF
isoVolume12Display.ScalarOpacityUnitDistance = 22.63797637059131

# hide data in view
Hide(calculator12, renderView1)

# show color bar/color legend
isoVolume12Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on a011LUT
a011LUT.Discretize = 0

# Properties modified on a011LUT
a011LUT.Discretize = 1

# Properties modified on a011LUT
a011LUT.NumberOfTableValues = 1

# Properties modified on a011LUT
a011LUT.NanColor = [1.0, 0.3333333333333333, 1.0]

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator13 = Calculator(Input=contour1)
calculator13.Function = ''

# Properties modified on calculator13
calculator13.ResultArrayName = '-101'
calculator13.Function = 'abs(-Normals_X*1/sqrt(2)+Normals_Y*0/sqrt(2)+Normals_Z*1/sqrt(2))'

# show data in view
calculator13Display = Show(calculator13, renderView1)
# trace defaults for the display properties.
calculator13Display.Representation = 'Surface'
calculator13Display.ColorArrayName = ['POINTS', '-101']
calculator13Display.LookupTable = a101LUT
calculator13Display.OSPRayScaleArray = '-101'
calculator13Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator13Display.SelectOrientationVectors = '-101'
calculator13Display.ScaleFactor = 10.164659881591797
calculator13Display.SelectScaleArray = '-101'
calculator13Display.GlyphType = 'Arrow'
calculator13Display.GlyphTableIndexArray = '-101'
calculator13Display.DataAxesGrid = 'GridAxesRepresentation'
calculator13Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator13Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume13 = IsoVolume(Input=calculator13)
isoVolume13.InputScalars = ['POINTS', '-101']
isoVolume13.ThresholdRange = [0.0, 0.9971184449998876]

# Properties modified on isoVolume13
isoVolume13.ThresholdRange = [0.9, 1.0]

# show data in view
isoVolume13Display = Show(isoVolume13, renderView1)
# trace defaults for the display properties.
isoVolume13Display.Representation = 'Surface'
isoVolume13Display.ColorArrayName = ['POINTS', '-101']
isoVolume13Display.LookupTable = a101LUT
isoVolume13Display.OSPRayScaleArray = '-101'
isoVolume13Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume13Display.SelectOrientationVectors = '-101'
isoVolume13Display.ScaleFactor = 9.348188781738282
isoVolume13Display.SelectScaleArray = '-101'
isoVolume13Display.GlyphType = 'Arrow'
isoVolume13Display.GlyphTableIndexArray = '-101'
isoVolume13Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume13Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume13Display.ScalarOpacityFunction = a101PWF
isoVolume13Display.ScalarOpacityUnitDistance = 22.63797619288293

# hide data in view
Hide(calculator13, renderView1)

# show color bar/color legend
isoVolume13Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(isoVolume13)

# set active source
SetActiveSource(calculator13)

# hide data in view
Hide(isoVolume13, renderView1)

# show data in view
calculator13Display = Show(calculator13, renderView1)

# show color bar/color legend
calculator13Display.SetScalarBarVisibility(renderView1, True)

# destroy isoVolume13
Delete(isoVolume13)
del isoVolume13

# Properties modified on calculator13
calculator13.Function = '-Normals_X*1/sqrt(2)+Normals_Y*0/sqrt(2)+Normals_Z*1/sqrt(2)'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
a101LUT.RescaleTransferFunction(-0.997118360706, 1.41109359264)

# Rescale transfer function
a101PWF.RescaleTransferFunction(-0.997118360706, 1.41109359264)

# create a new 'Iso Volume'
isoVolume13 = IsoVolume(Input=calculator13)
isoVolume13.InputScalars = ['POINTS', '-101']
isoVolume13.ThresholdRange = [-0.9971183607061904, 0.9971184449998876]

# Properties modified on isoVolume13
isoVolume13.ThresholdRange = [0.9, 1.0]

# show data in view
isoVolume13Display = Show(isoVolume13, renderView1)
# trace defaults for the display properties.
isoVolume13Display.Representation = 'Surface'
isoVolume13Display.ColorArrayName = ['POINTS', '-101']
isoVolume13Display.LookupTable = a101LUT
isoVolume13Display.OSPRayScaleArray = '-101'
isoVolume13Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume13Display.SelectOrientationVectors = '-101'
isoVolume13Display.ScaleFactor = 1.5545745849609376
isoVolume13Display.SelectScaleArray = '-101'
isoVolume13Display.GlyphType = 'Arrow'
isoVolume13Display.GlyphTableIndexArray = '-101'
isoVolume13Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume13Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume13Display.ScalarOpacityFunction = a101PWF
isoVolume13Display.ScalarOpacityUnitDistance = 5.178449640602032

# hide data in view
Hide(calculator13, renderView1)

# show color bar/color legend
isoVolume13Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator14 = Calculator(Input=contour1)
calculator14.Function = ''

# Properties modified on calculator14
calculator14.ResultArrayName = '10-1'
calculator14.Function = 'Normals_X*1/sqrt(2)+Normals_Y*0/sqrt(2)-Normals_Z*1/sqrt(2)'

# show data in view
calculator14Display = Show(calculator14, renderView1)
# trace defaults for the display properties.
calculator14Display.Representation = 'Surface'
calculator14Display.ColorArrayName = ['POINTS', '10-1']
calculator14Display.LookupTable = a101LUT
calculator14Display.OSPRayScaleArray = '10-1'
calculator14Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator14Display.SelectOrientationVectors = '10-1'
calculator14Display.ScaleFactor = 10.164659881591797
calculator14Display.SelectScaleArray = '10-1'
calculator14Display.GlyphType = 'Arrow'
calculator14Display.GlyphTableIndexArray = '10-1'
calculator14Display.DataAxesGrid = 'GridAxesRepresentation'
calculator14Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator14Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume14 = IsoVolume(Input=calculator14)
isoVolume14.InputScalars = ['POINTS', '10-1']
isoVolume14.ThresholdRange = [-0.9971184449998876, 0.9971183607061904]

# Properties modified on isoVolume14
isoVolume14.ThresholdRange = [0.9, 1.0]

# show data in view
isoVolume14Display = Show(isoVolume14, renderView1)
# trace defaults for the display properties.
isoVolume14Display.Representation = 'Surface'
isoVolume14Display.ColorArrayName = ['POINTS', '10-1']
isoVolume14Display.LookupTable = a101LUT
isoVolume14Display.OSPRayScaleArray = '10-1'
isoVolume14Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume14Display.SelectOrientationVectors = '10-1'
isoVolume14Display.ScaleFactor = 1.5545913696289064
isoVolume14Display.SelectScaleArray = '10-1'
isoVolume14Display.GlyphType = 'Arrow'
isoVolume14Display.GlyphTableIndexArray = '10-1'
isoVolume14Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume14Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume14Display.ScalarOpacityFunction = a101PWF
isoVolume14Display.ScalarOpacityUnitDistance = 5.178477815994204

# hide data in view
Hide(calculator14, renderView1)

# show color bar/color legend
isoVolume14Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator15 = Calculator(Input=contour1)
calculator15.Function = ''

# Properties modified on calculator15
calculator15.ResultArrayName = '0-11'
calculator15.Function = 'Normals_X*0/sqrt(2)-Normals_Y*1/sqrt(2)+Normals_Z*1/sqrt(2)'

# show data in view
calculator15Display = Show(calculator15, renderView1)
# trace defaults for the display properties.
calculator15Display.Representation = 'Surface'
calculator15Display.ColorArrayName = ['POINTS', '0-11']
calculator15Display.LookupTable = a011LUT
calculator15Display.OSPRayScaleArray = '0-11'
calculator15Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator15Display.SelectOrientationVectors = '0-11'
calculator15Display.ScaleFactor = 10.164659881591797
calculator15Display.SelectScaleArray = '0-11'
calculator15Display.GlyphType = 'Arrow'
calculator15Display.GlyphTableIndexArray = '0-11'
calculator15Display.DataAxesGrid = 'GridAxesRepresentation'
calculator15Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator15Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume15 = IsoVolume(Input=calculator15)
isoVolume15.InputScalars = ['POINTS', '0-11']
isoVolume15.ThresholdRange = [-0.9971183607061904, 0.9971184449998876]

# Properties modified on isoVolume15
isoVolume15.ThresholdRange = [0.9, 1.0]

# show data in view
isoVolume15Display = Show(isoVolume15, renderView1)
# trace defaults for the display properties.
isoVolume15Display.Representation = 'Surface'
isoVolume15Display.ColorArrayName = ['POINTS', '0-11']
isoVolume15Display.LookupTable = a011LUT
isoVolume15Display.OSPRayScaleArray = '0-11'
isoVolume15Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume15Display.SelectOrientationVectors = '0-11'
isoVolume15Display.ScaleFactor = 1.5545745849609376
isoVolume15Display.SelectScaleArray = '0-11'
isoVolume15Display.GlyphType = 'Arrow'
isoVolume15Display.GlyphTableIndexArray = '0-11'
isoVolume15Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume15Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume15Display.ScalarOpacityFunction = a011PWF
isoVolume15Display.ScalarOpacityUnitDistance = 5.178449640602032

# hide data in view
Hide(calculator15, renderView1)

# show color bar/color legend
isoVolume15Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToFirst()

# set active source
SetActiveSource(contour1)

# create a new 'Calculator'
calculator16 = Calculator(Input=contour1)
calculator16.Function = ''

# Properties modified on calculator16
calculator16.ResultArrayName = '01-1'
calculator16.Function = 'Normals_X*0/sqrt(2)+Normals_Y*1/sqrt(2)-Normals_Z*1/sqrt(2)'

# show data in view
calculator16Display = Show(calculator16, renderView1)
# trace defaults for the display properties.
calculator16Display.Representation = 'Surface'
calculator16Display.ColorArrayName = ['POINTS', '01-1']
calculator16Display.LookupTable = a011LUT
calculator16Display.OSPRayScaleArray = '01-1'
calculator16Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator16Display.SelectOrientationVectors = '01-1'
calculator16Display.ScaleFactor = 10.03901710510254
calculator16Display.SelectScaleArray = '01-1'
calculator16Display.GlyphType = 'Arrow'
calculator16Display.GlyphTableIndexArray = '01-1'
calculator16Display.DataAxesGrid = 'GridAxesRepresentation'
calculator16Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator16Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
a011LUT.RescaleTransferFunction(-0.999795064908, 0.999795107055)

# Rescale transfer function
a011PWF.RescaleTransferFunction(-0.999795064908, 0.999795107055)

# create a new 'Iso Volume'
isoVolume16 = IsoVolume(Input=calculator16)
isoVolume16.InputScalars = ['POINTS', '01-1']
isoVolume16.ThresholdRange = [-0.999795064908269, 0.999795064908269]

# Properties modified on isoVolume16
isoVolume16.ThresholdRange = [0.9, 1.0]

# show data in view
isoVolume16Display = Show(isoVolume16, renderView1)
# trace defaults for the display properties.
isoVolume16Display.Representation = 'Surface'
isoVolume16Display.ColorArrayName = ['POINTS', '01-1']
isoVolume16Display.LookupTable = a011LUT
isoVolume16Display.OSPRayScaleArray = '01-1'
isoVolume16Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume16Display.SelectOrientationVectors = '01-1'
isoVolume16Display.ScaleFactor = 4.358648681640625
isoVolume16Display.SelectScaleArray = '01-1'
isoVolume16Display.GlyphType = 'Arrow'
isoVolume16Display.GlyphTableIndexArray = '01-1'
isoVolume16Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume16Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume16Display.ScalarOpacityFunction = a011PWF
isoVolume16Display.ScalarOpacityUnitDistance = 8.368981594354445

# hide data in view
Hide(calculator16, renderView1)

# show color bar/color legend
isoVolume16Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-99.56315684834443, 294.04347988978793, 418.9441467678082]
renderView1.CameraFocalPoint = [99.99999426251588, 99.99999189647102, 99.99999612903687]
renderView1.CameraViewUp = [0.6113439685380899, -0.44588646440855795, 0.6537918728382413]
renderView1.CameraParallelScale = 111.11618786996414

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).