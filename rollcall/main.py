"""
Main module
"""

import os
import func_json as fj
import exceptions as exc
from datetime import date


def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def fileExists(fName):
    """
    Check if a file exists
    """
    if os.path.isfile(fName):
        return True
    return False

def add(json_str, sub, dire=pDir()):
    """
    Add a subject
    creates a new sub.json file
    """
    path = os.path.join(dire, sub + '.json')
    if fileExists(path):
        raise exc.SubjectExists("Records for this subject are already present")

    with open(path, "w") as recordFile:
        recordFile.write(json_str)

def fileDelete(fName):
    """
    Delete a file and return status
    """
    if fileExists(fName):
        os.remove(fName)
        return True
    return False

def delete(sub):
    """
    Delete a subject
    """
    if fileDelete(sub + '.json'):
        return True
    return False

def update(sub, tag, date=date.today()):
    """
    Update a subject
    """
    filename = sub + '.json'
    if not fileExists(filename):
        raise exc.SubjectError("Subject does not exit")

    if tag not in fj.TAGS.keys():
        raise exc.UnknownTag("Tag UNKNOWN")

    with open(filename, "r") as recordFile:
        json_string = recordFile.read()

    newdata = fj.update_json_string(json_string, date, fj.TAGS[tag])
    with open(filename, "w") as recordFile:
        recordFile.write(newdata)
    return True

def display_names(dire=pDir()):
    """
    yields all subject name
    """
    for filename in os.listdir(dire):
        name, ext = os.path.splitext(fName)
        if ext == '.json':
            yield filename


def display_subject():
    """
    displays a particular subject
    """
    pass

def display_all_subjects():
    """
    displays all the subjects
    preferably a generator
    """
    pass

def reset():
    """
    Reset subjects data
    """
    pass
