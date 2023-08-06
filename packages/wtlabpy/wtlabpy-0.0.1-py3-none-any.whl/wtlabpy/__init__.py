def p1a():
    return """<!DOCTYPE html>
<!--1a.html-->
<html lang="en">
<head>
<title>Information</title>
<meta charset="utf-8" />
</head>
<body>
<img src="C:\Users\USER\OneDrive\Desktop\wt lab\asgar.jpg.JPG" height="200" width="200" alt="My profile picture" />
<h1>Student information</h1>
<p>
Shaikh Asgar Sadiq<br />
USN:20IS086<br />
College:Sri Siddartha Institute of Technology<br />
email:20is086@ssit.edu.in<br />
Branch:Information Science and Engineering<br />
</p>
<hr />
<h2>Major and Grade</h2>
<p>
Bachelor of Engineering at
<em>Sri Siddartha Institute of Technology</em>
<br />
Grade:A<br />
CGPA:7.51<br />
SGPA:7.27<br />
<strong><a href="C:\Users\Desktop\wt lab\1b.html">Best Friend</a></strong><br />
<strong><a href="C:\Users\wt lab\1c.html">My Info</a></strong>
</p>
</body>
</html>
"""

def p1b():
    return """<!DOCTYPE html>
<!--1b.html-->
<html lang="en">
<head>
<title>My Bestfriend and Our Faculty</title>
<meta charset="utf-8" />
</head>
<body>
<center>
<h2>My Bestfriends</h2>
<img src="C:\Users\USER\Desktop\wt lab\IMG_0064.JPG" height="75%" width="50%" />
<hr />
<h2>Our Faculty</h2>
<img src="C:\Users\USER\Desktop\wt lab\IMG_9795.JPG" height="500" />
</center>
</body>
</html>
"""

def p1c():
    return """<!DOCTYPE html>
<!--1c.html-->
<html lang="en">
<head>
<title>My Info</title>
<meta charset="utf-8" />
</head>
<body>
<h1>More Information</h1>
<pre>
<h2>
My name is Shaikh Asgar Sadiq.
I am a student of SSIT ISE Dept.
My hobbies are playing cricket, riding bikes, etc.
My favorite bike is Honda Unicorn.
</h2>
</pre>
</body>
</html>
"""

def p2():
    return """<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Introduction page</title>
	<link rel="stylesheet" href="1.css">
</head>
<body>
	<h2> CHAPTER-01</h2>
	<center>
		<h1>Introduction to HTML5</h1>
	</center>
	<hr>
	<h3>Introduction</h3>
	<p> HTML is Hyper Text Markup Language, Latest version is HTML5. This is widely used version. <br>HTML runs under tags.
	</p>
	<h3>Tags</h3>
	<p> There are so many tags in HTML, Widely used tags are:-
		<br/> H1: This is the heading tag h1 prints most bigger words compared to other heading tags.
		<br/> html: HTML is the tag which contains the html code 
	</p>
</body>
</html>
//external css//
h1 {
	font: bold 2em Helvetica, 'Times New Roman';
}

h2 {
	font: bold 1.8em Helvetica, 'Times New Roman';
}

h3 {
	font: bold 1.2em Helvetica, 'Times New Roman';
}

p {
	font: 1em 'Times New Roman';
}

body {
	background-color: lightblue;
}
"""

def p3():
    return """<!DOCTYPE html>
<!--e36.html-->
<html lang="en">
<head>
<title>Exercise 3.6</title>
<style type="text/css">
ol {list-style-type: upper-roman;}
ol ol {list-style-type: upper-alpha;}
ol ol ol {list-style-type: decimal;}
li.pink {color: black;}
li.blue {color: blue;}
li.red {color: red;}
</style>
<meta charset="utf-8" />
</head>
<body bgcolor="skyblue">
<ol>
  <li class="black">Compact Cars
    <ol>
      <li>Two door
        <ol>
          <li>Hyundai Accent</li>
          <li>Chevrolet Cobalt</li>
          <li>Honda Civic</li>
        </ol>
      </li>
      <li>Four door
        <ol>
          <li>Hyundai Accent</li>
          <li>Chevrolet Cobalt</li>
          <li>Honda Civic</li>
        </ol>
      </li>
    </ol>
  </li>
  <li class="blue">Midsize Cars
    <ol>
      <li>Two door
        <ol>
          <li>Honda Accord</li>
          <li>Hyundai Genesis</li>
          <li>Nissan Altima</li>
        </ol>
      </li>
      <li>Four door
        <ol>
          <li>Honda Accord</li>
          <li>Dodge Avenger</li>
          <li>Ford Fusion</li>
        </ol>
      </li>
    </ol>
  </li>
  <li class="red">Sports Cars
    <ol>
      <li>Coupe
        <ol>
          <li>Jaguar XK</li>
          <li>Ford Mustang</li>
          <li>Nissan Z</li>
        </ol>
      </li>
      <li>Convertible
        <ol>
          <li>Mazda Miata</li>
          <li>Ford Mustang</li>
          <li>Lotus Elise</li>
        </ol>
      </li>
    </ol>
  </li>
</ol>
</body>
</html>
"""

def p4():
    return """<!DOCTYPE html>
<html>
<head>
<title>My calculator</title>
<script type="text/javascript">
	function call(click_id) {
		var v1 = parseFloat(document.getElementById("ip1").value);
		var v2 = parseFloat(document.getElementById("ip2").value);
		if (isNaN(v1) || isNaN(v2))
			alert("Enter a valid number");
		else if (click_id == "add")
			document.getElementById("output").value = v1 + v2;
		else if (click_id == "sub")
			document.getElementById("output").value = v1 - v2;
		else if (click_id == "mul")
			document.getElementById("output").value = v1 * v2;
		else if (click_id == "div")
			document.getElementById("output").value = v1 / v2;
	}
</script>
</head>
<body>
<center>
	<h1> A SIMPLE CALCULATOR PROGRAM</h1>
	<table style="background-color: yellow;" align="center">
		<tr>
			<td>
				<form method="get" action="">
					<div width="50%" align="center">
						<label>OP1<input type="text" id="ip1" /></label>
						<label>op2<input type="text" id="ip2" /></label>
						<label>total<input type="text" id="output" /></label>
					</div>
					<br>
					<div width="50%" align="center">
						<input type="button" value="+" id="add" onclick="call(this.id)" />
						<input type="button" value="-" id="sub" onclick="call(this.id)" />
						<input type="button" value="*" id="mul" onclick="call(this.id)" />
						<input type="button" value="/" id="div" onclick="call(this.id)" />
						<input type="reset" value="clear" />
					</div>
				</form>
			</td>
		</tr>
	</table>
</center>
</body>
</html>
"""

def p5():
    return """ <!DOCTYPE html>
<html>
<head>
	<title>Squares and Cubes</title>
</head>
<body onload="sqrcub();">
	<h1 style="text-align: center;color: brown;">Squares and Cubes Using JavaScript</h1>
	<hr>
	<div id="tab">
	</div>
	<script>
		function sqrcub()
		{
			var result = "<table border='1' cellpadding='10'><tr><th>SNO</th><th>SQUARE</th><th>CUBE</th></tr>";
			var i, sqr = 0, cube = 0;
			for (i = 0; i <= 10; i++)
			{
				sqr = i * i;
				cube = Math.pow(i, 3);
				result += "<tr><td>" + i + "</td><td>" + sqr + "</td><td>" + cube + "</td></tr>";
			}
			result += "</table>";
			document.getElementById("tab").innerHTML = result;
		}
	</script>
</body>
</html>
"""

def p6a():
    return """ <!DOCTYPE html>
<html lang="en">
<head>
	<title>Fibonacci Non Interactive</title>
	<meta charset="utf-8" />
</head>
<body>
	<script type="text/javascript">
		<!--
		var first = 1, second = 1, next, count;
		document.write("First 20 Fibonacci Numbers <br/><br/>");
		document.write("1 - 1 <br/> 2 - 1 <br/>");
		for (count = 3; count <= 20; count++) 
		{
			next = first + second;
			document.write(count + " - " + next + "<br/>");
			first = second;
			second = next;
		}
		// -->
	</script>
</body>
</html>
"""


def p6b():
    return """ <!DOCTYPE html>
<html lang="en">
<head>
	<title>Fibonacci Interactive</title>
	<meta charset="utf-8" />
</head>
<body>
	<script type="text/javascript">
		<!--
		var first = 1, second = 1, next, count;
		var number = prompt("How many Fibonacci numbers do you want? (3-50)", "");
		if (number >= 3 && number <= 50) 
		{
			document.write("First " + number + " Fibonacci Numbers <br /><br />");
			document.write("1 - 1 <br/> 2 - 1 <br />");
			for (count = 3; count <= number; count++) 
			{
				next = first + second;
				document.write(count + " - " + next + "<br />");
				first = second;
				second = next;
			}
		}
		else
			document.write("Error - number not in the range 3-50");
		//-->
	</script>
</body>
</html>
"""


def p7():
    return """ <!DOCTYPE html>
<html>
<head>
<title>JavaScript - Grow & Shrink Text</title>
<center>
<script language="JavaScript">
var c = 0, t1;

function start() {
    t1 = window.setInterval("incr()", 100);
}

function incr() {
    c = c + 1;
    t.innerHTML = "TEXT-GROWING : " + c + "pt";
    t.style.fontSize = c + "pt";
    window.status = c;
    if (c > 50) {
        window.clearTimeout(t1);
        alert("Font Size Reached 50pt. Text will Now Shrink");
        t1 = window.setInterval("decr()", 100);
    }
    t.style.color = "black";
}

function decr() {
    c = c - 1;
    t.innerHTML = "TEXT-SHRINKING: " + c + "pt";
    t.style.fontSize = c + "pt";
    window.status = c;
    if (c == 5) {
        window.clearTimeout(t1);
    }
    t.style.color = "blue";
}
</script>
<center>
</head>
<body bgcolor="skyblue" onload="start()">
    <center>
        <p id="t"></p>
    </center>
</body>
</html>
"""


def p8():
    return """ <!DOCTYPE html>
<html lang="en">
<head>
	<title>Illustrate form validation</title>
	<meta charset="utf-8" />
	<script type="text/javascript" src="validator.js"></script>
</head>
<body>
	<h3>Customer Information</h3>
	<form action="">
		<p>
			<label><input type="text" id="custName" />Name (last name, first name, middle initial)</label>
			<br /><br />
			<label><input type="text" id="phone" />Phone Number (ddd-ddd-dddd)</label>
			<br /><br />
			<input type="reset" id="Reset" />
			<input type="submit" id="Submit" />
		</p>
	</form>
	<script type="text/javascript" src="validator.js"></script>
</body>
</html>
//external javascript//
function chkName() {
	var myName = document.getElementById("custName");
	var pos = myName.value.search(/^[A-Z][a-z]+,?[A-Z][a-z]+,?[A-Z]\.?$/);
	if (pos !== 0) {
		alert("The name you entered (" + myName.value + ") is not in the correct form.\n" + "The correct form is: last-name, first-name, middle-initial\n" + "Please go back and fix your name");
		return false;
	} else
		return true;
}

function chkPhone() {
	var myPhone = document.getElementById("phone");
	var pos = myPhone.value.search(/^\d{3}-\d{3}-\d{4}$/);
	if (pos !== 0) {
		alert("The phone number you entered (" + myPhone.value + ") is not in the correct form.\n" + "The correct form is: ddd-ddd-dddd\n" + "Please go back and fix your phone number");
		return false;
	} else
		return true;
}

document.getElementById("custName").addEventListener("change", chkName);
document.getElementById("phone").addEventListener("change", chkPhone);
"""


def p9():
    return """ <!DOCTYPE html>
<html lang="en">
<head>
	<title>Orders</title>
	<script type="text/javascript" src="EventHandler.js"></script>
	<meta charset="utf-8" />
</head>
<body>
	<h3>Order Form</h3>
	<form name="orderForm" onSubmit="finish()">
		<p>
			<label>
				<input type="text" name="apples" size="3" onChange="appleHandler()" /> Apples
			</label>
		</p>
		<p>
			<label>
				<input type="text" name="oranges" size="3" onChange="orangeHandler()" /> Oranges
			</label>
		</p>
		<p>
			<label>
				<input type="text" name="bananas" size="3" onChange="bananaHandler()" /> Bananas
			</label>
		</p>
		<p>
			<input type="reset" name="reset" />
			<input type="submit" name="submit" />
		</p>
	</form>
</body>
</html>
//external javascript//
var total = 0;

function appleHandler() {
	var number = document.orderForm.apples.value;
	total = total + number * 0.59;
}

function orangeHandler() {
	var number = document.orderForm.oranges.value;
	total = total + number * 0.49;
}

function bananaHandler() {
	var number = document.orderForm.bananas.value;
	total = total + number * 0.39;
}

function finish() {
	total = total * 1.05; // Applying 5% sales tax
	alert("Thank you for your order\n" + "Your total cost is: $" + total.toFixed(2) + "\n");
}
"""


def p10():
    return """ <?php
$a = array(array(1, 2, 3), array(4, 5, 6), array(7, 8, 9));
$b = array(array(7, 8, 9), array(4, 5, 6), array(1, 2, 3));
$m = count($a);
$n = count($a[2]);
$p = count($b);
$q = count($b[2]);

echo "The first matrix:", "<br/>";
for ($row = 0; $row < $m; $row++) {
    for ($col = 0; $col < $n; $col++)
        echo " " . $a[$row][$col];
    echo "<br/>";
}

echo "The second matrix:" . "<br />";
for ($row = 0; $row < $p; $row++) {
    for ($col = 0; $col < $q; $col++)
        echo " " . $b[$row][$col];
    echo "<br/>";
}

echo "The Transpose for the first matrix is:" . "<br />";
for ($row = 0; $row < $m; $row++) {
    for ($col = 0; $col < $n; $col++)
        echo " " . $a[$col][$row];
    echo "<br/>";
}

if (($m === $p) and ($n === $q)) {
    echo "The Addition of Matrices is:" . "<br />";
    for ($row = 0; $row < 3; $row++) {
        for ($col = 0; $col < 3; $col++)
            echo " " . $a[$row][$col] + $b[$row][$col] . " ";
        echo "<br/>";
    }
}

if ($n === $p) {
    echo "The Multiplication of Matrices : <br />";
    $result = array();
    for ($i = 0; $i < $m; $i++) {
        for ($j = 0; $j < $q; $j++) {
            $result[$i][$j] = 0;
            for ($k = 0; $k < $n; $k++)
                $result[$i][$j] += $a[$i][$k] * $b[$k][$j];
        }
    }
    for ($row = 0; $row < $m; $row++) {
        for ($col = 0; $col < $q; $col++)
            echo " " . $result[$row][$col];
        echo "<br/>";
    }
}
?>
"""


def p11():
    return """ <?php
print "<h3>REFRESH PAGE</h3>";
$name = "counter.txt";
$file = fopen($name, "r");
$hits = fscanf($file, "%d");
fclose($file);
$hits[0]++;
$file = fopen($name, "w");
fprintf($file, "%d", $hits[0]);
fclose($file);
print "Total no of views: " . $hits[0];
?>
"""


def p12():
    return """ <!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="1"/> <!-- Refresh the page every 1 second -->
<style>
  p {
    color: white; /* Corrected the spelling of "color" */
    font-size: 90px; /* Corrected the syntax for font-size */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  body {
    background-color: black; /* Corrected the spelling of "background-color" */
  }
</style>
</head>
<body>
  <p><?php echo date("h :i :s A");?></p>
</body>
</html>
"""


