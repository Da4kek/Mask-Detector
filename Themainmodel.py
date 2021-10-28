import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Sequential, Conv2D, MaxPool2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping


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

learning_rate = 0.0001
epochs = 20

model = Sequential()
model.add(Conv2D(filters = 32,kernel_size = (3,3),input_shape=(150,150,3),activation = 'relu'))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(filters = 100,kernel_size = (3,3),activation = 'relu'))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(filters = 128,kernel_size = (3,3),activation = 'relu'))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128,activation = 'relu'))
model.add(Dense(2,activation='softmax'))

opt = Adam(lr = learning_rate,decay=learning_rate/epochs)
model.compile(loss='binary_crossentropy',optimizer = opt,metrics=['accuracy'])
stop = EarlyStopping(monitor='val_loss',patience=2)
model.summary()
results = model.fit_generator(train_image_gen,epochs =10,validation_data=test_image_gen,callbacks=[stop])
print('loss :',model.evaluate(test_image_gen)[0])
print('accuracy :',model.evaluate(test_image_gen)[1])

model.save('mask_detect.h5')