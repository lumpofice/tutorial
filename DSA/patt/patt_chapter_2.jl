# Here, we are converting from decimal to binary
for n = -8:0.25:8
	decimal = n
	binary_array_integer = []
	
	# Here are the functions that convert decimal to binary
	
	# final_output function takes the array elements and strings them
	# together with a join
	function final_outputs(h, fractional)
		if h == nothing
			h = []
		end
		if isempty(h) && fractional == nothing
			return 0
		elseif isempty(h) && fractional !== nothing
			append!(h, "0")
			arr_string = join(string.(h))
			return arr_string*fractional
		elseif fractional == nothing
			arr_string = 
				join(string.(reverse(h)))
			return arr_string
		else
			arr_string = 
				join(string.(reverse(h)))
			return arr_string*fractional
		end
	end

	# nonnegative constructs the integer array for nonnegative decimals
	function nonnegative(integer_part, binary_array_integer)
		if integer_part == 0
			return 
		end
		for i = 1:integer_part
			if integer_part >= 2^(i)
				continue
			else
				if isempty(binary_array_integer)
					for j = 1:i+1
						append!(
							binary_array_integer, 
							0
							)
					end
				end
				nonnegative(
				    integer_part - 2^(i-1), 
				    binary_array_integer
				    )
				binary_array_integer[i] = 1
				return binary_array_integer
			end
		end
	end

	# negative constructs the integer array for negative decimals
	function negative(x, binary_array_integer)
		if x == 0
			return
		end
		for i = 1:x
			if x >= 2^(i)
				continue
			else
				if isempty(binary_array_integer)
					if x in [(2^(m) - 1) for m in 1:x]
						for j = 1:i+2
							append!(
							  binary_array_integer,
							  0
							  )
						end
					else
						for j = 1:i+1
							append!(
							  binary_array_integer,
							  0
							  )
						end
					end
				end
				negative(x - 2^(i-1), binary_array_integer)
				binary_array_integer[i] = 1
				return
			end
		end
	end

	# rearranging_the_negative replaces 1s with 0s and 0s with 1s
	function rearranging_the_negative(negative)
		for i = 1:size(binary_array_integer, 1)
			if binary_array_integer[i] == 0
				binary_array_integer[i] = 1
			else
				binary_array_integer[i] = 0
			end
		end
		return binary_array_integer
	end

	# signature ascertains the signature of the input decimal
	function signature(integer_part, binary_array_integer)
		if integer_part >= 0
			return nonnegative(integer_part, binary_array_integer)
		else
			return rearranging_the_negative(
				 negative(abs(integer_part)-1, 
				      binary_array_integer)
				 )
		end
	end
	
	# fractional handles the fractional part of the input decimal
	function fractional(d, binary_array_fraction)
		if d == 0
			return
		end
		i = 1
		while d > 0
			while d < (2.0)^(-i)
				append!(binary_array_fraction, 0)
				i += 1
			end
			append!(binary_array_fraction, 1)
			d = d - (2.0)^(-i)
			i += 1
		end
		binary_array_fraction = vcat(["."], binary_array_fraction)
		arr_frac_string = join(string.(binary_array_fraction))
		return arr_frac_string
	end

	# initial_inputs delegates where the input goes
	function initial_inputs(decimal, binary_array_integer)
		binary_array_fraction = []
		decimal_parts = modf(decimal)
		integer_part = floor(Int, decimal_parts[2])
		fractional_part = decimal_parts[1]
		if decimal == -1
			println("11")
		elseif integer_part == -1
			append!(binary_array_integer, "11")
			println(final_outputs(
				binary_array_integer,
				fractional(
					   abs(fractional_part), 
					   binary_array_fraction
					   )
				)
			)
		elseif integer_part == 0 && fractional_part < 0
			append!(binary_array_integer, "1")
			println(final_outputs(
				binary_array_integer,
				fractional(
					   abs(fractional_part),
					   binary_array_fraction
					   )
				)
			)
		else
			println(final_outputs(
				signature(integer_part, binary_array_integer), 
				fractional(
					   abs(fractional_part), 
					   binary_array_fraction
					   )
				)
			)
		end
	end

	initial_inputs(decimal, binary_array_integer)
end
println("")
println("---------------------------------------------------------------------")
println("---------------------------------------------------------------------")
println("---------------------------------------------------------------------")
println("")
# We reiterate the decimal to binary coversion as we convert from binary 
# to 32-bit floating point. We start by shifting any present or non-present
# decimal point to the n+1 position, where position n contains the first 
# nonnegative 1 of the binary representation. From there, we construct the 
# exponent of the 32-bit decimal representation. We strip away everything
# up to and including the decimal point, from the left. We append '0' to what 
# remains of that, until 23 bits of data are acheived. 
for n = -8:0.25:8
	decimal = n
	binary_array_integer = []
	
	# Here are the functions that convert decimal to binary
	
	# final_output function takes the array elements and strings them
	# together with a join
	function final_outputs(h, fractional)
		if h == nothing
			h = []
		end
		if isempty(h) && fractional == nothing
			return 0
		elseif isempty(h) && fractional !== nothing
			append!(h, "0")
			arr_string = join(string.(h))
			return arr_string*fractional
		elseif fractional == nothing
			arr_string = 
				join(string.(reverse(h)))
			return arr_string
		else
			arr_string = 
				join(string.(reverse(h)))
			return arr_string*fractional
		end
	end

	# nonnegative constructs the integer array for nonnegative decimals
	function nonnegative(integer_part, binary_array_integer)
		if integer_part == 0
			return 
		end
		for i = 1:integer_part
			if integer_part >= 2^(i)
				continue
			else
				if isempty(binary_array_integer)
					for j = 1:i+1
						append!(
							binary_array_integer, 
							0
							)
					end
				end
				nonnegative(
				    integer_part - 2^(i-1), 
				    binary_array_integer
				    )
				binary_array_integer[i] = 1
				return binary_array_integer
			end
		end
	end

	# negative constructs the integer array for negative decimals
	function negative(x, binary_array_integer)
		if x == 0
			return
		end
		for i = 1:x
			if x >= 2^(i)
				continue
			else
				if isempty(binary_array_integer)
					if x in [(2^(m) - 1) for m in 1:x]
						for j = 1:i+2
							append!(
							  binary_array_integer,
							  0
							  )
						end
					else
						for j = 1:i+1
							append!(
							  binary_array_integer,
							  0
							  )
						end
					end
				end
				negative(x - 2^(i-1), binary_array_integer)
				binary_array_integer[i] = 1
				return
			end
		end
	end

	# rearranging_the_negative replaces 1s with 0s and 0s with 1s
	function rearranging_the_negative(negative)
		for i = 1:size(binary_array_integer, 1)
			if binary_array_integer[i] == 0
				binary_array_integer[i] = 1
			else
				binary_array_integer[i] = 0
			end
		end
		return binary_array_integer
	end

	# signature ascertains the signature of the input decimal
	function signature(integer_part, binary_array_integer)
		if integer_part >= 0
			return nonnegative(integer_part, binary_array_integer)
		else
			return rearranging_the_negative(
				 negative(abs(integer_part)-1, 
				      binary_array_integer)
				 )
		end
	end
	
	# fractional handles the fractional part of the input decimal
	function fractional(d, binary_array_fraction)
		if d == 0
			return
		end
		i = 1
		while d > 0
			while d < (2.0)^(-i)
				append!(binary_array_fraction, 0)
				i += 1
			end
			append!(binary_array_fraction, 1)
			d = d - (2.0)^(-i)
			i += 1
		end
		binary_array_fraction = vcat(["."], binary_array_fraction)
		arr_frac_string = join(string.(binary_array_fraction))
		return arr_frac_string
	end

	# initial_inputs delegates where the input goes
	function initial_inputs(decimal, binary_array_integer)
		binary_array_fraction = []
		decimal_parts = modf(decimal)
		integer_part = floor(Int, decimal_parts[2])
		fractional_part = decimal_parts[1]
		if decimal == -1
			return "11"
		elseif integer_part == -1
			append!(binary_array_integer, "11")
			return final_outputs(
				binary_array_integer,
				fractional(
					   abs(fractional_part), 
					   binary_array_fraction
					   )
				)
		elseif integer_part == 0 && fractional_part < 0
			append!(binary_array_integer, "1")
			return final_outputs(
				binary_array_integer,
				fractional(
					   abs(fractional_part),
					   binary_array_fraction
					   )
				)
		else
			return final_outputs(
				signature(integer_part, binary_array_integer), 
				fractional(
					   abs(fractional_part), 
					   binary_array_fraction
					   )
				)
		end
	end

	# ---------------------------------------------------------------------
	# Coverting binary to 32-bit floating point
	# ---------------------------------------------------------------------

	if decimal < 0
		first_position = "1"
		binary_input = initial_inputs(
			abs(decimal), binary_array_integer
			)
		if binary_input isa String
			# The following if case handles binary inputs with 
			# decimals, which means these binary inputs could 
			# have absolute values less than zero, which means 
			# that if the exponent has length less than 8 bits, 
			# we will need to insert '0' at the front of 
			# the exponent until the exponent has a length 
			# of 8 bits.
			if findfirst(".", binary_input) !== nothing
				k = findfirst(".", binary_input)
				ones_position = findfirst("1", binary_input)
				# ---------------------------------------------
				# EXPONENT
				# ---------------------------------------------
				# Building the exponent
				k_minus_ones_position = k[1] - ones_position[1]
				decimal_exponent = 127 + k_minus_ones_position
				floating_point_exponent = 
					initial_inputs(decimal_exponent, [])
				floating_point_exponent_zero_removed = 
					deleteat!(collect(
						floating_point_exponent), 1)
				while length(
					floating_point_exponent_zero_removed
					) < 8
					insert!(
					floating_point_exponent_zero_removed,
					1,'0')
				end
				println("decimal: ", decimal)
				println("floating exponent: ",
					join(
					string.(
					floating_point_exponent_zero_removed
					))
					)
				# Shifting the decimal point to the n+1 
				# position, where position n contains 
				# the first nonnegative 1
				binary_input_shift = []
				for i in 1:length(binary_input)
					if i == k[1] && k[1] == 2
						for j in 3:length(binary_input)
							append!(
							binary_input_shift,
							binary_input[j]
							)
						end
						insert!(
							binary_input_shift,
							ones_position[1],
							binary_input[i]
							)	
						break
					elseif i == k[1]
						insert!(
							binary_input_shift,
							ones_position[1] + 1,
							binary_input[i]
							)
					else
						append!(
							binary_input_shift,
							binary_input[i]
							) 
					end
				end
				println("binary: ", binary_input)
				println("shifting the binary decimal: ", 
					join(string.(binary_input_shift)))
				# ---------------------------------------------
				# FRACTION
				# ---------------------------------------------
				# Here, strip away the information up to and 
				# including the decimal point, from the left.
				if isassigned(
					binary_input_shift,ones_position[1]+1)
					if k[1] == 2
						float_fraction = deleteat!(
						  	binary_input_shift, 
						  	1:ones_position[1]
						  	)
						while length(
							float_fraction) < 23
							append!(float_fraction,
								 '0')
						end
					else
						float_fraction = deleteat!(
							  binary_input_shift,
							  1:ones_position[1]+1
							  )
						while length(
							float_fraction) < 23
							append!(float_fraction,
								 '0')
						end
					end
				else
					float_fraction = 
						"00000000000000000000000"
				end
				println("float fraction: ", 
					join(string.(float_fraction)))
			else
				k = length(binary_input) + 1
				ones_position = findfirst(
						"1", binary_input)
				# ---------------------------------------------
				# EXPONENT
				# ---------------------------------------------
				# Building the exponent
				k_minus_ones_position = k[1] - ones_position[1]
				decimal_exponent = 127 + k_minus_ones_position
				floating_point_exponent = 
					initial_inputs(decimal_exponent, [])
				floating_point_exponent_zero_removed = 
					deleteat!(collect(
						floating_point_exponent), 1)
				println("decimal: ", decimal)
				println("floating exponent: ",
					join(
					string.(
					floating_point_exponent_zero_removed
					))
					)
				binary_input_shift = []
				for i in 1:length(binary_input)
					append!(binary_input_shift, 
						 binary_input[i])
				end
				insert!(binary_input_shift, 
					 ones_position[1] + 1, ".")
				println("binary: ", binary_input)
				println("shifting the binary decimal: ",
					join(string.(binary_input_shift)))
				# ---------------------------------------------
				# FRACTION
				# ---------------------------------------------
				# Here, strip away the information up to and 
				# including the decimal point, from the left.
				if isassigned(binary_input_shift,
					       ones_position[1]+2)
					float_fraction = deleteat!(
						binary_input_shift,
						1:ones_position[1]+1
						)
					while length(
						float_fraction) < 23
						append!(float_fraction,
							 '0')
					end
				else
					float_fraction = 
						"00000000000000000000000"
				end
				println("float fraction: ",
					join(string.(float_fraction)))
			end
		else
			println(binary_input)
		end
	else
		first_position = "0"
		binary_input = initial_inputs(decimal, binary_array_integer)
		if binary_input isa String
			# The following if case handles binary inputs with 
			# decimals, which means these binary inputs could 
			# have absolute values less than zero, which means 
			# that if the exponent has length less than 8 bits, 
			# we will need to insert '0' at the front of 
			# the exponent until the exponent has a length 
			# of 8 bits.
			if findfirst(".", binary_input) !== nothing
				k = findfirst(".", binary_input)
				ones_position = findfirst("1", binary_input)
				# ---------------------------------------------
				# EXPONENT
				# ---------------------------------------------
				# Building the exponent
				k_minus_ones_position = k[1] - ones_position[1]
				decimal_exponent = 127 + k_minus_ones_position
				floating_point_exponent = 
					initial_inputs(decimal_exponent, [])
				floating_point_exponent_zero_removed = 
					deleteat!(collect(
						floating_point_exponent), 1)
				while length(
					floating_point_exponent_zero_removed
					) < 8
					insert!(
					floating_point_exponent_zero_removed,
					1,'0')
				end
				println("decimal: ", decimal)
				println("floating exponent: ",
					join(
					string.(
					floating_point_exponent_zero_removed
					))
					)
				# Shifting the decimal point to the n+1 
				# position, where position n contains 
				# the first nonnegative 1
				binary_input_shift = []
				for i in 1:length(binary_input)
					if i == k[1] && k[1] == 2
						for j in 3:length(binary_input)
							append!(
							binary_input_shift,
							binary_input[j]
							)
						end
						insert!(
							binary_input_shift,
							ones_position[1],
							binary_input[i]
							)	
						break
					elseif i == k[1]
						insert!(
							binary_input_shift,
							ones_position[1] + 1,
							binary_input[i]
							)
					else
						append!(
							binary_input_shift,
							binary_input[i]
							) 
					end
				end
				println("binary: ", binary_input)
				println("shifting the binary decimal: ", 
					join(string.(binary_input_shift)))
				# ---------------------------------------------
				# FRACTION
				# ---------------------------------------------
				# Here, strip away the information up to and 
				# including the decimal point, from the left.
				if isassigned(
					binary_input_shift,ones_position[1]+1)
					if k[1] == 2
						float_fraction = deleteat!(
						  	binary_input_shift, 
						  	1:ones_position[1]
						  	)
						while length(
							float_fraction) < 23
							append!(float_fraction,
								 '0')
						end
					else
						float_fraction = deleteat!(
							  binary_input_shift,
							  1:ones_position[1]+1
							  )
						while length(
							float_fraction) < 23
							append!(float_fraction,
								 '0')
						end
					end
				else
					float_fraction = 
						"00000000000000000000000"
				end
				println("float fraction: ", 
					join(string.(float_fraction)))
			else
				k = length(binary_input) + 1
				ones_position = findfirst(
						"1", binary_input)
				# ---------------------------------------------
				# EXPONENT
				# ---------------------------------------------
				# Building the exponent
				k_minus_ones_position = k[1] - ones_position[1]
				decimal_exponent = 127 + k_minus_ones_position
				floating_point_exponent = 
					initial_inputs(decimal_exponent, [])
				floating_point_exponent_zero_removed = 
					deleteat!(collect(
						floating_point_exponent), 1)
				println("decimal: ", decimal)
				println("floating exponent: ",
					join(
					string.(
					floating_point_exponent_zero_removed
					))
					)
				binary_input_shift = []
				for i in 1:length(binary_input)
					append!(binary_input_shift, 
						 binary_input[i])
				end
				insert!(binary_input_shift, 
					 ones_position[1] + 1, ".")
				println("binary: ", binary_input)
				println("shifting the binary decimal: ",
					join(string.(binary_input_shift)))
				# ---------------------------------------------
				# FRACTION
				# ---------------------------------------------
				# Here, strip away the information up to and 
				# including the decimal point, from the left.
				if isassigned(binary_input_shift,
					       ones_position[1]+2)
					float_fraction = deleteat!(
						binary_input_shift,
						1:ones_position[1]+1
						)
					while length(
						float_fraction) < 23
						append!(float_fraction,
							 '0')
					end
				else
					float_fraction = 
						"00000000000000000000000"
				end
				println("float fraction: ",
					join(string.(float_fraction)))
			end
		else
			first_poisition = "0"
			floating_point_exponent_zero_removed = "00000000"
			float_fraction = "00000000000000000000000"
		end
	end
	println("32-bit float: ", first_position*" "*
		join(string.(floating_point_exponent_zero_removed))*" "*
		join(string.(float_fraction)))
		println("")
end

