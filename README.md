# Coder Buddy

Coder Buddy is an AI-powered project generator and coding assistant. It helps you plan, architect, and generate code for web projects using modern tech stacks, and saves project metadata and implementation details to a PostgreSQL database.

## Features

- **AI Project Planning:** Converts user prompts into structured project plans.
- **Task Architecture:** Breaks down plans into actionable coding tasks.
- **Automated Coding:** Generates code for each task and writes files to a `generated_project` directory.
- **Web Search Integration:** Uses DuckDuckGo to search for tech stack versions and project references.
- **Database Storage:** Saves project and task details to PostgreSQL for tracking and analytics.
- **Streamlit UI:** Interactive interface for project generation and management.

## Tech Stack

- Python
- LangChain & LangGraph
- Streamlit
- SQLAlchemy
- PostgreSQL

## Setup

1. **Clone the repository:**

   ```
   git clone https://github.com/anshraz27/ai-code-buddy.git
   cd ai-code-buddy
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   - Create a `.env` file with your PostgreSQL connection string:
     ```
     DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/dbname
     ```

4. **Run the Streamlit app:**
   ```
   streamlit run streamlit_app.py
   ```

## Usage

- Enter a project prompt in the Streamlit UI (e.g., "Build a colourful modern todo app in html css and js").
- Coder Buddy will generate a plan, break it into tasks, and create code files.
- Project and task details are saved to the database for future reference.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
