# Minimum distance between point p, which lies along vector a-b, and a 
# random point x
using LinearAlgebra
using VMLS

a = rand(1:50, 40, 1);
b = rand(1:50, 40, 1);

# Line through a and b
line(theta) = (1 - theta).*a .+ theta.*b;

# theta below is the minimum theta
theta(x) = -( sum( (a .- x).*(b .- a) ) )./( (norm(b .- a))^2 );

# p will be line(theta(x))

x = rand(1:50, 40, 1);

# The minimum distance between p and x should be perpendicular to the line
# a-b
perpendicular = sum( ( line(theta(x)) .- x ).*( a .- b ) );

println(perpendicular);

