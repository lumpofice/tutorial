# Orthonormal Basis of two dimensions
using LinearAlgebra
using VMLS

x = [1, 2, 3, -4]
y = [-5, 4, 3, 2]

# So, orthonormal basis will have size OB = 2
OB = 2

# Orthonormal Basis: set_e
set_e = Set([])

println("x:")
println(x)

println("y:")
println(y)

e = zeros(0)
append!(e, (1/norm(x)).*x)
push!(set_e, e)

println("set_e after element 1 added:")
println(set_e)

for k = 1:(OB - 1)
	global y
	global set_e
	new_element_terms = Set([])	
	for j = 1:k
		term_dot = 0
		for i = 1:size(x, 1)
			term_dot += y[i]*collect(set_e)[j][i]
		end
		push!(new_element_terms, term_dot.*collect(set_e)[j])
	end
	summing_non_y_terms = zeros(size(y, 1))
	for n = 1:length(new_element_terms)
		summing_non_y_terms -= collect(new_element_terms)[n]
	end
	new_element = y + summing_non_y_terms
	push!(set_e, (1/norm(new_element))*new_element)
	println("set_e after element 2 added:")
	println(set_e)
end

