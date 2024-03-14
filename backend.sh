#!/bin/bash

# Define the JSON file
json_file="data.json"

# Function to get Date
function get_date {
	date=$(date +"%d-%m-%Y")
};

# Function to get Time
function get_time {
	time=$(date +"%I:%M:%S %p")
};

# Function to get Weather details
function get_weather {
    api_key="58377e0738b50ef9671a0018445acf80"
    city="Mumbai"
    formatted_city=${city// /%20}
    response=$(curl -s "")
    temperature=$(echo $response | jq -r '.main.temp' | awk '{printf "%.2f", $1 - 273.15}')
    weather_description=$(echo $response | jq -r '.weather[0].description')
};

# Function to get Monitor Memory (RAM Usage) / Memory Usage
function get_monitor_memory {
	monitor_memory=$(free -m | awk 'NR==2{printf "%.2f%% \n", $3*100/$2}')
};

# Function to get Swap usage
function get_swap_usage {
	swap_usage=$(free -m | awk 'NR==3{printf "%.2f%% \n", $3*100/$2}')
};

# Function to get Disk usage (Disk usage of /-root directory)
function get_disk_usage {
	disk_usage=$(df -h | awk '$NF=="/"{printf "%s", $5}')
};

# Function to get CPU Usage
function get_cpu_usage {
	cpu_usage=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF - 2)}')
};

# Function to get Internet Connectivity
function get_internet_connectivity {
	check_internet=$(ping -c 1 -q google.com >&/dev/null; echo $?)
	internet_connectivity="Internet is "
	if [ "$check_internet" -eq 0 ]
	then
		internet_connectivity+="Connected" # 0 - if success - connected to the internet
		wifi_name=$(iwconfig 2>&1 | grep -o "ESSID:\".*\"" | cut -d '"' -f 2)
	else
			internet_connectivity+="Not Connected" # 2 - if not success - not connected to the internet
            wifi_name="Wifi is Not Connected"
	fi
};

# Function to get OS Type
function get_os_type {
	device_os="Device OS Type is "
	if [[ "$OSTYPE" == "linux-gnu"* ]]; then
		device_os+=" Linux"
		os_name=$(grep '^NAME=' /etc/os-release | cut -d '=' -f 2 | tr -d '"')
		os_version=$(grep PRETTY_NAME /etc/os-release | cut -d '=' -f 2 | tr -d '"')
	elif [[ "$OSTYPE" == "darwin"* ]]; then
		device_os+="Mac OS X"
	elif [[ "$OSTYPE" == "cygwin" ]]; then
		device_os+="Cygwin (POSIX compatibility layer for Windows)"
	elif [[ "$OSTYPE" == "msys" ]]; then
		device_os+="MSYS (Lightweight shell and GNU utilities for Windows)"
	elif [[ "$OSTYPE" == "win32" ]]; then
		device_os+="Windows (unlikely)"
	elif [[ "$OSTYPE" == "freebsd"* ]]; then
		device_os+="FreeBSD"
	else
		device_os+="Unknown"
	fi
};

# Function to get Device Architecture
function get_dev_arch {
	dev_arch=$(uname --m)
};

# Function to get Kernel details
function get_kernel_det {
	# kernel release
	kernel_rel=$(uname -r)
};

# Function to get device Hostname
function get_dev_hostname {
	hostname=$(hostname)
};

# Function to get IP Address
function get_ip_add {
	# Internal IP (network IPv4)
	internal_ip=$(hostname -I | awk '{print $1}')
	
	# Extenral IP (IPv6)
	external_ip=$(hostname -I | awk '{print $2}')
};

# Function to get Name (DNS) Servers
function get_dns_servers {
	# Run nmcli command and store the output
    output=$(nmcli dev show)

    # Extract IP4.DNS[1] value and store it in a variable
    ip4_dns1=$(echo "$output" | grep 'IP4.DNS\[1\]' | awk '{print $2}')

    # Extract IP4.DNS[2] value and store it in a variable
    ip4_dns2=$(echo "$output" | grep 'IP4.DNS\[2\]' | awk '{print $2}')
};

# Function to get Logged in Users
function get_loggedin_users {
	loggedin_users=$(users)
};

# Function to get Load Average, System Uptime
function get_load_avg {
	load=$(uptime) || echo "Failed to get load"
	
	load1=$(echo "$load" | awk -F'load average: ' '{ print $2 }' | awk -F', ' '{ print $1 }') || echo "Failed to get load 1"
	
	load5=$(echo "$load" | awk -F'load average: ' '{ print $2 }' | awk -F', ' '{ print $2 }') || echo "Failed to get load 5"
	
	load15=$(echo "$load" | awk -F'load average: ' '{ print $2 }' | awk -F', ' '{ print $3 }')
};

# Function to update JSON file with current data
# Function to update JSON file with current data
function update_json {
    get_date
    get_time
    get_weather
    get_monitor_memory
    get_swap_usage
    get_disk_usage
    get_cpu_usage
    get_internet_connectivity
    get_os_type
    get_dev_arch
    get_kernel_det
    get_dev_hostname
    get_ip_add
    get_dns_servers
    get_loggedin_users
    get_load_avg
    
    # Construct JSON string
    json_content=$(cat <<-END
    {
        "date": "$date",
        "time": "$time",
        "city": "$city",
        "temperature": "$temperature",
        "weather_description": "$weather_description",
        "monitor_memory": "$monitor_memory",
        "swap_usage": "$swap_usage",
        "disk_usage": "$disk_usage",
        "cpu_usage": "$cpu_usage",
        "internet_connectivity": "$internet_connectivity",
        "wifi_name": "$wifi_name",
        "device_os": "$device_os",
        "os_name": "$os_name",
        "os_version": "$os_version",
        "dev_arch": "$dev_arch",
        "kernel_rel": "$kernel_rel",
        "hostname": "$hostname",
        "internal_ip": "$internal_ip",
        "external_ip": "$external_ip",
        "ip4_dns1": "$ip4_dns1",
        "ip4_dns2": "$ip4_dns2",
        "loggedin_users": "$loggedin_users",
        "load1": "$load1",
        "load5": "$load5",
        "load15": "$load15"
    }
END
    )
    
    # Save JSON string to file
    echo "$json_content" > "$json_file"
};

# Main function
function main {
	# To run the script continuously
	while true; do
		update_json
		sleep 1
	done
};

# Call the main function
main
