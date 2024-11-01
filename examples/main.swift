// simple data declaration

let num1 : Int = 10
num1 = 20
let num2: Float = 20.01
let strs : String = "Hello"

// array data declaration
let arrs : [Int] = [10,10]
let dicts : [String:Int] = ["a":10,"b":20]


// selection statement
if (num1 > num2) {
    num1 = 1
} else {
    num2 = 2
}

// loops
for i in 10..100 {
    num1 = num1 + 1
}

while (num1 < 10) {
    num1 = num1 + 1
}
repeat {
    num1 = num1 + 1
} while (num1 < 10)


// function declaration
func myFunction(a: Int,b: Int) -> Int {
    a = a + 1
}
