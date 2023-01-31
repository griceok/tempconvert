import org.apache.flink.streaming.api.scala._

object FahrenheitToCelsius {
  def fahrenheitToCelsius(temp_f: Double): Double = {
    (temp_f - 32) * (5.0/9.0)
  }

  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val inputStream = env.fromElements(70.0, 75.0, 80.0, 85.0, 90.0)

    val resultStream = inputStream
      .map(fahrenheitToCelsius)
      .print()

    env.execute("Fahrenheit to Celsius Conversion")
  }
}
