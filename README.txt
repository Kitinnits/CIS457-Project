To run the project, fork it, and install it to your preferred computer. 
Use VS Code, a command window, or any other coding platform to open it.

On Windows: 
Open two Command Prompt windows, running part2-server.py first on one and part2-client.py on the other. (It is important that server file is ran before the client).
Once the two programs are connected, the client will prompt the user to send a message to the server.
When the server receives the message, the client can continue to send messages or the server can choose to respond.
The server and client can send as many messages to each other as they want. The side that sends the message will see their messages sent one after the other.
The one receiving the message will see a line of empty text thats credited to them, this is a bug we are looking to fix to make the end product cleaner.
When you are ready to stop the converstaion and close the program, send the message 'quit' and the other side will receive a message that the connection is terminated and the programs can be closed.

On MacOS:
Open two terminals and navigate to where the project is installed on the computer. 
If you don't know where the files were downloaded to, drag the file itself from the finder application and it the terminal will show you its path.
Run part2-server.py first with the command 'python3 part2-server.py' in one window and part2-client.py on the other with a similar command.
A connection will be initated when the client is opened and you are free to type as many messages to each side as you would like.
Empty lines show up with the message being sent on the receiving side but doesn't mess with functionality so it will be fixed to look cleaner soon.
To stop the program, one side sends the message 'quit' to close the connection and safely close the program.

