html_page = '''
<html><head>
<title>Pair-up tool</title>
<script language="javascript">
pause = 3000

people = new Array(%s)

numPairs = %s

document.write("<style type='text/css'>")
for(i = 1; i <= numPairs; i++)
  document.write("#hot" + i + " {color:black; background:green}")
document.write("</style>");

currLine = 1
function cycleColors() {
  for(i = 1; i <= numPairs; i++) {
    obj = eval("document.all.hot" + i)
    obj.style.color = (i == currLine)? "white":"black"
    obj.style.background = (i == currLine)? "green":"white"
  }
  currLine++;
  if(currLine > numPairs) currLine = 1;
  setTimeout("cycleColors()", pause)
}
</script>
</head>
<body onLoad="cycleColors()">
<font FACE="Verdana,Tahoma,Arial,Helvetica,Sans">
<center>
<TABLE BORDER="4" CELLPADDING="2" CELLSPACING="0">
<script>
x = 0
for(i = 1; i <= numPairs; i++) {
  document.write("<TR id=hot" + i + "><TD><b><font size='+2'>" +  people[x++] +
    "</font></b></TD></TR>")
}
</script>
</TABLE></body></html>
'''
