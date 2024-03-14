import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import json

# Load JSON data from file
with open('data.json') as f:
    data = json.load(f)
    
# Retrieve and store each value as strings
date = data['date']
current_time = data['time']
city = data['city']
temperature = data['temperature']
weather_description = data['weather_description']
monitor_memory = data['monitor_memory']
swap_usage = data['swap_usage']
disk_usage = data['disk_usage']
cpu_usage = data['cpu_usage']
internet_connectivity = data['internet_connectivity']
wifi_name = data['wifi_name']
device_os = data['device_os']
os_name = data['os_name']
os_version = data['os_version']
dev_arch = data['dev_arch']
kernel_rel = data['kernel_rel']
hostname = data['hostname']
internal_ip = data['internal_ip']
external_ip = data['external_ip']
ip4_dns1 = data['ip4_dns1']
ip4_dns2 = data['ip4_dns2']
loggedin_users = data['loggedin_users']
load1 = data['load1']
load5 = data['load5']
load15 = data['load15']

class App:
    def __init__(self, root, data):
        self.root = root
        self.root.geometry('800x420')
        self.root.title('Linux Monitoring System')
        self.root.configure(bg='#070F2B')
        self.data = data
            
        # Show image screen
        self.show_image_screen()
        
        # Schedule the tables with new data
        self.root.after(1000, self.update_data)
        
    def update_data(self):
        # Load JSON data from file
        with open('data.json') as f:
            self.data = json.load(f)
        # Update the tables with new data
        self.update_tables(self.data)
        # Schedule the tables with new data
        self.root.after(1000, self.update_data)

    def show_image_screen(self):
        # Load and display the image
        self.image = Image.open("logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.photo, bg='#070F2B')
        self.image_label.pack(pady=20)

        # Progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TProgressbar", background='#070F2B', troughcolor='#070F2B', bordercolor='#070F2B', lightcolor='#070F2B', darkcolor='#070F2B', troughrelief='flat')
        style.configure("Horizontal.TProgressbar", foreground='#FFFFFF', background='#535C91')
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate', style="Horizontal.TProgressbar")
        self.progress.pack(pady=20)

        # Update the progress bar
        self.fill_progress_bar()

    def fill_progress_bar(self):
        # Fills the progress bar gradually
        for i in range(100):
            time.sleep(0.05)
            self.progress['value'] = i+1
            self.root.update_idletasks()
        self.show_another_screen()

    def show_another_screen(self):
        # Clear previous widgets
        self.image_label.destroy()
        self.progress.destroy()

        # Tab panes
        self.tab_control = ttk.Notebook(self.root)
        headings = ['Basic System and Weather Information', 'Resource Monitoring', 'Network and Connectivity', 'System Details']
        
        self.tables = []  # List to store tables
        
        for i in range(4):
            tab = ttk.Frame(self.tab_control)
            self.tab_control.add(tab, text=headings[i])
            
            # Add table to each tab
            table = ttk.Treeview(tab, columns=('Data', 'Value'), show='headings')
            table.heading('Data', text='Data')
            table.heading('Value', text='Value')
            
            # Populate tables based on tab index
            if i == 0:
                table.insert('', 'end', values=('City', city))
                table.insert('', 'end', values=('Temperature', (temperature + '°C')))
                table.insert('', 'end', values=('Date', date))
                table.insert('', 'end', values=('Time', current_time))
            elif i == 1:
                table.insert('', 'end', values=('Monitor Memory', monitor_memory))
                table.insert('', 'end', values=('Swap Usage', swap_usage))
                table.insert('', 'end', values=('Disk Usage', disk_usage))
                table.insert('', 'end', values=('CPU Usage', cpu_usage))
                table.insert('', 'end', values=('Load 1', load1))
                table.insert('', 'end', values=('Load 5', load5))
                table.insert('', 'end', values=('Load 15', load15))
            elif i == 2:
                table.insert('', 'end', values=('Internet Connectivity', internet_connectivity))
                table.insert('', 'end', values=('Wifi Name', wifi_name))
                table.insert('', 'end', values=('Internal IP', internal_ip))
                table.insert('', 'end', values=('External IP', external_ip))
                table.insert('', 'end', values=('IP4 DNS 1', ip4_dns1))
                table.insert('', 'end', values=('IP4 DNS 2', ip4_dns2))
            elif i == 3:
                table.insert('', 'end', values=('Device OS', device_os))
                table.insert('', 'end', values=('OS Name', os_name))
                table.insert('', 'end', values=('OS Version', os_version))
                table.insert('', 'end', values=('Device Architecture', dev_arch))
                table.insert('', 'end', values=('Kernel Release', kernel_rel))
                table.insert('', 'end', values=('Hostname', hostname))
                table.insert('', 'end', values=('Logged in Users', loggedin_users))
            
            table.pack(expand=True, fill='both')
            
            self.tables.append(table)  # Add table to the list

        self.tab_control.pack(expand=1, fill="both")

    # Method to update the tables
    def update_tables(self, data):
        for i, table in enumerate(self.tables):
            table.delete(*table.get_children())  # Clear previous data
            if i == 0:
                table.insert('', 'end', values=('City', data['city']))
                table.insert('', 'end', values=('Temperature', (data['temperature'] + '°C')))
                table.insert('', 'end', values=('Date', data['date']))
                table.insert('', 'end', values=('Time', data['time']))
            elif i == 1:
                table.insert('', 'end', values=('Monitor Memory', data['monitor_memory']))
                table.insert('', 'end', values=('Swap Usage', data['swap_usage']))
                table.insert('', 'end', values=('Disk Usage', data['disk_usage']))
                table.insert('', 'end', values=('CPU Usage', data['cpu_usage']))
                table.insert('', 'end', values=('Load 1', data['load1']))
                table.insert('', 'end', values=('Load 5', data['load5']))
                table.insert('', 'end', values=('Load 15', data['load15']))
            elif i == 2:
                table.insert('', 'end', values=('Internet Connectivity', data['internet_connectivity']))
                table.insert('', 'end', values=('Wifi Name', data['wifi_name']))
                table.insert('', 'end', values=('Internal IP', data['internal_ip']))
                table.insert('', 'end', values=('External IP', data['external_ip']))
                table.insert('', 'end', values=('IP4 DNS 1', data['ip4_dns1']))
                table.insert('', 'end', values=('IP4 DNS 2', data['ip4_dns2']))
            elif i == 3:
                table.insert('', 'end', values=('Device OS', data['device_os']))
                table.insert('', 'end', values=('OS Name', data['os_name']))
                table.insert('', 'end', values=('OS Version', data['os_version']))
                table.insert('', 'end', values=('Device Architecture', data['dev_arch']))
                table.insert('', 'end', values=('Kernel Release', data['kernel_rel']))
                table.insert('', 'end', values=('Hostname', data['hostname']))
                table.insert('', 'end', values=('Logged in Users', data['loggedin_users']))
            else:
                for j in range(6):
                    table.insert('', 'end', values=(f'Row {j+1}', f'Value {j+1}'))
          
def main():
    root = tk.Tk()
    app = App(root, data)
    root.mainloop()

if __name__ == "__main__":
    main()
