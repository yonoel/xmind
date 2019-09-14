# Authoring Tasks
##Contents
    Task outcomes
    Defining tasks
    Locating tasks
    Configuring tasks
    Passing arguments to a task constructor
    Adding dependencies to a task
    Ordering tasks
    Adding a description to a task
    Replacing tasks
    Skipping tasks
    Up-to-date checks (AKA Incremental Build)
    Task rules
    Finalizer tasks
    Lifecycle tasks
    Summary
  This was all about simple tasks, but Gradle takes the concept of tasks further. Gradle supports enhanced tasks, which are tasks that have their own properties and methods. This is really different from what you are used to with Ant targets. Such enhanced tasks are either provided by you or built into Gradle.
## Task outcomes
+ (no label) or EXECUTED

     Task executed its actions.
   
+ UP-TO-DATE

    Task’s outputs did not change.
+ FROM-CACHE

    Task’s outputs could be found from a previous execution.
+ SKIPPED
    
    Task did not execute its actions.
    
+ NO-SOURCE
    
    Task did not need to execute its actions.For example, source files are .java files for JavaCompile.
## Defining tasks
We have already seen how to define tasks using strings for task names in this chapter. There are a few variations on this style, which you may need to use in certain situations.
```$xslt
Example 1. Defining tasks using strings for task names

task('hello') {
    doLast {
        println "hello"
    }
}

task('copy', type: Copy) {
    from(file('srcDir'))
    into(buildDir)
}
Example 2. Defining tasks using the tasks container
tasks.create('hello') {
    doLast {
        println "hello"
    }
}

tasks.create('copy', Copy) {
    from(file('srcDir'))
    into(buildDir)
}
Example 3. Defining tasks using a DSL specific syntax
// Using Groovy dynamic keywords

task(hello) {
    doLast {
        println "hello"
    }
}

task(copy, type: Copy) {
    from(file('srcDir'))
    into(buildDir)
}
```
## Locating tasks
```$xslt
task hello
task copy(type: Copy)

// Access tasks using Groovy dynamic properties on Project

println hello.name
println project.hello.name

println copy.destinationDir
println project.copy.destinationDir
println tasks.hello.name
println tasks.named('hello').get().name

println tasks.copy.destinationDir
println tasks.named('copy').get().destinationDir
println tasks.getByPath('hello').path
println tasks.getByPath(':hello').path
println tasks.getByPath('projectA:hello').path
println tasks.getByPath(':projectA:hello').path
```
## Configuring tasks
As an example, let’s look at the Copy task provided by Gradle. To create a Copy task for your build, you can declare in your build script:
```$xslt
task myCopy(type: Copy)

```
This creates a copy task with no default behavior. The task can be configured using its API (see Copy). The following examples show several different ways to achieve the same configuration.

Just to be clear, realize that the name of this task is “myCopy”, but it is of type “Copy”. You can have multiple tasks of the same type, but with different names. You’ll find this gives you a lot of power to implement cross-cutting concerns across all tasks of a particular type.
```$xslt
Copy myCopy = tasks.getByName("myCopy")
myCopy.from 'resources'
myCopy.into 'target'
myCopy.include('**/*.txt', '**/*.xml', '**/*.properties')
```
   

   