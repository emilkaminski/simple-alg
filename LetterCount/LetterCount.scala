import scala.collection.mutable.Map

object LetterCount {

    val str = " This is a string to count letters."
    var m = collection.mutable.Map.empty[Char, Int]

    def main (args: Array[String]) {

        for (a <- str) if (m.contains(a)) m(a) = m(a) + 1 else m(a) = 1

        println(m)

    }
}