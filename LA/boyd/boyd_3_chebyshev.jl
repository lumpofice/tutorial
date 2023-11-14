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
x = rand(1:n, 40, 1);
count = 0;
a = stdev(x);

for i = 1:size(x, 1)
	if abs(x[i] - avg(x)) > a
		global count += 1;
	end
end

println("Total coordinates above ", a, ":");
println(count);
println();

norm_x = norm(x);
println("Norm is ", norm_x)
println();
rms_x = norm(x)/sqrt(size(x, 1));
rhs_cheby = (rms_x/a)^2;
lhs_cheby = count/size(x, 1);

println("Here is Chebyshev");
println("LHS: ", lhs_cheby);
println("RHS: ", rhs_cheby);
println()

std_x = stdev(x);
println("Stadard Deviation is ", std_x, ":");
println();
rhs_cheby_std = (std_x/a)^2;
lhs_cheby_std = count/size(x, 1);

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

count = 0

for i = 1:size(a)[1]
	for j = 1:size(x)[1]
		if abs(demean(x)[j]) > abs(a[i] - avg(x))
			global count += 1
		end
	end
	if count/size(x)[1] >= (stdev(x)/abs(a[i] - avg(x)))^2
		println("Chebyshev did not hold.")
		println("LHS:", " ", count/size(x)[1])
		println("RHS:", " ", (stdev(x)/(a[i] - avg(x)))^2)
		println("-----------------------")
	else
		println("LHS:", " ", count/size(x)[1])
		println("RHS:", " ", (stdev(x)/(a[i] - avg(x)))^2)
		println("------------------------")
	end
end
