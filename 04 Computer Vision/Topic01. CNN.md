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

## References

- Stanford CS231n
- AI Innovation Square (KR)
