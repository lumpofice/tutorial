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

for (var i = 0; i < x.length; i++) {
	var scaled_x_coordinate = (1/norm_x)*x[i];
	e.push(scaled_x_coordinate);
}

console.log("Here is e_1:");
console.log(e);

set_e.add(e);

console.log("Here is set_e containing e_1:");
console.log(set_e);

for (var k = 0; k < OB-1; k++) {
	var e = [];
	var new_element_terms = new Set([]);
	for (j = 0; j <= k; j++) {
		var term = [];
		var term_dot = 0;
		for (i = 0; i < x.length; i++) {
			term_dot += y[i]*Array.from(set_e)[j][i];
		}
		for (var n = 0; n < x.length; n++) {
			var scaled_term_coordinate = 
				(term_dot)*Array.from(set_e)[j][n];
			term.push(scaled_term_coordinate);
		}
		new_element_terms.add(term);
	}
	var summing_non_y_terms = Array.apply(null, Array(4)).
		map(function (x, i) {return 0;});
	for (var m = 0; m < new_element_terms.size; m++) {
		summing_non_y_terms = 
			summing_non_y_terms.map(
				(x, index) => x - 
				Array.from(new_element_terms)[m][index]
			);	
	}
	var new_element_before_scaling = y.map(function(x, index) {
		return x + summing_non_y_terms[index];
	});
	var the_sum = 0;
	for (a = 0; a < new_element_before_scaling.length; a++) {
		the_sum += (new_element_before_scaling[a])**2;
	}
	var norm_new_element_before_scaling = Math.sqrt(the_sum);
	for (b = 0; b < new_element_before_scaling.length; b++) {
		e.push((1/norm_new_element_before_scaling)*
		new_element_before_scaling[b]);
	}
	set_e.add(e);
	console.log("set_e after element 2 added:");
	console.log(set_e);
}
