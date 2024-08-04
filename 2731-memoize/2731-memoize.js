/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    a = {}
    return function(...args) {
        if (!(args in a)){
            a[args] = fn(...args)
        }
        return a[args]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */