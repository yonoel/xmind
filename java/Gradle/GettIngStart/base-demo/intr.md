# Creating New Gradle Builds
## Initialize a project
```
mkdir basic-demo
cd basic-demo
gradle init
```

    ├── build.gradle  Gradle build script for configuring the current project
    ├── gradle
    │   └── wrapper
    │       ├── gradle-wrapper.jar  Gradle Wrapper executable JAR
    │       └── gradle-wrapper.properties  Gradle Wrapper configuration properties
    ├── gradlew  
    ├── gradlew.bat  
    └── settings.gradle  Gradle settings script for configuring the Gradle build
## Create a task
 in build.gradle

```
task copy(type: Copy, group: "Custom", description: "Copies sources to the dest directory") {
    from "src"
    into "dest"
}
```
注意不是ide里写,是在控制台里
```
./gradlew copy
```
## Apply a plugin
```
plugins {
    id "base"
}

```
Now add a task that creates a zip archive from the src directory.
```
task zip(type: Zip, group: "Archive", description: "Archives sources in a zip file") {
    from "src"
    setArchiveName "basic-demo-1.0.zip"
}
```
## Explore and debug your build
Let’s see what else we can do with Gradle in our new project. A full reference to the command-line interface is available as well.

### Discover available tasks
The tasks command lists Gradle tasks that you can invoke, including those added by the base plugin, and custom tasks you just added as well.


```
./gradlew tasks
```
### Analyze and debug your build
Gradle also provides a rich, web-based view of your build called a build scan.


Try creating a build scan by adding --scan when executing a task.

### Discover available properties
The properties command tells you about a project’s attributes.


```
❯ ./gradlew properties

```