# wiki
This is a project that belongs to CS50's Web Programming course. 

### open the project
If you want to execute the project you need to:
  * Install django in your pc.
  * For this project I use a library called markdown so you have to install it as well.
  * Initialize the virtual enviroment (venv), to do this you have to type on the terminal **wiki\Scripts\activate.bat** (this works on VSCode).
  * Write **python manage.py runserver** .

## Structure
* **encyclopedia** is my app for the **wiki** project.
* I use a django form for the page, you can see the class newPage Form on **encyclopedia/forms.py**.
* Respect the **view.py** I wrote on this file the functions for the correct behavior of the page.
* **util.py** has the fuctions for listing, saving and getting the entry of the markdown files that are saved on the folder *entries*.
* **urls.py** saves the urls for the page.
* The html files are located on the folder *templates*.


