'use strict';

module.exports = function(app) {
  var weaponsController = require('../controllers/DaggerfallWeaponryController');
  var morgan = require('morgan');
  
  app.use(morgan('dev'));

  // define endpoints and hook them up to controller functions 
  // (lambda style)
  app.route('/weapons')
    .get(weaponsController.get_all_weapons)

  app.route('/weapons/:weaponId')
    .get(weaponsController.get_weapon)
    .put(weaponsController.update_weapon)
    .delete(weaponsController.delete_weapon);
};
