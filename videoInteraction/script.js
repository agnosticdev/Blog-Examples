
(function($){

   //very quick plugin for swapping videos into a variable until you are ready for them
   $.fn.videoInteraction = function(){
                this.each(function(){
                    //varibles
                        var self = $(this),
                        $image = self.parent().find('.image-overlay'),
                        $video = self.find('iframe');

                        //remove the video until we are ready for it
                        $video.remove();
                        //bind an event to the image overlay
                        $image.on('click', handleVideoSwap);
                        //this function hides the image overlay and starts the youtube player
                        function handleVideoSwap(e){
                                $(e.target).css('display', 'none');
                                self.append($video);
                        }
                });
    };

    $('.video-embed').videoInteraction();

}(jQuery));

