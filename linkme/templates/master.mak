<!doctype html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" data-useragent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ShareOnce</title>

    
    <meta name="description" content="shareonce" />
    
    <meta name="author" content="Riccardo Cagnasso" />
    <meta name="copyright" content="Riccardo Cagnasso" />

    <link rel="stylesheet" href="${request.static_path('linkme:static/dist/css/stylesheet.css')}" />
    <script src="${request.static_path('linkme:static/dist/js/home.js')}"></script>
  </head>
  <body>

    <nav class="top-bar" data-topbar>
      <ul class="title-area">
        <li class="name">
          <h1><a href="/">ShareOnce</a></h1>
        </li>
      </ul>
    </nav>

    ${self.body()}

    <script>
      $(document).foundation();

      var doc = document.documentElement;
      doc.setAttribute('data-useragent', navigator.userAgent);
    </script>
  
  </body>
</html>