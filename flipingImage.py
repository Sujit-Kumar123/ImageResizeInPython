from PIL import Image
import easygui
inputPath = easygui.fileopenbox(title="Select input image file")
outputPathLeft = easygui.filesavebox(title="Select saved path")
outputPathBottom = easygui.filesavebox(title="Select saved path")
inputImage = Image.open(inputPath)
inputImage.transpose(Image.FLIP_LEFT_RIGHT).save(outputPathLeft)
inputImage.transpose(Image.FLIP_TOP_BOTTOM).save(outputPathBottom)
