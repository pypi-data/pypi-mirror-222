# 加速数组循环库(Accelerated array loop library)

## 1. 简介(abstract)

```
由于python语言的自身特性，导致其在循环上的效率很低，因此得采取一定措施提升速度。本库依托于numba库，加速数组循环的同时完成求差、和、均值等功能，目的是避免重复编写加速代码。
Due to the characteristics of the python language, its efficiency in the loop is very low, so some measures must be taken to improve the speed. This library relies on numba library to accelerate the array cycle while completing the difference, sum, mean and other functions, the purpose is to avoid repeated writing of acceleration code.
```

## 2. 使用说明(Use Method)

> * **install the lib**: pip install michaelPanExpediteLib
>
> * ```python
>   import numpy as np
>   from michaelPanExpediteLib.expedite_array_circulation import circulation_array
>   
>   
>   arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>   arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>   temp_array = np.ones((3, 3))
>   temp_array_num = np.zeros((3, 3))
>   x_dim = 3
>   y_dim = 3
>   # circulation_array(data1, data2, temp_array, y_dim, x_dim, data_fill, method, temp_array_num=None)
>   temp_array, temp_array_num = circulation_array(arr1, arr2, temp_array, y_dim, x_dim, 1, 'add', temp_array_num)
>   ```

## 3.作者及联系方式

```
# ***************************************************************
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2023.8
# ***************************************************************
```

