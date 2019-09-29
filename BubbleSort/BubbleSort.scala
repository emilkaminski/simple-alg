object BubbleSort {

    val arr = Array(1,4,5,11,7,3,19,12)

    def main (args: Array[String]) {

        for (a <- 0 to (arr.length - 1)) {
            
            var change = 0
            for (b <- a to (arr.length - 1)) {
                if (arr(b) < arr(a)) {
                    change = 1
                    var aa = arr(a)
                    arr(a) = arr(b)
                    arr(b) = aa
                } 
            }

        }



        for (a <- arr) println(a)

    }

}