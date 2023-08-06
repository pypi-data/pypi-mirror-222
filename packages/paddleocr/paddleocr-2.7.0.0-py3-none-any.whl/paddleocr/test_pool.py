import paddle 

test_x = paddle.to_tensor([[[[1,2],[4,5],[8,9]]]], dtype='float32')
print(test_x.shape)

pool_22 = paddle.nn.AvgPool2D(kernel_size=2, stride=2, padding=0)
pool_32 = paddle.nn.AvgPool2D(kernel_size=[3,2], stride=[3,2], padding=0)

print(pool_22(test_x))
print(pool_32(test_x))
