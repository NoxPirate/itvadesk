# ITvaDesk

ITvaDesk is a web-based ticketing and helpdesk management application. It provides a platform for users to submit tickets and for administrators to manage and respond to these requests, facilitating structured IT support workflows.

## Features

* **Ticketing System**: Users can create support tickets (`ticket_form.html`), which can then be viewed and managed via a dashboard interface (`ticket_detail.html`).


* **User Management**: The application includes authentication modules (`auth.py`) allowing for separate user and admin access.


* **Dashboards**: Dedicated dashboards for users (`user_dashboard.html`) and administrators (`admin_dashboard.html`) to manage the ticketing lifecycle.


* **Database Integration**: Built-in support for SQLite for persistent data storage, with utility scripts for database initialization and inspection (`init_db.py`, `inspect_db.py`).


* **Communication Utilities**: Includes modules for email-related functionality to support notifications or ticket updates (`email_utils.py`).



## Technologies Used

* **Framework**: Python-based web framework (implied by the `app/` and `templates/` structure, commonly Flask).


* **Database**: SQLite (`db.sqlite3`).


* **Frontend**: HTML5, CSS3, and JavaScript.



## Project Structure

The project follows a standard Python web application directory structure:

* **`app/`**: Contains the core backend logic, including routes (`views.py`), data models (`models.py`), authentication (`auth.py`), and configuration (`config.py`).


* **`templates/`**: Contains the HTML templates for the UI, including dashboards, login pages, and ticket forms.


* **`static/`**: Holds static files such as CSS (`style.css`), JavaScript (`script.js`), and images (e.g., `logo.webp`).


* **Root Scripts**: Contains entry points and management utilities like `run.py`, `create_admin.py`, and `init_db.py`.



## Getting Started

1. **Environment Setup**: Ensure you have the required Python dependencies installed, as specified in `requirements.txt`.


2. **Initialize Database**: Run the initialization script to set up the SQLite database:


```bash
python init_db.py

```



```
3.  **Run the Application**: Launch the application using the `run.py` script[cite: 4]:
    ```bash
python run.py

```
