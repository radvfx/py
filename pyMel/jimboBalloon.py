#!/usr/bin/python
## create a variety of balloons
## from Dan Marsch 12-2-2010
## Jimbo (12-06-10) added 'minBalloonDrop setting' to balloonDrop under 'finalizeBallon' def.

import maya.cmds as mc
import random

global minBalloonDrop, balloonDrop, balloonRadius, balloonQuantity, balloonRandom
balloonRadius = 1.0
minBalloonDrop = 0.0
balloonDrop = 0.0
balloonQuantity = 1
balloonRandom = False

# Check if the window exists.
if mc.window( 'balloonGeneratorWindow', exists=True ):
	mc.deleteUI( balloonGeneratorWindow, window=True );

def initializeBalloon(initRadius):
	mc.polySphere(sx = 12, sy = 8, n = "balloonTemp", r = initRadius)
	mc.rename( "polySphere1", "balloonTempHistory")
	mc.polySoftEdge( a = 180 )
	mc.lattice( n = 'balloon', cp = True, dv = (2, 4, 2), objectCentered = True,  ldv = (2, 3, 2), outsideLattice = True )
	mc.hide()
	mc.select('balloonTemp.vtx[84]', r=True)
	mc.ChamferVertex()
	mc.rename( "polyChamfer1", "tempChamfer" )
	mc.setAttr( 'tempChamfer.width', .1 )
	mc.delete( 'balloonTemp.f[72]' )
	return

def balloonAttributes():
	global minBalloonDrop, balloonDrop, balloonRadius, balloonQuantity
	balloonRadius = mc.floatSliderGrp(balloonRadiusInput, query=True, value=True)
	minBalloonDrop = mc.floatSliderGrp(minBalloonDropInput, query=True, value=True)
	balloonDrop = mc.floatSliderGrp(balloonDropInput, query=True, value=True)
	balloonQuantity = mc.intSliderGrp(balloonQuantityInput, query=True, value=True)

	adjustRadius(balloonRadius)
	adjustDrop(balloonDrop, balloonRadius)
	return

def adjustRadius(newRadius):
	d = newRadius * 2
	mc.setAttr( 'balloonTempHistory.radius', balloonRadius)
	mc.setAttr( 'balloonLattice.scale', d,d,d, type = "double3" )
	mc.setAttr( 'balloonBase.scale', d,d,d, type = "double3" )
	adjustDrop(balloonDrop, newRadius)
	return

def adjustDrop(newDrop, newRadius):
	global balloonDrop
	mc.softSelect(softSelectEnabled = False)
	mc.select( "balloonLattice.pt[0:1][0][0]", "balloonLattice.pt[0:1][0][1]", r = True ) 
	newDrop = (newDrop * newRadius)
	mc.move( (-1 * (newRadius + newDrop)), a = True, y = True)
	return

def setRandom():
	global balloonRandom
	balloonRandom = mc.checkBoxGrp(balloonRandomInput, query=True, value1=True)
	return

def finalizeBalloon():
	global minBalloonDrop, balloonDrop, balloonRadius, balloonQuantity, balloonRandom
	mc.delete('balloonTemp')
	for n in range(0, balloonQuantity):
		if balloonRandom == 1:
			randRad = random.uniform(.75, 1.25)
			r = randRad * balloonRadius
			d = random.uniform(minBalloonDrop, balloonDrop )
			print d
		else:
			r = balloonRadius	
			d = balloonDrop
		initializeBalloon(r)
		adjustDrop(d, r)
		tieOff()
		## add grid offset XYZ here
	closeWindow()

## def controlSelectName() here -- name of nCloth control
## def finalizeRibbon() here
## def createBaseGrid() here
## def connectBallons2Ribbons() here (by name)
## def connect Ribbons2Grid() here

def tieOff():
	global balloonRadius, balloonQuantity
	knotVals = mc.pointPosition('balloonTemp.vtx[96]', w=True)
	knotThickness = balloonRadius * .05
	endHeight = balloonRadius * .15
	knotRadius = knotVals[0]
	knotPos = ( knotVals[1] - (.5 * knotThickness))

	mc.polyCylinder( n="knotTemp", r=knotRadius, h=knotThickness, sx=12, sy=3, sz=0, rcp=0, cuv=3)
	mc.delete( 'knotTemp.f[36:37]')
	mc.setAttr( 'knotTemp.translateY', knotPos )
	mc.scale(1.25, 1.75, 1.25, 'knotTemp.vtx[12:35]', r=True )
	mc.lattice( n='knot', cp=True,  dv =(2, 2, 2), objectCentered=True, ldv=(2,2,2))
	mc.move( (.75 * knotThickness), 'knotLattice.pt[1][0][0:1]', r=True, y=True)
	mc.move( (.25 * knotThickness), 'knotLattice.pt[0][0][0:1]', r=True, y=True)

	mc.duplicate('knotTemp')
	mc.rotate(180, 'knotTemp1', z=True)

	mc.polyCone( n="endTemp", r=knotRadius*2, h=endHeight, sx=12, sy=6, sz=3, rcp=0, cuv=3)
	mc.delete( 'endTemp.f[60:83]', 'endTemp.f[96:107]')
	mc.setAttr( 'endTemp.translateY', knotPos - knotThickness/2 )	
	mc.scale( 1.15, 1, 1.15, 'endTemp.vtx[36:59]') 
	mc.move((.5 * endHeight), 'endTemp.vtx[0:11]', 'endTemp.vtx[72]', y=True, r=True)
	mc.polyUnite( 'balloonTemp', 'knotTemp', 'knotTemp1', 'endTemp', ch=True )
	mc.polySoftEdge( a = 180 )
	mc.polyMergeVertex( d=.001)

	mc.polyEditUV('polySurface1.map[0:126]', pu=0.5, pv=1, su=1, sv=0.575)
	mc.polyEditUV('polySurface1.map[127:230]', pu=0.5, pv=0.35, su=2, sv=.25)
	mc.polyEditUV('polySurface1.map[267:318]', u=0, v=-0.1, pu=0.5, pv=0, su=1, sv=.5)
	mc.polyEditUV('polySurface1.map[231:266]', 'polySurface1.map[319]', u=0, v=-.175, pu=0.5, pv=0.25, su=0.25, sv=0.25)
	mc.polyMergeUV('polySurface1.map[103:126]', d=0.5, ch=True )
	mc.polyEditUV('polySurface1.map[104]',  r=False, u=0)
	mc.polyEditUV('polySurface1.map[103]', r=False, u=1)
	mc.polySmooth('polySurface1',  mth=0, dv=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=0, suv=0, peh=0, sl=1, dpe=1, ps=0.1 , ro=1, ch=True)

	mc.DeleteHistory()
	mc.delete( 'knotTemp1')
	mc.rename('polySurface1', 'balloon1')
	mc.select(cl=True)
	return

def closeWindow():
	global balloonGeneratorWindow
	mc.deleteUI( balloonGeneratorWindow, window=True );
	mc.headsUpMessage( 'Here is your balloon!', verticalOffset = 50);




# Make a new window
balloonGeneratorWindow = mc.window( title="Balloon Generator", widthHeight=(400, 260), sizeable=False);

# Create a layout for the windows appearance
mc.columnLayout(adjustableColumn=True );

# Define the Balloon input fields
balloonRadiusInput = mc.floatSliderGrp( field=True, min=.1, max=10.0, value=balloonRadius, label="Balloon Radius", dragCommand='balloonAttributes()', changeCommand='balloonAttributes()' )
minBalloonDropInput = mc.floatSliderGrp( field=True, min=0.0, max=0.5, value=minBalloonDrop, pre=2, label=" Minimum Balloon Drop", dragCommand='balloonAttributes()', changeCommand='balloonAttributes()' )
balloonDropInput = mc.floatSliderGrp( field=True, min=0.0, max=0.5, value=balloonDrop, pre=2, label="Balloon Drop", dragCommand='balloonAttributes()', changeCommand='balloonAttributes()' )
balloonQuantityInput = mc.intSliderGrp( field=True, min=0, max=100, value=balloonQuantity, label="Balloon Quantity", changeCommand='balloonAttributes()')
balloonRandomInput = mc.checkBoxGrp( value1=False, label='Randomize Attributes', changeCommand='setRandom()')

mc.button( label='Create Balloon(s)', command='finalizeBalloon()', width=396 )
	
mc.setParent( '..' );

# Resize and display the window
mc.window(balloonGeneratorWindow, edit=True, widthHeight=(512, 260));
mc.showWindow( balloonGeneratorWindow );

initializeBalloon(balloonRadius);

