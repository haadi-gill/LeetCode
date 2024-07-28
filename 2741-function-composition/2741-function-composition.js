/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        return recurse(x, functions.length-1)
    }

    function recurse(val, index){
        if (index < 0){
            return val
        }
        val = functions[index](val)
        return recurse(val, index-1)
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */