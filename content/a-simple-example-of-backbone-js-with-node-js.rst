A simple example of Backbone.js with Node.js
############################################
:date: 2012-01-17 21:33
:author: yiyang
:category: Javascript
:slug: a-simple-example-of-backbone-js-with-node-js

| Here is a example that how to use Backbone.js Model/Collection/View
with Node.js.
|  That's, without browser, totally in command console we can still see
backbone.js in action :)

::

    var Backbone = require('backbone');

    var Song = Backbone.Model.extend({
        defaults:{
            name: "Not specified",
            artist: "Not specified"
        }
    });

    var Album = Backbone.Collection.extend({
            model: Song,
            initialize: function(models, options){
                this.bind("add", options.view.showNewSongAdded);
            }
    });

    var AppView = Backbone.View.extend({
        initialize: function(){
            this.album = new Album(null, {view: this});
        },
        addNewSong: function(song){
            this.album.add(song);
        },
        showNewSongAdded: function(model){
            console.log("-----------------new song just added:----------------------");
            console.log(model.attributes);
            console.log("=============Album title list==============================");
            console.log(this.toJSON()); //supurise, this refers to Album now, since this function was invoked from Album!!!

        },
        _ensureElement : function(){ //overwrite this to make it work in node, otherwise document.createDom is called.
        }

    });

    var song1 = new Song({ name: "Running up the hill", artist: "Kate Bush"});
    var song2 = new Song({ name: "Wonder", artist: "Natalie merchant"});
    var song3 = new Song({ name: "Saultan of Swings", artist:"Dire Stratis"});

    var app = new AppView;

    app.addNewSong(song1);
    app.addNewSong(song2);
    app.addNewSong(song3);

