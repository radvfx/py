#!/usr/bin/python
## make the base plane
import maya.cmds as mc
import maya.mel as mm

## Check if window exists
if mc.window( 'addWindWindow', exists=True):
	mc.deleteUI( addWindWindow, window=True);

## Do it
def addWind():
	mm.eval( "air -pos -12 28.5 0 -name \"bAir\" -m 10 -att 1 -dx 1 -dy 0.1 -dz 0 -s 0.5 -iv 0 -iro 1 -vco 0 -es 0 -mxd 20 -vsh none -vex 0 -vof 0 0 0 -vsw 360 -tsr 0.5;" )
	mc.setAttr( 'bAir.useMaxDistance', 0 )
	mc.select( 'balloon1' )
        mm.eval( "connectDynamic -f bAir balloonNCloth" )
	mc.select( 'ribbonTemp' )
        mm.eval( "connectDynamic -f bAir ribbonNCloth" )
	mc.select( 'ribbonBit' )
        mm.eval( "connectDynamic -f bAir ribbonBitNCloth" )
	closeWindow()

## close the window when you're done
def closeWindow():
	global addWindWindow
	mc.deleteUI( addWindWindow, window=True );
	mc.headsUpMessage( 'The Air is added', verticalOffset = 50 );

## Make a new window
addWindWindow = mc.window( title="addWindWindow", widthHeight=(400,260), sizeable=False );

## Create a layout for the window appearance
mc.columnLayout(adjustableColumn=True );
mc.button( label='Add Wind', command='addWind()', width=396 )
mc.setParent( '..' );

## Resize and display the window
mc.window(addWindWindow, edit=True, widthHeight=(512,260));
mc.showWindow( addWindWindow );
