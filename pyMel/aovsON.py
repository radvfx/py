#!/usr/bin/python
# set the AOVs needed
import maya.cmds as mc
import maya.mel as mm


## set all of the AOVs needed, starting with std MPC order
def makeAOVs():
        mc.setAttr( 'fb_setup1.pass[0].name', "primary", type= "string" )
        mc.setAttr( 'fb_setup1.pass[0].type', "rgba_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[0].format' , "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[0].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[1].name', "color", type= "string" )
        mc.setAttr( 'fb_setup1.pass[1].type', "rgba_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[1].format' , "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[1].enable', 0 )

	mc.setAttr( 'fb_setup1.pass[2].name', "diffuse", type="string" )
        mc.setAttr( 'fb_setup1.pass[2].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[2].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[2].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[3].name', "specular", type="string" )
        mc.setAttr( 'fb_setup1.pass[3].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[3].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[3].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[4].name', "reflection", type="string" )
        mc.setAttr( 'fb_setup1.pass[4].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[4].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[4].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[5].name', "refraction", type="string" )
        mc.setAttr( 'fb_setup1.pass[5].type', "rgb_fp", type="string")
        mc.setAttr( 'fb_setup1.pass[5].format', "exr", type="string")
        mc.setAttr( 'fb_setup1.pass[5].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[6].name', "indirect", type="string" )
        mc.setAttr( 'fb_setup1.pass[6].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[6].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[6].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[7].name', "incandescence", type="string" )
        mc.setAttr( 'fb_setup1.pass[7].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[7].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[7].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[8].name', "additional", type="string")
        mc.setAttr( 'fb_setup1.pass[8].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[8].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[8].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[9].name', "occlusion", type="string")
        mc.setAttr( 'fb_setup1.pass[9].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[9].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[9].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[10].name', "shadow", type="string" )
        mc.setAttr( 'fb_setup1.pass[10].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[10].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[10].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[11].name', "rgb_shadow", type="string" )
        mc.setAttr( 'fb_setup1.pass[11].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[11].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[11].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[12].name', "scatter", type="string" )
        mc.setAttr( 'fb_setup1.pass[12].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[12].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[12].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[13].name', "ambient", type="string" )
        mc.setAttr( 'fb_setup1.pass[13].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[13].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[13].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[14].name', "ID", type="string" )
        mc.setAttr( 'fb_setup1.pass[14].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[14].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[14].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[15].name', "ID2", type="string" )
        mc.setAttr( 'fb_setup1.pass[15].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[15].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[15].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[16].name', "ID3", type="string" )
        mc.setAttr( 'fb_setup1.pass[16].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[16].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[16].enable', 0 )

        mc.setAttr( 'fb_setup1.pass[17].name', "depth", type="string" )
        mc.setAttr( 'fb_setup1.pass[17].type', "m", type="string" )
        mc.setAttr( 'fb_setup1.pass[17].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[17].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[18].name', "motion", type="string" )
        mc.setAttr( 'fb_setup1.pass[18].type', "n", type="string")
        mc.setAttr( 'fb_setup1.pass[18].format', "exr", type="string")
        mc.setAttr( 'fb_setup1.pass[18].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[19].name', "normal", type="string" )
        mc.setAttr( 'fb_setup1.pass[19].type', "n", type="string")
        mc.setAttr( 'fb_setup1.pass[19].format', "exr", type="string")
        mc.setAttr( 'fb_setup1.pass[19].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[20].name', "position", type="string" )
        mc.setAttr( 'fb_setup1.pass[20].type', "n", type="string")
        mc.setAttr( 'fb_setup1.pass[20].format', "exr", type="string")
        mc.setAttr( 'fb_setup1.pass[20].enable', 1 )

	## standard AOVs end here
	## optional AOVs start below

        mc.setAttr( 'fb_setup1.pass[22].name', "softFaceMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[22].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[22].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[22].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[23].name', "softNoseMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[23].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[23].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[23].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[24].name', "softLipsMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[24].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[24].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[24].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[25].name', "softLeftEyeMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[25].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[25].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[25].enable', 1 )

        mc.setAttr( 'fb_setup1.pass[26].name', "softRightEyeMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[26].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[26].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[26].enable', 1 )
        
	mc.setAttr( 'fb_setup1.pass[27].name', "softHalfFaceMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[27].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[27].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[27].enable', 1 )
	
	mc.setAttr( 'fb_setup1.pass[28].name', "softBrowMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[28].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[28].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[28].enable', 1 )
	
	mc.setAttr( 'fb_setup1.pass[29].name', "softTopHeadMatte", type="string" )
        mc.setAttr( 'fb_setup1.pass[29].type', "rgb_fp", type="string" )
        mc.setAttr( 'fb_setup1.pass[29].format', "exr", type="string" )
        mc.setAttr( 'fb_setup1.pass[29].enable', 1 )
	
	
	mc.setAttr ( "miDefaultOptions.rayTracing" , 1 )
	mc.setAttr ( "miDefaultOptions.minSamples" , 0 )
	mc.setAttr ( "miDefaultOptions.maxSamples" , 2 )
	mc.setAttr ( "miDefaultOptions.filter" , 3 )
	mc.setAttr ( "miDefaultOptions.jitter" , 1 )
	mc.setAttr ( "miDefaultOptions.sampleLock" , 0 )
	mc.setAttr ( "miDefaultOptions.maxRayDepth" , 5 )
	mc.setAttr ( "miDefaultOptions.maxReflectionRays" , 10 )
	mc.setAttr ( "miDefaultOptions.maxRefractionRays" , 10 )
	mc.setAttr ( "miDefaultOptions.maxRayDepth" , 20 )
	mc.setAttr ( "miDefaultOptions.maxShadowRayDepth" , 10 )
	mc.setAttr ( "miDefaultOptions.maxReflectionBlur" , 5 )
	mc.setAttr ( "miDefaultOptions.maxRefractionBlur" , 5 )
	
	mc.setAttr ( "miDefaultOptions.finalGather" , 1 )
	mc.setAttr ( "miDefaultOptions.finalGatherRays" , 300 )
	mc.setAttr ( "miDefaultOptions.finalGatherMaxRadius" , 100 )
	mc.setAttr ( "miDefaultOptions.finalGatherMinRadius" , 10 )
	mc.setAttr ( "miDefaultOptions.finalGatherFilter" , 1 )
	mc.setAttr ( "miDefaultOptions.finalGatherTraceDiffuse" , 1 )
	mc.setAttr ( "miDefaultOptions.finalGatherTraceReflection" , 2 )
	mc.setAttr ( "miDefaultOptions.finalGatherTraceRefraction" , 2 )
	mc.setAttr ( "miDefaultOptions.finalGatherTraceDepth" , 4 )

	closeWindow()

def closeWindow():
        global aovONWindow
        mc.deleteUI( aovONWindow, window=True );
        mc.headsUpMessage( 'all Honda AOVs are ON.', verticalOffset = 50 );

## Make a new window
aovONWindow = mc.window( title="aovOnWindow", widthHeight=(400,260), sizeable=False );

## Create a layout for the window appearance
mc.columnLayout( adjustableColumn=True );
mc.button( label='MakeAOVs', command='makeAOVs()', width=396 )
mc.setParent( '..' );

## Resize and display the window
mc.window( aovONWindow, edit=True, widthHeight=(512,260));
mc.showWindow( aovONWindow );
