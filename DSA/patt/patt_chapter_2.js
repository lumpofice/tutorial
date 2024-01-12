// Converting decimal to binary

for (var n = -2; n <= 2; n += 0.5) {
	var decimal = n;
	var binary_array_integer = [];
	var binary_array_fraction = [];

	function final_outputs(h, fractional) {
		if (
			binary_array_integer.length == 0 && 
			fractional === undefined 
		) {
			return 0;
		}
		else if (
			binary_array_integer.length == 0 && 
			fractional !== undefined
		) {
			binary_array_integer.push("0");
			var arr_string = binary_array_integer.join("");
			return arr_string.concat('', fractional);
		}
		else {
			var arr_string =
				binary_array_integer.reverse().join("");
			return arr_string.concat('', fractional);
		}
		// more code here
	}

	function fractional(d, binary_array_fraction) {
		if (d == 0) {
			return
		}
		var i = 1;
		while (d > 0) {
			while (d < (2.0)**(-i)) {
				binary_array_fraction.push(0);
				i += 1;
			}
			binary_array_fraction.push(1);
			d = d - (2.0)**(-i);
			i += 1;
		}
		binary_array_fraction.splice(0, 0, ".");
		var arr_frac_string = binary_array_fraction.join("");
		return arr_frac_string
	}

	function initial_inputs(decimal, binary_array_integer) {
		var integer_part;
		var fractional_part_process_0;
		var fractional_part_process_1;
		var fractional_part;
		if (decimal < 0) {
			integer_part = Math.ceil(decimal);
		}
		else {
			integer_part = Math.floor(decimal);
		}
		fractional_part_process_0 = 
			decimal.toString().indexOf(".");
		if (fractional_part_process_0 == -1) {
			if (decimal == -1) {
				console.log("11");
			}
		}
		else {
			fractional_part_process_1 = 
				decimal.toString().substring(
					fractional_part_process_0
				);
			if (decimal < 0) {
				fractional_part = 
					(-1)*Number(fractional_part_process_1);
			}
			else {
				fractional_part = 
					Number(fractional_part_process_1);
			}
			if (integer_part == -1) {
				binary_array_integer.push("11");
				console.log(
				    final_outputs(
					binary_array_integer,
					fractional(
						Math.abs(fractional_part),
						binary_array_fraction
					)
				    )
				);
			}
			else if (integer_part == 0 && fractional_part < 0) {
				binary_array_integer.push("1");
				console.log(
					final_outputs(
						binary_array_integer,
						fractional(
						    Math.abs(fractional_part),
						    binary_array_fraction
						)
					)
				);
			}
		}
	}

	initial_inputs(decimal, binary_array_integer);
}
