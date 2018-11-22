$(document).ready(function(){    
	// Adds an arrow-up / arrow-down icon to open/close collapse panels
	$('.collapse').on('show.bs.collapse', function(){
		$(this).parent().find(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
	}).on('hide.bs.collapse', function(){
		$(this).parent().find(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
	});

	// goes and changes each "moment" element to display how long ago that element's timestamp was.
	$(".moment").each(function(i) {
	    var date = $(this).html();
	    var fromStr = moment(date, "YYYYMMDDHH").fromNow();
	    $(this).html(fromStr);
	});

	// highlight today in the schedule calendar
	var todayDateComponents = moment().format("MMM DD").split(" ");
	var todayMonth = todayDateComponents[0];
	var todayDay = parseInt(todayDateComponents[1]);
	$(".calendarDate").each(function(i) {
		var dateComponents = $(this).html().split(" ");
		var month = dateComponents[0];
		var day = parseInt(dateComponents[1]);
		if (month.startsWith(todayMonth) && todayDay == day) {
			$(this).css("background-color", "hsl(55, 100%, 50%)");
		}
	});

	// only show certain content if they should be released
	$(".visible-after").each(function(i) {
	    var dateStr = $(this).attr("data-visible-after");
	    var releaseDate = moment(dateStr, "YYYYMMDDHH");
	    if (!releaseDate.isSameOrBefore(moment())) {
	    	$(this).remove();
	    }
	});
});