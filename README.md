# MyWordle
A clone of the popular Wordle game, built with Django for the backend and HTMX for dynamic frontend interactions. In the game, players have six attempts to guess a five-letter word, receiving feedback through colored tiles that indicate correct letters and their placement.

## Technologies Used
- **Backend**: Django for handling game logic.
- **Frontend**: HTMX (and a little JavaScript) for dynamic HTML updates.
- **Database**: SQLite for storing words.

## Installation
1. **Clone the Repository**:
   ```shell
   git clone https://github.com/blackmidinewroad/MyWordle.git
   cd MyWordle
   ```

2. **Install Dependencies**:
   ```shell
   pipenv install
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the project root with the following:
   ```
   SECRET_KEY='your-secret-key-here'
   ALLOWED_HOSTS='localhost,127.0.0.1'
   ```
   Generate a secure `SECRET_KEY` using:
   ```shell
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Database Setup**:
   ```shell
   python manage.py migrate
   ```

5. **Load Words Into Database**

   Run these management commands:
   ```shell
   python manage.py load_words game/static/text/dictionary.txt
   python manage.py load_words game/static/text/answer_words.txt --answer-words
   ```

## Usage
1. **Run the Server**:
   ```shell
   python manage.py runserver
   ```

2. **Open http://localhost:8000 in your browser to play**
