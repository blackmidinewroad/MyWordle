# MyWordle
A clone of the popular Wordle game, built with Django for the backend and HTMX for dynamic frontend interactions. In the game, players have six attempts to guess a five-letter word, receiving feedback through colored tiles that indicate correct letters and their placement.

## Technologies Used
- **Backend**: Django for handling game logic.
- **Frontend**: HTMX (and a little JavaScript) for dynamic HTML updates.
- **Database**: SQLite for storing word lists.

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/blackmidinewroad/MyWordle.git
   cd MyWordle
   ```

2. **Install Pipenv** (if not already installed):
   ```
   pip install pipenv
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root with the following:
   ```
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```
   Generate a secure `SECRET_KEY` using:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Set Up Virtual Environment and Install Dependencies**:
   Use the `Pipfile` to install dependencies in a virtual environment.
   ```
   pipenv install
   ```

5. **Activate the Virtual Environment**:
   ```
   pipenv shell
   ```

6. **Database Setup**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Update database with words**:
   Run these management commands.
   ```
   python manage.py load_words game/static/text/dictionary.txt
   python manage.py load_words game/static/text/answer_words.txt --answer-words
   ```

8. **Run the Server**:
   ```
   python manage.py runserver
   ```
   Open http://localhost:8000 in your browser to play.
