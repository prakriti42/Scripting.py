"""
Script for performing differntiation using the python deep learning framework.setdefault()
""" 


import tensorflow as tf 
"""Finding the derivative of the function 
y = x**3 wrt x when x = 6 
"""

x = tf.Variable(6.0)
with tf.GradientTape() as tape:
    y = pow(x,3)
dy_by_dx = tape.gradient(y,x)
print(dy_by_dx.numpy())

""" Using non scalar tensor on tf.GradientTape 
"""
m = tf.Variable(tf.random.normal((3, 2)), name='w')
c = tf.Variable(tf.zeros(2, dtype=tf.float32), name='b')
x = [[1., 2., 3.]]

with tf.GradientTape(persistent=True) as tape:
  y = x @ m + c
  loss = tf.reduce_mean(y**2)
[dl_dw, dl_db] = tape.gradient(loss, [m, c])
print(m.shape)
print(dl_dw.shape)

my_vars = {
    'w': m,
    'b': c
}

grad = tape.gradient(loss, my_vars)
print(grad['b'])


    

