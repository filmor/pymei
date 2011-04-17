# A set of helpers that construct a basic MeiDocument framework, including all
# of the required elements.
import logging
lg = logging.getLogger('pymei')

from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod

def create(docname):
    doc = MeiDocument.MeiDocument(docname)
    
    # set up the header
    root_el = mod.mei_()
    mei_head = mod.meihead_()
    file_desc = mod.filedesc_()
    title_stmt = mod.titlestmt_()
    title = mod.title_()
    title_stmt.add_children([title])
    
    encoding_desc = mod.encodingdesc_()
    proj_desc = mod.projectdesc_()
    dsc = mod.p_()
    dsc.value = u"This file was generated by PyMEI 1.0"
    proj_desc.addchildren([dsc])
    
    file_desc.add_children([title_stmt])
    encoding_desc.add_children([proj_desc])
    
    mei_head.add_children([file_desc, encoding_desc])
    
    # set up the body
    music = mod.music_()
    bd = mod.body_()
    md = mod.mdiv_()
    sc = mod.score_()
    
    md.add_children([sc])
    bd.add_children([md])
    music.add_children([bd])
    
    root_el.addchildren([mei_head, music])
    doc.addelement(root_el)
    
    
    
    return doc