import c4d
import random
from c4d import gui

def main():

    obj1 = doc.SearchObject("Cube"); 
    #Where Cube is made editable, Type: c4d.PolygonObject
    
    #For each point on "Cube"
    for x in range(obj1.GetPointCount()):
        
        #Set that point with itself minus a random number from 0 to 10
        #__sub__() is defined to subtract from all components
        #on the c4d.Vector.
        obj1.SetPoint(x,(obj1.GetPoint(x)- random.random()*10 ));
        

    #Update OpenGL Viewport
    obj1.Message(c4d.MSG_UPDATE)
    c4d.EventAdd()
    
if __name__=='__main__':
    main()

#SEE SCREENSHOTS IN POINTLEVELMANIPULATION FOLDER
