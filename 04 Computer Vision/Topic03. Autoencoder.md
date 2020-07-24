## Autoencoder

An autoencoder is a network which encodes and decodes data.

In other words, it compresses the data, and reconstructs and outputs it,
like PCA method (Principal Components Analysis), but more non-linearly.

[Check how autoencoder looks like (Keras Blog).](https://blog.keras.io/img/ae/autoencoder_schema.jpg)

The interesting thing about autoencoder is that it is self-supervised,
evaluating the output with the data generated from input (or just input).

Main usage of autoencoder is denoising and dimensionality reduction
(for visualizing the data).

Denoising, for example, we can construct a quite-different
autoencoder, that feed inputs with noise, compare with original-clean
image, so that make our model remove noises on a new dataset.

## References
- The Keras Blog
