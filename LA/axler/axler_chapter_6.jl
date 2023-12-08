# Orthonormal Basis of two dimensions
using LinearAlgebra
using VMLS

x_1 = [1, 0, 0, 0]
x_2 = [0, 1, 0, 0]
x_3 = [0, 0, 1, 0]
x_4 = [0, 0, 0, 1]

basis = Vector{Int}[]

push!(basis, x_1)
push!(basis, x_2)
push!(basis, x_3)
push!(basis, x_4)

println("Here is our basis:")
println(basis)
println("")

# So, orthonormal basis will have size dimension = 2
dimension = 4

# Orthonormal Basis: ortho_basis
ortho_basis = Set([])

e = zeros(0)
append!(e, (1/norm(x_1)).*x_1)
push!(ortho_basis, e)

println("ortho_basis after element 1 added:")
println(ortho_basis)
println("")

for k = 2:dimension
	global basis
	global ortho_basis
	new_element_terms = Set([])	
	for j = 1:k-1
		term_dot = 0
		for i = 1:size(x_1, 1)
			term_dot += 
			collect(basis)[k][i]*collect(ortho_basis)[j][i]
		end
		push!(new_element_terms, term_dot.*collect(ortho_basis)[j])
	end
	summing_scaled_terms = zeros(size(x_1, 1))
	for n = 1:length(new_element_terms)
		summing_scaled_terms -= collect(new_element_terms)[n]
	end
	new_element_before_scaling = collect(basis)[k] + summing_scaled_terms
	push!(ortho_basis, 
	       (1/norm(new_element_before_scaling)).*new_element_before_scaling)
	println("ortho_basis after new_element added:")
	println(ortho_basis)
	println("")
end

println("Turning Set to Array:")
ortho_basis_array = [i for i in ortho_basis]
typeof(ortho_basis_array)
println(ortho_basis_array)

