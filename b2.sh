find . -name index.html | perl -lne 'print "<br><a href=\"$_\">$_</a>"' > index.html
