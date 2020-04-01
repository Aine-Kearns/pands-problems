# pands-problems
This folder contains python programmes developed as part of the Programme and Scripting Module for Data Analytics in GMIT.  
## List of programs within this repository
bmi.py is a programme that will calculate bmi after asking the user to input height in centimetres and weight in kilograms - homework from week 2 <br>
- here it is necessary define both variables and then change height from cm to m and square it<br>
- and then divide weight by height<br>
secondstring.py is a programme that allows the user to input a sentence and outputs every second letter in reverse order - homework from week 3<br>
- add a string using input<br>
- print out every second letter (::2)in the string (which is the variable "s")in reverse order (using the - before 2)<br> 
collatz.py is a programme that will take an integer that is entered by the user and output values based on specified calculations homework from week 4<br>
- allow the user to input a integer "x" requires int at the start of the input command, and I defined "y" as "2" because dividing by y will help to establish if the result is even <br>
- then using a while loop that will loop through the script until the condition is met in this case when x is not longer greater than 1<br>
- in the while "loop" and if condition was carried out if the outcome was even or "else" the other calculation was carried out if the outcome was an odd integer<br> 
weekday.py is a programme that will tell the user if today is a weekday or the weekend - homework from week 5<br>
- using the import datetime module for python and setting the variable "now" to find out the day of the week when the script was run it was possible to use an "if" statement to return if it was weekday or "else" print if it was a "weekend"<br>
squareroot.py is a programme that will provide the user with the square root of a number - homework from week 6<br>
- this was a tricky programme that was originally set up with the wrong function<br>
- following feedback and searches online (links are embedded in the script) it was possible to find the algorithm needed and then embed this in a while loop to continue to run and refine the algorithm until the difference was smaller than 0.00000001<br>
es.py is a programme that will read in a version of Moby Dick in a text file format and calculate the number of "e" letters in the document - homework from week 7<br>
- this required downloading a text file of Moby Dick (link to file is available in the script) and then opening the text file with a command in the python script<br>
- once opened a subsequent command to read the file and then count the number of e's in the text in upper and lower case<br>
week8plots.py is a programme that creates a plot - homework week 8<br>
- imported numpy and matplotlib to facilitate plot drawing<br>
- defined the array for the plot and then used the features to draw and label the plot
## Revision History
### March 30th 2020
Commenced the Readme file in order to track version updates and revisions within this folder<br>
Created week8plots.py with initial plot script<br>
Committed week8plots.py and Readme changes to github<br>
### March 31st 2020
Updated weekday.py to include reference to website that provided information on importing datetime module<br>
Updated week8plots.py to include the function of the program in the introduction at the beginning of the program<br>  
Updated collatz.py to remove unneccessary variable setting to produce a less complicated script<br>
Attempted to make changes to squareroot.py and although code will run it will not run succesfully need to further consider this method - not currently usable with this new method, will work with original function<br>
### April 1st 2020
Updated squareroot.py to try to include the Newton Method but as I am not familiar with this I also held onto the original method so I could check the result<br>
Updated week8plots.py to change view and to add titles and legends<br>
Completed second update on squareroot.py to embed the while loop successfully within it, this was challenging!<br>