## Flask Application Design for Social Media Post Generation

### HTML Files
- **index.html**: Main page of the application where users can interact to generate social media posts.
- **posts.html**: Page displaying the generated social media posts.

### Routes
- **`/`**: Home route, should display the `index.html` file.
- **`/generate_post`**: Route to handle the post generation process. This route should:
  - Accept a POST request with parameters containing the brand characteristics.
  - Utilize a Flask template to render the `posts.html` file with the generated post.
- **`/posts`**: Route to retrieve and display the generated social media posts in the `posts.html` file.