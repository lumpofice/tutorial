# Orthonormal Basis of two dimensions
using LinearAlgebra
using VMLS

x = rand(1:50, 2, 1)
y = rand(1:50, 2, 1)

set_e = Set([])
println("set_e empty:")
println(set_e)

println("x:")
println(x)

println("y:")
println(y)

e = zeros(0)
append!(e, (1/norm(x)).*x)
push!(set_e, e)

println("set_e after element 1 added:")
println(set_e)

term = 0

for i = 1:size(x, 1)
	global term
	term += y[i]*collect(set_e)[1][i]
end

e = zeros(0)
append!(e, y - term.*collect(set_e)[1])
push!(set_e, e)

println("set_e after element 2 added:")
println(set_e)
