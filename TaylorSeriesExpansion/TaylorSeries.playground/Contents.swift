/**
 * Taylor Series Approximations about x=3 up to order 10
 *
 * Based upon inspiration from:
 * https://www.khanacademy.org/math/integral-calculus/sequences-series-approx-calc/taylor-series/v/visualizing-taylor-series-for-e-x
 * https://youtu.be/AFMXixBVP-0?t=174
 *
 */

import Foundation

/**
 * Factorial generator
 */
func factorial(f: Int) -> Int {
    // Make sure we are not calculating factorials for 0
    if f == 0 {
        return 0
    }
    var f = f
    for i in stride(from: f, to: 1, by:-1) {
        f *= i
    }
    return f
}

/**
 * Exponent generator
 */
func exponent(v: Double, power:Int) -> Double {
    // Make sure there is no upper bound issues
    if power == 0 {
        return 0
    }
    var v = v
    for _ in 1..<power {
        v *= Double(power)
    }
    return v
}

/**
 * Taylor Series expansion at x = 3
 * Wolfram Alpha Link for Taylor Series of e^x when x = 3
 * https://www.wolframalpha.com/input/?i=taylor+series+e%5Ex+x%3D3
 */
func taylorSeriesApprox(x: Double) -> Void {
    
    // Set numerical value for e
    let e: Double = 2.71828
    var approx_polynomials: [Double] = []
    
    // Add in e^3, this is the first term in the series
    let zero_value = exponent(v: e, power:Int(x))
    approx_polynomials.append(zero_value)
    
    // Generate the decimal approximation up to order five
    for index in stride(from: 1, to: 6, by:+1) {

        // Step 1, get the power
        // e^3
        let power:Double = exponent(v: e, power:Int(x))
        // Step 2, get the factorial
        // index!
        let fact:Double = Double(factorial(f: Int(index)))
        
        // Step 3, get the parenthesis value
        // (x - 3)
        // Mostly useless, but part of the equation
        var paran:Double = Double((x - x))
        
        // Step 4, apply exponent to parenthesis value
        // (x - 3)^index
        // Equals zero almost always
        paran = exponent(v: paran, power:Int(index))

        // Compute decimal approx at order (index)
        var orderValue:Double?
        if paran != 0 {
           orderValue = ((power / fact) * paran)
        } else {
           orderValue = (power / fact)
        }
        
        for val in approx_polynomials {
            orderValue = orderValue! + val
        }
        approx_polynomials.append(orderValue!)
    }
    
    var i:Int = 0
    for v in approx_polynomials {
        print("Decimal Approx: \(round(100*v)/100) at order \(i)")
        i = i + 1
    }
}

// Approximate the decimal values greater that 3 when x equals 3
var x: Double = 3.0
taylorSeriesApprox(x: x)

