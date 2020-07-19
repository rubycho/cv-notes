## Using a Pre-trained Model

### Transfer Learning

Transfer Learning refers to the learning method using a pre-trained model, modify 
a little bit to make it fit on different dataset or a problem.

There are three scenarios, according to the stanford cs231n. 
Today, we will apply one method of them.

The method is: use a pre-trained model for classification called VGG16,
remove FC layers of it, add new FC layers at the end,
and train(back-propagation) only new added FC layers,
eventually changing the classifying part of a pre-trained model.

The thing that makes this possible is that the main responsibility of conv, pool layers
is feature extraction, and the dense layers which is placed nearly with output layer,
classifies or do other problem-related-decision things using extracted features.
(Though, in cs231n, it says that later conv layer also fits to the original data, that's why we do fine-tuning.)

## References

- Stanford CS231n
- The Keras Blog
