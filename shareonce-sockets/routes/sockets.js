var express = require('express.io');
app = express().http().io()

app.io.route('customers', {
    create: function(req) {
        // create your customer
    },
    update: function(req) {
        // update your customer
    },
    remove: function(req) {
        // remove your customer
    },
});

