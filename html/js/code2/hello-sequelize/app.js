"use strict"
const Sequelize = require('sequelize');
const config = require('./config');

// var mysql  = require('mysql');
// var connection = mysql.createConnection({
//     host     : 'localhost',
//     user     : 'root',
//     password : '123456',
//     database : 'test'
// });

// connection.connect();

// connection.query("select * from pets",function(err,result){
//     if(err){
//         console.log('[SELECT ERROR] - ',err.message);
//         return;
//       }

//      console.log('--------------------------SELECT----------------------------');
//      console.log(result);
//      console.log('------------------------------------------------------------\n\n');  
// })

// connection.end();

var sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.host,
    dialect: 'mysql',
    pool: {
        max: 5,
        min: 0,
        idle: 30000
    }
});

// 定义pet对象
var Pet = sequelize.define('pet', {
    id: {
        type: Sequelize.STRING(50),
        primaryKey: true
    },
    name: Sequelize.STRING(100),
    gender: Sequelize.BOOLEAN,
    birth: Sequelize.DATE,
    createdAt: Sequelize.DATE,
    updatedAt: Sequelize.DATE,
    version: Sequelize.BIGINT
}, {
        timestamps: false
    });

   //Pet.findByPrimary(1).then((result)=>console.log(result.name)).catch((err)=>console.log(err.message));
    // (async ()=>{
    //     await Pet;
    // })
  (async () => {
        await Pet.findByPrimary(1).then((result)=>console.log(result.name+"2")).catch((err)=>console.log(err));
    })();
var now = new Date();
   /* (async () => {
        var dog = await Pet.create({
            id: 1,
            name: 'Odie',
            gender: false,
            birth: '2008-08-08',
            createdAt: now,
            updatedAt: now,
            version: 0
        });
        console.log('created: ' + JSON.stringify(dog));
    })();*/

    
    