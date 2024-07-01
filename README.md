# Cinematic Vault: A Treasure Trove of Global Cinema

Welcome to Cinematic Vault, an interactive Streamlit application designed to catalog and explore the gems of global cinema. With this app, you can add, update, delete, and analyze cinematic treasures from around the world.

## Features

### Home
- **View All Cinematic Treasures**: Browse through the entire collection of cinematic gems stored in the vault.
- **Cinematic Diversity**: Visualize the diversity of films by language.
- **Cream of the Crop**: Discover the top-rated movies in the vault.

### Add Cinematic Gem
- Add new movies to the vault with details like title, director, release year, language, rating, genre, runtime, box office, awards, cinematographer, soundtrack composer, critical reception, user reviews, cultural impact, and trivia.

### Discover Treasures
- **Filter Cinematic Treasures**: Filter movies based on various criteria such as title, director, release year, language, rating, genre, awards, cinematographer, and soundtrack composer.
- **Find Cinematic Soulmates**: Find the most similar movie in the vault based on a unique 'DNA' similarity algorithm.

### Update Cinematic Gem
- Update the details of existing movies in the vault.

### Remove from Vault
- Remove movies from the vault.

### Cinematic Analysis
- **Cinematic Timeline**: Visualize the distribution of movies over time based on their release year, rating, box office, and language.
- **Language Diversity Over Time**: Track the diversity of languages in cinema over different years.
- **Cinematic Quotient Analysis**: Calculate and analyze a unique 'Cinematic Quotient' for each movie.
- **Sentiment Analysis of User Reviews**: Perform sentiment analysis on user reviews to visualize the relationship between IMDb ratings and user review sentiments.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/cinematic-vault.git
   cd cinematic-vault
   ```

2. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

## Database

The app uses SQLite to store the cinematic treasures. The database is automatically created and managed by the app.

## Usage

1. **Home**: Browse the collection, visualize diversity, and discover top-rated movies.
2. **Add Cinematic Gem**: Fill in the form to add a new movie to the vault.
3. **Discover Treasures**: Use filters to find specific movies or discover movies similar to your favorites.
4. **Update Cinematic Gem**: Select a movie to update its details.
5. **Remove from Vault**: Select a movie to remove it from the vault.
6. **Cinematic Analysis**: Explore various analyses and visualizations to gain insights into the collection.

## Helper Functions

The app includes several helper functions for database operations and unique functionalities like generating movie DNA, finding cinematic soulmates, and calculating cinematic quotients.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## Acknowledgments

Thanks to the open-source community for providing the tools and libraries that made this project possible.

---

Enjoy exploring the world of cinema with Cinematic Vault!
