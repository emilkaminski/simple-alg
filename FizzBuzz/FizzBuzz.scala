object FizzBuzz{
    def main(args:Array[String]){
        for (i <- 1 to 100) {
            var x3:Int = i%3
            var x5:Int = i%5
            if (x3 != 0 & x5 != 0) println(i)
            if (x3 == 0 & x5 != 0) println("Fizz")
            if (x3 != 0 & x5 == 0) println("Buzz")
            if (x3 == 0 & x5 == 0) println("FizzBuzz")
        }
    }
}