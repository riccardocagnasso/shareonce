$ ->
    copy_sel = ($ '#copy-button')

    copy_sel.on 'click', (e) ->
        e.preventDefault();

    copy_sel.clipboard
        path: '/static/jquery.clipboard.swf'

        copy: ->
            ($ '#url').val()
