import os
import numpy
from PIL import Image
allfiles=os.listdir(os.getcwd())
img_list=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]
w,h=Image.open(img_list[0]).size
total_length = len(img_list)
sample_size = 50
number_of_runs = total_length - sample_size
for k in range(number_of_runs):
    arr=numpy.zeros((h,w,3),numpy.float)
    img_sublist = img_list[k:k+sample_size]
    for im in img_sublist:
        im_array = numpy.array(Image.open(im), dtype = numpy.float)
        arr = arr+ im_array/sample_size
    arr = numpy.array(numpy.round(arr), dtype = numpy.uint8)
    out = Image.fromarray(arr, mode = "RGB")
    out.save("averaged" + str(k) + ".png")



# # Create a numpy array of floats to store the average (assume RGB images)
# arr=numpy.zeros((h,w,3),numpy.float)
#
# # Build up average pixel intensities, casting each image as an array of floats
# for im in imlist:
#     imarr=numpy.array(Image.open(im),dtype=numpy.float)
#     arr=arr+imarr/N
#
# # Round values in array and cast as 8-bit integer
# arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
#
# # Generate, save and preview final image
# out=Image.fromarray(arr,mode="RGB")
# out.save("Average.png")
# out.show()



# for k in range(number_of_runs):
#     for i in range(k, k+sample_size):
#         print(sum(dummyList[k:k+sample_size]))
