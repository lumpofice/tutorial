// Orthonormal Basis of four dimensions

var x_1 = [1, 0, 0, 0];
var x_2 = [0, 1, 0, 0];
var x_3 = [0, 0, 1, 0];
var x_4 = [0, 0, 0, 1];

var basis = [];
basis.push(x_1);
basis.push(x_2);
basis.push(x_3);
basis.push(x_4);

const dimension = 4;

var ortho_basis = new Set([]);

var e = [];

var the_sum = 0;
for (var i = 0; i < x_1.length; i++) {
	the_sum += (x_1[i])**2;
}
var norm_x_1 = Math.sqrt(the_sum);
for (var i = 0; i < x_1.length; i++) {
	var scaled_x_1_coordinate = (1/norm_x_1)*x_1[i];
	e.push(scaled_x_1_coordinate);
}

ortho_basis.add(e);

console.log("Here is ortho_basis containing e_1:");
console.log(ortho_basis);
console.log("");

for (var k = 2; k < dimension+1; k++) {
	var e = [];
	var new_element_terms = new Set([]);
	for (j = 0; j <= k-2; j++) {
		// Building each <e, y>e in this loop
		var term = [];
		var term_dot = 0;
		for (i = 0; i < x_1.length; i++) {
			term_dot += basis[k-1][i]*Array.from(ortho_basis)[j][i];
		}
		for (var n = 0; n < x_1.length; n++) {
			var scaled_term_coordinate = 
				(term_dot)*Array.from(ortho_basis)[j][n];
			term.push(scaled_term_coordinate);
		}
		new_element_terms.add(term);
	}
	// Summing each <e, y>e term within new_element_terms
	var summing_scaled_terms = Array.apply(null, Array(4)).
		map(function (x, i) {return 0;});
	for (var m = 0; m < new_element_terms.size; m++) {
		summing_scaled_terms = 
			summing_scaled_terms.map((x, index) => x - Array.from(new_element_terms)[m][index]);	
	}
	// This is the y - <e1, y>e1 - ... - <em, y>em numerator in the
	// Gram-Schmidt Process
	var new_element_before_scaling = basis[k-1].map(function(x, index) {
		return x + summing_scaled_terms[index];
	});
	// This is the norm in the denominator of the Gram-Schmidt Process
	var the_sum = 0;
	for (a = 0; a < new_element_before_scaling.length; a++) {
		the_sum += (new_element_before_scaling[a])**2;
	}
	var norm_new_element_before_scaling = Math.sqrt(the_sum);
	// This loop applies the norm to each term in the 
	// new_element_before_scaling
	for (b = 0; b < new_element_before_scaling.length; b++) {
		e.push((1/norm_new_element_before_scaling)*
		new_element_before_scaling[b]);
	}
	ortho_basis.add(e);
	console.log("ortho_basis after new element added:");
	console.log(ortho_basis);
	console.log("");
}

console.log("Turning Set to Array:");
var ortho_basis_array = Array.from(ortho_basis);
console.log(ortho_basis_array);
