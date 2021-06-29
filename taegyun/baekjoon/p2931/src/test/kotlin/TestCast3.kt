import kotlin.test.Test
import kotlin.test.BeforeTest
import kotlin.test.assertEquals

import java.io.PrintStream
import java.io.ByteArrayOutputStream
import java.io.InputStreamReader
import com.google.common.io.Resources
import java.nio.charset.StandardCharsets

class CastTest3 {
  val ouputStream = ByteArrayOutputStream()

  @BeforeTest fun init() {
    System.setIn(this.javaClass.getResourceAsStream("case3.txt"))
    System.setOut(PrintStream(ouputStream))
  }

  @Test(timeout = 1000) fun test() {
    Solution().solution()

    val result = Resources.toString(Resources.getResource("result3.txt"), StandardCharsets.UTF_8)    
    assertEquals(result, ouputStream.toString().trim())
  }
}