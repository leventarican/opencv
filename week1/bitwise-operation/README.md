* the code `bitwise-operation.py` is the same example as in `application-sunglass-filter`
    * instead of arithmetic ops, bitwise operations are used.
* _bitwise operations_ are extremly fast compared to _arithmetic operations_
* AND operation: https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14
* OR operation: https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#gab85523db362a4e26ff0c703793a719b4
* NOT operation: https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga0002cf8b418479f4cb49a75442baee2f
* XOR operation: https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga84b2d8188ce506593dcc3f8cd00e8e2c
```
dst = cv.bitwise_XXX( src1, src2[, dst[, mask]] )

XXX stands for the operation

src1 - first input.
src2 - second input.
dst - output array that has the same size and type as the input array.
mask - optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed. The operation is applied only on those pixels of the input images where the mask is non-zero.

```
