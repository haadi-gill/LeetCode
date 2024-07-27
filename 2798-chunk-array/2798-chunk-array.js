/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length === 0){
        return arr
    }
    if (arr.length < size){
        return [arr]
    }
    var pos = 0
    var subs = []
    while (pos+size <= arr.length){
        subs.push(arr.slice(pos, pos+size))
        pos += size
    }
    if (pos !== arr.length ){
        subs.push(arr.slice(pos, arr.length))
    }
    return subs
};
