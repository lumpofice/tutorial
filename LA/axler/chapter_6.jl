# Orthonormal Basis of two dimensions
using LinearAlgebra
using VMLS

x = rand(1:50, 2, 1)
y = rand(1:50, 2, 1)

println("x:")
println(x)

println("y:")
println(y)

term = 0
element_one = (1/norm(x)).*x

println("element_one:")
println(element_one)

for i = 1:size(x, 1)
	global term
	term += y[i]*element_one[i]
end

println("term:")
println(term)

element_two = y - term.*element_one
println("element_two:")
println(element_two)

