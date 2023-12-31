# Converting decimal to binary
for n = 2:.5:4
	num = n
	arr = []
	arr_frac = []
	function g(h, t)
		if isempty(arr)
			return 0
		else
			arr_string = join(string.(reverse(arr)))
			return arr_string*t
		end
	end
	function f_1(x, arr)
		if x == 0
			return 
		end
		for i = 1:x
			if x >= 2^(i)
				continue
			else
				if isempty(arr)
					for j = 1:i+1
						append!(arr, 0)
					end
				end
				f_1(x - 2^(i-1), arr)
				arr[i] = 1
				return arr
			end
		end
	end
	function f_2(x, arr)
		if x == 0
			return
		end
		for i = 1:x
			if x >= 2^(i)
				continue
			else
				if isempty(arr)
					if x in [(2^(m) - 1) for m in 1:x]
						for j = 1:i+2
							append!(arr, 0)
						end
					else
						for j = 1:i+1
							append!(arr, 0)
						end
					end
				end
				f_2(x - 2^(i-1), arr)
				arr[i] = 1
				return
			end
		end
	end
	function j(f_2)
		for i = 1:size(arr, 1)
			if arr[i] == 0
				arr[i] = 1
			else
				arr[i] = 0
			end
		end
		return arr
	end
	function h(x, arr)
		if x >= 0
			return f_1(x, arr)
		else x < 0
			return j(f_2(abs(x)-1, arr))
		end
	end
	function t(d, arr_frac)
		i = 1
		while d > 0
			while d < (2.0)^(-i)
				append!(arr_frac, 0)
				i += 1
			end
			append!(arr_frac, 1)
			d = d - (2.0)^(-i)
			i += 1
		end
		arr_frac = vcat(["."], arr_frac)
		arr_frac_string = join(string.(arr_frac))
		return arr_frac_string
	end
	function k(num, arr)
		parts = modf(num)
		integer_part = floor(Int, parts[2])
		fractional_part = parts[1]
		if num == -1
			println(11)
		else
			println(g(
				h(integer_part, arr), 
				t(abs(fractional_part), arr_frac)
				)
			)
		end
	end
	k(num, arr)
end
