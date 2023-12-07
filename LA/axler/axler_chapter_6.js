// Orthonormal Basis of two dimensions

var x = [1, 2, 3, -4];
var y = [-5, 4, 3, 2];

const OB = 2;

var set_e = new Set([]);

console.log("Here is x:");
console.log(x);

console.log("Here is y:");
console.log(y);

var e = [];

var the_sum = 0;
for (var i = 0; i < x.length; i++) {
	the_sum += (x[i])**2;
}
var norm_x = Math.sqrt(the_sum);
console.log(norm_x);

for (var i = 0; i < x.length; i++) {
	var scaled_x_coordinate = (1/norm_x)*x[i];
	e.push(scaled_x_coordinate);
}

console.log("Here is e_1:")
console.log(e);

set_e.add(e);

console.log("Here is set_e containing e_1:")
console.log(set_e)

