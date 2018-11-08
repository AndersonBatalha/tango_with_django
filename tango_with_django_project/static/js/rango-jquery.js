$(document).ready(function () {
    $('#about-btn').click(function (event) {
        alert('You clicked the button using JQuery!');
    })

    $('p').hover(function () {
        $(this).css('color', 'blue');
    },
    function () {
        $(this).css('color', 'red');
    });

    $('#about-btn').addClass('btn-danger'); // adicionar classes a um elemento através do seu id.

    $('#about-btn').click(function () {
        msgstr = $('#msg').html();
        msgstr = msgstr + 'oooo'
        $('#msg').html(msgstr);
    });
});