# BG3_VFX_Recompiler_Scripts
These Scripts are made to fully Edit lsfx.lsx in various ways (Change Colours, Rescale etc.)

Overview
The VFX_Color_Changer_by_Shivero package contains a collection of Python scripts designed for modifying colors and rescaling visual effects in files, likely targeting XML structures. These scripts are useful for artists, animators, or developers working with visual effects (VFX) who need to quickly adjust colors or sizes of their assets.

Scripts and Their Usage:

Recoloring:

The Scripts are setup to target lsfx.lsx Files.

1. The Target File and the Script need to be in the same Directory.

2. To understand how the Scripts work i named them the same Style! The Scripts evaluate what theyre facing by the Filename of the Targetfile.

For Example if you have a File VFX_EFFECT_CAST_DAMAGE_LIGHTNING_HANDKEY_01.lsfx.lsx THE Script WILL DONT DO ANYTHING

3. If you have the Script Named VFX_EFFECT_CAST_DAMAGE_LIGHTNING_BLUE_HANDKEY_01.lsfx.lsx and you execute the Blueto4Convert, the script know by the "Blue" in the Filename what it has and what it needs to do. Then Your Files will be converted into 4 other Colors.
4. The Script will automatically generate new Files with their corresponding Color in the Name
![image](https://github.com/ShiveroCodes/BG3_VFX_Recompiler_Scripts/assets/113947317/05cea041-e475-4ad4-945f-91dd3260dcfd)

So to clear up again Blueto4Convert Files with Blue in its Name, while Yellowto4Convert targets Files with Yellow in the name


Rescaling is Basically the same thing.

If you have a VFX file with 4m in the name it will scale it up by 1.5 Steps (Can be all defined inside the scripts) and spit out 6m 8m 10m and 12m Files.


