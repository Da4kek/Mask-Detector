# Contents:

1. **Introduction to the idea.**
2. **Introduction to the project itself.**
3. **Requirements.**
4. **Debugging and testing.**
5. **Conclusion.** 
---
# The Idea: 

> The idea used for the project is so called the Neural network.


- *Neural networks, also known as artificial neural networks (ANNs) or simulated neural networks (SNNs), are a subset of machine learning and are at the heart of deep learning algorithms. Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.*
- *There are 3 main types of Neural Networks or ANNs*

**Types of ANNs:**
1. Artificial Neural Networks
2. Convolutional Neural Networks
3. Recurrent Neural Networks

> The type which is used in this project is the `Convolutional Neural Networks or CNNs`.

### Convolutional Neural Networks: 
> Convolutional neural networks are neural networks used primarily to classify images, cluster images by similarity (photo search), and perform object recognition within scenes. For example, convolutional neural networks (ConvNets or CNNs) are used to identify faces, individuals, street signs, tumors, platypuses (platypi?) and many other aspects of visual data.

> The efficacy of convolutional nets in image recognition is one of the main reasons why the world has woken up to the efficacy of deep learning. In a sense, CNNs are the reason why deep learning is famous.
---
# The Project:

`The idea behind this project is to make a CNN model that will predict whether or not the person wearing a mask`
> - The source file contains 2 `.py` files, `.h5` file and 3 other folders  
> - The `Themainmodel.py` file contains the codes where the model is built from scratch
> - The `Evaluating.py` file contains the codes where the model is tested on real world portraits of people

> - The `mask_detect.h5` is the model/output that we've got from `Themainmodel.py` file, we will be using the file later in the `Evaluating.py` file for testing and debugging.

> The folders `test`,`train` and `val` are meant to contain the main data and are arranged like: 

![image](https://user-images.githubusercontent.com/61820492/139258586-0cc767dc-7199-407b-a0bd-1a52ae07f51b.png)

- The `train` data is used for training the model with both with and without mask portraits.
- After training the model the `test` data is used for testing the model, so that we can save the model to `mask_detect.h5`.
- the `val` data is used for the output(finally after saving our model, ie for predicting).
---
# Requirements: 

> Although we have python installed, we still have some software and hardware requirements to run the project.

**Software Installation:**
- `pip install numpy`
- `pip install matplotlib`
- `pip install tensorflow==2.2.0`
- `pip install keras`
- `pip install keras-utils`

**hardware Requirements**:

> To run neural network models, we do need some resources, practically most neural networks are developed in the cloud and then implemented locally, so I recommend to run `Themainmodel.py` in some cloud based programming interface such as google colab. But since it's already developed and saved the model you can go locally for the `Implementation.py` file.
---
# Debugging and testing:

1. change your directory to `Mask-Detector`.
2. run the file by typing `python Evaluating.py` in your command prompt.

![image](https://user-images.githubusercontent.com/61820492/139261438-02cc4f2c-8190-410a-888c-e794995e9a36.png)

3. here you will be entering the path of the image you want to test the model on.

![image](https://user-images.githubusercontent.com/61820492/139262027-affb2757-93e4-42ea-8c8c-1a53e464c117.png)

4. the expected output will be like: 

![image](https://user-images.githubusercontent.com/61820492/139262237-2d1cbde1-6870-483b-9bd7-a101a4fb188a.png)

5. you can always check with the command prompt as well for a reference.

![image](https://user-images.githubusercontent.com/61820492/139262369-b9a9d5ed-a2da-4564-b848-9d89f7e1dd10.png)

6. check with without mask as well.

![image](https://user-images.githubusercontent.com/61820492/139262901-68962612-3578-4fdd-82b4-0492c38cd33d.png)

7. to close the program either press `ctrl +c` in the command prompt or just press the `X` in the output panel.
---
# Conclusion:
> I would like to conclude my project by emphasizing the import of data and programming.

---
