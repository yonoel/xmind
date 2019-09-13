'use strict';

// 引入hello模块:
var nodeone = require('./nodeone');

var s = 'Michael';

nodeone.prototype.greet(s); // Hello, Michael!
nodeone.prototype.add(1,2);