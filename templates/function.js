function clear(){
    document.getElementById('result').innerHTML="";
}

function searchData(){
    var content = $('#content').val();
    $('#content').val('');

    $.ajax({
        url:'/search/'+content,
        type:'GET',
        contentType: 'application/json',
        dataType:'json',
        success: function(response){
            var i = 0;
            for()
            $.each(response, function(){
                f = '<a class="alert alert-primary" role="alert">';
                f = f + response[i].content;
                f = f + '</a>';
                i = i+1;
                $('#result').append(f);
            });
        },
        error: function(response){
            alert(JSON.stringify(response));
        }
    });
}