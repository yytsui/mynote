==============
Tips
==============

Search and Replace in all files within a directory recursively on Linux
========================================================================

http://www.jonasblog.com/2006/05/search-and-replace-in-all-files-within-a-directory-recursively.html

It's much more simpler to use the 'rpl' command, as shown below:

rpl -x'.cpp' -x'.h' -R "old-string" "new-string" *

Here, all files with a .cpp or .h suffix wil be searched for

an "old-string". If found the "old-string" is replaced by the

"new-string" in all directories recursively.

To install on Ubuntu or Debian just do 'apt-get install rpl'.

youtube-dl download playlist and use title name as file name
=============================================================

youtube-dl  -o '%(stitle)s.%(ext)s' http://www.youtube.com/playlist?list=PLF35EE6F0A1ADF8AE
