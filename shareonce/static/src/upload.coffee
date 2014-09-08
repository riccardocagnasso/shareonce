max_file_size = 20*Math.pow(2, 20)

chunkedReaderIterator = (file) ->
    obj =
        file: file
        init: ->
            this.i = 0
            this.maxChunkSize = 300 * (Math.pow 2, 10)
            this.chunks = Math.ceil (this.file.size / this.maxChunkSize)

        init_socket: ->
            this.socket = io.connect '/file'
            that = this
            this.socket.on 'chunkdone', ->
                progress = parseInt (obj.i / obj.chunks * 100), 10
                ($ '#uploadbar span').css 'width', progress+'%'
                ($ '#progressmeter').html progress+'%'

                obj.next()


            this.socket.on 'filedone', (data) ->
                progress = parseInt (obj.i / obj.chunks * 100), 10
                ($ '#uploadbar span').css 'width', progress+'%'
                ($ '#progressmeter').html progress+'%'

                ($ '#url').val data.url
                ($ '#copy-button').removeClass 'disabled'
                ($ '#upload-button').removeClass 'disabled'
                that.socket.disconnect()

            this.socket.on 'toobig', ->
                progress = 0
                ($ '#uploadbar span').css 'width', progress+'%'
                ($ '#progressmeter').html progress+'%'

                ($ '#url').val 'ERROR! FILE TOO BIG! EXTERMINATE! EXTERMINATE!'
                ($ '#copy-button').removeClass 'disabled'
                ($ '#upload-button').removeClass 'disabled'
                that.socket.disconnect()

        start: ->
            if this.file.size <= max_file_size
                this.init_socket()
                this.socket.emit 'upload',
                    filename: this.file.name
                    size: this.file.size
                    mime: this.file.type
                this.next()
            else
                console.log('tooo big')

        next: ->
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

        submit: (e, data) ->
            ($ '#upload-button').addClass 'disabled'
            file = data.files[0]

            reader = chunkedReaderIterator(file)
            reader.start()
            false
