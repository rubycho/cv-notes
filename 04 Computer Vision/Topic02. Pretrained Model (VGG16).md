## Using a Pre-trained Model

### Transfer Learning

Transfer Learning refers to the learning method using a pre-trained model, modify 
a little bit to make it fit on different dataset or a problem.

There are three scenarios, according to the stanford cs231n.

Today, I will talk about one of them, using a pre-trained model for classification,
remove FC layers of it, add new FC layers at the end,
and train(back-propagation) only new added FC layers,
eventually changing the classifying part of a pre-trained model.

The thing that makes this possible is that the main responsibility of conv, pool layers
is feature extraction, and the dense layers which is placed nearly with output layer,
classifies or do other problem-related-decision things using extracted features.
(Though, in cs231n, it says that later conv layer also fits to the original data, that's why we do fine-tuning.)

For example, VGG-16 is a model trained with 14 million images belonging to 1000 classes.
We can use this model to only classify whether the image has a cat or a dog with a dataset.

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

### Replacing classifier on VGG16

Soon.

### Using InceptionV3

Soon.

## References

- Stanford CS231n
- Neuro Hive: VGG16 – Convolutional Network for Classification and Detection 
- AI Innovation Square (KR)
