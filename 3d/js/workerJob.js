import { getImage } from "./checkload.js";
//getImage = require('./checkload.js');
self.addEventListener("message", function(e) {
    var args = e.data.args;
    console.log(args[0]);
    getImage(args[0], args[1], args[2], args[3]);
}, false);
//getImage(x,y,step);