#! /usr/bin/env python
# Python script template for SAGA tool execution (automatically created, experimental)

import saga_api, sys, os

##########################################
def Call_SAGA_Module(fDEM):            # pass your input file(s) here

    # ------------------------------------
    # initialize input dataset(s)
    dem    = saga_api.SG_Get_Data_Manager().Add_Grid(unicode(fDEM))
    if dem == None or dem.is_Valid() == 0:
        print 'ERROR: loading grid [' + fDEM + ']'
        return 0

    # ------------------------------------
    # initialize output dataset(s)
    outgrid = saga_api.SG_Get_Data_Manager().Add_Grid(dem.Get_System())

    # ------------------------------------
    # call module: Ordinary Kriging
    Module = saga_api.SG_Get_Module_Library_Manager().Get_Module('statistics_kriging','0')

    Parms = Module.Get_Parameters() # default parameter list
    Parms.Get(unicode('POINTS')).Set_Value(use_variable_of_dataset_here) # input NOT optional shapes
    Parms.Get(unicode('FIELD')).Set_Value(0)
    Parms.Get(unicode('TQUALITY')).Set_Value(0)
    Parms.Get(unicode('LOG')).Set_Value(0)
    Parms.Get(unicode('BLOCK')).Set_Value(0)
    Parms.Get(unicode('DBLOCK')).Set_Value(100.000000)
    Parms.Get(unicode('TARGET_DEFINITION')).Set_Value(0)
    Parms.Get(unicode('TARGET_USER_XMIN')).Set_Value(0.000000)
    Parms.Get(unicode('TARGET_USER_XMAX')).Set_Value(100.000000)
    Parms.Get(unicode('TARGET_USER_YMIN')).Set_Value(0.000000)
    Parms.Get(unicode('TARGET_USER_YMAX')).Set_Value(100.000000)
    Parms.Get(unicode('TARGET_USER_SIZE')).Set_Value(1.000000)
    Parms.Get(unicode('TARGET_USER_COLS')).Set_Value(100)
    Parms.Get(unicode('TARGET_USER_ROWS')).Set_Value(100)
    Parms.Get(unicode('TARGET_USER_FITS')).Set_Value(1)
    Parms.Get(unicode('VARIANCE_CREATE')).Set_Value(0)
    Parms.Get(unicode('SEARCH_RANGE')).Set_Value(0)
    Parms.Get(unicode('SEARCH_RADIUS')).Set_Value(1000.000000)
    Parms.Get(unicode('SEARCH_POINTS_ALL')).Set_Value(0)
    Parms.Get(unicode('SEARCH_POINTS_MIN')).Set_Value(16)
    Parms.Get(unicode('SEARCH_POINTS_MAX')).Set_Value(20)
    Parms.Get(unicode('SEARCH_DIRECTION')).Set_Value(0)

    if Module.Execute() == 0:
        print 'Module execution failed!'
        return 0

    print
    print 'The module has been executed.'
    print 'Now you would like to save your output datasets, please edit the script to do so.'
    return 0                           # remove this line once you have edited the script

    # ------------------------------------
    # save results
    path   = os.path.split(fDEM)[0]
    if path == '':
        path = './'
    outgrid.Save(saga_api.CSG_String(path + '/outgrid'))

    print
    print 'Module successfully executed!'
    return 1

##########################################
if __name__ == '__main__':
    print 'Python - Version ' + sys.version
    print saga_api.SAGA_API_Get_Version()
    print
    print 'Usage: %s <in: filename>'
    print
    print 'This is a simple template, please edit the script and add the necessary input and output file(s)!'
    print 'We will exit the script for now.'
    sys.exit()                         # remove this line once you have edited the script
    # This might look like this:
    # fDEM    = sys.argv[1]
    # if os.path.split(fDEM)[0] == '':
    #    fDEM    = './' + fDEM
    fDEM = './../test_data/test.sgrd'  # remove this line once you have edited the script


    saga_api.SG_UI_Msg_Lock(1)
    if os.name == 'nt':    # Windows
        os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['SAGA'] + '/bin/saga_vc_Win32/dll'
        saga_api.SG_Get_Module_Library_Manager().Add_Directory(os.environ['SAGA'] + '/bin/saga_vc_Win32/modules', 0)
    else:                  # Linux
        saga_api.SG_Get_Module_Library_Manager().Add_Directory(os.environ['SAGA_MLB'], 0)
    saga_api.SG_UI_Msg_Lock(0)

    Call_SAGA_Module(fDEM)             # pass your input file(s) here
