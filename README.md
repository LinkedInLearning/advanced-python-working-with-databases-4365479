# Advanced Python: Working with Databases
This is the repository for the LinkedIn Learning course Advanced Python: Working with Databases. The full course is available from [LinkedIn Learning][lil-course-url].

![Advanced Python: Working with Databases][lil-thumbnail-url] 

To create functional and useful Python applications, you need a database. Databases allow you to store data from user sessions, track inventory, make recommendations, and more.  However, Python is compatible with many options: SQLite, MySQL, and PostgreSQL, among others. Selecting the right database is a skill that advanced developers are expected to master. This course provides an excellent primer, comparing the different types of databases that can be connected through the Python Database API. Instructor Kathryn Hodge teaches the differences between SQLite, MySQL, and PostgreSQL and shows how to use the ORM tool SQLAlchemy to query a database. The final chapters put your knowledge to practical use in two hands-on projects: developing a full-stack application with Python, PostgreSQL, and Flask and creating a data analysis app with pandas and Jupyter Notebook. By the end, you should feel comfortable creating and using databases and be able to decide which Python database is right for you.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

Kathryn Hodge 
                            
Software Engineer

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/kathryn-hodge).

[lil-course-url]: https://www.linkedin.com/learning/advanced-python-working-with-databases-22307421?dApp=59033956&leis=LAA
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQGxhz_OMvM_mQ/learning-public-crop_675_1200/0/1683668063867?e=2147483647&v=beta&t=frT7osblpohhLDjZqRYyklw6-Fay7Mgtr5hsv0QvLuc
