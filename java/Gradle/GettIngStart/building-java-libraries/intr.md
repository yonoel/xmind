# Building Java Libraries
## Create a library project
```
$ mkdir building-java-libraries
$ cd building-java-libraries
```
## Run the init task
```
$ gradle init --type java-library --project-name jvm-library
> Task :wrapper
> Task :init

BUILD SUCCESSFUL in 4s
2 actionable tasks: 2 executed
```
    ├── build.gradle
    ├── gradle
    │   └── wrapper 
    │       ├── gradle-wrapper.jar
    │       └── gradle-wrapper.properties
    ├── gradlew
    ├── gradlew.bat
    ├── settings.gradle
    └── src
        ├── main
        │   └── java 
        │       └── Library.java
        └── test
            └── java 
                └── LibraryTest.java
## Review the generated project files
in Generated settings.gradle
```
rootProject.name = 'building-java-libraries' 
```               
in Generated build.gradle
```
plugins {
    id 'java-library'
}

repositories {
    jcenter() 
}

dependencies {
    api 'org.apache.commons:commons-math3:3.6.1' 

    implementation 'com.google.guava:guava:26.0-jre' 

    testImplementation 'junit:junit:4.12' 
}
```
in Generated src/main/java/Library.java
The build script adds the java-library plugin. This is an extension of the java-base plugin and adds additional tasks for compiling Java source code.
```
package jvm.library;

public class Library {
    public boolean someLibraryMethod() {
        return true;
    }
}
```
The generated JUnit specification, src/test/java/jvm/library/LibraryTest.java is shown next:

Generated src/test/java/LibraryTest.java
```
package jvm.library;

import org.junit.Test;
import static org.junit.Assert.*;

public class LibraryTest {
    @Test public void testSomeLibraryMethod() {
        Library classUnderTest = new Library();
        assertTrue("someLibraryMethod should return 'true'", classUnderTest.someLibraryMethod());
    }
}
```
## Assemble the library JAR
To build the project, run the build task. You can use the regular gradle command, but when a project includes a wrapper script, it is considered good form to use it instead.

```
$ ./gradlew build
```

The first time you run the build, Gradle will check whether or not you already have the JUnit libraries and other listed dependencies in your cache under your ~/.gradle directory. If not, the libraries will be downloaded and stored there. The next time you run the build, the cached versions will be used. The build task compiles the classes, runs the tests, and generates a test report.


## Customize the library JAR 
in build.gradle
```
version = '0.1.0'
```
Another common requirement is customizing the manifest file, typically by adding one or more attributes. Let’s include the library name and version in the manifest file by configuring the jar task. Add the following to the end of your build script:

```
jar {
    manifest {
        attributes('Implementation-Title': project.name,
                   'Implementation-Version': project.version)
    }
}
```
## Adding API documentation
The java-library plugin has built-in support for Java’s API documentation tool via the javadoc task.

```
Run the javadoc task.
```

