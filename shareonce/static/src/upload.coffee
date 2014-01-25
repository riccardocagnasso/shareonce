$ ->
    ($ '#fileupload').fileupload
        dataType: 'json'

        start: (e) ->
            ($ '#upload-button').addClass 'disabled'
            true

        progressall: (e, data) ->
            progress = parseInt (data.loaded / data.total * 100), 10
            ($ '#uploadbar span').css 'width', progress+'%'
            ($ '#progressmeter').html progress+'%'

        done: (e, data) ->
            ($ '#url').val data.response().result['url']
            ($ '#copy-button').removeClass 'disabled'
            ($ '#upload-button').removeClass 'disabled'
            true