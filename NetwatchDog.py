import subprocess
import time
import csv
import os

# Configuration
output_file = 'ping_results.csv'  # Output file for results

def ping(host, ping_count):
    """Ping a host and return detailed results."""
    try:
        # Run the ping command
        result = subprocess.run(['ping', '-c', str(ping_count), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()

        # Check for success
        if result.returncode == 0:
            return f"{host}: Successful\n{output.strip()}"
        else:
            return f"{host}: Failed - {result.stderr.decode().strip()}"
    except Exception as e:
        return f"{host}: Error - {str(e)}"

def log_results(results):
    """Log the ping results to a CSV file."""
    file_exists = os.path.isfile(output_file)
    with open(output_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Host', 'Result'])  # Write header
        for host, result in results.items():
            writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), host, result])

def main():
    # Prompt user for hosts and ping count
    hosts_input = input("Enter a comma-separated list of hosts to ping: ")
    ping_count = int(input("Enter the number of pings to send per host: "))
    hosts = [host.strip() for host in hosts_input.split(',')]
    
    try:
        while True:
            results = {}
            for host in hosts:
                print(f"Pinging {host}...")
                results[host] = ping(host, ping_count)
                print(results[host])  # Print detailed output to console
            log_results(results)
            print("Ping results logged.")
            time.sleep(60)  # Wait for 60 seconds before the next ping cycle
    except KeyboardInterrupt:
        print("Ping monitoring stopped.")

if __name__ == "__main__":
    main()
