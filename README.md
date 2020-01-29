<h1 align="center">
Scandi Kitchen
</h1>

<div align="center">
	<!--add my own images-->
    <img src="https://scandi-food-milestone3.herokuapp.com/static/img/logo.jpg" border="0">
</div>
<br>

[Skandi Kitchen](#) is a recipe sharing website, created in order to educate people about Nordic/Scandinavian cooking tradition and inspire to try this unique cuisine. It is also designed for Scandinavian people who have recipes to share with the audience or would like to learn something new. The website's functionality allows users to register and create their own account which would allow them to create, update and remove recipes as they wish. All the users are allowed to view recipes, however, only registered ones are allowed to modify content. The website's design and logo are also inspired by Scandinavian tradition or neutral colors and minimal approach, giving a sense of lightness and allowing the user to navigate and find things effortlessly.

<br><br>
[**Check out Scani Kitchen here**](https://scandi-food-milestone3.herokuapp.com/)

</div>

## UX

### Project Purpose

This website was designed and created in order to give user a niche to be exposed to traditional food of northern Europe, where they can easily navigate in order to view all the available recipes, search if they are looking for something in particular and finally if they would want to share their own recipes they are able to register, and have full (create, update, delete) control of the recipes they want to share. Upon registration, every user is also provided with a profile page where they can upload their picture and see all the recipes they have created. Users are also allowed to visit each other's profiles in order to see recipes posted by a particular person.



### User Experience

- On page entry the user is first exposed to an overall feel of the brand, cool minty blue and white are dominating colors through the page giving the site a sense of modernity and minimalistic approach which is common in nordic design. At the top left of the page is the brand logo, which conveniently directs the user back to the home page on click, on the right user is provided with navigation encouraging to register, login or go to about page where they can read more about the Scandi Kitchen's manifesto and familiarise with the site's purpose.
Navigation bar shrinks into a hamburger icon providing the user a drop-down menu for their convenience to search on mobile devices. 

- The search bar is included in navigation for users who know exactly what they are looking for, upon entering a word search will automatically take the user to the most suitable recipe. Search is accessible to both registered and guest users.

- Right under navigation, there is a slider-banner for a visual appeal that display's the name of the page and carousel of Scandinavian food pictures. Right under the banner user is provided with recipe cards in order to be able to discover a new recipe with minimal search effort or navigation. 15 recipes are displayed per page in order to save scrolling space, the website is paginated to provide the user a convenient way to go through pages rather than scroll to infinity.

- All recipes are displayed using bootstrap cards for visual appeal, user is taken to a particular recipe page upon a click on the image or a link indicating "read more", user is also allowed to go on post author's profile page and discover all the recipes posted by them, upon clicking the name of the author on the card. Each recipe card includes recipe image, a short description of the dish, publishing date, and post author. Each recipe is them sorted by date, displaying newer posts first.

- User doesn't need to be registered to view recipes, however, they are only given the option to create a recipe upon registration. If decided to join user is exposed to registration form upon clicking the "register" button which is clearly displayed in a navigation bar and can't be missed. The registration form consists of email, username, password and confirm password fields, which are all compulsory data. If missed a field user is prompted to fill in an empty field. Upon entering email and username these are checked for a match in order to prevent clashing emails and user manes. Each registered user is assigned a unique ID which is later matched with their inputted profile picture and their posts. If a user's entered password and confirm password fields don't match they are prompted to enter a matching password. If registration goes successfully user is then directed to login form where they are asked to enter their username(email?) and password if either one doesn't match what was submitted on registration user, will be asked to enter information again if both fields are answered correctly user is then automatically taken to their account page.

- In the account page, the user can see a picture field which is by default a placeholder image that appears the same for all registered users. Under the image, user can see their username, a form to update their profile information and all the recipes they have created. 

-If the user wants to change any of their details such as email, username or profile image they can do it using an update form which is displayed in their profile page, updated information will be matched with their id and overwritten.

- Once registered and logged in user is given a "create recipe" option, which appears in navigation only once logged-in. Upon clicking the link user is then redirected to the recipe creation page, which consists of a form where information such as 'recipe description', 'image URL', 'ingredients' and 'cooking method' is required. Each field also has a little explanation sentence of how information should be entered for the best presentation.

- Once all information on a new recipe is entered and submitted, the recipe automatically appears in users' profiles as well as on the home page. Users can only edit recipes when logged in and only their own posts. Once users decided to edit their post they simply need to click on the recipe either on their own profile or from the home page and as the recipe is linked to their unique user ID they will be given options to delete or edit the recipe. If the user clicks the delete button a pop up will appear enquiring if the user really wants to delete the recipe, once OK is clicked recipe will be removed from the website and database. If clicked cancel pop up will disappear and nothing will change.



### User Stories

- #### 
    - A user who is looking into a website that has to do with a particular cuisine wants to get a full sense of the culture and sense of aesthetics common to the area, therefore it's important that the website is following Scandinavian/Nordic design aesthetic.
    - A user visiting recipe website has the intention of finding their next meal, therefore it's important that the site is easy to navigate and recipes are easy to find, whether the user chooses to browse or search by word.
    - For a user that wants to make their meal following instructions directly from the website, it is important that ingredient, cooking instruction and irrelevant info about the meal are presented separately in a manner that is easy to follow.
    - For somebody who is interested in Scandi/Nordic food and willing to make a contribution it is important to be able to upload and amend new recipes easily, as well as to have a record of all the recipes that they have already uploaded.

## Features

### Existing Features

1. #### Home Page for all users:
    
    -  The navigation bar consists of a logo that operates as a link directing user back to an index page from wherever they are, links to register or login, link to about page and a search field. Navigation is responsive and transforms into a hamburger menu for the best mobile experience. Navigation functionality was executed using bootstrap4 classes.
    
    - A carousel slider banner with a page name is used for decorative purposes, powered with JS images are changing by themselves, however, arrows are added to a slider for users that don't want to wait but would like to see all images. Dots at the bottom of the slider indicate the number of pictures and which image is currently showing.

    - Right under the slider recipes are displayed in neat bootstrap4 cards, 15 images per page. Overload is paginated and little numbers bar appear at the bottom of the page once the recipe amount exceeds its limit.
    
    - Footer is located at the bottom of the page providing links to social media, the option to email and an icon-link to a GitHub repository of the page.


2. #### Home Page for logged-in users:
    
    -  The home page consists of all same features for both guests and logged-in users, the only difference being a 'create recipe' link that appears on a navigation menu only once register has logged in as well as log-out option.
    
    
3. #### Recipe Listing
    
    - Recipe listing is displayed directly on the home page, in order to provide the user with the most important content with minimal navigation and clicks. A maximum number of recipe cards to be displayed on the page is 15, once the number of recipes uploaded exceeds this number, pagination appears at the bottom of the page allowing the user to go to the second page and load more recipes.

    
4. #### Recipe Page 
  
    - The user is directed to the recipe page by clicking recipe name or a button read the recipe on the recipe card at the home page.

    - Once on the recipe page, the user is exposed to the Recipe name followed by the user-name of the user who has posted the recipe and the date when it has been posted. Following is an image of the dish and a short description of this particular meal. Under this, there are two lists with recipe ingredients and cooking methods.

    - If the user viewing the recipe is a creator of it, they will also see two buttons allowing them to update and delete the recipe. If the user isn't the creator these buttons will not appear. The user who has created the recipe and the recipe itself is linked by a unique user id.
    
5. #### Upload Recipe

	- Once on the create recipe page user is exposed to a form with 5 inpot fields:
		- Title
		- About Recipe
		- Cooking Method
		- Ingrediants
		- Image URL
	under these input titles, there are small descriptions of how the user should input information and what kind of input is expected. For example cooking methods and ingredients are required to be separated by a comma after each method or ingredient in order for it to be displayed as a list as a result.

	-At the bottom of the list, there is a 'POST' button which will create a recipe on submission and redirect the user to that recipe page.
    
    
6. #### Edit/Delete Recipe
    
    - Once the user (creator of recipe) clicks Update button they are redirected to create recipe page with information already prefilled from the previous recipe, here they can change what they want and click post, which will redirect them back to the recipe page.

    - Once the user (creator of recipe) clicks Delete button a pop up appears asking if a user is sure they want to delete the post (this was implemented in order to prevent accidental post removals).

6. #### Search Recipe
    
    - The search field is provided in the navigation bar for all users to search for recipes by entering a word. The search engine looks for word matches in the existing recipes and redirects user to search page that displais all filtered recipes.
### Features Left to Implement

1. #### User profile recipe view

    - Once in their own profile page users should see not only their details but also all the recipes they have uploaded, that way it would be easier to edit and delete posts accordingly without having to search. At the moment the user can see all their recipes if they click on their name in the recipe card, however, it is not visible when they are in their profile page.

2. #### Liked page

	- In the future, I want to implement an additional view of liked recipes. Each recipe would have a little outline of the heart, which logged in users can click and the recipe will be added to their ' favorites page' if the heart is clicked again the recipe is removed. This way it would be easier for users to save recipes they like rather than searching them every time they want to cook it again. This feature is presented in my original wireframes and has not been implemented due to the lack of time.

2. #### Comment area

	- The feature allowing to leave recipe reviews and comments would help users share their experiences, tips, etc, would make the page much more personal and interactive, forming cooking community rather than just being a recipe sharing page. 

2. #### Overall design amends

    - Due to the complexity of the page, design choices were not the primary focus, therefore I intend on amending the overall design of the application adding more custom CSS and making it look more modern and interesting.
    
## Database

### SQLite

- The database used for this project was SQLite, I chose to use this database due to the fact that I was already familiar with it and using it at work, I have informed student care as well as my mentor about this decision.

## Technologies Used

- #### Python
- #### HTML5
- #### CSS/Bootstrap4
- #### JS/JQuery
- #### SQLite
- #### Flask

## Testing

- #### Manual testing

- Entered different words in search field and checked that page was redirecting every time and displaying all suitable recipes.
- Clicked on all navigation links while not legged in and checked that all pages redirect correctly.
- Clicked on recipe name to check that it leads me to recipe page.
- Clicked on read recipe button to check that it also redirects to recipe page.
- Clicked on user name displayed on recipe card to check that it leads to a user page displaying all the recipes posted by that user.

- Tried to register a new user entering an email that I have already used to make sure user wouldn't be created, then repeated same procss for username.
- Tried to register a new user enterning non matching password makimg sure this wouldn't work.
- Created a new user fulfilling all requirements and clicked on account button in navigation to make sure user account was really created.
- Inside user account uploaded picture and tried to update information, then checked that user information was indeed changed.

- Tried to log in existing user using incorrect password to make sure user wouldn't be recognised.
- Logged in existing user.
- Uploaded recipe and checked that it appeared in the home page.
- Selected a recipe created by this user and tried to update information saved and checked that info was updated.
- Selected a recipe created by this user deleted it.
- Logged user out.

- Ran manual testing above on different operating systems, scalled screen size and checked on different devices.

## Deployment

-Website was built in Visual Studio Code, a local GIT directory was used for version control and then pushed to Github.

-Heroku app use the DATABASE_URL config var to designate the URL of an app’s primary database.

-A Procfile is used so that Heroku know what commands are run by the application and how to run the app.

-Heroku's deployment from Github repository function was used to deploy.

## Credits

### Media

- #### Images and Recipes were taken from following pages:
    - https://littlesunnykitchen.com/swedish-smorgastarta-sandwich-cake/
    - https://foodandjourneys.net/finnish-salmon-soup-lohikeitto/
    - http://www.cookr.com/recipes/karjalanpiirakka-karelian-pies
    - https://www.food.com/recipe/karjalan-piirakka-karelian-pie-with-egg-butter-137150
    - https://sweden.se/culture-traditions/classic-swedish-food-meatballs/
    - http://vagabondbaker.com/2015/01/08/korvapuusti/
    - https://www.meillakotona.fi/reseptit/sienisalaatti-suolasienista

### Help with code

- Info about indexing (https://docs.sqlalchemy.org/en/13/core/constraints.html?highlight=indexes).
- Tried to better understand WTF forms in order to be able to use them through the app (https://wtforms.readthedocs.io/en/stable/crash_course.html).
- Info on data classes (https://realpython.com/python-data-classes/).
- Info on validators and how to use them (https://www.youtube.com/watch?v=jR2aFKuaOBs).
- Info of how to create pagination (https://www.youtube.com/watch?v=PSWf2TjTGNY),(https://pypi.org/project/paginate/).
- How to implement strf time (https://www.programiz.com/python-programming/datetime/strftime).
- Overall information on different aspect of python, used this page a lot (https://realpython.com/).
- Flask and database setup tutrials + lots of useful info (https://www.youtube.com/playlist?list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM)

### Acknowledgements

Thanks to my mentor Spencer Barriball for advice and support.

## Disclaimer

All content on the website, including images, is used for educational purposes only and I do not own copyrights. Please find links above that lead to original sources.