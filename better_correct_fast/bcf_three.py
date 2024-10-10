# better_correct_fast/bcf_three.py
# -*- coding: utf-8 -*-

# A wrapper for the undocumented IfcOpenShell wrapper
# https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bcf/bcf/v3/bcfxml.py

# TODO does not work with snapshot yet

import bcf.v3.bcfxml as BCF # type: ignore # TODO concider better alias

def create(): # TODO come up with a better alias
    bcf = BCF.BcfXml() # TODO might this bcf and new_bcf not be double?
    new_bcf = bcf.create_new("LKJDLFJ") # TODO set input for a project name

    # Get topic # TODO do this in another def
    new_topic = new_bcf.add_topic(
        title="New Topic Title",
        description="This is a description of the new topic.",
        author="John Doe", # This might be redundant
        topic_type="Issue", # This might be redundant
        topic_status="Open" # This might be redundant
    )

    return new_bcf

def save(bcf): # TODO add a filename as an input
    bcf.save("test.bcf")
    # TODO add user output