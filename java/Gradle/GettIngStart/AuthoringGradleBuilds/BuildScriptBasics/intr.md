# Contents
    Projects and tasks
    Hello world
    Build scripts are code
    Task dependencies
    Dynamic tasks
    Manipulating existing tasks
    Groovy DSL shortcut notations
    Extra task properties
    Using Ant Tasks
    Using methods
    Default tasks
    Configure by DAG
    External dependencies for the build script
## Projects and tasks
Everything in Gradle sits on top of two basic concepts: projects and tasks.

## Hello world
To try this out, create the following build script named build.gradle.
```
task hello {
    doLast {
        println 'Hello world!'
    }
}
```

```
> gradle -q hello
```
## Build scripts are code
Example 3. Using Groovy or Kotlin in Gradle’s tasks
```
task upper {
    doLast {
        String someString = 'mY_nAmE'
        println "Original: $someString"
        println "Upper case: ${someString.toUpperCase()}"
    }
}
```
```
task count {
    doLast {
        4.times { print "$it " }
    }
}
```
## Task dependencies
As you probably have guessed, you can declare tasks that depend on other tasks.

```
task hello {
    doLast {
        println 'Hello world!'
    }
}
task intro {
    dependsOn hello
    doLast {
        println "I'm Gradle"
    }
}
```
## Dynamic tasks
```
4.times { counter ->
    task "task$counter" {
        doLast {
            println "I'm task number $counter"
        }
    }
}
```
## Manipulating existing tasks
Once tasks are created they can be accessed via an API. For instance, you could use this to dynamically add dependencies to a task, at runtime. Ant doesn’t allow anything like this.
```
4.times { counter ->
    task "task$counter" {
        doLast {
            println "I'm task number $counter"
        }
    }
}
task0.dependsOn task2, task3

task hello {
    doLast {
        println 'Hello Earth'
    }
}
hello.doFirst {
    println 'Hello Venus'
}
hello.configure {
    doLast {
        println 'Hello Mars'
    }
}
hello.configure {
    doLast {
        println 'Hello Jupiter'
    }
}
```
## Groovy DSL shortcut notations
There is a convenient notation for accessing an existing task. Each task is available as a property of the build script:
```
task hello {
    doLast {
        println 'Hello world!'
    }
}
hello.doLast {
    println "Greetings from the $hello.name task."
}
```
## Extra task properties
You can add your own properties to a task. To add a property named myProperty, set ext.myProperty to an initial value. From that point on, the property can be read and set like a predefined task property.
```
task myTask {
    ext.myProperty = "myValue"
}

task printTaskProperties {
    doLast {
        println myTask.myProperty
    }
}
```
## Using methods
Gradle scales in how you can organize your build logic. The first level of organizing your build logic for the example above, is extracting a method.
```
// 都是递归调用
task checksum {
    doLast {
        fileList('./antLoadfileResources').each { File file ->
            ant.checksum(file: file, property: "cs_$file.name")
            println "$file.name Checksum: ${ant.properties["cs_$file.name"]}"
        }
    }
}

task loadfile {
    doLast {
        fileList('./antLoadfileResources').each { File file ->
            ant.loadfile(srcFile: file, property: file.name)
            println "I'm fond of $file.name"
        }
    }
}

File[] fileList(String dir) {
    file(dir).listFiles({file -> file.isFile() } as FileFilter).sort()
}
```
## Default tasks
Gradle allows you to define one or more default tasks that are executed if no other tasks are specified.
```
defaultTasks 'clean', 'run'

task clean {
    doLast {
        println 'Default Cleaning!'
    }
}

task run {
    doLast {
        println 'Default Running!'
    }
}

task other {
    doLast {
        println "I'm not a default task!"
    }
}
```
## Configure by DAG
As we later describe in full detail (see Build Lifecycle), Gradle has a configuration phase and an execution phase. After the configuration phase, Gradle knows all tasks that should be executed. Gradle offers you a hook to make use of this information. A use-case for this would be to check if the release task is among the tasks to be executed. Depending on this, you can assign different values to some variables.


```
task distribution {
    doLast {
        println "We build the zip with version=$version"
    }
}

task release {
    dependsOn 'distribution'
    doLast {
        println 'We release now'
    }
}

gradle.taskGraph.whenReady { taskGraph ->
    if (taskGraph.hasTask(":release")) {
        version = '1.0'
    } else {
        version = '1.0-SNAPSHOT'
    }
}
```
## External dependencies for the build script
If your build script needs to use external libraries, you can add them to the script’s classpath in the build script itself. You do this using the buildscript() method, passing in a block which declares the build script classpath.
```
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath group: 'commons-codec', name: 'commons-codec', version: '1.2'
    }
}
```
Having declared the build script classpath, you can use the classes in your build script as you would any other classes on the classpath. The following example adds to the previous example, and uses classes from the build script classpath.
```
import org.apache.commons.codec.binary.Base64

buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath group: 'commons-codec', name: 'commons-codec', version: '1.2'
    }
}

task encode {
    doLast {
        def byte[] encodedString = new Base64().encode('hello world\n'.getBytes())
        println new String(encodedString)
    }
}
```
