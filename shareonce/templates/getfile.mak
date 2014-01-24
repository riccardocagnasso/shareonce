<%inherit file="master.mak"/>

<div class="row">
    <div class="columns">
        <p class="panel">
        You are about to download <strong>${token.upload.file.filename}</strong><br>
        If the download does not start in 10 seconds <a href="${request.route_url('file.serve', token=token.urlid)}"> click here.</a>
        </p>
    </div>
</div>
