# Orthonormal Basis of four dimensions
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

# So, orthonormal basis will have size dimension = 4
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
		# Building each <e, y>e in this looping
		term_dot = 0
		for i = 1:size(x_1, 1)
			term_dot += 
			collect(basis)[k][i]*collect(ortho_basis)[j][i]
		end
		push!(new_element_terms, term_dot.*collect(ortho_basis)[j])
	end
	# Summing each <e, y>e term within new_element_terms
	summing_scaled_terms = zeros(size(x_1, 1))
	for n = 1:length(new_element_terms)
		summing_scaled_terms -= collect(new_element_terms)[n]
	end
	# This is y - <e1, y>e1 - ... - <em, y>em in Gram-Schmidt
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

# Converting basis for subspace U to orthonormal basis, then using that 
# orthonormal basis to find the minimum distance between a vector v 
# and the subspace of U

println("")
println("")
println("----------------")
println("----------------")
println("----------------")
println("----------------")
println("----------------")
println("")

u_1 = [1, 1, 0, 0]
u_2 = [1, 1, 1, 2]

basis_U = Vector{Int}[] 

push!(basis_U, u_1)
push!(basis_U, u_2)

println("Here is our basis for U:")
println(basis_U)
println("")

# So, our orthonormal basis will have size dimension = 2
dimension_U = 2

# Orthonormal Basis: ortho_basis_U
ortho_basis_U = Set([])

e_1 = zeros(0)
append!(e_1, (1/norm(u_1)).*u_1)
push!(ortho_basis_U, e_1)

println("ortho_basis after element 1 added:")
println(ortho_basis_U)
println("")

for k = 2:dimension_U
	global basis_U
	global ortho_basis_U
	new_element_terms = Set([])	
	for j = 1:k-1
		# Building each <e, y>e in this looping
		term_dot = 0
		for i = 1:size(u_1, 1)
			term_dot += 
			collect(basis_U)[k][i]*collect(ortho_basis_U)[j][i]
		end
		push!(new_element_terms, term_dot.*collect(ortho_basis_U)[j])
	end
	# Summing each <e, y>e term within new_element_terms
	summing_scaled_terms = zeros(size(u_1, 1))
	for n = 1:length(new_element_terms)
		summing_scaled_terms -= collect(new_element_terms)[n]
	end
	# This is y - <e1, y>e1 - ... - <em, y>em in Gram-Schmidt
	new_element_before_scaling = collect(basis_U)[k] + summing_scaled_terms
	push!(ortho_basis_U, 
	       (1/norm(new_element_before_scaling)).*new_element_before_scaling)
	println("ortho_basis after new_element added:")
	println(ortho_basis_U)
	println("")
end

println("Turning Set to Array:")
ortho_basis_U_array = [i for i in ortho_basis_U]
typeof(ortho_basis_U_array)
println(ortho_basis_U_array)

println("")
println("Here, we minimize the distance between our vector v")
println("and the subspace U")
println("")

vector_v = [1, 2, 3, 4]

# Computing the terms of vector_v, written in terms of the orthonormal basis
# for subspace U
terms_projection_U = Set([])
for k = 1:dimension_U
	global basis_U
	global ortho_basis_U
	global vector_v
	global terms_projection_U
	term_dot = vector_v'*collect(ortho_basis_U)[k]
	push!(terms_projection_U, term_dot.*collect(ortho_basis_U)[k])
end

# Summing the terms of vector_v
summing_vector_v_terms = zeros(size(u_1, 1))
for n = 1:length(terms_projection_U)
	global summing_vector_v_terms
	summing_vector_v_terms += collect(terms_projection_U)[n]
end

projection_U = summing_vector_v_terms

println("Here is our projection of vector_v onto subspace U:")
println(projection_U)

println("")
println("Here is the minimum distance between vector_v and subspace U:")
println(norm(vector_v .- projection_U))

