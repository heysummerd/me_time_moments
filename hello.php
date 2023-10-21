<!DOCTYPE html>
<html>
  <head>
    <!--
    Author: Jessa K. West, Summer Davis, Eden Bishop, Raghaad Abujabal
    Date:   October 2023
    Filename: hello.html
   -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Me Time Moments: Hello Page</title>
  </head>

  <body>
    <header>
      <img id="logo" src="https://github.com/heysummerd/me_time_moments/blob/images/metimemomentslogo.png?raw=true" alt="me time moments logo">
    </header>
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST["name"];
        echo "<h1>Hello, $name!</h1>";
    } else {
        echo "<h1>Invalid request</h1>";
    }

  </body>
  <footer>
    Me Time Moments | HackTX23 Web App by Jessa K. West, Summer Davis, Eden Bishop, Raghaad Abujabal of ACC
  </footer>
</html>
