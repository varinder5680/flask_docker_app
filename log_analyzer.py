log_path = "/var/log/syslog"
error_count=0
warning_count=0
info_count=0

with open(log_path) as f:
    for line in f:
        e=line.lower()
        if "error" in e:
            error_count+=1
        if  "warning" in e:
            warning_count+=1
        if "info " in e:
            info_count+=1 
print(f"======Log Summary====")
print(f"erroe line : {error_count}")
print(f"warning_count: {warning_count}")
print(f"info times :{info_count}")
