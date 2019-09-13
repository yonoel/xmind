'use strict';
var s = 'Hello';

function greet(name) {
    console.log(s + ', ' + name + '!');
}
function add(){
     let args = arguments;
    //console.log(args);
    let sum = 0;
   for (let index = 0; index < args.length; index++) {
       const element = args[index];
       sum += element;
   }
   console.log(sum);
}
function Nodeone(){

}
Nodeone.prototype.greet = greet;
Nodeone.prototype.add = add;

module.exports = Nodeone;

