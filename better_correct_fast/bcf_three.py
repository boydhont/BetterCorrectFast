# better_correct_fast/bcf_three.py
# -*- coding: utf-8 -*-

# A wrapper for the undocumented IfcOpenShell wrapper
# https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bcf/bcf/v3/bcfxml.py

# TODO does not work with snapshot yet. Snapshots are part of the viewport element with the name "snapshot.jpg". It will be included in the archive under the folder named after top_guid. It is supposed to be saved in the ViewPoint, under "Snapshot", then the text as "snapshot.jpg"
# TODO delete this icon.png later on

import uuid

import bcf.v3.bcfxml as BCF # type: ignore
import bcf.v3.topic as TOPIC # type: ignore
import bcf.v3.visinfo as VIS # type:ignore
import bcf.v3.model as MDL # type: ignore

from pathlib import Path

def create(title="BetterCorrectFast: Check this out!", description="Automatically generated topic by BetterCorrectFast", project_name=""): # TODO come up with a better alias # TODO come up with better placeholder values
    
    # Create the elements
    bcf = BCF.BcfXml().create_new(project_name)
    topic = _get_topic(title, description)
    
    # Add the elements
    bcf.topics[topic.guid] = topic

    return bcf

def _get_topic(title, description, author="BetterCorrectFast", topic_type="Issue", topic_status="Open"): # TODO come up with better placeholder values

    # Create the elements
    topic = TOPIC.TopicHandler().create_new(
        title=title,
        description=description,
        author=author,
        topic_type=topic_type,
        topic_status=topic_status
    )

    viewpoint = _get_viewpoint() # TODO add user input for the picture
    
    # Add the elements
    topic.add_visinfo_handler(viewpoint) # TODO make the filename dynamic # TODO just type the stuf that is in there
 
    return topic

def _get_viewpoint(): # A Viewpoint is called VisualizationInfoHandler in IfcOpenShell for some reason
    # TODO get the snapshot etc
    # Create elements
    
    visualization_info = _get_visualization_info()
    
    viewpoint = VIS.VisualizationInfoHandler(visualization_info) # TODO add the snapshot?
    # TODO add the visualizationinfo and add it to the viewpoint
    
    return viewpoint

def _get_visualization_info(): # TODO add the bitmaps dynamically
    
    # Create elements
    snapshot_filepath = _get_default_snapshot_path()# TODO do dynamic over input variable
    # TODO add checks for the file format
    bitmap = _get_bitmap_from_filepath(snapshot_filepath) 
    
    visualization_info = MDL.VisualizationInfo(
        guid=str(uuid.uuid4()),  # Generate a random GUID
        bitmaps = MDL.VisualizationInfoBitmaps(bitmap=[bitmap]) # The VisualizationInfoBitmaps is just some controlled array that hold multiple bitmaps
    )
    
    return visualization_info

def _get_bitmap_from_filepath(filepath): # TODO add support for more filetypes than .jpg
    
    bitmap = MDL.Bitmap(
        format=MDL.BitmapFormat.JPG,
        reference=filepath,
        location=MDL.Point(x=0.0, y=0.0, z=0.0),  # Set your actual location here
        normal=MDL.Direction(x=0.0, y=0.0, z=1.0),  # Set your actual normal here
        up=MDL.Direction(x=0.0, y=1.0, z=0.0),  # Set your actual up vector here
        height=1080.0,  # TODO Set your actual height here
    )
    
    return bitmap

def _get_default_snapshot_path(): # TODO change to icon
    
    current_file = Path(__file__).resolve()
    snapshot_path = current_file.parent / 'assets' / 'snapshot.jpg'

    print(f"The default snapshot file is being used {'and is located' if snapshot_path.exists() else ', but was not found'} at: {snapshot_path}") # User feedback
    
    return str(snapshot_path)

def save(bcf, filename):
    bcf.save(filename)
    # TODO add user output