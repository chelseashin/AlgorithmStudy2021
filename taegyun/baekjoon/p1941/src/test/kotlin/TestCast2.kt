import kotlin.test.Test
import kotlin.test.BeforeTest
import kotlin.test.assertEquals

import java.io.PrintStream
import java.io.ByteArrayOutputStream
import java.io.InputStreamReader
import com.google.common.io.Resources
import java.nio.charset.StandardCharsets

class CastTest2 {
  val ouputStream = ByteArrayOutputStream()

  @BeforeTest fun init() {
    System.setIn(this.javaClass.getResourceAsStream("case2.txt"))
    System.setOut(PrintStream(ouputStream))
  }

  @Test() fun test() {
    Solution().solution()

    val result = Resources.toString(Resources.getResource("result2.txt"), StandardCharsets.UTF_8)    
    assertEquals(result, ouputStream.toString().trim())
  }
}