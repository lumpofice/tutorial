# Converting decimal to binary
for n = -2.25:0.25:2
	decimal = n
	binary_array_integer = []
	binary_array_fraction = []
	
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




for n = -2.25:0.25:2
	decimal = n
	binary_array_integer = []
	binary_array_fraction = []
	
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

	binary_input = initial_inputs(decimal, binary_array_integer)
	if binary_input isa String
		if findfirst(".", binary_input) !== nothing
			k = findfirst(".", binary_input)
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
						3,
						binary_input[i]
						)	
					break
				elseif i == k[1]
					insert!(
						binary_input_shift,
						3,
						binary_input[i]
						)
				else
					append!(
						binary_input_shift,
						binary_input[i]
						) 
				end
			end
			println("")
			println(join(string.(binary_input_shift)))
		end
	end
end
