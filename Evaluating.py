from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt 
from tensorflow.keras.preprocessing.image import array_to_img,img_to_array,ImageDataGenerator,load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from matplotlib.image import imread


image_data_gen = ImageDataGenerator(rotation_range=20,
                                    height_shift_range=0.2,
                                    width_shift_range=0.2,
                                    shear_range = 0.15,
                                    horizontal_flip = True,
                                    zoom_range =0.15,
                                    fill_mode = 'nearest',
                                    rescale = 1.0/255)
train_dir = '.\\train\\'
train_image_gen = image_data_gen.flow_from_directory(train_dir,target_size = (150,150),batch_size = 10)
test_dir = '.\\test\\'
test_image_gen = image_data_gen.flow_from_directory(test_dir,batch_size=10,target_size = (150,150))

model = load_model('mask_detect.h5')
dir = input("Please give me a image path: ")
test_image = imread(dir)
plt.imshow(test_image)
test_image = image.load_img(dir, target_size=(150, 150))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = model.predict(test_image)
s = train_image_gen.class_indices
a = result.argmax()
name = []
for i in s:
    name.append(i)
for i in range(len(s)):
    if(i == a):
        q = name[i]
plt.title(q)
plt.show()