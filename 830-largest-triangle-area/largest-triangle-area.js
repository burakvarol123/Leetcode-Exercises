/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function(points) {
    const area = (a, b ,c) => Math.abs((b[0] -a[0])*(c[1]- a[1])- (b[1]-a[1])*(c[0]-a[0]))/2
    let best = 0
    const n = points.length;
    for (let i=0; i  <n; i++){
        for (let j=i+1; j < n; j++){
            for (let k= j +1; k < n; k++){
                best = Math.max(best, area(points[i], points[j], points[k]));
            }
        }
    } 
    return best;
};