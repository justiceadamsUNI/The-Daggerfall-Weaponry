'use strict';

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Scheme of our weapon models which will be stored in the mongo DB
var WeaponSchema = new Schema({
  name: {
    type: String,
	lowercase: true,
    required: 'Please enter the name of the weapon!'
  },
  type: {
	type: String,
    enum: ['dagger', 'mace', 'sword', 'war-axe', 'battleaxe', 'greatsword', 'war-hammer', 'bow', 'crossbow'],
    required: 'Please enter the weapon type {dagger, mace, sword, war-axe, battleaxe, greatsword, war-hammer, bow, crossbow}'
  },
  damage: {
    type: Number,
    required: 'Please enter the base damage of the weapon!'
  },
  weight: {
    type: Number,
    required: 'Please enter the weight of the weapon!'
  },
  value: {
    type: Number,
    required: 'Please enter the base value of the weapon!'
  },
});

module.exports = mongoose.model('Weapons', WeaponSchema);