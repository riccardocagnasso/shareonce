<!doctype html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" data-useragent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>LinkMe</title>

    
    <meta name="description" content="linkme" />
    
    <meta name="author" content="Riccardo Cagnasso" />
    <meta name="copyright" content="Riccardo Cagnasso" />

    <link rel="stylesheet" href="${request.static_path('linkme:static/dist/css/stylesheet.css')}" />
    <script src="${request.static_path('linkme:static/dist/js/foundation.js')}"></script>
  </head>
  <body>

    <nav class="top-bar" data-topbar>
      <ul class="title-area">
        <li class="name">
          <h1><a href="#">My Site</a></h1>
        </li>
        <li class="toggle-topbar menu-icon"><a href="#">Menu</a></li>
      </ul>

      <section class="top-bar-section">
        <!-- Right Nav Section -->

        <ul class="right">
          <li class="active"><a href="#">Right Button Active</a></li>
          <li class="has-dropdown">
            <a href="#">Right Button with Dropdown</a>
            <ul class="dropdown">
              <li><a href="#">First link in dropdown</a></li>
            </ul>
          </li>
        </ul>

        <!-- Left Nav Section -->
        <ul class="left">
          <li><a href="#">Left Nav Button</a></li>
        </ul>

      </section>
    </nav>

    ${self.body()}

    <script>
      $(document).foundation();

      var doc = document.documentElement;
      doc.setAttribute('data-useragent', navigator.userAgent);
    </script>
  
  </body>
</html>