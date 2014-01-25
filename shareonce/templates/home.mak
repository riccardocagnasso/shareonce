<%inherit file="master.mak"/>

<div>
    <div class="columns large-3">

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
        Lorem ipsum Ea elit Duis voluptate adipisicing eiusmod laborum commodo dolore dolor labore cillum nostrud eu cupidatat culpa nulla et sit in in laboris pariatur sit dolor non fugiat proident proident velit ad nostrud adipisicing id irure proident voluptate laborum fugiat magna non dolor pariatur mollit fugiat ex in ut et velit Duis reprehenderit adipisicing aliquip do aliquip eiusmod laborum et aute consectetur ad dolore Ut deserunt non aliquip in sunt ullamco reprehenderit minim labore id Ut laboris aute anim do cillum Duis nostrud irure cupidatat in Excepteur mollit in enim proident exercitation Duis nisi commodo in non ad non consectetur ea labore sed Excepteur nostrud ullamco nisi enim dolore veniam nostrud culpa consequat adipisicing cupidatat aliquip voluptate ad sint veniam dolor do cupidatat tempor ut in dolor enim deserunt aute id in velit adipisicing eiusmod in ea mollit ut nulla id officia ea officia ea aliquip adipisicing ut ad voluptate enim mollit eiusmod deserunt anim Excepteur in nulla est in deserunt nisi qui amet.
    </div>
</div>