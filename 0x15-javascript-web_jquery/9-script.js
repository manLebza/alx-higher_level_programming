const $ = window.$;
$.get('htts://fourtonfish.com/hellosalut/?lang=fr',
	function (data, textStatus) {
		$('DIV#hello').text(data.hello);
	});
