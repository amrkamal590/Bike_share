
Explore US Bikeshare Data Exploration project "1"

https://camo.githubusercontent.com/f98bd2ee3cf7c3f1300b751aee446f4adeca930d07122709b8db848d0cbf3ee9/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031382f4a616e756172792f35613732336165665f66643239786272727371316c3732686d2f66643239786272727371316c3732686d2e6a7067




Basic Data Exploration with pandas on Bikeshare Data
Basic Udacity project using pandas library in Python for their bikeshare data exploration.

Project Overview:
This project focuses on pandas library usage and simple statistics methods to perform a rudimentary analysis on the bikeshare data from three major U.S. cities - Chicago, Washington, and New York City - to display information such as most popular days or most common stations.

Running the program:
You can input 'python bikeshare.py' on your terminal to run this program. I use Anaconda's command prompt on a Windows 10 machine.

Program Details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

Most popular month
Most popular day
Most popular hour
Most popular start station
Most popular end station
Most popular combination of start and end stations
Total trip duration
Average trip duration
Types of users by number
Types of users by gender (if available)
The oldest user (if available)
The youngest user (if available)
The most common birth year amongst users (if available)
Finally, the user is prompted with the choice of restarting the program or not.
Project Data:
chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.

  
