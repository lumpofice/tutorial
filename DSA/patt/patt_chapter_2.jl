# Converting decimal to binary
num = 0 
arr = []
function g(h)
	if isempty(arr)
		return 0
	else
		return join(string.(reverse(arr)))
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
function h(x, arr)
	if x >= 0
		return f_1(x, arr)
	else x < 0
		return f_2(x, arr)
	end
end
println(g(h(num, arr)))

