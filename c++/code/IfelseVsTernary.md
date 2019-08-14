## If-else Vs Ternary

If else vs ternary comparison; the actual code looks very simple but could be lengthy for if-else and sometimes complicated and short for ternary code. 

Example
<script src="https://gist.github.com/bhaumikmistry/cffd44f80b7beca4860cb1876adb8e33.js?file=if_else.cpp"></script>
VS
<script src="https://gist.github.com/bhaumikmistry/cffd44f80b7beca4860cb1876adb8e33.js?file=ternary.cpp"></script>

### Details on assambly
Using ```gcc -S file_name``` you can create assambly code alos [available as gist](https://gist.github.com/bhaumikmistry/cffd44f80b7beca4860cb1876adb8e33). The assambly code comes out to be equal for both files as you'll see the int initialization can be seen different, and that is the only difference in the file with ```gcc --version``` which is ```gcc.exe (i686-win32-dwarf-rev1, Built by MinGW-W64 project) 7.2.0```.

### Graphs
After running in loop ```n=41000000``` I have collected some data and the chart shows simple answer as the iteration goes up the difference in time execution also grows.
<script src="https://gist.github.com/bhaumikmistry/cffd44f80b7beca4860cb1876adb8e33.js?file=graph.png"></script>


### More discussion and stack*OverFlow* answer links
+ [embeddedgurus](https://embeddedgurus.com/stack-overflow/2009/02/efficient-c-tips-6-dont-use-the-ternary-operator/)
+ [nynaeve](http://www.nynaeve.net/?p=178)
+ [questions/3565368](https://stackoverflow.com/questions/3565368/ternary-operator-vs-if-else)
+ [questions/6754454](https://stackoverflow.com/questions/6754454/speed-difference-between-if-else-and-ternary-operator-in-c)