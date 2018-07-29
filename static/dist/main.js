var API_PATH="/api2";

$(document).ready(function(){
	 // abs path recommned



	$('#textarea-urls-raw').val(' github.com \n  http://kyshel.me  \n 8.8.8.8');

	$("#btn-urls-seq").on("click", function() {
		init_view();
		urls_array=get_urls_new_from_raw($('#textarea-urls-raw').val());
		get_status_code_recur(urls_array,urls_array.length,0)
	});
	

	$("#btn-url-submit").on("click", function() {
		init_view();
		show_loader('Loading,please wait...');

		var post_data={
			op:"getUrlsStatusCode",
			urls:get_urls_new_from_raw($('#textarea-urls-raw').val()),
		};


		$.ajax({
			method: "POST",
			url: API_PATH,
			data: JSON.stringify(post_data),
			dataType:'json',
			contentType: 'application/json;charset=UTF-8',
		}).done( function(response,status,xhr) {
			hide_loader();
			$(".btn-ajax").prop("disabled",false);
			//$('#response-raw').html(JSON.stringify(response))
			var html='';
			for (var i = 0; i < response.length; i++) {
				html=html+ '<a href="'+ response[i][0] +
				'" target="_blank">'+response[i][0] + '</a> -> ' + 
				response[i][1] + '<br>'
			}

			$('#response-raw').append(html)


			//console.log(response)
		}).fail( function(e) {
			//console.log(e.responseText)
			$('#response-raw').html('ERROR:<br>'+e.responseText)
			//console.log(e)
		});
	});


	$('#btn-preview').hover(function () {
		$('#textarea-urls-raw').hide();
		urls_new_str=''
		urlsNew=get_urls_new_from_raw($('#textarea-urls-raw').val());
		for (i in urlsNew) {
			urls_new_str = urls_new_str +urlsNew[i]  + '\n'
		} 
		$( "#textarea-urls-raw" ).after( '<pre id="textarea-urls-new">'+
			urls_new_str
			+'</pre>' );
		$('#textarea-urls-new').highlight(get_urls_washed_from_raw($('#textarea-urls-raw').val()));
	},function(){
		$("#textarea-urls-new").remove();
		$('#textarea-urls-raw').show();
	});


	test();
});

$( document ).ajaxStart(function() {
	$(".btn-ajax").prop("disabled",true);
});





function test(){
	$("#btn-urls-seq").click();
}



function get_status_code_recur(newUrls,length,cur){
	if (cur == length) {
		hide_loader('All urls has done!');
		$(".btn-ajax").prop("disabled",false);
		return
	} 
	show_loader('Checking ->' + newUrls[cur] )

	var post_data={
		op:"getUrlStatusCode",
		url:newUrls[cur],
	};

	$.ajax({
		method: "POST",
		url: API_PATH,
		data: JSON.stringify(post_data),
		contentType: 'application/json;charset=UTF-8',
	}).done( function(response,status,xhr) {
		$('#response-raw').append('<a href="'+
			newUrls[cur]+
			'" target="_blank">'+
			newUrls[cur]+
			'</a> ->'+
			response +
			'<br>')
		get_status_code_recur(newUrls,length,cur+1)
	}).fail( function(e) {
		$('#response-raw').html('ERROR:<br>'+e.responseText)
	});
}


function init_view(){
	$('#response-raw').html('')
	$(".btn-ajax").prop("disabled",true);
}

function show_loader(text=''){
	$('#sec-loader').html(text+'<img src="/img/index.beating-heart-preloader.svg">');
}

function hide_loader(text=''){
	$('#sec-loader').html(text);
}

function get_urls_washed_from_raw(raw_str){
	arrayOfRawUrls = raw_str.split(/[\r\n]+/)
	url=''
	washedUrls=[]

	for (var i = 0; i < arrayOfRawUrls.length; i++) {
		washedUrl=arrayOfRawUrls[i].replace(/^\s+|\s+$/g, '');
		washedUrls.push(washedUrl)
	}

	return washedUrls
}

function get_urls_new_from_raw(raw_str){
	washedUrls = get_urls_washed_from_raw(raw_str)
	url=''
	newUrls=[]

	for (var i = 0; i < washedUrls.length; i++) {
		washedUrl=washedUrls[i];
		if (is_url_with_protocal(washedUrl)) {
			newUrls.push(washedUrl)
		} else {
			checked=0
			if($("#cb-add-http").is(':checked')){
				checked=1
				newUrls.push('http://'+washedUrl)

			}
			if($("#cb-add-https").is(':checked')){
				checked=1
				newUrls.push('https://'+washedUrl)
			}
			if($("#cb-add-ftp").is(':checked')){
				checked=1
				newUrls.push('ftp://'+washedUrl)
			}
			if (checked==0) {
				newUrls.push('http://'+washedUrl)
			}
		}
	}

	return newUrls;
}










function is_url_with_protocal(surl){
	var reg = /^(http|https|ftp):\/\//g;
	return surl.match(reg)?1:0;
}










