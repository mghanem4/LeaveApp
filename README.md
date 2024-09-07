
# Leave Application System

## Overview

This project is a **Leave Management System** built using **Python** and **SQL operations**. The system allows employees to request leaves and stores their information in a database. Managers will eventually be able to log in, view leave requests, and approve or decline them. 

### Features

- **User Authentication**: A login page for users with credential validation.
- **Leave Request Form**: A form that validates user inputs before submitting leave requests.
- **Database Integration**: A SQLite database to store user credentials and leave information.

### Pending Features

- [ ] **Manager Login**: To allow managers to access the system.
- [ ] **Manager View**: A page where managers can view submitted leave requests.
- [ ] **Approve/Decline Requests**: Managers will be able to approve or reject leave requests.

## Installation and Setup

### Requirements

Ensure you have the following installed:

- Python 3.x
- SQLite (for database management)

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/leaveapp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LeaveApp
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### Database Setup

The application uses an **Access database** (`login_creds.accdb`) to store user credentials and leave details. Make sure the database is correctly placed in the project folder.

- **login_creds.accdb**: Stores login credentials and leave data.

## Project Structure

- `main.py`: The main file that starts the application.
- `msac.py`: Contains helper functions and database interactions.
- `assets/`: Folder containing static assets like images, CSS, and other media files.
- `login_creds.accdb`: The Access database storing user credentials and leave data.
- `README.md`: Project documentation (this file).

## Usage

1. **Login Page**: Users can log in using their credentials stored in the database.
2. **Leave Form**: After login, users can submit their leave requests through the form.
3. **Validation**: The form checks for valid inputs before submitting.
4. **Leave Submission**: Upon successful validation, the request is stored in the database.

## Future Development

- **Manager Access**: A separate page for managers to view, approve, or decline leave requests.
- **Enhanced Validation**: Add more robust validation for leave requests.
- **Email Notifications**: Automatic email notifications to managers for new leave requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
