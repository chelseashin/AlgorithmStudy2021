plugins {
  kotlin("jvm") version "1.4.21"
}

repositories {
  mavenCentral()
}

dependencies {
  implementation("com.google.guava:guava:30.0-jre")
  testImplementation("org.jetbrains.kotlin:kotlin-test")
  testImplementation("org.jetbrains.kotlin:kotlin-test-junit")
}