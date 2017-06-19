
var _el = jQuery(".lightbox");

if(_el.length > 0) {

	$(function(){

		if(typeof(jQuery.magnificPopup) == "undefined") {
			return false;
		}

		jQuery.extend(true, jQuery.magnificPopup.defaults, {
			tClose: 		'Close',
			tLoading: 		'Loading...',

			gallery: {
				tPrev: 		'Previous',
				tNext: 		'Next',
				tCounter: 	'%curr% / %total%'
			},

			image: 	{ 
				tError: 	'Image not loaded!' 
			},

			ajax: 	{ 
				tError: 	'Content not loaded!' 
			}
		});

		_el.each(function() {

			var _t 			= jQuery(this),
				options 	= _t.attr('data-plugin-options'),
				config		= {},
				defaults 	= {
					type: 				'image',
					fixedContentPos: 	false,
					fixedBgPos: 		false,
					mainClass: 			'mfp-no-margins mfp-with-zoom',
					closeOnContentClick: true,
					closeOnBgClick: 	true,
					image: {
						verticalFit: 	true
					},

					zoom: {
						enabled: 		false,
						duration: 		300
					},

					gallery: {
						enabled: false,
						navigateByImgClick: true,
						preload: 			[0,1],
						arrowMarkup: 		'<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
						tPrev: 				'Previous',
						tNext: 				'Next',
						tCounter: 			'<span class="mfp-counter">%curr% / %total%</span>'
					},
				};

			if(_t.data("plugin-options")) {
				config = jQuery.extend({}, defaults, options, _t.data("plugin-options"));
			}

			jQuery(this).magnificPopup(config);

		});

	});

}


if(jQuery(".masonry-gallery").length > 0) {

	jQuery(".masonry-gallery").each(function() {
		var _container = jQuery(this),
			columns	= _container.attr('data-columns');

		var _bigImageNo 		= _container.attr('data-img-big'),
			_containerWidth		= _container.width(),
			_firstElemWidth 	= _containerWidth / columns;

		_container.children('a').css({"width":_firstElemWidth+"px"});
		

		// Set Big Image
        if(parseInt(_bigImageNo) > 0) {


			_bigImageNo = Number(_bigImageNo) - 1; 
			_container.find('a:eq('+_bigImageNo+')').css({ width: _firstElemWidth * 2 + 'px'});

			$(function() {

				setTimeout( function() {
					_container.isotope({
						masonry: {
							columnWidth: _firstElemWidth 
						}
					});

					_container.isotope('layout');

				}, 1000);
			
			});

        }

	});


}



var owls = $('.owl-carousel');

if (owls.length > 0) {

	$.each(owls, function(){
		$(this).owlCarousel( JSON.parse($(this).attr('data-plugin-options')) );
	});

}



$('.single-slide').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
     dots: false,
    asNavFor: '.thumb-slide'
});
$('.thumb-slide').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    asNavFor: '.single-slide',
    focusOnSelect: true,
    arrows: false	,
    responsive: [
    {
      breakpoint: 767,
      settings: {
          arrows: true,
          slidesToShow: 2,
          slidesToScroll: 1,
      }
    }
    ]
});

