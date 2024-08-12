# learning-python
Shopping List
By Michele Selivon, URI   Brazil
Timelimit: 1
Valentina is a very dedicated woman, and she works late every day. To save her time, she writes down the items at the same time she remembers. She uses a mobile app for this task.
The problem is that the application does not delete duplicate items and as Valentina is distracted, she frequently notes the same item more than once and the list gets too long. You should improve the app used by Valentina. Make a code that excludes duplicate items from the shopping list and sorts them in alphabetical order.
Input
The first input line contains an integer N (N < 100) that indicates the number of test cases that follows. Each shopping list consists of a single line that contains from 1 to 1000 items or words composed only of lowercase letters (from one up to 20 chars), without accents and separated by a space.
Output
The output consist of N lines, each representing one of Valentina's shopping lists, with no items repeated and sorted in alphabetical order.

Training List
By Vinicius Coelho   Brazil
Timelimit: 1
SAP is promoting in its headquarters an event to train candidates for interviews, being presented by the illustrious boss Pietro and hosted in partnership with some universities from Brazil. A form for the interested candidates was created, with fields for basic data such as:
•	Complete name;
•	University; and
•	E-mail for contact.
The amount of interested candidates was much larger than the expected by the organizers, making necessary the confection of lanyards for access into the event. Many booths for distributing the lanyards were created along the entrance of the building, each with a list of registered attendees. However, many of the registered candidates did not show up, leaving a surplus of lanyards. The organizer team wants to know how many people did show up, but, since they are too tired, they asked you to help.
Input
The first line of each test is a single integer C (1 <= C <= 1000), representing the amount of registered candidates. The next line is composed of C integers separated by a space, each being 1 if the corresponding candidate joined the event, and 0 if he didn't.
Output
The output should be a single integer, representing the amount of candidates that joined the event.

Name Lists
By Sergio Costa, UFMA   Brazil
Timelimit: 1
Marta wants to choose some names for her future son or daughter. She found a list of names, but she didn't like its presentation. She wanted to have a list of names, where each line was ordered according to the length of the name, from smallest to largest. On each line, only one name of a given size will appear. For example, consider a list with the names Eva and Ana. In the proposed presentation, Eva will appear on the first line while Ana on the second.
How about we make an algorithm that produces this list of names?
Input
The input consists of a first line containing an integer N, which can vary from 2 to 1000. The integer N represents the number of names in your collection. After that, there are N lines containing, each one, a name, which can be between 2 and 19 characters long.
Output
The output consists of one or more lines. Each line has a list of names ordered by size, starting with the smallest size. On each line, you will only have one name of a given size, and the next names of the same size will appear on the next lines, in the order they came in the input.

Encryption
By Neilor Tonin, URI   Brazil
Timelimit: 1
You have been asked to build a simple encryption program. This program should be able to send coded messages without someone been able to read them. The process is very simple. It is divided into two parts.

First, each uppercase or lowercase letter must be shifted three positions to the right, according to the ASCII table: letter 'a' should become letter 'd', letter 'y' must become the character '|' and so on. Second, each line must be reversed. After being reversed, all characters from the half on (truncated) must be moved one position to the left in ASCII. In this case, 'b' becomes 'a' and 'a' becomes '`'.

For example, if the resulting word of the first part is "tesla", the letters "sla" should be moved one position to the left. However, if the resulting word of the first part is "t#$A", the letters "$A" are to be displaced.
Input
The input contains a number of cases of test. The first line of each case of test contains an integer N (1 ≤ N ≤ 1 * 10⁴), indicating the number of lines the problem should encrypt. The following N lines contain M characters each M (1 ≤ M ≤ 1 * 10³).
Output
For each input, you must present the encrypted message.

DDD
Adapted by Neilor Tonin, URI   Brazil
Timelimit: 1
Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:

 
If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.
Input
The input consists in a unique integer number.
Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.

LED
Unknown Author
Timelimit: 1
John wants to set up a panel containing different numbers of LEDs. He does not have many leds, he is not sure if he will be able to mount the desired number. Considering the configuration of the LEDs of the numbers below, make an algorithm that helps John to discover the number of LEDs needed to set the value.
Note: For Javascript programmers, it is recommended to use of "input.trim().split('\n')" to avoid some known problems.

 
Input
The input contains an integer N, (1 ≤ N ≤ 2000) corresponding to the number of test cases, followed by N lines, each line containing a number (1 ≤ V ≤ 10100) corresponding to the value that John wants to set with the leds.
Output
For each test case, print one line containing the number of LEDs that John needs to set the desired value, followed by the word "leds".

Mjölnir
By Ricardo Martins, IFSULDEMINAS   Brazil
Timelimit: 1
Odin created to Thor the most faithful and powerful possible weapon, Mjolnir hammer. Made of a special mystical ore called Uru and forged in the heart of a star by blacksmiths Gods of Asgard , Brokk and Eitri , blacksmiths legendary.
One day , Thor challenged his friends to see who could raise the Mjölnir .
Write a program that , given a name , and the force in Newtons applied to try to lift the Thunder Hammer , inform the person succeeded in lifting it .
Input
An integer C shall be informed , which is the amount of test cases. Each test case begins with one word , which is the first name of who is trying to raise Mjölnir , and an integer N ( 1 ≤ N ≤ 25000 ), indicating the force applied upward in Newtons to pull the hammer of so try to lift it.
Output
For each test case print a 'Y' character , if the person has managed to raise or 'N' if you have not achieved .

Diving
By Leonardo Fernandes, IFSC   Brazil
Timelimit: 1
In a given diving competition, each dive has a degree of difficulty and is evaluated by seven judges. After each jump, the judges, who don't communicate with each other, show their scores. A dive is evaluated between zero and ten by each judge. After the scores are presented, the highest and the lowest scores are discarded. The remaining scores are added and the sum is multiplied by the degree of difficulty of the dive, which is a number between 1.2 and 3.8 defined before the dive. So, for example, assuming a diver's jump has difficulty 2.0 and his scores are 6,0, 5,0, 5,0, 5,0, 5,0, 5,0 and 4,0. Discarding the highest and lowest scores, we get to a result of 25.0. This result is then multiplied by the degree of difficulty 2.0 for a final score of 50.0. You program must display the results of a competition following these rules.
Input
The first row of input has the number of diversN (0 ≤ N ≤ 100). Next, the name of each competitor is followed by the degree of difficulty D (1.2 ≤ D ≤ 3.8) of the dive and, in the next line, the seven scores S1 to S7 (0 ≤ S1 to S7 ≤ 10)given by the judges.
Output
The output must show the results of the competition, with the name of each diver followed by the final score, in the order in which the data was input.

Dijkstra
By Abner Samuel P. Palmeira, IFSULDEMINAS   Brazil
Timelimit: 1
In the game The Witcher, Sigismund Dijkstra is the leader of the Redanian Secret Service, because of this he is one of the most important people in the world.
In addition Dijkstra has a large treasure, which has several types of jewelry.
Dijkstra is very curious to know how many different types of jewelry his treasure has.
Knowing that you are the best programmer on the continent Dijkstra hired you to check how many different types of jewelry he has in his treasure.
Input
The entry consists of several lines and each contains a string describing one of Dijkstra's jewels. This string is composed only of the characters '(' and ')', the sum of the length of all the string does not exceed 106.
Output
Print how many different kinds of jewelry Dijkstra has.

Bean
By André da Cruz   Brazil
Timelimit: 1
It is said in the surroundings of Montes Claros that, long ago in the municipal market, Sebastião and his companions of work always play a game of divination after the delivery of agricultural products harvested in the week that happened. The game, "Guess Where the Bean is", consists in hiding a grain of beans in one of four opaque glasses, and after shuffling them, the bettor must guess in which glass the vegetable is.
 
This year, due to the great cultural and historical success and the enormous amount of people who practice this game in the municipal market, the city council decided to hold a "Guess Where the Bean is '' championship. However, she needs a program to show viewers where the beans were after the end of a game. Knowing that the next Programming Marathon will take place in the city, she soon commissioned a solution from the excellent programmers. In this way, you should assist the organization in this mission with a program that will inform, at the end of a match, where the beans were.
Input
The entry will contain only one line with four integers, C1, C2, C3 and C4 separated by a space. The value Ci = 1 indicates that the beans were in cup number i, and Ci = 0 indicates that the ith cup was empty at the end of the game. There will always be exactly one glass with the beans.
Output
Write in the output a line containing an integer between 1 and 4, corresponding to the position where the beans were.

WERTYU
By Gordon V. Cormack   Canada
Timelimit: 1
 

A common typing error is to place the hands on the keyboard one row to the right of the correct position. So "Q" is typed as "W" and "J" is typed as "K" and so on. You must decode a message typed in this manner.
Input
Input consists of several lines of text. Each line may contain digits, spaces, upper case letters (except Q, A, Z), or punctuation shown above [except back-quote (`)]. Keys labelled with words [Tab, BackSp, Control, etc.] are not represented in the input. You are to replace each letter or punction symbol by the one immediately to its left on the QWERTY keyboard shown above. Spaces in the input should be echoed in the output.
Output
For each input line, print a corresponding output line with the decoded message.

Deciphering the Encrypted Card
By Hamilton José Brumatto   Brazil
Timelimit: 1
The oldest known cipher is the Cipher of Caesar. Caesar wrote his letters by exchanging each letter for the next in the alphabet, to avoid that, when the letter was intercepted, enemy could read it. Over time, encryption has acquired better quality, but encryption based on substitution is still an interesting child's play, for example:
ZEN I T

POLAR
In this child's play, when writing a letter, the letter Z is replaced by the letter P and vice versa, as well as: E by O and so on. The phrase coded as follows: "Osro roxre osri caftide" can be deciphered as: "Este texto esta cifrado". As the game got serious, you were prompted for a program that decrypts encrypted messages from a supplied key.
Input
The input contains several test cases. Each test case begins with a line indicating two integers C and N, 0 < C < 21 and 0 < N < 100. C is the size of the cipher. On the next two lines is the C-sized cipher indicating which characters from the first line will be replaced by characters from the second line, a character appears only once, on the first or second line.
The cipher can contain letters from 'A' to 'Z', numbers from '0' to '9' plus white space and some punctuation symbols: '.' ',' ';' ':' '(' ')' '!' and '?'. In the next N lines are sentences and sentences encrypted by the cipher provided, which you must decipher. Each line contains a minimum of 1 and a maximum of 1000 characters. Any printable ASCII (non-extended) characters are allowed, in this case no accented characters are present, not even 'ç'.
Output
For each input test case your program must generate for each sentence line at the input a sentence line with the deciphered output, respecting the capitalization of the letter (capital letters are deciphered as case-sensitive when it is possible to apply, If it is not possible then it will be deciphered as lowercase letters). After each test case, a blank line should be printed, including after the last one.
VaiNaSort
By Ricardo Martins, IFSULDEMINAS   Brazil
Timelimit: 1
Professor Odracir Snitram studied various methods of ordering, as well as their respective complexities. One day, he decides to make a test, creating a method, with a box and N stones, numbered from 1 to N. The idea was to draw all the stones, one at a time, so that the sequence of numbers drawn was exactly 1 to N, that is, by drawing the number 1 first, then the number 2, then the 3, and so on, until the last one, which would be N. After drawing everything, if the attempt did not work, all the stones were Returned in the box, and the draw began again until it worked out. This method was named VaiNaSort!
Write a program that, given the amount of stones, and all attempts until you draw correctly, count the attempts.
Input
The input has several test cases. Each one starts with an integer N (2 ≤ N ≤ 10000), representing the amount of stones in the box. Next, there will be a few draw attempts, each formed with the numbers from 1 to N, in any order, until the expected order is achieved. The entry ends with N = 0.
Output
For each test case, print the total number of attempts.

Encrypted Christmas Letter
By Jessica Dagostini, beecrowd   Brazil
Timelimit: 1
Mister Klaus receives the most diverse letters from children all over the world. Every year, with no exceptions, he selects some of the cooler Christmas letters to give them more attention. This year, one of these letters caught the eye of Klaus for a particular reason the letter was encrypted! Inside the envelope, there was the letter with the Christmas request and an attached note that said:
"Mister Santa Klaus: I imagine that you must receive thousands of Christmas letters every year, and maybe it must be annoying to read all of them without a challenge. I hope that my letter brings you a bit of fun! I changed all word vowels by symbols. Use this table to correctly read my request!"
 
Let's help Santa to translate this letter?
Input
The input consists of several test cases and ends with EOF. Each test case corresponds to a phrase F (5 < F < 256), composed by lower letters, the symbols from the decryption table and white spaces. Each test case is ended by a line break.
Output
Prints the decrypted phrase, with the help of the table given by the author of the letter.


