Here's a straightforward guide on how to use the **NetwatchDog** tool:

### How to Use NetwatchDog

1. **Install Python**:
   - Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**:
   - If you have Git installed, you can clone the repository using:
     ```bash
     git clone https://github.com/yourusername/NetwatchDog.git
     ```
   - Alternatively, you can download the ZIP file of the repository from GitHub and extract it.

3. **Navigate to the Directory**:
   - Open your Command Prompt (Windows) or Terminal (macOS/Linux).
   - Use the `cd` command to navigate to the directory where you saved `NetwatchDog.py`:
     ```bash
     cd path/to/NetwatchDog
     ```

4. **Run the Script**:
   - Execute the script by typing:
     ```bash
     python NetwatchDog.py
     ```

5. **Input Hosts**:
   - When prompted, enter a comma-separated list of hosts you want to ping. For example:
     ```
     Enter a comma-separated list of hosts to ping: 8.8.8.8, google.com
     ```

6. **Specify Ping Count**:
   - Next, input the number of pings you wish to send to each host. For instance:
     ```
     Enter the number of pings to send per host: 4
     ```

7. **Monitor the Output**:
   - The script will begin pinging the specified hosts and will display the results in the console. You’ll see output like:
     ```
     Pinging 8.8.8.8...
     8.8.8.8: Successful
     Pinging google.com...
     google.com: Successful
     Ping results logged.
     ```

8. **Check the Log**:
   - The results of your ping attempts will be saved in a CSV file named `ping_results.csv` in the same directory. You can open this file with any spreadsheet application (like Excel) to view the logged results.

9. **Stopping the Tool**:
   - To stop the monitoring, simply press `Ctrl + C` in the command line. You will see a message indicating that the monitoring has stopped:
     ```
     Ping monitoring stopped.
     ```

### Tips for Effective Use

- **Multiple Hosts**: You can ping multiple hosts simultaneously to monitor various network resources.
- **Frequent Monitoring**: The tool is set to log results every 60 seconds. You can modify this delay in the code if needed.
- **Troubleshooting**: If you encounter any issues, ensure your firewall or antivirus software is not blocking the ping command.

This should help you get started with using **NetwatchDog** effectively! If you have any further questions or need assistance, feel free to ask!
