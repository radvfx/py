#!/usr/bin/python
## make the base plane
import maya.cmds as mc
import maya.mel as mm

## Check if window exists
if mc.window( 'addGravityWindow', exists=True):
	mc.deleteUI( addGravityWindow, window=True);

## Do it
def addGravity():
	mm.eval( "gravity -pos 0 0 0 -name\"bGrav\" -m 10 -att 0 -dx 0 -dy 1 -dz 0 -mxd -1 -vsh none -vex 0 -vof 0 0 0 -vsw 360 -tsr 0.5;" )
	mc.select( 'balloon1' )
        mm.eval( "connectDynamic -f bGrav balloonNCloth" )
	## mc.select( 'ribbonTemp' )
        ## mm.eval( "connectDynamic -f bGrav ribbonNCloth" )
	closeWindow()

## close the window when you're done
def closeWindow():
	global addGravityWindow
	mc.deleteUI( addGravityWindow, window=True );
	mc.headsUpMessage( 'The base  is done', verticalOffset = 50 );

## Make a new window
addGravityWindow = mc.window( title="addGravityWindow", widthHeight=(400,260), sizeable=False );

## Create a layout for the window appearance
mc.columnLayout(adjustableColumn=True );
mc.button( label='Add Gravity', command='addGravity()', width=396 )
mc.setParent( '..' );

## Resize and display the window
mc.window(addGravityWindow, edit=True, widthHeight=(512,260));
mc.showWindow( addGravityWindow );
