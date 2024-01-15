from PIL import Image
import easygui
inputPath=easygui.fileopenbox(title="Select input image file")
outputPath=easygui.filesavebox(title="Select saved path")
inputImage=Image.open(inputPath)
width, height=inputImage.size
print(width,height)
resizedImage=inputImage.resize((int(width/2),int(height/2)))
print(resizedImage.size)
resizedImage.save(outputPath)