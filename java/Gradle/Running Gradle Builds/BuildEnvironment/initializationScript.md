# Initialization Scripts
##Using an init script
There are several ways to use an init script:

+ Specify a file on the command line. The command line option is -I or --init-script followed by the path to the script. The command line option can appear more than once, each time adding another init script. The build will fail if any of the files specified on the command line does not exist.

+ Put a file called init.gradle (or init.gradle.kts for Kotlin) in the USER_HOME/.gradle/ directory.

+ Put a file that ends with .gradle (or .init.gradle.kts for Kotlin) in the USER_HOME/.gradle/init.d/ directory.

+ Put a file that ends with .gradle (or .init.gradle.kts for Kotlin) in the GRADLE_HOME/init.d/ directory, in the Gradle distribution. This allows you to package up a custom Gradle distribution containing some custom build logic and plugins. You can combine this with the Gradle wrapper as a way to make custom logic available to all builds in your enterprise.
## Writing an init script
Similar to a Gradle build script, an init script is a Groovy or Kotlin script. Each init script has a Gradle instance associated with it. Any property reference and method call in the init script will delegate to this Gradle instance.

Each init script also implements the Script interface.
###Configuring projects from an init script
You can use an init script to configure the projects in the build. This works in a similar way to configuring projects in a multi-project build. The following sample shows how to perform extra configuration from an init script before the projects are evaluated. This sample uses this feature to configure an extra repository to be used only for certain environments.

```
in init.gradle
allprojects {
    repositories {
        mavenLocal()
    }
}

in build.gradle 
repositories {
    mavenCentral()
}

task showRepos {
    doLast {
        println "All repos:"
        println repositories.collect { it.name }
    }
}
> gradle --init-script init.gradle -q showRepos

```

