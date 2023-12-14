// Chebyshev
console.log("Here is Chebyshev with a fixed a varaible.");
console.log("");
var n = 50;
var x = Array.from({length: 40}, () => Math.floor(Math.random()*50));

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
	if (demean_x[i] > stdev_x) {
		count += 1;
	}
}

console.log("Chebyshev, when a = stdev_x: count/x.length < 1")
console.log("The LHS of Chebyshev:")
console.log(count/x.length);

if (count/x.length < (stdev_x/stdev_x)**2) {
	console.log("Chebyshev works when a = stdev_x");
}

