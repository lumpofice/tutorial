// Chebyshev
console.log("Here is Chebyshev with a fixed a varaible.");
console.log("");
var n = 50;
var x = Array.from({length: 40}, () => Math.floor(Math.random()*n));

// Finding the average of the x coordinates
var sum_x_terms = 0;
for (var i = 0; i < x.length; i++) {
	sum_x_terms += x[i];
}
var mean_x = sum_x_terms/x.length;

// De-mean the vector x
var demean_x = Array.apply(null, Array(0)).map(function () {});
for (var i = 0; i < x.length; i++) {
	demean_x.push(x[i] - mean_x);
}

// The square terms in the standard deviation calculation--a vector
var stdev_x_square_terms = Array.apply(null, Array(0)).map(function () {});
for (var i = 0; i < x.length; i++) {
	stdev_x_square_terms.push((demean_x[i])**2);
}

// Calculating the standard deviation of x
var stdev_x_square_terms_sum = 0;
for (var i = 0; i < x.length; i++) {
	stdev_x_square_terms_sum += stdev_x_square_terms[i];
}

var stdev_x = Math.sqrt(stdev_x_square_terms_sum/x.length);
console.log("stdev_x:");
console.log(stdev_x);
console.log("");

// Counting the number of coordinates in the de-meaned x vector that are
// larger than the stdev_x
var count = 0;
for (var i = 0; i < x.length; i++) {
	if (Math.abs(demean_x[i]) > stdev_x) {
		count += 1;
	}
}

console.log("Chebyshev, when a = stdev_x: count/x.length < 1")
console.log("The LHS of Chebyshev:")
console.log(count/x.length);

if (count/x.length < (stdev_x/stdev_x)**2) {
	console.log("Chebyshev works when a = stdev_x");
}


// Chebyshev on each coordinate of a random vector
console.log("");
console.log("Chebyshev with a varaibles contained within a vector.");
var a = Array.from({length : 40}, () => Math.ceil(Math.random()*n));
var x_vector = Array.from({length: 40}, () => Math.floor(Math.random()*n));

// Computing the mean of vector x
var sum_x_vector_terms = 0;
for (var i = 0; i < x_vector.length; i++) {
	sum_x_vector_terms += x_vector[i];
}

var mean_x_vector = sum_x_vector_terms/x_vector.length

// Demeaning vector x
var demean_x_vector = Array.apply(null, Array(0)).map(function () {});
for (var i = 0; i < x_vector.length; i++) {
	demean_x_vector.push(x_vector[i] - mean_x_vector);
}

// Computing the standard deviation of x
var x_vector_stdev_square_terms = 
	Array.apply(null, Array(0)).map(function () {});
for (var i = 0; i < x_vector.length; i++) {
	x_vector_stdev_square_terms.push(demean_x_vector[i]**2);
}

var x_vector_stdev_square_terms_sum = 0;
for (var i = 0; i < x_vector.length; i++){
	x_vector_stdev_square_terms_sum += x_vector_stdev_square_terms[i];
}

var stdev_x_vector = 
	Math.sqrt(x_vector_stdev_square_terms_sum/x_vector.length);
console.log("");
console.log("stdev_x_vector");
console.log(stdev_x_vector);
console.log("");

// Iterating over vector a and comparing LHS with RHS of Chebyshev for 
// each coordinate of vector a
for (var i = 0; i < a.length; i++){
	var count_vector = 0;
	for (var j = 0; j < x_vector.length; j++){
		if (Math.abs(demean_x_vector[j]) > a[i]){
			count_vector += 1;
		}
	}
	console.log("---------------------");
	console.log("-------a is:---------");
	console.log(a[i]);
	console.log("-------count is:-----");
	console.log(count_vector);
	console.log("---stdev is:---------");
	console.log(stdev_x_vector);
	console.log("---------------------");
	if ((count_vector/x_vector.length) >= (stdev_x_vector/a[i])**2){
		console.log("Chebyshev did not hold");
		console.log("LHS:");
		console.log(count_vector/x_vector.length);
		console.log("RHS:");
		console.log((stdev_x_vector/a[i])**2);
		console.log("----------------");
	}
	else {	
		console.log("LHS:");
		console.log(count_vector/x_vector.length);
		console.log("RHS:");
		console.log((stdev_x_vector/a[i])**2);
		console.log("----------------");
	}
}
