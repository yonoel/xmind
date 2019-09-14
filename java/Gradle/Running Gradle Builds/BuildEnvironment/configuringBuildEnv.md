#Build Environment
Gradle provides multiple mechanisms for configuring behavior of Gradle itself and specific projects. The following is a reference for using these mechanisms.

When configuring Gradle behavior you can use these methods, listed in order of highest to lowest precedence (first one wins):

1. Command-line flags such as --build-cache. These have precedence over properties and environment variables.

2. System properties such as systemProp.http.proxyHost=somehost.org stored in a gradle.properties file.
Gradle properties such as org.gradle.caching=true that are typically stored in a gradle.properties file in a project root directory or GRADLE_USER_HOME environment variable.
3. Environment variables such as GRADLE_OPTS sourced by the environment that executes Gradle.

Aside from configuring the build environment, you can configure a given project build using Project properties such as -PreleaseType=final.
## Gradle properties
Setting up a consistent environment for your build is as simple as placing these settings into a gradle.properties file. The configuration is applied in following order (if an option is configured in multiple locations the last one wins):
+ gradle.properties in project root directory.

+ gradle.properties in GRADLE_USER_HOME directory.

+ system properties, e.g. when -Dgradle.user.home is set on the command line.
## System properties
Using the -D command-line option, you can pass a system property to the JVM which runs Gradle. The -D option of the gradle command has the same effect as the -D option of the java command.

You can also set system properties in gradle.properties files with the prefix systemProp.
```$xslt
systemProp.gradle.wrapperUser=myuser
systemProp.gradle.wrapperPassword=mypassword
```
## Environment variables
## Project properties
You can add properties directly to your Project object via the -P command line option.

##Configuring JVM memory
You can adjust JVM options for Gradle in the following ways:

The org.gradle.jvmargs Gradle property controls the VM running the build. It defaults to -Xmx512m "-XX:MaxMetaspaceSize=256m"

...吧啦吧啦还有两种ci啊代理啊


