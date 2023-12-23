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
			summing_scaled_terms.map((x, index) => 
				x - Array.from(new_element_terms)[m][index]);	
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


// Converting basis for subspace U to orthonormal basis, then using that
// orthonormal basis to find the minimum distance between a vector v
// and the subspace of U

console.log("-----------------------");
console.log("-----------------------");
console.log("-----------------------");
console.log("-----------------------");
console.log("-----------------------");

var u_1 = [1, 1, 0, 0];
var u_2 = [1, 1, 1, 2];

var basis_U = [];
basis_U.push(u_1);
basis_U.push(u_2);

const dimension_U = 2;

var ortho_basis_U = new Set([]);

var e_1 = [];

var the_sum_e_1 = 0;
for (var i = 0; i < u_1.length; i++) {
	the_sum_e_1 += (u_1[i])**2;
}
var norm_u_1 = Math.sqrt(the_sum_e_1);
for (var i = 0; i < u_1.length; i++) {
	var scaled_u_1_coordinate = (1/norm_u_1)*u_1[i];
	e_1.push(scaled_u_1_coordinate);
}

ortho_basis_U.add(e_1);

console.log("Here is ortho_basis_U containing e_1:");
console.log(ortho_basis_U);
console.log("");

for (var k = 2; k < dimension_U + 1; k++) {
	var e = [];
	var new_element_terms = new Set([]);
	for (j = 0; j <= k-2; j++) {
		// Building each <e, y>e in this loop
		var term = [];
		var term_dot = 0;
		for (i = 0; i < u_1.length; i++) {
			term_dot += 
				basis_U[k-1][i]*
				Array.from(ortho_basis_U)[j][i];
		}
		for (var n = 0; n < u_1.length; n++) {
			var scaled_term_coordinate = 
				(term_dot)*Array.from(ortho_basis_U)[j][n];
			term.push(scaled_term_coordinate);
		}
		new_element_terms.add(term);
	}
	// Summing each <e, y>e term within new_element_terms
	var summing_scaled_terms = Array.apply(null, Array(4)).
		map(function (x, i) {return 0;});
	for (var m = 0; m < new_element_terms.size; m++) {
		summing_scaled_terms = 
			summing_scaled_terms.map((x, index) => 
				x - Array.from(new_element_terms)[m][index]);	
	}
	// This is the y - <e1, y>e1 - ... - <em, y>em numerator in the
	// Gram-Schmidt Process
	var new_element_before_scaling = basis_U[k-1].map(function(x, index) {
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
	ortho_basis_U.add(e);
	console.log("ortho_basis_U after new element added:");
	console.log(ortho_basis_U);
	console.log("");
}

console.log("Turning Set to Array:");
var ortho_basis_U_array = Array.from(ortho_basis_U);
console.log(ortho_basis_U_array);

console.log("-----------------------");
console.log("Here, we minimize the distance between our vector v")
console.log("and the subspace U")
console.log("")

var vector_v = [1, 2, 3, 4];

// Computing the terms of vector_v, written in terms of the orthogonal basis
// for subspace U
var terms_projection_U = new Set([]);
for (var k = 0; k < dimension_U; k++) {
	// Building each <v, e>v in the following loops
	var vector_v_term_scalar = 0;
	var vector_v_term = [];
	for (var i = 0; i < vector_v.length; i++) {
		vector_v_term_scalar += 
			vector_v[i]*Array.from(ortho_basis_U)[k][i];
	}
	for (var j = 0; j < vector_v.length; j++) {
		var vector_v_scaled_term_coordinate = 
			vector_v_term_scalar*Array.from(ortho_basis_U)[k][j];
		vector_v_term.push(vector_v_scaled_term_coordinate);
	}
	terms_projection_U.add(vector_v_term);
}
// Summing each <v, e>v term within terms_projection_U
var summing_scaled_vector_v_terms = Array.apply(null, Array(4)).
	map(function (x, i) {return 0;});
for (var n = 0; n < dimension_U; n++) {
	console.log(Array.from(terms_projection_U)[n])
	summing_scaled_vector_v_terms =
		summing_scaled_vector_v_terms.map((x, index) =>
			x + Array.from(terms_projection_U)[n][index]);
}

var projection_U = summing_scaled_vector_v_terms;

console.log("Here is our projection of vector_v onto subspace U:");
console.log(projection_U);

console.log("");
console.log("Here is the minimum distance between vector_v and subspace U:");
var vector_v_minus_projection_U = Array.apply(null, Array(4)).
	map(function (x, i) {
		return Array.from(vector_v)[i] - 
			Array.from(projection_U)[i];
	});
var norm_vector_v_minus_projection_U_sum = 0;
for (var k = 0; k < vector_v.length; k++) {
	norm_vector_v_minus_projection_U_sum += 
		Array.from(vector_v_minus_projection_U)[k]**2;
}
var norm_projection_U = Math.sqrt(norm_vector_v_minus_projection_U_sum);
console.log(norm_projection_U);
