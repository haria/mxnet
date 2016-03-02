import mxnet as mx

def get_symbol(num_classes = 89):
    data = mx.symbol.Variable(name='data')
    conv1 = mx.symbol.Convolution(name='conv1', data=data , num_filter=64, pad=(3,3), kernel=(7,7), stride=(2,2), no_bias=False)
    bn_conv1 = mx.symbol.BatchNorm(name='bn_conv1', data=conv1 )
    conv1_relu = mx.symbol.Activation(name='conv1_relu', data=bn_conv1 , act_type='relu')
    pool1 = mx.symbol.Pooling(name='pool1', data=conv1_relu , pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    res2a_branch1 = mx.symbol.Convolution(name='res2a_branch1', data=pool1 , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2a_branch1 = mx.symbol.BatchNorm(name='bn2a_branch1', data=res2a_branch1 )
    res2a_branch2a = mx.symbol.Convolution(name='res2a_branch2a', data=pool1 , num_filter=64, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2a_branch2a = mx.symbol.BatchNorm(name='bn2a_branch2a', data=res2a_branch2a )
    res2a_branch2a_relu = mx.symbol.Activation(name='res2a_branch2a_relu', data=bn2a_branch2a , act_type='relu')
    res2a_branch2b = mx.symbol.Convolution(name='res2a_branch2b', data=res2a_branch2a_relu , num_filter=64, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn2a_branch2b = mx.symbol.BatchNorm(name='bn2a_branch2b', data=res2a_branch2b )
    res2a_branch2b_relu = mx.symbol.Activation(name='res2a_branch2b_relu', data=bn2a_branch2b , act_type='relu')
    res2a_branch2c = mx.symbol.Convolution(name='res2a_branch2c', data=res2a_branch2b_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2a_branch2c = mx.symbol.BatchNorm(name='bn2a_branch2c', data=res2a_branch2c )
    res2a = mx.symbol.ElementWiseSum(name='res2a', *[bn2a_branch1,bn2a_branch2c] )
    res2a_relu = mx.symbol.Activation(name='res2a_relu', data=res2a , act_type='relu')
    res2b_branch2a = mx.symbol.Convolution(name='res2b_branch2a', data=res2a_relu , num_filter=64, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2b_branch2a = mx.symbol.BatchNorm(name='bn2b_branch2a', data=res2b_branch2a )
    res2b_branch2a_relu = mx.symbol.Activation(name='res2b_branch2a_relu', data=bn2b_branch2a , act_type='relu')
    res2b_branch2b = mx.symbol.Convolution(name='res2b_branch2b', data=res2b_branch2a_relu , num_filter=64, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn2b_branch2b = mx.symbol.BatchNorm(name='bn2b_branch2b', data=res2b_branch2b )
    res2b_branch2b_relu = mx.symbol.Activation(name='res2b_branch2b_relu', data=bn2b_branch2b , act_type='relu')
    res2b_branch2c = mx.symbol.Convolution(name='res2b_branch2c', data=res2b_branch2b_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2b_branch2c = mx.symbol.BatchNorm(name='bn2b_branch2c', data=res2b_branch2c )
    res2b = mx.symbol.ElementWiseSum(name='res2b', *[res2a_relu,bn2b_branch2c] )
    res2b_relu = mx.symbol.Activation(name='res2b_relu', data=res2b , act_type='relu')
    res2c_branch2a = mx.symbol.Convolution(name='res2c_branch2a', data=res2b_relu , num_filter=64, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2c_branch2a = mx.symbol.BatchNorm(name='bn2c_branch2a', data=res2c_branch2a )
    res2c_branch2a_relu = mx.symbol.Activation(name='res2c_branch2a_relu', data=bn2c_branch2a , act_type='relu')
    res2c_branch2b = mx.symbol.Convolution(name='res2c_branch2b', data=res2c_branch2a_relu , num_filter=64, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn2c_branch2b = mx.symbol.BatchNorm(name='bn2c_branch2b', data=res2c_branch2b )
    res2c_branch2b_relu = mx.symbol.Activation(name='res2c_branch2b_relu', data=bn2c_branch2b , act_type='relu')
    res2c_branch2c = mx.symbol.Convolution(name='res2c_branch2c', data=res2c_branch2b_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn2c_branch2c = mx.symbol.BatchNorm(name='bn2c_branch2c', data=res2c_branch2c )
    res2c = mx.symbol.ElementWiseSum(name='res2c', *[res2b_relu,bn2c_branch2c] )
    res2c_relu = mx.symbol.Activation(name='res2c_relu', data=res2c , act_type='relu')
    res3a_branch1 = mx.symbol.Convolution(name='res3a_branch1', data=res2c_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn3a_branch1 = mx.symbol.BatchNorm(name='bn3a_branch1', data=res3a_branch1 )
    res3a_branch2a = mx.symbol.Convolution(name='res3a_branch2a', data=res2c_relu , num_filter=128, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn3a_branch2a = mx.symbol.BatchNorm(name='bn3a_branch2a', data=res3a_branch2a )
    res3a_branch2a_relu = mx.symbol.Activation(name='res3a_branch2a_relu', data=bn3a_branch2a , act_type='relu')
    res3a_branch2b = mx.symbol.Convolution(name='res3a_branch2b', data=res3a_branch2a_relu , num_filter=128, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn3a_branch2b = mx.symbol.BatchNorm(name='bn3a_branch2b', data=res3a_branch2b )
    res3a_branch2b_relu = mx.symbol.Activation(name='res3a_branch2b_relu', data=bn3a_branch2b , act_type='relu')
    res3a_branch2c = mx.symbol.Convolution(name='res3a_branch2c', data=res3a_branch2b_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3a_branch2c = mx.symbol.BatchNorm(name='bn3a_branch2c', data=res3a_branch2c )
    res3a = mx.symbol.ElementWiseSum(name='res3a', *[bn3a_branch1,bn3a_branch2c] )
    res3a_relu = mx.symbol.Activation(name='res3a_relu', data=res3a , act_type='relu')
    res3b_branch2a = mx.symbol.Convolution(name='res3b_branch2a', data=res3a_relu , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3b_branch2a = mx.symbol.BatchNorm(name='bn3b_branch2a', data=res3b_branch2a )
    res3b_branch2a_relu = mx.symbol.Activation(name='res3b_branch2a_relu', data=bn3b_branch2a , act_type='relu')
    res3b_branch2b = mx.symbol.Convolution(name='res3b_branch2b', data=res3b_branch2a_relu , num_filter=128, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn3b_branch2b = mx.symbol.BatchNorm(name='bn3b_branch2b', data=res3b_branch2b )
    res3b_branch2b_relu = mx.symbol.Activation(name='res3b_branch2b_relu', data=bn3b_branch2b , act_type='relu')
    res3b_branch2c = mx.symbol.Convolution(name='res3b_branch2c', data=res3b_branch2b_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3b_branch2c = mx.symbol.BatchNorm(name='bn3b_branch2c', data=res3b_branch2c )
    res3b = mx.symbol.ElementWiseSum(name='res3b', *[res3a_relu,bn3b_branch2c] )
    res3b_relu = mx.symbol.Activation(name='res3b_relu', data=res3b , act_type='relu')
    res3c_branch2a = mx.symbol.Convolution(name='res3c_branch2a', data=res3b_relu , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3c_branch2a = mx.symbol.BatchNorm(name='bn3c_branch2a', data=res3c_branch2a )
    res3c_branch2a_relu = mx.symbol.Activation(name='res3c_branch2a_relu', data=bn3c_branch2a , act_type='relu')
    res3c_branch2b = mx.symbol.Convolution(name='res3c_branch2b', data=res3c_branch2a_relu , num_filter=128, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn3c_branch2b = mx.symbol.BatchNorm(name='bn3c_branch2b', data=res3c_branch2b )
    res3c_branch2b_relu = mx.symbol.Activation(name='res3c_branch2b_relu', data=bn3c_branch2b , act_type='relu')
    res3c_branch2c = mx.symbol.Convolution(name='res3c_branch2c', data=res3c_branch2b_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3c_branch2c = mx.symbol.BatchNorm(name='bn3c_branch2c', data=res3c_branch2c )
    res3c = mx.symbol.ElementWiseSum(name='res3c', *[res3b_relu,bn3c_branch2c] )
    res3c_relu = mx.symbol.Activation(name='res3c_relu', data=res3c , act_type='relu')
    res3d_branch2a = mx.symbol.Convolution(name='res3d_branch2a', data=res3c_relu , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3d_branch2a = mx.symbol.BatchNorm(name='bn3d_branch2a', data=res3d_branch2a )
    res3d_branch2a_relu = mx.symbol.Activation(name='res3d_branch2a_relu', data=bn3d_branch2a , act_type='relu')
    res3d_branch2b = mx.symbol.Convolution(name='res3d_branch2b', data=res3d_branch2a_relu , num_filter=128, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn3d_branch2b = mx.symbol.BatchNorm(name='bn3d_branch2b', data=res3d_branch2b )
    res3d_branch2b_relu = mx.symbol.Activation(name='res3d_branch2b_relu', data=bn3d_branch2b , act_type='relu')
    res3d_branch2c = mx.symbol.Convolution(name='res3d_branch2c', data=res3d_branch2b_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn3d_branch2c = mx.symbol.BatchNorm(name='bn3d_branch2c', data=res3d_branch2c )
    res3d = mx.symbol.ElementWiseSum(name='res3d', *[res3c_relu,bn3d_branch2c] )
    res3d_relu = mx.symbol.Activation(name='res3d_relu', data=res3d , act_type='relu')
    res4a_branch1 = mx.symbol.Convolution(name='res4a_branch1', data=res3d_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn4a_branch1 = mx.symbol.BatchNorm(name='bn4a_branch1', data=res4a_branch1 )
    res4a_branch2a = mx.symbol.Convolution(name='res4a_branch2a', data=res3d_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn4a_branch2a = mx.symbol.BatchNorm(name='bn4a_branch2a', data=res4a_branch2a )
    res4a_branch2a_relu = mx.symbol.Activation(name='res4a_branch2a_relu', data=bn4a_branch2a , act_type='relu')
    res4a_branch2b = mx.symbol.Convolution(name='res4a_branch2b', data=res4a_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4a_branch2b = mx.symbol.BatchNorm(name='bn4a_branch2b', data=res4a_branch2b )
    res4a_branch2b_relu = mx.symbol.Activation(name='res4a_branch2b_relu', data=bn4a_branch2b , act_type='relu')
    res4a_branch2c = mx.symbol.Convolution(name='res4a_branch2c', data=res4a_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4a_branch2c = mx.symbol.BatchNorm(name='bn4a_branch2c', data=res4a_branch2c )
    res4a = mx.symbol.ElementWiseSum(name='res4a', *[bn4a_branch1,bn4a_branch2c] )
    res4a_relu = mx.symbol.Activation(name='res4a_relu', data=res4a , act_type='relu')
    res4b_branch2a = mx.symbol.Convolution(name='res4b_branch2a', data=res4a_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4b_branch2a = mx.symbol.BatchNorm(name='bn4b_branch2a', data=res4b_branch2a )
    res4b_branch2a_relu = mx.symbol.Activation(name='res4b_branch2a_relu', data=bn4b_branch2a , act_type='relu')
    res4b_branch2b = mx.symbol.Convolution(name='res4b_branch2b', data=res4b_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4b_branch2b = mx.symbol.BatchNorm(name='bn4b_branch2b', data=res4b_branch2b )
    res4b_branch2b_relu = mx.symbol.Activation(name='res4b_branch2b_relu', data=bn4b_branch2b , act_type='relu')
    res4b_branch2c = mx.symbol.Convolution(name='res4b_branch2c', data=res4b_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4b_branch2c = mx.symbol.BatchNorm(name='bn4b_branch2c', data=res4b_branch2c )
    res4b = mx.symbol.ElementWiseSum(name='res4b', *[res4a_relu,bn4b_branch2c] )
    res4b_relu = mx.symbol.Activation(name='res4b_relu', data=res4b , act_type='relu')
    res4c_branch2a = mx.symbol.Convolution(name='res4c_branch2a', data=res4b_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4c_branch2a = mx.symbol.BatchNorm(name='bn4c_branch2a', data=res4c_branch2a )
    res4c_branch2a_relu = mx.symbol.Activation(name='res4c_branch2a_relu', data=bn4c_branch2a , act_type='relu')
    res4c_branch2b = mx.symbol.Convolution(name='res4c_branch2b', data=res4c_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4c_branch2b = mx.symbol.BatchNorm(name='bn4c_branch2b', data=res4c_branch2b )
    res4c_branch2b_relu = mx.symbol.Activation(name='res4c_branch2b_relu', data=bn4c_branch2b , act_type='relu')
    res4c_branch2c = mx.symbol.Convolution(name='res4c_branch2c', data=res4c_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4c_branch2c = mx.symbol.BatchNorm(name='bn4c_branch2c', data=res4c_branch2c )
    res4c = mx.symbol.ElementWiseSum(name='res4c', *[res4b_relu,bn4c_branch2c] )
    res4c_relu = mx.symbol.Activation(name='res4c_relu', data=res4c , act_type='relu')
    res4d_branch2a = mx.symbol.Convolution(name='res4d_branch2a', data=res4c_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4d_branch2a = mx.symbol.BatchNorm(name='bn4d_branch2a', data=res4d_branch2a )
    res4d_branch2a_relu = mx.symbol.Activation(name='res4d_branch2a_relu', data=bn4d_branch2a , act_type='relu')
    res4d_branch2b = mx.symbol.Convolution(name='res4d_branch2b', data=res4d_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4d_branch2b = mx.symbol.BatchNorm(name='bn4d_branch2b', data=res4d_branch2b )
    res4d_branch2b_relu = mx.symbol.Activation(name='res4d_branch2b_relu', data=bn4d_branch2b , act_type='relu')
    res4d_branch2c = mx.symbol.Convolution(name='res4d_branch2c', data=res4d_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4d_branch2c = mx.symbol.BatchNorm(name='bn4d_branch2c', data=res4d_branch2c )
    res4d = mx.symbol.ElementWiseSum(name='res4d', *[res4c_relu,bn4d_branch2c] )
    res4d_relu = mx.symbol.Activation(name='res4d_relu', data=res4d , act_type='relu')
    res4e_branch2a = mx.symbol.Convolution(name='res4e_branch2a', data=res4d_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4e_branch2a = mx.symbol.BatchNorm(name='bn4e_branch2a', data=res4e_branch2a )
    res4e_branch2a_relu = mx.symbol.Activation(name='res4e_branch2a_relu', data=bn4e_branch2a , act_type='relu')
    res4e_branch2b = mx.symbol.Convolution(name='res4e_branch2b', data=res4e_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4e_branch2b = mx.symbol.BatchNorm(name='bn4e_branch2b', data=res4e_branch2b )
    res4e_branch2b_relu = mx.symbol.Activation(name='res4e_branch2b_relu', data=bn4e_branch2b , act_type='relu')
    res4e_branch2c = mx.symbol.Convolution(name='res4e_branch2c', data=res4e_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4e_branch2c = mx.symbol.BatchNorm(name='bn4e_branch2c', data=res4e_branch2c )
    res4e = mx.symbol.ElementWiseSum(name='res4e', *[res4d_relu,bn4e_branch2c] )
    res4e_relu = mx.symbol.Activation(name='res4e_relu', data=res4e , act_type='relu')
    res4f_branch2a = mx.symbol.Convolution(name='res4f_branch2a', data=res4e_relu , num_filter=256, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4f_branch2a = mx.symbol.BatchNorm(name='bn4f_branch2a', data=res4f_branch2a )
    res4f_branch2a_relu = mx.symbol.Activation(name='res4f_branch2a_relu', data=bn4f_branch2a , act_type='relu')
    res4f_branch2b = mx.symbol.Convolution(name='res4f_branch2b', data=res4f_branch2a_relu , num_filter=256, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn4f_branch2b = mx.symbol.BatchNorm(name='bn4f_branch2b', data=res4f_branch2b )
    res4f_branch2b_relu = mx.symbol.Activation(name='res4f_branch2b_relu', data=bn4f_branch2b , act_type='relu')
    res4f_branch2c = mx.symbol.Convolution(name='res4f_branch2c', data=res4f_branch2b_relu , num_filter=1024, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn4f_branch2c = mx.symbol.BatchNorm(name='bn4f_branch2c', data=res4f_branch2c )
    res4f = mx.symbol.ElementWiseSum(name='res4f', *[res4e_relu,bn4f_branch2c] )
    res4f_relu = mx.symbol.Activation(name='res4f_relu', data=res4f , act_type='relu')
    res5a_branch1 = mx.symbol.Convolution(name='res5a_branch1', data=res4f_relu , num_filter=2048, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn5a_branch1 = mx.symbol.BatchNorm(name='bn5a_branch1', data=res5a_branch1 )
    res5a_branch2a = mx.symbol.Convolution(name='res5a_branch2a', data=res4f_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(2,2), no_bias=True)
    bn5a_branch2a = mx.symbol.BatchNorm(name='bn5a_branch2a', data=res5a_branch2a )
    res5a_branch2a_relu = mx.symbol.Activation(name='res5a_branch2a_relu', data=bn5a_branch2a , act_type='relu')
    res5a_branch2b = mx.symbol.Convolution(name='res5a_branch2b', data=res5a_branch2a_relu , num_filter=512, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn5a_branch2b = mx.symbol.BatchNorm(name='bn5a_branch2b', data=res5a_branch2b )
    res5a_branch2b_relu = mx.symbol.Activation(name='res5a_branch2b_relu', data=bn5a_branch2b , act_type='relu')
    res5a_branch2c = mx.symbol.Convolution(name='res5a_branch2c', data=res5a_branch2b_relu , num_filter=2048, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn5a_branch2c = mx.symbol.BatchNorm(name='bn5a_branch2c', data=res5a_branch2c )
    res5a = mx.symbol.ElementWiseSum(name='res5a', *[bn5a_branch1,bn5a_branch2c] )
    res5a_relu = mx.symbol.Activation(name='res5a_relu', data=res5a , act_type='relu')
    res5b_branch2a = mx.symbol.Convolution(name='res5b_branch2a', data=res5a_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn5b_branch2a = mx.symbol.BatchNorm(name='bn5b_branch2a', data=res5b_branch2a )
    res5b_branch2a_relu = mx.symbol.Activation(name='res5b_branch2a_relu', data=bn5b_branch2a , act_type='relu')
    res5b_branch2b = mx.symbol.Convolution(name='res5b_branch2b', data=res5b_branch2a_relu , num_filter=512, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn5b_branch2b = mx.symbol.BatchNorm(name='bn5b_branch2b', data=res5b_branch2b )
    res5b_branch2b_relu = mx.symbol.Activation(name='res5b_branch2b_relu', data=bn5b_branch2b , act_type='relu')
    res5b_branch2c = mx.symbol.Convolution(name='res5b_branch2c', data=res5b_branch2b_relu , num_filter=2048, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn5b_branch2c = mx.symbol.BatchNorm(name='bn5b_branch2c', data=res5b_branch2c )
    res5b = mx.symbol.ElementWiseSum(name='res5b', *[res5a_relu,bn5b_branch2c] )
    res5b_relu = mx.symbol.Activation(name='res5b_relu', data=res5b , act_type='relu')
    res5c_branch2a = mx.symbol.Convolution(name='res5c_branch2a', data=res5b_relu , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn5c_branch2a = mx.symbol.BatchNorm(name='bn5c_branch2a', data=res5c_branch2a )
    res5c_branch2a_relu = mx.symbol.Activation(name='res5c_branch2a_relu', data=bn5c_branch2a , act_type='relu')
    res5c_branch2b = mx.symbol.Convolution(name='res5c_branch2b', data=res5c_branch2a_relu , num_filter=512, pad=(1,1), kernel=(3,3), stride=(1,1), no_bias=True)
    bn5c_branch2b = mx.symbol.BatchNorm(name='bn5c_branch2b', data=res5c_branch2b )
    res5c_branch2b_relu = mx.symbol.Activation(name='res5c_branch2b_relu', data=bn5c_branch2b , act_type='relu')
    res5c_branch2c = mx.symbol.Convolution(name='res5c_branch2c', data=res5c_branch2b_relu , num_filter=2048, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=True)
    bn5c_branch2c = mx.symbol.BatchNorm(name='bn5c_branch2c', data=res5c_branch2c )
    res5c = mx.symbol.ElementWiseSum(name='res5c', *[res5b_relu,bn5c_branch2c] )
    res5c_relu = mx.symbol.Activation(name='res5c_relu', data=res5c , act_type='relu')
    pool5 = mx.symbol.Pooling(name='pool5', data=res5c_relu , pad=(0,0), kernel=(7,7), stride=(1,1), pool_type='avg')
    flatten_0=mx.symbol.Flatten(name='flatten_0', data=pool5)
    fc89 = mx.symbol.FullyConnected(name='fc89', data=flatten_0 , num_hidden=89, no_bias=False)
    softmax = mx.symbol.SoftmaxOutput(data=fc89, name='softmax')
    return softmax