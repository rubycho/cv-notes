## Using Pre-trained Model

### Transfer Learning

Transfer Learning means using a pre-trained model, and re-train it by finely tuning parameters, 
to make it fit into our current dataset, or a problem. This method is also called as Fine Tuning.

The pro of the deep learning is that we can use pre-trained model 
(which is sufficiently trained with large dataset) for solving other problems.

This is because the main responsibility of conv, pool layers is feature extraction, 
and the dense layers which is placed nearly with output layer, 
classifies or do other problem-related-decision things using extracted features.

The trained part of conv and pool layers are called convolutional base,
and as you can guess, we don't re-train the convolutional base on re-training, 
and only remove the dense part and re-connect new dense layers which gets input from the base.
Which means, backpropagation will be done only on re-connected new layer parameters, not on convolutional base.

For example, VGG-16 is a model trained with 14 million images belonging to 1000 classes.
We can use this model to classify whether the image has a cat or a dog with a dataset.

### VGG-16 architecture

You can check out the layers of VGG-16 on below link.

[VGG-16 network (neurohive)](https://neurohive.io/en/popular-networks/vgg16/)

The abstract code on Keras would be like this:

```python
Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=(224, 224, 3))
Conv2D(64, (3, 3), padding='same', activation='relu')
MaxPooling2D((2, 2))
Conv2D(128, (3, 3), padding='same', activation='relu')
Conv2D(128, (3, 3), padding='same', activation='relu')
MaxPooling2D((2, 2))
Conv2D(256, (3, 3), padding='same', activation='relu')
Conv2D(256, (3, 3), padding='same', activation='relu')
Conv2D(256, (3, 3), padding='same', activation='relu')
MaxPooling2D((2, 2))
Conv2D(512, (3, 3), padding='same', activation='relu')
Conv2D(512, (3, 3), padding='same', activation='relu')
Conv2D(512, (3, 3), padding='same', activation='relu')
MaxPooling2D((2, 2))
Flatten()
Dense(4096, activation='relu')
Dense(4096, activation='relu')
Dense(1000, activation='softmax')
```

### Helpful class, functions on Keras

- [ImageDataGenerator](https://keras.io/api/preprocessing/image/#imagedatagenerator-class):
Class used for Data Augmentation.
- [ImageDataGenerator.flow_from_directory()](https://keras.io/api/preprocessing/image/#flowfromdirectory-method):
Function used to create a augmented-data batch-per-iterator. 
- [VGG16](https://keras.io/api/applications/vgg/#vgg16-and-vgg19)
: a VGG-16 model.
- [Model](https://keras.io/api/models/model/)
: compile(), get_layer(), fit(), fit_generator() will be used on next content.

### Replacing classifier

Soon.

## References

Neuro Hive: VGG16 – Convolutional Network for Classification and Detection 
AI Innovation Square (KR)
