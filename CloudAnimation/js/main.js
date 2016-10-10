/**
 * @file
 * A JavaScript file to perform a cloud animation
 *
 */
 function animationPipeline() {

   var self = this,
   w = window.innerWidth,
   h = window.innerHeight,
   stage = document.getElementById('stage'),
   grass = document.getElementById('grass'),
   cloud = document.getElementsByClassName('cloud'),
   sunElem = document.getElementById('sun'),
   sunElemWidth = sunElem.innerWidth,
   clock = document.getElementById("clock"),
   time = document.getElementById("time"),
   sunTL = new TimelineMax({repeat:-1, repeatDelay:3.0}),
   moonData = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH3wkHAAkny7NQsAAABANJREFUeNrt201uGzsQhVFR0F68/+V4NfZA0MSQaKl/yCrW+aZB8h66fXTJ2GkXvdXP9+Wn9+vt69I8pfXyUneggAQQKD59oJAs1c0j2I9CFgQMK2JBoJCKAgFDjlgBYDheWRAwZEHAsB5aCMjsxYADEDjgAAQMOJQcSJQLOByAwAEHIHDAoefdwJASL0g0HNYDEDjgUGQgEY9UcNTsCoeUZEGi4rAegMABh6IesRyrZEES4rAeuoEhBVuQDDish6YAgUMu6Y5VAmTRSbUemgHEesgdJDkO66HhC2I5BAgccsRaG4fjlYYtiOUQICvNqPXQKCDWQ4DAIZf0Gjgcr+QOIs0E4mglR6wFcTheyRFLmgXE0UqAwCFACl6+3D90FhDrIUAkfQ7EeggQSfe7asX1cEHX4QviaCVAJH0OxHoIEEmASIcCcbwSIJKe1qqth++ByIJIZwNx95AsiASIdCgQxyvJgkiASHtqFY9XvhciCyIBIg0E4m+vJAsiASIBIo0C4v4hWRAJkP+ylgJEOgqIT1TJgkiASIC4qAsQCRApNhBHDcmCuIcIEAkQCRDHLAEiAWJFBIgEiASIY5YEiASIFREgEiBWRIBIgFgRASIBYkUEiASIrIgAgUSASIBYEQECiQCRALEiAgQSASJIABEketS87J0P8Ov+DGVBJEDkqOU9OmI5aqn7df94nxbEknhfnV+3IJYEjt779AkICRyAgKJNX+PuIO4l3gUgkHgHG08BXqTjFhhvAIEEEjgAAQUOQCAB46h31FwqQYHj9bvxt1gLvthqz+/MZ2hBrIkPls67aD7VQIHj9Tu4edxxvwBAmf/BbUEsChid591cHkGB4vVzdsRK+kWzKpZoH8wWxKpA0XmeLZNmrQMm6tfW3+fniOUYVhrE5iOWFbEw5TA8eTYWpPDCbEFU7QPTgkidD4Xr1t8oVchP88p6dEbguvcPkCyIVHA9PgJiRWRBJOuxHYgVkQWRrMd2IFZEpSBt/Y2+w67V18MRS3CcBcRRSy7pUuH12A3Eisgl3YVdRdfDEUtwjADiqCVHLEctFVuPw4FAopVwuIMIjtFA3EfkDuKopQLrcSoQSJQdx+lAIFFmHC7pgmP2glgRZcUxDAgkyohj6BHLX/8qJcDR/0FLokwfulM+1SFRlhPJtGMPJMpwXJ96L4BE0e+y0y/OkCgqjhBAIFFUHGGAQKJoMMIBAUXRcIQEAomi4AgLBBI4wvy/RH5QkIABCCi6xP1ZvTQ/QAgJHIBAAgYgoCjPP39I+280IAEDEFDgAAQUMACBBAxAQNFKOJYFAgoYgIACBiCgQAEILGAAAgoYgMACBSCwQAGIimGBAhBggAAEGCAAAQeCQf0CVbnx2DzGKuQAAAAASUVORK5CYII=',
   sunData = 'data:image/png;base64,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';

   /**
    * Setup styles and events
    **/
   self._initilize = function() {
    self.setupStage();
    clock.style.top = (h / 4) + 'px';
    window.setInterval(self.updateClock, 1000);
   };

   /**
    * Setup the stage and fire off the stage animations
    **/
   self.setupStage = function() {
    grass.style.top = (h - 70) + 'px';
    stage.style.height = h + 'px';
    self.runAnimation(cloud[0], 33.0, {left:(w + 100)});
    self.runAnimation(cloud[1], 27.0, {left:(w + 100)});
    self.runAnimation(cloud[2], 39.0, {right:(w + 100)});
    self.runAnimation(cloud[3], 42.0, {left:(w + 100)});
    self.animateSun();
   };

   /**
    * Create the pulsating animation with GSAP
    **/
   self.animateSun = function() {
    sunTL.append( new TweenLite(sunElem, 1.0, {scale: 1.1}) );
    sunTL.append( new TweenLite(sunElem, 1.0, {scale: 1.0}) );
   };
   /**
    * Generalized animation method
    **/
   self.runAnimation = function(elem, time, css) {
    TweenLite.to(elem, time, {css, onComplete:self.resetAnimation, onCompleteParams:[elem, css]});
   };
   /** 
    * Callback method fired after the cloud animation completes
    **/
   self.resetAnimation = function(elem, css) {
    if (elem.id === 'cloud3') {
      elem.style.right = -400 + 'px';
    } else {
      elem.style.left = -400 + 'px';
    }
    // random time variable to run cloud animation length
    var t = Math.floor(Math.random() * 40) + 15;
    self.runAnimation(elem, t, css);
   };
   /**
    * Method that is fired every second to update the clock
    **/
   self.updateClock = function(){
    var timeNow = new Date();

    var currentHours = timeNow.getHours();
    var currentMinutes = timeNow.getMinutes();
    var currentSeconds = timeNow.getSeconds();

    currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;
    currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;

    var timeOfDay = ( currentHours < 12 ) ? 'AM' : 'PM';

    currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;

    currentHours = ( currentHours == 0 ) ? 12 : currentHours;
    
    self.l(timeOfDay + ' ' + currentHours);

    if ((timeOfDay == 'PM' && currentHours >= 9 && currentHours != 12) || (timeOfDay == 'AM' && currentHours <= 8)) {
      stage.style.backgroundColor = '#333';
      stage.style.display = 'block';
      sunElem.firstElementChild.src = moonData;
    } else {
      stage.style.backgroundColor = '#ccece4';
      stage.style.display = 'block';
      sunElem.firstElementChild.src = sunData;
    }

    // Create the display
    var currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds + " " + timeOfDay;

    // Update the time display
    time.innerHTML = currentTimeString;
   };
   /**
    * Logging Function
    **/
   self.l = function(message) {
    console.log(message);
   };

   // Initialize the functionality of the controller
   self._initilize();

 } // End animationPipeline


 var interval = setInterval(function() {
  if(document.readyState === 'complete') {
    clearInterval(interval);
    var pipe = animationPipeline();
  }
 }, 100);
