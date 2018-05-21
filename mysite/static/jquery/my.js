$('.js-question-like').on('click', function () {
    var $btn = $(this);
    question_id = $btn.data('id')
    $.ajax({
        method: "POST",
        url : "/like/",
        data: {"question_id": question_id, "csrfmiddlewaretoken": csrftoken, },
        dataType: 'json'
    })
        .done(function (data) {
            console.log(data);
            $('#question_likes-'+question_id.text(data.likes))
        })
    return false;
});