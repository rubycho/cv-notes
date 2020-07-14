## CNN (Convolutional Neural Networks)

### What is CNN?

CNN: A Neural Network architecture, usually used for computer vision problems.

- transforms 3D input to 3D output.
- use shared parameters called filters or kernels.
- can try pooling to downsample along the spatial dimensions (width, height).

[check pic representing CNN (cs231n)](https://cs231n.github.io/assets/cnn/cnn.jpeg)

### Image Shape

- Shape of image: (H, W, C)
- Shape of images(batch): (B, H, W, C)
- Each item means Batch, Height, Width, Channel.

### Kernel (Filter)

- Kernel is a matrix, for example shape of 3 by 3, that has weight values for each item(index).
- Kernel could be used in one channel. (height, width)
- We put the kernel upon the image, and calculate the values.

[see how kernel works (stackoverflow)](https://stats.stackexchange.com/a/188216)

- If the image has multiple channel, than we can use different kernel for each channel, and sum the results.
- The height and width shrinks after applying the kernel (convolution).
- You can use padding (adding rows, columns) to prevent shrinking.

### So, How Conv Layer works?

The basic operation is: "Filter and Stride", as we can see in the previous image.

- Starting from the available-left-top-most pixel, apply the kernel.
- Stride to the next pixel and apply kernel.


- If multiple channels, can use different kernels for each channel,
 and sum up results of each channel, and add bias value.

The result of Conv Layer is commonly called "Featrue Map (F-Map)".

#### Output with multiple channels

- We sum the results if the input has multiple channels. But then, it will result only one channel.
- We can make output to have multiple channels, by using more filters.
- For example, if we have n input channel and m expected output channels, use n*m kernels.

### How Pooling Layer works?

- Pooling layer: layer that extracts representative values from regions divided by filter (divided like square grid).

[see how pooling works](https://cs231n.github.io/assets/cnn/maxpool.jpeg)

## CNN with Keras Example; Sequential Model

Let we initialized Sequential model in Keras, and see how to build CNN.

```python
model.add(layers.Conv2D(4, (3, 3), 
                        activation='relu', input_shape=(28, 28, 1)))
```
- The # of channel in output is 4, and filter shape is (3, 3).
- It will use relu as activation function, and input layer(image) shape is (28, 28, 1), a grayscale image (MNIST).


- We will need 4 kernels, 4 bias, 4 * (3 * 3 + 1) = 40 parameters.
- output shape: (26, 26, 4)

```python
model.add(layers.MaxPooling2D((2, 2)))
```

- It will do max pooling by F = 2.
- output shape: (13, 13, 4)

```python
model.add(layers.Conv2D(8, (3, 3), activation='relu'))
```

- The # of channel in output is 8, and filter shape is (3, 3).
- We will need 4 * 8 kernels, ((3 * 3) * 4 + 1) * 8 = 296 parameters.


- output shape: (11, 11, 8)

```python
model.add(layers.MaxPooling2D((2, 2)))
```

- output shape: (5, 5, 8) (throw away last row and column)

```python
model.add(layers.Conv2D(16, (3, 3), activation='relu'))
```

- The # of channel in output is 16, and filter shape is (3, 3).
- need 8*16 kernels, ((3 * 3) * 8 + 1) * 16 = 1168 parameters.


- output shape: (3, 3, 16)

```python
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

- we now flatten and use Dense(Fully Connected) Layer, do as we did on multi-class classification.
- commonly, we can see that channels grow, but width, height shrinks.
