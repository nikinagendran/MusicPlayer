import sys # module in the system---it will allow to us emany things on the system 

from PyQt6.QtWidgets import * #telling file to go to the folder.subfolder + * means a wild card and it imports everything from the PyQt6 widgets 

# TO CREATE A WINDOW  
# # capital letter followed by a parantehses is a constructor and not a method(method is a camelcase + has lower case letters) 
app = QApplication(sys.argv) # just starts the app(nothing to do with the visual component)
window = QMainWindow() #to make the window visual
window.show() # to actually to see the window--shows the window of the app(method--it worksupon/changes the window object)
sys.exit(app.exec()) # actually actually shows the window...makes sure that it stays open 





