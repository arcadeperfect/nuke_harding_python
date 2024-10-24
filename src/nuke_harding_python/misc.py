import nuke

def hide_viewer_lines():
    for n in nuke.allNodes("Viewer"):
        n['hide_input'].setValue(True)
