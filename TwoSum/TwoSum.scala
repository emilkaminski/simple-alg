object TwoSum {

    val ll = Array (2,3,7,5,11,2,18)
    val checkN:Int = 8

    def main (args: Array[String]) {
        for (i <- 0 to (ll.length-1)) {
            for (ii <-i+1 to (ll.length-1)) {
                if ( (ll(i)+ll(ii) ) == checkN ) {
                    println(ll(i),"-",ll(ii))
                }
            }
        }

    }   
}