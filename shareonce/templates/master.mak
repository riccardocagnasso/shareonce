<!doctype html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" data-useragent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ShareOnce</title>

    
    <meta name="description" content="shareonce" />
    
    <meta name="author" content="Riccardo Cagnasso" />
    <meta name="dcterms.rightsHolder" content="Riccardo Cagnasso" />

    <link rel="stylesheet" href="${request.static_path('shareonce:static/dist/css/stylesheet.css')}" />
    <script src="${request.static_path('shareonce:static/dist/js/home.js')}"></script>

    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-50302768-1', 'shareonce.net');
      ga('send', 'pageview');

    </script>
  </head>
  <body>

    <nav class="top-bar" data-topbar>
      <ul class="title-area">
        <li class="name">
          <h1><a href="/"><i class="fi-upload-cloud"></i> ShareOnce</a></h1>
        </li>
      </ul>

      <section class="top-bar-section">
        <ul class="right">
          <li><a href="${request.route_url('privacy')}">privacy</a></li>
        </ul>
      </section>
    </nav>

    <br>

    ${self.body()}

    <script>
      $(document).foundation();

      var doc = document.documentElement;
      doc.setAttribute('data-useragent', navigator.userAgent);
    </script>
  </body>
</html>