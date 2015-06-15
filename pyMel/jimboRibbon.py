#!/usr/bin/python
## make a balloon ribbon

import maya.cmds as mc
import random

global ribbonWidth, ribbonHeight, ribbonSubX, ribbonSubY
ribbonWidth  = 24.0
ribbonHeight = 0.165
ribbonSubX   = 240.0
ribbonSubY   = 2.0

if mc.window( 'ribbonGeneratorWindow', exists=True ):
	mc.deleteUI( ribbonGeneratorWindow, window=True );

def initializeRibbon(initWidth):
	mc.polyPlane(sx = 240, sy = 2.0, n = "ribbonTemp", w = initWidth, h = 0.165)
	mc.rename("polyPlane1", "ribbonTempHistory")
	mc.polySoftEdge( a = 180)
	mc.lattice( n = 'ribbon', cp = True, dv = (2, 4, 2), objectDentered = True, ldv = (2, 3, 2), outsideLattice = True )
        mc.hide()
	mc.select('ribbonTempHistory.vtx[1]', r=True )
	mc.ChamferVertex()
	mc.rename( "polyChamfer1", "tempChamfer" )
	mc.seAttr( 'tempChamfer.width', 1)
	mc.delete( 'ribbonTemp.vtx[72]' )
	return

def ribbonAttributes():
	global ribbonWidth, ribbonHeight, ribbonSubX, ribbonSubY
	ribbonWidth = mc.floatSliderGrp(ribbonWidthInput, query=True, value=True)
	ribbonHeight = mc.floatSliderGrp(ribbonHeightInput, query=True, value=True)
	ribbonSubX = mc.floatSliderGrp(ribbonSubXInput, query=True, value=True)
	ribbonSubY = mc.floatSliderGrp(ribbonSubYInput, query=True, value=True)

	adjustRibbonWidth(ribbonWidth)
	return

def adjustRibbonWidth(newWidth):
	w = newWidth * 2
	mc.setAttr('ribbonTempHistory.width', newWidth)
	return


def finalizeRibbon():
	global ribbonWidth, ribbonHeight, ribbonSubX, ribbonSubY
	mc.delete('ribbonTemp')
	initializeRibbon(ribbonWidth)
	adjustRibbonWidth(ribbonWidth)
	mc.makeIdentity( apply=True, translate=True, rotate=True, scale=True )
	## add grid offset here
	closeWindow()

def closeWindow():
	global ribbonGeneratorWindow
	mc.deleteUI( ribbonGeneratorWindow, window=True);
	mc.headsUpMessage( 'Your ribbon is done.', verticalOffset = 50);

# Make a new window
ribbonGeneratorWindow = mc.window( title="Ribbon Generator", widthHeight= (400,260), sizeable=False);

#Create a layout for the window appearance
mc.columnLayout(adjustableColumn=True );

# Define the Ribbon input fields
ribbonWidth = mc.floatSliderGrp( field = True, min=0.1, max = 100.0, value=ribbonWidth, label="Ribbon Width", dragCommand='ribbonAttributes()',changeCommand='ribbonAttributes()' )
ribbonHeight = mc.floatSliderGrp( field = True, min=0.05, max = 1.0, value=ribbonHeight, label="Ribbon Height", dragCommand='ribbonAttributes()',changeCommand='ribbonAttributes()' )
ribbonSubX = mc.floatSliderGrp( field = True, min=0.0, max = 240.0, value=ribbonSubX, label="Ribbon Subdivisions X", dragCommand='ribbonAttributes()',changeCommand='ribbonAttributes()' )
ribbonSubY = mc.floatSliderGrp( field = True, min=0.0, max = 2.0, value=ribbonSubY, label="Ribbon Subdivisions Y", dragCommand='ribbonAttributes()',changeCommand='ribbonAttributes()' )

mc.button( label='Create Ribbon', command='finalizeRibbon()', width=396 )

initializeRibbon(ribbonWidth);
