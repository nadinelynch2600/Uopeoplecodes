import FreeCAD as App

class MyViewObject():
    def __init__(self, viewObj):
        viewObj.Proxy = self
    def getIcon(self):
        return """
            /* XPM */
            static char * rocket_xpm[] = {
            "16 16 43 1",
            " 	c None",
            ".	c #516EB2",
            "+	c #5D79BE",
            "@	c #9BB4FF",
            "#	c #4361A4",
            "$	c #FFFFFF",
            "%	c #ECEDED",
            "&	c #D5D5D5",
            "*	c #C3C3C3",
            "=	c #ACACAC",
            "-	c #E7E6E6",
            ";	c #CFCFCF",
            ">	c #BDBDBE",
            ",	c #A6A7A7",
            "'	c #F9F9F9",
            ")	c #E1E1E1",
            "!	c #C9C8C9",
            "~	c #B7B8B7",
            "{	c #A1A1A0",
            "]	c #F3F3F3",
            "^	c #DADBDB",
            "/	c #C3C4C3",
            "(	c #B2B2B2",
            "_	c #9B9C9B",
            ":	c #EDECED",
            "<	c #D5D5D4",
            "[	c #969595",
            "}	c #E6E7E6",
            "|	c #CECFCE",
            "1	c #BDBDBD",
            "2	c #A6A6A6",
            "3	c #909090",
            "4	c #4C5C8A",
            "5	c #FF0000",
            "6	c #333F62",
            "7	c #FF1F00",
            "8	c #FF7600",
            "9	c #A9A9A9",
            "0	c #FFB200",
            "a	c #B4B4B4",
            "b	c #FFD600",
            "c	c #C7C7C7",
            "d	c #BBBBBB",
            "                ",
            "                ",
            "        .       ",
            "       +..      ",
            "      @..#.     ",
            "      $%&*=     ",
            "      $-;>,     ",
            "      ')!~{     ",
            "      ]^/(_     ",
            "      :<*=[     ",
            "      }|123     ",
            "       456      ",
            "      47876     ",
            "       909      ",
            "       aba      ",
            "      cacdc     "};
         """

class MyClass():
    def __init__(self, name):
        self.Type = 'MyClass'
        # See https://forum.freecadweb.org/viewtopic.php?t=11897 for an alternative using Part::FeaturePython, which has all the things necessary for drawing a shape by default.
        # If you're just positioning sub-elements, an App::DocumentObjectGroupPython provides the folder behaviour by default with its .Group and should be enough.
        obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", name)
        MyViewObject(obj.ViewObject)
        # Use App::PropertySubLink and App::PropertySubLinkList to select specific faces for attachment
        obj.addProperty('App::PropertyLink', 'NoseCone', 'Rocket', 'Nose cone')
        obj.addProperty('App::PropertyLink', 'BodyTube', 'Rocket', 'Body tube')
        obj.addProperty('App::PropertyLinkList', 'Fins', 'Rocket', 'List of objects to attach as fins')
        obj.addProperty('App::PropertyLink', 'Exhaust', 'Rocket', 'Hot stuff')
        obj.Proxy = self
    def execute(self, obj):
        # Check if we can proceed
        if (obj.NoseCone is None) or (obj.BodyTube is None) or (obj.Fins is None) or (obj.Exhaust is None):
            raise Exception("Missing parameter, all parts of the rocket must be defined or it won't fly")

        # Remove elements from the folder
        while len(obj.Group) > 0:
            o = obj.Group[-1]
            obj.removeObject(o)
            # If the object was generated on the fly by a previous execute() run, use this to discard it from the document
            #App.ActiveDocument.removeObject(o.Name)

        # Add elements in chosen order, so that they are visually displayed under the folder in the tree
        obj.addObject(obj.NoseCone)
        obj.addObject(obj.BodyTube)
        for fin in obj.Fins:
            obj.addObject(fin)
        obj.addObject(obj.Exhaust)

        print('Do stuff here to position the objects as desired, for example create an Assembly object and put some constraints.')

# Hack from https://forum.freecadweb.org/viewtopic.php?f=22&t=54481
if __name__ == '__main__':
    Gui.doCommand("import MyTest")
    Gui.doCommand("MyTest.MyClass('Rocket')")
