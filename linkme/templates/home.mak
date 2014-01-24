<%inherit file="master.mak"/>

<div class="row">
    <input id="fileupload" type="file" name="file" data-url="/upload">

    <div id="uploadbar" class="progress radius round">
      <span class="meter" style="width: 0%"></span>
    </div>
</div>

<div class="row collapse">
    <div class="small-10 columns">
        <input type="text" id="url" placeholder="url will appear here">
    </div>
    <div class="small-2 columns">
        <button id="copy-button" class="button postfix">copy</a>
    </div>
</div>