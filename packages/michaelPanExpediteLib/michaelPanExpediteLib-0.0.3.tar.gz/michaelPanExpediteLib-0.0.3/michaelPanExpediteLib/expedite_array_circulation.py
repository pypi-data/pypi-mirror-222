from numba import jit, prange


@jit(nopython=True, nogil=True)
def circulation_array(data1, data2, temp_array, y_dim, x_dim, data_fill, method, temp_array_num=None):
    """
    :param data1: a numpy array
    :param data2: a numpy array
    :param temp_array: a temp numpy array
    :param y_dim: The y dimension of arrays 1 and 2
    :param x_dim: The x dimension of arrays 1 and 2
    :param data_fill: fill-value of arrays 1 and 2
    :param method: 'add' or 'mean' or 'divide' or 'multiply' or 'minus'
    :param temp_array_num: Counting array
    :return: output array and counting array

    an example are as follows:
        import numpy as np
        from michaelPanExpediteLib.expedite_array_circulation import circulation_array

        arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        temp_array = np.ones((3, 3))

        temp_array_num = np.zeros((3, 3))

        x_dim = 3

        y_dim = 3

        temp_array, temp_array_num = circulation_array(arr1, arr2, temp_array, y_dim, x_dim, 1, 'add', temp_array_num)
    """
    for i in prange(x_dim):
        for j in prange(y_dim):
            if data1[j, i] != data_fill and data2[j, i] != data_fill:
                if method == 'mean':
                    temp_array[j, i] = (data1[j, i] + data2[j, i]) / 2
                elif method == 'add':
                    temp_array[j, i] = data1[j, i] + data2[j, i]
                elif method == 'divide':
                    temp_array[j, i] = data1[j, i] / data2[j, i]
                elif method == 'multiply':
                    temp_array[j, i] = data1[j, i] * data2[j, i]
                elif method == 'minus':
                    temp_array[j, i] = data1[j, i] - data2[j, i]
                else:
                    raise Exception('method param error, please check it!')
                if temp_array_num is not None:  # when array is not None
                    temp_array_num[j, i] += 1
            elif data1[j, i] == data_fill and data2[j, i] != data_fill:
                temp_array[j, i] = data2[j, i]
            elif data1[j, i] != data_fill and data2[j, i] == data_fill:
                temp_array[j, i] = data1[j, i]
            else:
                temp_array[j, i] = data_fill
    return temp_array, temp_array_num

