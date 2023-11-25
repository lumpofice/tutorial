using LinearAlgebra
using VMLS

# Let l be a line, defined as
# l(phi) = (1 - phi)*a + phi*b, where a and b are n-vectors.

# Theta is the minimum of the parameter, phi, used in computing the distance
# between a point along the line, l, and an n-vector, x.

theta(x, a, b) = -( sum( (a - x).*(b - a) ) )/( sum( (a - b).*(a - b) ) )

# p is the point along the line, l, from which the distance between
# line l and vector x is the minimum.
p(theta, a, b) = (1 - theta)*a + theta*b

# With l, theta, x, and p given as above, f below should be equal to 0.
f(p, x, a, b) = sum( (p - x).*(b - a) )

a_0 = rand(1:50, 100, 1)
b_0 = rand(1:50, 100, 1)
x_0 = rand(1:50, 100, 1)

theta_0 = theta(x_0, a_0, b_0)
println("Here is theta:")
println(theta_0)
println("")

p_0 = p(theta_0, a_0, b_0)
println("Here is p:")
println(p_0)
println("")

f_0 = f(p_0, x_0, a_0, b_0)
println("Here is f:")
println(f_0)
println("")

