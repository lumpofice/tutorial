# Converting decimal to binary
num = 50
arr = []
function f(x, arr)
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
			f(x - 2^(i-1), arr)
			arr[i] = 1
			return arr
		end
	end
end
raw_array = f(num, arr)
println(join(string.(reverse(raw_array))))

