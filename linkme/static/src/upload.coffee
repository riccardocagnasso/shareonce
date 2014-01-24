$ ->
    ($ '#fileupload').fileupload
        dataType: 'json'

        progressall: (e, data) ->
            progress = parseInt (data.loaded / data.total * 100), 10
            console.log progress
            ($ '#uploadbar span').css 'width', progress+'%'

        done: (e, data) ->
            ($ '#url').val(data.response().result['url'])