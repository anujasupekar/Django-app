$(document).ready(main);

function main() {
	$("#upvoteBtn").click(function() {
		console.log($("#upvoteBtn").val())
		$.ajax({
	        url: url_vote,
	        type: "POST",
	        data: {
	            'votes': $("#upvoteBtn").val(), 
	            'csrfmiddlewaretoken': csrf_token,
	            click: true
	        }
	    }).done(function() {
	    	window.location.reload();
	    });
	});

	$("#downvoteBtn").click(function() {
		console.log($("#downvoteBtn").val())
		$.ajax({
	        url: url_vote,
	        type: "POST",
	        data: {
	            'votes': $("#downvoteBtn").val(), 
	            'csrfmiddlewaretoken': csrf_token,
	            click: true
	        }
	    }).done(function() {
	    	window.location.reload();
	    });
	});
}