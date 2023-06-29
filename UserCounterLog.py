import re

# Path to the Apache log file
log_file_path = 'acess.log'

# Regular expression pattern to extract information from the log line
log_pattern = r'^([\d.]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"$'

totalOfConnections = 0
users = []
# Open the log file in read mode
with open(log_file_path, 'r') as log_file:
    # Read each line of the file
    for line in log_file:
        # Apply the regular expression to the log line
        match = re.match(log_pattern, line)
        
        if match:
            # Extract the information from the log line
            ip_address = match.group(1)
            datetime = match.group(2)
            request = match.group(3)
            status_code = match.group(4)
            response_size = match.group(5)
            referrer_url = match.group(6)
            user_agent = match.group(7)
            
            if request == 'GET / HTTP/1.1' and status_code == '200':
                print(f"Acesso Registrado em:{datetime}")
                print(f"Estado da requisição:{status_code}")
                totalOfConnections += 1
                users.append(ip_address)
    
print(f'++++++++++++++++++++++++++++++++++++++++++')
print(f'Total de acessos: {totalOfConnections}')
print(f'Total de usuários: {len(set(users))}')
print(f'++++++++++++++++++++++++++++++++++++++++++')

