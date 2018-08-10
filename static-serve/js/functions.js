$(document).ready(function(){
    function fetchNotes(){
        $("#notes-container").empty();
        $.ajax({
            url: $('#notes-container').attr('url'),
            method: 'GET',
            success: function(data){
                parseNotes(data);
            },
            error: function(data){
                console.log('error');
                console.log(data);
            }
        });
    };


    function parseNotes(data){
        $.each(data, function(key, value){
            $("#notes-container").append('<p>' + value.content + '</p>')
        });
    };


    fetchNotes();


    $('#create-note').submit(function(e){
        e.preventDefault();
        this_ = $(this);
        formData = this_.serialize();
        $.ajax({
            url: this_.attr('action'),
            method: 'POST',
            data: formData,
            success: function(data){
                this_.find("input[type=text], textarea").val("")
                fetchNotes();
            },
            error: function(data){
                console.log('error');
                console.log(data);
            }
        })
    });
});