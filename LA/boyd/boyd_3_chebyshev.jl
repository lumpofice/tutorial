using LinearAlgebra;
using VMLS;

#= This is an example of Chebyshev's inequality, in which variable 
a is a single, fixed value 
_______________________________________
_______________________________________
_______________________________________
_______________________________________
=# 

n = 50;
x_scalar = rand(1:n, 40, 1);
count = 0;
count_stdev = 0;
a_scalar = stdev(x_scalar);

for i = 1:size(x_scalar, 1)
	if abs(x_scalar[i]) > a_scalar
		global count += 1;
	end
	if abs(x_scalar[i] - avg(x_scalar)) > a_scalar
		global count_stdev += 1;
	end
end

norm_x_scalar = norm(x_scalar);
println("Norm is ", norm_x_scalar)
println();
rms_x_scalar = norm(x_scalar)/sqrt(size(x_scalar, 1));
rhs_cheby = (rms_x_scalar/a_scalar)^2;
lhs_cheby = count/size(x_scalar, 1);

println("Here is Chebyshev");
println("LHS: ", lhs_cheby);
println("RHS: ", rhs_cheby);
println()

std_x_scalar = stdev(x_scalar);
println("Stadard Deviation is ", std_x_scalar, ":");
println();
rhs_cheby_std = (std_x_scalar/a_scalar)^2;
lhs_cheby_std = count_stdev/size(x_scalar, 1);

println("Here is Chebyshev for standard deviation");
println("LHS: ", lhs_cheby_std);
println("RHS: ", rhs_cheby_std);
println()


#= This is an example of Chebyshev's inequality, 
in which each variable a is a component of a vector 
_______________________________________
_______________________________________
_______________________________________
_______________________________________
=#

a = rand(1:50, 100, 1)

x = rand(1:50, 30, 1)
demean(x) = x .-avg(x)

println("Here is Chebyshev from a vector of a variables.")
println()


for i = 1:size(a)[1]
	count = 0
	for j = 1:size(x)[1]
		if abs(demean(x)[j]) > a[i]
			count += 1
		end
	end
	println("**************************************")
	println("********a is: ", a[i], "**************")
	println("********count is: ", count, "*********")
	println("********std is: ", stdev(x), "*********")
	println("**************************************")
	if count/size(x)[1] >= (stdev(x)/a[i])^2
		println("Chebyshev did not hold.")
		println("LHS:", " ", count/size(x)[1])
		println("RHS:", " ", (stdev(x)/a[i])^2)
		println("-----------------------")
	else
		println("LHS:", " ", count/size(x)[1])
		println("RHS:", " ", (stdev(x)/a[i])^2)
		println("------------------------")
	end
end
