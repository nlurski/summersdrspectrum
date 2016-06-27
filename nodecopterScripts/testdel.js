var arDrone = require('ar-drone');
var client = arDrone.createClient();


client.config('control:altitude_max', 33300);
client.takeoff();
client.up(1);
client
  .after(3000, function() {
    this.stop();
  })
  .after(10000, function() {
    this.stop();
    this.land();
  });
