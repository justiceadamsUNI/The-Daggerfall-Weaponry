'use strict';

var mongoose = require('mongoose'),
	WeaponsDB = mongoose.model('Weapons');

// list all weapons in armory
exports.get_all_weapons = function(req, res) {
  WeaponsDB.find({}, function(err, weapon) {
    if (err)
      res.send(err);
    res.json(weapon);
  });
};

// store a weapon
exports.store_a_weapon = function(req, res) {
  var new_weapon = new WeaponsDB(req.body);
  new_weapon.save(function(err, weapon) {
    if (err)
      res.send(err);
    res.json(weapon);
  });
};

// see specific weapon in armory
exports.get_weapon = function(req, res) {
  WeaponsDB.findById(req.params.weaponId, function(err, weapon) {
    if (err)
      res.send(err);
    res.json(weapon);
  });
};

// update specific weapon in armory
exports.update_weapon = function(req, res) {
  WeaponsDB.findOneAndUpdate({_id: req.params.weaponId}, req.body, {new: true}, function(err, weapon) {
    if (err)
      res.send(err);
    res.json(WeaponsDB);
  });
};

// remove specific weapon from armory
exports.delete_weapon= function(req, res) {
  WeaponsDB.remove({
    _id: req.params.weaponId
  }, function(err, weapon) {
    if (err)
      res.send(err);
    res.json({ message: 'Weapon successfully removed from armory' });
  });
};