#Katie Proctor
#11/16/2019
#Purpose: Homework 8 Redo - Batch Reprojection Tool

#import necessary modules and site packages, and set environment
import arcpy
from arcpy import env
env.workspace = r"G:\ADVGIS_GIS\AVDGIS_GIS.gdb"
env.overwriteOutput = True

#assigning parameter variables for project tool
inPath = arcpy.GetParameterAsText(0)
outPath = arcpy.GetParameterAsText(1)
targetFC = arcpy.GetParameterAsText(2)

#determine variables for target projection dataset
target_desc = arcpy.Describe(targetFC)
target_spRef = target_desc.spatialReference
target_csName = target_desc.spatialReference.name

#change workspace to list feature classes
env.workspace = inPath
env.overwriteOutput = True
fcList = arcpy.ListFeatureClasses()

#loop through list of feature classes in workspace
for fc in fcList:
    #determine variables for each fc in fcList
    desc = arcpy.Describe(fc)
    spRef = desc.spatialReference
    csName = desc.spatialReference.name
    if csName != target_csName: #if spatial reference name for target and fc do not match, fc will be reprojected
        if inPath.endswith(".gdb") and outPath.endswith(".gdb"): #rootnames are not changed
            arcpy.management.Project(fc, outPath + "/" + fc + "_projected", target_spRef)
        if inPath.endswith(".gdb"): #outpath is a folder, so .shp is added to output name
            arcpy.management.Project(fc, outPath + "/" + fc + "_projected.shp", target_spRef)
        if outPath.endswith(".gdb"): #input is folder so output name is missing last four characters
            arcpy.management.Project(fc, outPath + "/" + fc[:-4] + "_projected", target_spRef)
        else: #both input and output are folders so output name is missing .shp and .shp is added to end of output name
            arcpy.management.Project(fc, outPath + "/" + fc[:-4] + "_projected.shp", target_spRef)
