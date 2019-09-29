import scala.math.Integral.Implicits._

object BinarySearch {
    def main (args:Array[String]) {
        val a = Array(1,3,5,7,23,45,56,67,78,89,222)
        val check = 7
        println(binarySearch(a,check))
    }

    def binarySearch(arr:Array[Int], check:Int) : Int = {

        var left = 0 
        var right = arr.length
        
        while (left < right) {
            val (cut, remainder) = (left + right) /% 2        
            if (arr(cut)==check) return cut
            if (arr(cut) < check) left = cut else right = cut
        }
        
        return -1
    }

}