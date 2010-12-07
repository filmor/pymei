from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class barre_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"barre", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chorddef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chorddef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chordmember_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chordmember", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chordtable_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chordtable", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class harm_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"harm", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

