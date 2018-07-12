var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000,
  morgan = require('morgan'),
  mongoose = require('mongoose'),
  Task = require('./api/models/DaggerfallWeaponryModel'),
  bodyParser = require('body-parser');
  
// mongoose DB instance url connection
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/DaggerfallWeaponryDB'); 

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// register app routes
var routes = require('./api/routes/DaggerfallWeaponryRoutes');
routes(app);

// add 404 redirect for incorrect routes
app.use(function(req, res) {
  res.status(404).send({url: req.originalUrl + ' not found'})
});

app.listen(port);
console.log('Server started on PORT: ' + port);
console.log('*** Developed by Justice Adams *** ');
console.log(
`
                                   
         @*    @@                         
        @@      @*                        
       @         @                        
      @@  @@@@   @@           ____                              ____      ____                
     @@   @@ @@   @@         / __ \\____ _____ _____ ____  _____/ __/___ _/ / /               
    @@@        @  @@@       / / / / __  / __  / __  / _ \\/ ___/ /_/ __  / / /                 
   @@@@@    @@   @@@@@     / /_/ / /_/ / /_/ / /_/ /  __/ /  / __/ /_/ / / /                 
  @@@@    @@       @@@@   /_____/\\__,_/\\__, /\\__, /\\___/_/  /_/  \\__,_/_/_/                  
 @@@@     @@@       @@@@              /____//____/                 
*@@@@@  @@@@@@@@@  @@@@@   _       __                    
 @@@@@@@@@@@@@@@@@@@@@@&  | |     / /__  ____ _____  ____  ____  _______  __               
  @@@@@@@@@@@@@@@@@@@@@   | | /| / / _ \\/ __  / __ \\/ __ \\/ __ \\/ ___/ / / /                   
   @@@@  @ @@@@@  @@@@    | |/ |/ /  __/ /_/ / /_/ / /_/ / / / / /  / /_/ /                   
    @@@     @@    @@@     |__/|__/\\___/\\__,_/ .___/\\____/_/ /_/_/   \\__, /                   
     @@     .@    @@                       /_/                     /____/                      
      @@@   @@  @@@                       
       @@  @@   @@                        
        @  @    @                         
           @                              
          @                               
          @                               
           @@.  
`)