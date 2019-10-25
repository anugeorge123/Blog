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
//$("#btn_signup").click(function(e){
//$("#formid").submit()
//alert("helloo");
//});
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
               alert("Signup done successfully");
             }
             else if(data.val =="failure")
             {
               alert("Password Incorrect");
             }
             else if(data.val=="Error")
             {
               alert("Error");
             }
             else
             {
             alert(data.val);
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
;
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
//    alert("ajax call");
    $.ajax({
    url : "/login/",
    type : "POST",
    data : formData,
    dataType:'json',
    contentType: false,
    processData: false,
        success : function(data)
         {
            $('#txt_username').val("");
		    $('#txt_password').val("");
        console.log(data);
            if (data.val == "success")
             {
               alert("Login Successfull");
             }
            else if(data.val =="failed")
             {
               alert("Username / Password Incorrect!");
             }

        },
        // handle a non-successful response
        error : function(xhr,errmsg,errors) {
        console.log(xhr.status + ": " + xhr.responseText);
        console.log(errors)// provide a bit more info about the error to the console
        }
    });
});




