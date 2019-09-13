'use strict'
const { PI } = Math; // 把Math对象给与了PI这个对象

exports.area = (r) => PI * r ** 2; // 暴露了一个方法叫area(),参数是r，返回值是PI*r*r*2

exports.circumference = (r) => 2 * PI * r;// 暴露了一个方法叫circumference(),参数是r，返回值是PI*r*2

// note