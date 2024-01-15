#pip install easygui
#pip install rembg
import easygui
from rembg import remove
from PIL import Image
inputPath=easygui.fileopenbox(title="Select input image file")
outputPath=easygui.filesavebox(title="Select saved path")
inpt=Image.open(inputPath)
outpr=remove(inpt)
outpr.save(outputPath)