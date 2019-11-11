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

$("#formid").submit(function(e) {
    var url = $('#url').val();
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
    url : url,
    type : "POST",
    data : formData,
    dataType:'json',
    contentType: false,
    processData: false,
        success : function(data)
        {
            console.log(data);
            if(data.pass)
            {
                 alert(data.pass);
            }
            if (data.val =="Success")
             {
               document.getElementById("alert").innerHTML = "Signup done successfully. Please login to continue!";
             }
             else if(data.val =="failure")
             {
 document.getElementById("alert").innerHTML = "Error";
             }
             else if(data.val=="Error")
             {
 document.getElementById("alert").innerHTML = "Error";
             }


             else
             {

             $("#formid :input:not(input[type='hidden'],input[type='submit'])").each(function ()
              {
                 var current = $(this).parent();
                 var current_name = $(this).attr('name');
                 $.each(data.dict1, function (index, value)
                 {
                     if (current_name == index)
                      {

                      current.after("<div class='error'></div>");
                     current.next().html(value);
//;
                     }
                 });
             });
           }
       },
        // handle a non-successful response
        error : function(xhr,errmsg,errors) {
        console.log(xhr.status + ": " + xhr.responseText);
        console.log(errors)// provide a bit more info about the error to the console
        }
    });
});

$("#btn_login").click(function(e){

$("#loginform").submit()
});
$("#loginform").submit(function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
    url : "/login/",
    type : "POST",
    data : formData,
    dataType:'json',
    contentType: false,
    processData: false,
        success : function(data)
         {
            console.log(data);
            if (data.val == "success")
             {
	        	window.location.replace("/")
             }
            else if(data.val =="failed")
             {
             document.getElementById("error").innerHTML = "Username / Password Incorrect!";
//               alert("Username / Password Incorrect!");
             }

        },
        // handle a non-successful response
        error : function(xhr,errmsg,errors)
         {
              document.getElementById("error").innerHTML = "Username / Password Incorrect!";
        console.log(xhr.status + ": " + xhr.responseText);
        console.log(errors)// provide a bit more info about the error to the console
        }
    });
});




$("#btn_submit").click(function(e){
e.preventDefault();
$.ajax({
	url:"/comment/",
	type:"post",
	datatype:"json",
	data:$("#commentform").serialize(),
	success:function(data)
	{
		if(data.val="success")
		{

			  document.getElementById("alert").innerHTML = "Success";

		}
		else
		{
		 document.getElementById("alert").innerHTML = "Error During submission";
		}

	},
	error:function()
	{
	if(data.val="Already exist")
	{
	document.getElementById("error").innerHTML = "Already exist";
	}
document.getElementById("error").innerHTML = "Empty fields not allowed";
	}
	});
});


$("#btn_send").click(function(e){
e.preventDefault();
$.ajax({
	url:"/contact/",
	type:"post",
	datatype:"json",
	data:$("#contactform").serialize(),
	success:function(data)
	{
		if(data.val="success")
		{
			document.getElementById("alert").innerHTML = "Success";
		}

	},
	error:function()
	{
 document.getElementById("error").innerHTML = "Empty field not allowed!";
	}
	});
});


$("#btn_newsletter").click(function(e){
e.preventDefault();
$.ajax({
	url:"/about/",
	type:"post",
	datatype:"json",
	data:$("#newsletterform").serialize(),
	success:function(data)
	{

		if(data.val=="success")
		{
			document.getElementById("alert").innerHTML = "Subscribed !";
		}
		else
		{
		document.getElementById("alert").innerHTML = "Error !";
		}


	},
	error:function()
	{


    $("#newsletterform :input:not(input[type='hidden'],input[type='submit'])").each(function ()
         {
            var current = $(this).parent();
            var current_name = $(this).attr('name');
            alert(data.error);
            $.each(data.error, function (index, value)
            {
//            alert(index, current_name);
            $('#alert').html(value);
            });
         });

 document.getElementById("alert").innerHTML = "Empty field not allowed!";
	}
	});
});



