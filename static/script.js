/* When the form (document) is loaded and user click type="submit", call function(e) */
$(document).on('submit', '#send-message', function(e) {
	e.preventDefault();		// Prevent reloading and going to another page
	$.ajax({
		type:'POST',		// method="POST"
		url:'/send',		// To views.send
		data: {
			username:$('#username').val(),
			angkringan_id:$('#angkringan_id').val(),
			message:$('#message').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(data) {
			// alert(data);	// Alert an HttpResponse
		}
	});
	document.getElementById('message').value = '';
});