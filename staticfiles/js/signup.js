$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name +'=')) {
                         cookieValue =decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) ||
/^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});
$("#btn_signup").click(function(e){
$("#formid").submit()
});
$("#formid").submit(function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
    url : "{% url 'r_home' %}",
    type : "POST",
    data : formData,
    dataType:'json',
    contentType: false,
    processData: false,
        success : function(data) {
        console.log(data);
            if (data.result != "success")
             {
            alert("error");

             }
             else{
             alert("success");
             }
        },
        // handle a non-successful response
        error : function(xhr,errmsg,errors) {
        console.log(xhr.status + ": " + xhr.responseText);
        console.log(errors)// provide a bit more info about the error to the console
        }
    });
});


//$.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         function getCookie(name) {
//             var cookieValue = null;
//             if (document.cookie && document.cookie != '') {
//                 var cookies = document.cookie.split(';');
//                 for (var i = 0; i < cookies.length; i++) {
//                     var cookie = jQuery.trim(cookies[i]);
//                     // Does this cookie string begin with the name we want?
//                     if (cookie.substring(0, name.length + 1) == (name +'=')) {
//                         cookieValue =decodeURIComponent(cookie.substring(name.length + 1));
//                         break;
//                     }
//                 }
//             }
//             return cookieValue;
//         }
//         if (!(/^http:.*/.test(settings.url) ||
///^https:.*/.test(settings.url))) {
//             // Only send the token to relative URLs i.e. locally.
//             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         }
//     }
//});
//$("#btn_signup").click(function(e){
//
//e.preventDefault();
//alert("ajax call");
//$.ajax({
//	url:"{% url 'r_home' %}",
//	type:"post",
//	datatype:"json",
//	data:$("#formid").serialize(),
//
//	success:function(data)
//	{
//		if(data.status)
//		{
//            	alert(data.val)
//		}
//		else
//		{
//
//		}
//	},
//	error:function()
//	{
//	alert("Connection Failed");
//	}
//	});
//});
//
