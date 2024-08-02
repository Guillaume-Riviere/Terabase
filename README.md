# TeraBase - Database for Tera

TeraBase is a web application that allows users to search for and display various data from the game Tera using JSON files. The application includes search, filtering, and pagination features, as well as a modal to display item details.

## Features

- Search for items by name or description.
- Filter items by ID.
- Display item details in a modal.
- Paginate search results.
- Show a loading indicator during the search.

## Prerequisites

- A web server to serve HTML, CSS, and JavaScript files.
- JSON files containing game data must be available in the Data/ directory.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Guillaume-Riviere/Terabase
    ```

2. Place the JSON files in the Data/ directory.

3. Open the index.html file in a web browser using LiveServer.

## Project Structure


- `index.html`: The main HTML file containing the structure of the application.
- `style.css`: The main CSS file for the application's styling.
- `item.css`: The CSS file for styles specific to the items.
- `Data/`: The directory containing the JSON files with the game data.

## Use

1. Open index.html in a web browser.
2. Use the search bar to search for items by name or description.
3. Check the "Search by ID" checkbox to search for items by ID.
4. Click on an item in the search results to display its details in a modal.
5. Use the "Load More" button to display more results.

## Code JavaScript

The JavaScript code is included in the index.html file and handles the following functionalities:

- Loading item data from JSON files.
- Searching and filtering items.
- Displaying search results.
- Managing the modal to display item details.
- Showing a loading indicator during the search.

## Contribute

Contributions are welcome! Please follow these steps to contribute:

- Fork the repository.
- Create a branch for your feature (git checkout -b feature/my-feature).
- Commit your changes (git commit -am 'Add a new feature').
- Push your branch (git push origin feature/my-feature).
- Open a Pull Request.

## Licence

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
