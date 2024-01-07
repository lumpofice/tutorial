// Converting decimal to binary

for (var n = -2; n <= 2; n += 0.5) {
	var decimal = n;
	var binary_array_integer = [];
	var binary_array_fraction = [];

	function initial_inputs(decimal, binary_array_integer) {
		var integer_part = Math.floor(decimal);
		var fractional_part_process_0 = 
			decimal.toString().indexOf(".");
		var fractional_part = 0;
		if (fractional_part_process_0 == -1) {
			fractional_part = 0;
			// the console calls will be removed
			console.log("integer_part: ", integer_part);
			console.log("fractional_part: ", fractional_part);
		}
		else {
			var fractional_part_process_1 = 
				decimal.toString().substring(
					fractional_part_process_0
				);
			fractional_part = 
				Number(fractional_part_process_1);
			if (decimal == -1) {
				console.log("11");
			}
			else if (integer_part == -1) {
				binary_array_integer.push("1");
				// more code here
				// the console calls will be removed
				console.log("integer_part: ", integer_part);
				console.log("fractional_part: ", fractional_part);
			}
			else {
				// more code here
				// the console calls will be removed
				console.log("integer_part: ", integer_part);
				console.log("fractional_part: ", fractional_part);
			}
		}
	}

	initial_inputs(decimal, binary_array_integer);
}
