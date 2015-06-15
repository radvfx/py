#!/usr/bin/python
# set the AOVs needed
import maya.cmds as mc
import maya.mel as mm


## set all of the AOVs needed, starting with std MPC order
setAttr -type "string" fb_setup1.pass[0].name "primary";
setAttr -type "string" fb_setup1.pass[0].type "rgba_fp";
setAttr -type "string" fb_setup1.pass[0].format "exr";
setAttr "fb_setup1.pass[0].enable" 1; 

setAttr -type "string" fb_setup1.pass[1].name "color";
setAttr -type "string" fb_setup1.pass[1].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[1].format "exr";
setAttr "fb_setup1.pass[1].enable" 1; 

setAttr -type "string" fb_setup1.pass[2].name "diffuse";
setAttr -type "string" fb_setup1.pass[2].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[2].format "exr";
setAttr "fb_setup1.pass[2].enable" 1; 

setAttr -type "string" fb_setup1.pass[3].name "specular";
setAttr -type "string" fb_setup1.pass[3].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[3].format "exr";
setAttr "fb_setup1.pass[3].enable" 1; 

setAttr -type "string" fb_setup1.pass[3].name "reflection";
setAttr -type "string" fb_setup1.pass[3].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[3].format "exr";
setAttr "fb_setup1.pass[3].enable" 1; 

setAttr -type "string" fb_setup1.pass[4].name "refraction";
setAttr -type "string" fb_setup1.pass[4].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[4].format "exr";
setAttr "fb_setup1.pass[4].enable" 0; 

setAttr -type "string" fb_setup1.pass[5].name "indirect";
setAttr -type "string" fb_setup1.pass[5].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[5].format "exr";
setAttr "fb_setup1.pass[5].enable" 1; 

setAttr -type "string" fb_setup1.pass[6].name "incandescence";
setAttr -type "string" fb_setup1.pass[6].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[6].format "exr";
setAttr "fb_setup1.pass[6].enable" 0; 

setAttr -type "string" fb_setup1.pass[7].name "additional";
setAttr -type "string" fb_setup1.pass[7].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[7].format "exr";
setAttr "fb_setup1.pass[7].enable" 0; 

setAttr -type "string" fb_setup1.pass[8].name "occlusion";
setAttr -type "string" fb_setup1.pass[8].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[8].format "exr";
setAttr "fb_setup1.pass[8].enable" 1; 

setAttr -type "string" fb_setup1.pass[9].name "shadow";
setAttr -type "string" fb_setup1.pass[9].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[9].format "exr";
setAttr "fb_setup1.pass[9].enable" 0; 

setAttr -type "string" fb_setup1.pass[10].name "rgb_shadow";
setAttr -type "string" fb_setup1.pass[10].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[10].format "exr";
setAttr "fb_setup1.pass[10].enable" 1; 

setAttr -type "string" fb_setup1.pass[11].name "scatter";
setAttr -type "string" fb_setup1.pass[11].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[11].format "exr";
setAttr "fb_setup1.pass[11].enable" 0; 

setAttr -type "string" fb_setup1.pass[12].name "ambient";
setAttr -type "string" fb_setup1.pass[12].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[12].format "exr";
setAttr "fb_setup1.pass[12].enable" 0; 

setAttr -type "string" fb_setup1.pass[13].name "ID";
setAttr -type "string" fb_setup1.pass[13].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[13].format "exr";
setAttr "fb_setup1.pass[13].enable" 1; 

setAttr -type "string" fb_setup1.pass[14].name "ID2";
setAttr -type "string" fb_setup1.pass[14].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[14].format "exr";
setAttr "fb_setup1.pass[14].enable" 1; 

setAttr -type "string" fb_setup1.pass[15].name "ID3";
setAttr -type "string" fb_setup1.pass[15].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[15].format "exr";
setAttr "fb_setup1.pass[15].enable" 1; 

setAttr -type "string" fb_setup1.pass[16].name "depth";
setAttr -type "string" fb_setup1.pass[16].type "n";
setAttr -type "string" fb_setup1.pass[16].format "exr";
setAttr "fb_setup1.pass[16].enable" 1; 

setAttr -type "string" fb_setup1.pass[17].name "motion";
setAttr -type "string" fb_setup1.pass[17].type "m";
setAttr -type "string" fb_setup1.pass[17].format "exr";
setAttr "fb_setup1.pass[17].enable" 1; 

setAttr -type "string" fb_setup1.pass[18].name "normal";
setAttr -type "string" fb_setup1.pass[18].type "n";
setAttr -type "string" fb_setup1.pass[18].format "exr";
setAttr "fb_setup1.pass[18].enable" 1; 

setAttr -type "string" fb_setup1.pass[19].name "position";
setAttr -type "string" fb_setup1.pass[19].type "n";
setAttr -type "string" fb_setup1.pass[19].format "exr";
setAttr "fb_setup1.pass[19].enable" 1; 

setAttr -type "string" fb_setup1.pass[20].name "ID4";
setAttr -type "string" fb_setup1.pass[20].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[20].format "exr";
setAttr "fb_setup1.pass[20].enable" 1; 

setAttr -type "string" fb_setup1.pass[21].name "ID5";
setAttr -type "string" fb_setup1.pass[21].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[21].format "exr";
setAttr "fb_setup1.pass[21].enable" 1; 

setAttr -type "string" fb_setup1.pass[22].name "ID6";
setAttr -type "string" fb_setup1.pass[22].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[22].format "exr";
setAttr "fb_setup1.pass[22].enable" 1; 

setAttr -type "string" fb_setup1.pass[23].name "ID7";
setAttr -type "string" fb_setup1.pass[23].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[23].format "exr";
setAttr "fb_setup1.pass[23].enable" 1; 

setAttr -type "string" fb_setup1.pass[24].name "crackMatte";
setAttr -type "string" fb_setup1.pass[24].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[24].format "exr";
setAttr "fb_setup1.pass[24].enable" 1; 

setAttr -type "string" fb_setup1.pass[25].name "rainStreakMatte";
setAttr -type "string" fb_setup1.pass[25].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[25].format "exr";
setAttr "fb_setup1.pass[25].enable" 1; 

setAttr -type "string" fb_setup1.pass[26].name "paintOverMatte";
setAttr -type "string" fb_setup1.pass[26].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[26].format "exr";
setAttr "fb_setup1.pass[26].enable" 1; 

setAttr -type "string" fb_setup1.pass[27].name "dirtMatte";
setAttr -type "string" fb_setup1.pass[27].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[27].format "exr";
setAttr "fb_setup1.pass[27].enable" 1; 

setAttr -type "string" fb_setup1.pass[28].name "rampMatte";
setAttr -type "string" fb_setup1.pass[28].type "rgb_fp";
setAttr -type "string" fb_setup1.pass[28].format "exr";
setAttr "fb_setup1.pass[28].enable" 1; 
