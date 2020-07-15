## CNN (Convolutional Neural Networks)

### What is CNN?

CNN: A Neural Network architecture, usually used for computer vision problems.

- use layers that transforms 3D input to 3D output.
- use shared parameters called filters or kernels.
- can try pooling to downsample along the spatial dimensions (in width, height).

[Check pic representing CNN (cs231n)](https://cs231n.github.io/assets/cnn/cnn.jpeg)

### Kernel (Filter)

- a matrix, for example shape of 3 by 3, that has weight values for each item (index).
- We put the kernel upon the target matrix, and calculate the values.

[See how kernel works (stackoverflow)](https://stats.stackexchange.com/a/188216)

+ The height and width shrinks after applying the kernel.
+ You can use padding (adding rows, columns) to prevent shrinking.

### So, How Conv Layer works?

The basic operation is: "Filter and Stride", as we can see in the previous link.

- For each depth slice (= channel) in layer input:
    - Starting from the available-left-top-most pixel, apply the kernel.
    - Loop: stride to the next pixel and apply kernel.
- Sum the result(matrix) of each channel.

The pseudo code would be like this:
```
for i = 1 ... n:
    output_feature_map += apply_kernel(input[i], kernel[i])
```

+ The result of conv layer is commonly called as feature map.

### Multiple Feature Maps as Output of Conv Layer

- We sum the kernel results when input has multiple channels (depth > 1),
then it will result only one feature map.
- We can make output to have multiple feature maps, by using more filters.
- If we have input depth n and output depth m, we use number of n*m kernels.

The pseudo code would be like this:
```
for i = 1 ... m:
    for j = 1 ... n:
        output_feature_maps[i] += apply_kernel(input[j], kernel[i][j])
```

### How Pooling Layer works?

- Pooling layer: layer that extracts representative values from regions divided by filter
(divided like square grid).

[See how pooling works](https://cs231n.github.io/assets/cnn/maxpool.jpeg)

## CNN with Keras Example; Sequential Model

Let we initialized Sequential model in Keras, and see how to build CNN.

```python
model.add(layers.Conv2D(4, (3, 3), 
                        activation='relu', input_shape=(28, 28, 1)))
```
- The depth of output is 4, and filter shape is (3, 3).
- It will use relu as activation function, and input(image) shape is (28, 28, 1), a grayscale image (MNIST).

+ We will need 4 kernels, 4 bias, 4 * (3 * 3 + 1) = 40 parameters.
+ output shape: (26, 26, 4)

```python
model.add(layers.MaxPooling2D((2, 2)))
```

- It will do max pooling by F = 2.
- output shape: (13, 13, 4)

```python
model.add(layers.Conv2D(8, (3, 3), activation='relu'))
```

- The depth of output is 8, and filter shape is (3, 3).
- We will need 4 * 8 kernels, ((3 * 3) * 4 + 1) * 8 = 296 parameters.

+ output shape: (11, 11, 8)

```python
model.add(layers.MaxPooling2D((2, 2)))
```

- output shape: (5, 5, 8) (throw away last row and column)

```python
model.add(layers.Conv2D(16, (3, 3), activation='relu'))
```

- The depth of output is 16, and filter shape is (3, 3).
- need 8 * 16 kernels, ((3 * 3) * 8 + 1) * 16 = 1168 parameters.

+ output shape: (3, 3, 16)

```python
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

- We now flatten and use Dense(Fully Connected) Layer, do as we did on multi-class classification.
- Commonly, we can see that channels grow, but width, height shrinks.

## References

- Stanford CS231n
- AI Innovation Square (KR)
