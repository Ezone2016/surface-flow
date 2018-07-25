ARRAYNAME = "f_tot"  # pressure, density, EPS, EFFSTR, DISP, etc.
ARRAYASSOCIATION = "Point" # "Point" or "Cell"
UNITS = "eVA^-2" # specify units for display 
MODE = "Min" # "Min" or "Max"

def get_value(dataset):
    """Function that returns the Min or Max value for ARRAYNAME in the current
    dataset"""
    if ARRAYASSOCIATION == "Point":
        dsa = dataset.GetPointData()
    elif ARRAYASSOCIATION == "Cell":
        dsa = dataset.GetCellData()
    else:
        raise RuntimeError, "Unknown assoctiation %s" % ARRAYASSOCIATION
    array = dsa.GetArray(ARRAYNAME)
    # if arrayname is missing, we silently ignore.
    if array:
        if MODE == "Min":
            return array.GetRange(-1)[0]
        elif MODE == "Max":
            return array.GetRange(-1)[1]
        else:
            raise RuntimeError, "Unknown MODE %s" % MODE
    return None

input = self.GetInputDataObject(0, 0)
output = self.GetOutputDataObject(0)

chosen_value = None

if input.IsA("vtkMultiBlockDataSet"):
    iter = input.NewIterator()
    iter.UnRegister(None)
    iter.InitTraversal()
    while not iter.IsDoneWithTraversal():
        curInput = iter.GetCurrentDataObject()
        cur_value = get_value(curInput)
        if MODE == "Min":
            test_result = (chosen_value == None) or (cur_value < chosen_value)
        elif MODE == "Max":
            test_result = (chosen_value == None) or (cur_value > chosen_value)
        else:
            raise RuntimeError, "Unknown MODE %s" % MODE
        if test_result:
            chosen_value = cur_value
        iter.GoToNextItem();
else:
    chosen_value = get_value(input)

# FIXME: Determine Min/Max in parallel.

if chosen_value == None:
    print "ERROR: Could not determine value, using 0"
    print "Check data type (ARRAYASSOCIATION) and array name(ARRAYNAME)"
    chosen_value = 0
outputarray = vtk.vtkStringArray()
outputarray.SetName("%s" % MODE)
outputarray.SetNumberOfTuples(1)
outputarray.SetValue(0, "%s %s = %g %s." % (MODE, ARRAYNAME, chosen_value,UNITS))
output.GetRowData().AddArray(outputarray)
