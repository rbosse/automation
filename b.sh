ls *.jpg | perl -lne 'print "$_<br><img src=\"$_\"/>"' > index.html

