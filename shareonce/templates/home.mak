<%inherit file="master.mak"/>

<div>
    <div class="columns large-3">

        <div class="row">
            <br>
            <br>
        </div>

        <div class="row">
            <button id="upload-button" class="button success round fileinput-button">
                <i class="fi-plus"></i>
                <span>Select a file</span>
                <!-- The file input field used as target for the file upload widget -->
                <input id="fileupload" type="file" name="file" data-url="/upload">
            </button> or simply <strong>drop</strong> one anywhere.
        </div>

        <div class="row">
            <div class="columns large-10">
                <div id="uploadbar" class="progress radius round">
                  <span class="meter" style="width: 0%"></span>
                </div>
            </div>
            
            <div class="columns large-2">
                <span id="progressmeter"></span>
            </div>
        </div>

        <div class="row collapse">
            <div class="small-10 columns">
                <input type="text" id="url" placeholder="url will appear here">
            </div>
            <div class="small-2 columns">
                <button id="copy-button" class="button postfix disabled">copy</button>
            </div>
        </div>

    </div>

    <div class="columns large-3"></div>

    <div class="columns large-6">
        <div class="explain">
            <h3>How it works?</h3>
            <br>
            When you upload a file a link will be generated.<br>
            <br>
            The link will be valid for 72 hours.<br>
            <br>
            The link can be used to download the file.<br>
            <br>
            Once the link is used, is not valid anymore.<br>
        </div>
    </div>
</div>