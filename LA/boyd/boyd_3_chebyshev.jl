using LinearAlgebra;
using VMLS;

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

