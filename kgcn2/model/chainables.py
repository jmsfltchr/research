import tensorflow as tf


class DenseChainable:

    def __init__(self, num_outputs, dense_layer=tf.layers.Dense):
        self._num_outputs = num_outputs
        self._dense_layer = dense_layer(self._num_outputs)

    def __call__(self, input_tensor):
        input_tensor_size = input_tensor.shape.as_list()
        if input_tensor_size[1] != self._num_outputs:
            raise ValueError(f'Input tensor has dimension {input_tensor_size[1]}, expected {self._num_outputs}')

        return self._dense_layer(input_tensor)
