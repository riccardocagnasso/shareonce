$ ->
    ($ '#fileupload').fileupload
        dataType: 'json'

        progressall: (e, data) ->
            progress = parseInt (data.loaded / data.total * 100), 10
            ($ '#uploadbar span').css 'width', progress+'%'
            ($ '#progressmeter').html progress+'%'

        done: (e, data) ->
            ($ '#url').val(data.response().result['url'])