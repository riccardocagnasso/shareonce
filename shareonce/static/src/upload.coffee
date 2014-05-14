chunkedReaderIterator = (file) -> 
    obj = 
        i: 0
        file: file
        init: ->
            this.maxChunkSize = Math.pow 2, 20
            this.chunks = Math.ceil (this.file.size / this.maxChunkSize)
            this.socket = io.connect '/file'

            this.socket.on 'chunkdone', ->
                progress = parseInt (obj.i / obj.chunks * 100), 10
                ($ '#uploadbar span').css 'width', progress+'%'
                ($ '#progressmeter').html progress+'%'

                obj.next()


            this.socket.on 'filedone', (data) ->
                console.log data

        start: ->
            this.socket.emit 'upload', 
                filename: this.file.name
                size: this.file.size
                mime: this.file.type
            this.next()

        next: ->
            console.log('next')
            if this.i >= this.chunks
                null
            else
                chunk = this.file.slice(this.i*this.maxChunkSize,
                        (this.i+1)*this.maxChunkSize)

                this.uploadChunk(chunk)
                this.i += 1
                this.i
        uploadChunk: (chunk) ->
            reader = new FileReader()

            that = this
            reader.onload = (evt) ->
                console.log 'emit'
                that.socket.emit 'chunk', evt.target.result

            reader.readAsDataURL chunk

        progress: (percent) ->
            true

    obj.init()
    obj



$ ->
    ($ '#fileupload').fileupload
        dataType: 'json'
        maxChunkSize: 100000
        start: (e) ->
            true

        done: (e, data) ->
            ($ '#url').val data.response().result['url']
            ($ '#copy-button').removeClass 'disabled'
            ($ '#upload-button').removeClass 'disabled'
            true

        submit: (e, data) ->
            ($ '#upload-button').addClass 'disabled'
            file = data.files[0]


            reader = chunkedReaderIterator(file)
            reader.start()
            false